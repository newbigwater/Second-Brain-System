from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}
EXCLUDE_PARTS = {"99. Artifact"}

LAYER_DIRS = [
    "01. Core",
    "02. Business",
    "03. Project",
    "04. Application",
]

FRONTMATTER_RE = re.compile(r"(?s)\A---\n(.*?)\n---\n")

# Links
MDLINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def should_skip(rel: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    if any(part in EXCLUDE_PARTS for part in rel.parts):
        return True
    if rel.name == "_MOC_.md":
        return True
    if rel.suffix.lower() != ".md":
        return True
    return False


def split_frontmatter(text: str) -> tuple[str | None, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end() :]


def upsert_list(fm: str, key: str, items: list[str]) -> str:
    # remove existing key block (simple YAML list) if present
    pat = re.compile(rf"(?ms)^{re.escape(key)}\s*:\s*\n(?:^\s*-\s*.*\n)*")
    fm2 = pat.sub("", fm)

    block = [f"{key}:"]
    for it in items:
        block.append(f"  - {it}")
    return fm2.rstrip() + "\n" + "\n".join(block) + "\n"


def remove_yaml_list_block(fm: str, key: str) -> str:
    pat = re.compile(rf"(?ms)^{re.escape(key)}\s*:\s*\n(?:^\s*-\s*.*\n)*")
    return pat.sub("", fm)


def normalize_frontmatter(fm: str) -> str:
    """
    Cleanup known frontmatter corruptions introduced by earlier automation:
    - Remove any list items that point to generated Master Prompts.
    - Remove any indented list items directly under Version (invalid YAML continuation).
    """
    # Remove any list-item "continuations" under Version scalar (invalid YAML)
    fm = re.sub(
        r"(?m)^(Version\s*:\s*.+?)\s*\r?\n(?:\s+-\s+.+\r?\n)+",
        r"\1\n",
        fm,
    )

    lines = fm.splitlines()
    out: list[str] = []
    prev_nonempty = ""
    for line in lines:
        if "99. Artifact/Master Prompt.md" in line and re.match(r"^\s*-\s+.+$", line):
            continue
        if re.match(r"^Version\s*:\s*.+$", prev_nonempty) and re.match(r"^\s+-\s+.+$", line):
            # list item accidentally attached under Version scalar
            continue
        out.append(line)
        if line.strip():
            prev_nonempty = line
    return "\n".join(out) + ("\n" if fm.endswith("\n") else "")

def normalize_target(raw: str) -> str:
    raw = raw.strip()
    # strip <...>
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1].strip()
    raw = unquote(raw)
    # strip surrounding quotes
    raw = raw.strip().strip('"').strip("'")
    return raw


def strip_anchor_and_query(target: str) -> str:
    # remove query and fragments
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return target


def is_external(target: str) -> bool:
    t = target.lower()
    return t.startswith("http://") or t.startswith("https://") or t.startswith("mailto:")


def vaultish_to_repo_rel(target: str) -> str:
    """
    Many wikilinks are like:
      00. Second-Brain-System/00.03. AI/01. Core/...
    Convert to repo-relative by removing the vault prefix when present.
    """
    t = target.replace("\\", "/").lstrip("/")
    prefix = "00. Second-Brain-System/00.03. AI/"
    if t.startswith(prefix):
        return t[len(prefix) :]
    return t


def resolve_to_repo_file(current_file: Path, target: str) -> str | None:
    target = normalize_target(target)
    if not target:
        return None
    if target.startswith("#"):
        return None
    if is_external(target):
        return None

    target = strip_anchor_and_query(target)
    target = vaultish_to_repo_rel(target)

    # If it's an absolute-ish path within repo (starts with a top layer), treat as repo-root-relative
    repo_rel: Path
    if any(target.startswith(layer + "/") for layer in ("01. Core", "02. Business", "03. Project", "04. Application")):
        repo_rel = Path(target)
    else:
        # treat as relative path from current file
        abs_path = (current_file.parent / target).resolve()
        try:
            repo_rel = abs_path.relative_to(ROOT)
        except ValueError:
            # resolved outside the repo root; ignore
            return None

    # If no extension, Obsidian link may omit ".md"
    cand = ROOT / repo_rel
    if cand.exists() and cand.is_file():
        pass
    else:
        if cand.suffix == "":
            cand2 = cand.with_suffix(".md")
            if cand2.exists() and cand2.is_file():
                cand = cand2
                repo_rel = cand.relative_to(ROOT)
            else:
                return None
        else:
            return None

    rel = Path(str(repo_rel).replace("\\", "/"))
    # Exclusions for References list (we only want guideline docs)
    if should_skip(rel):
        return None
    return str(rel).replace("\\", "/")


def extract_targets_from_text(text: str) -> list[str]:
    targets: list[str] = []
    for _label, t in MDLINK_RE.findall(text):
        targets.append(t)
    for inner in WIKILINK_RE.findall(text):
        # supports [[path|display]]
        t = inner.split("|", 1)[0].strip()
        targets.append(t)
    return targets


def iter_guideline_files() -> list[Path]:
    out: list[Path] = []
    for base in LAYER_DIRS:
        d = ROOT / base
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            rel = p.relative_to(ROOT)
            if should_skip(rel):
                continue
            out.append(p)
    uniq = {str(p.relative_to(ROOT)).replace("\\", "/"): p for p in out}
    return [uniq[k] for k in sorted(uniq.keys())]


def main() -> int:
    updated = 0
    for p in iter_guideline_files():
        rel_self = str(p.relative_to(ROOT)).replace("\\", "/")
        txt = p.read_text(encoding="utf-8", errors="ignore")
        fm, body = split_frontmatter(txt)
        if fm is None:
            # no frontmatter: we still add one with References
            fm = ""

        # Clean previously injected artifact references / YAML corruptions from frontmatter.
        fm = normalize_frontmatter(fm)

        # Parse targets from body + from frontmatter (but exclude backlinks and previous References to avoid recursion).
        fm_parse = remove_yaml_list_block(fm, "References")
        fm_parse = remove_yaml_list_block(fm_parse, "backlinks")

        targets = extract_targets_from_text(body) + extract_targets_from_text(fm_parse)
        refs: set[str] = set()
        for t in targets:
            r = resolve_to_repo_file(p, t)
            if not r:
                continue
            if r == rel_self:
                continue
            refs.add(r)

        fm2 = upsert_list(fm, "References", sorted(refs))
        new_txt = "---\n" + fm2.rstrip() + "\n---\n" + body
        if new_txt != txt:
            p.write_text(new_txt, encoding="utf-8")
            updated += 1

    print(f"Updated files (References): {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

