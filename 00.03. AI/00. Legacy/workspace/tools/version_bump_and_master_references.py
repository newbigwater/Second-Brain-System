from __future__ import annotations

import re
from pathlib import Path

from artifact_master_prompt import ROOT, TARGETS


EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}


LAYER_DIRS = [
    "01. Core",
    "10. Business",
    "20. Personal",
]


MASTER_PROMPTS = sorted({
    f"{base}/99. Artifact/Master Prompt.md"
    for (_title, base, _includes) in TARGETS
})


FRONTMATTER_RE = re.compile(r"(?s)\A---\n(.*?)\n---\n")


def should_skip(rel: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    if "99. Artifact" in rel.parts:
        return True
    if rel.name == "_MOC_.md":
        return True
    return False


def split_frontmatter(text: str) -> tuple[str | None, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end() :]


def parse_version(raw: str) -> tuple[int, int] | None:
    raw = raw.strip().strip('"').strip("'")
    m = re.match(r"^v(\d+)\.(\d+)$", raw)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def bump_version(existing: str) -> str:
    parsed = parse_version(existing)
    if parsed:
        major, minor = parsed
        return f"v{major}.{minor+1}"
    # fallback: if it's like "v1", bump to v1.1; otherwise leave as v1.0
    m = re.match(r"^v(\d+)$", existing.strip())
    if m:
        return f"v{int(m.group(1))}.1"
    return "v1.0"


def upsert_version(fm: str, *, bump_if_present: bool = True) -> tuple[str, str]:
    """
    Returns (new_frontmatter_body, version_value).
    If Version exists, bump it by +1 minor (vX.Y -> vX.(Y+1)).
    If missing, add Version: v1.0.
    """
    # find Version or version
    m = re.search(r"(?m)^(Version|version)\s*:\s*(.+?)\s*$", fm)
    if m:
        current = m.group(2).strip()
        new_ver = bump_version(current) if bump_if_present else current
        fm2 = re.sub(r"(?m)^(Version|version)\s*:\s*.+?\s*$", f"Version: {new_ver}", fm)
        return fm2, new_ver

    # append at end
    fm2 = fm.rstrip() + ("\n" if fm.strip() else "")
    fm2 += "Version: v1.0\n"
    return fm2, "v1.0"


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

    # include top-level suite doc as a guideline too (optional but useful)
    for top in ["docs/ChatGPT Custom Instructions – AI Project Suite.md", "readme.md"]:
        p = ROOT / top
        if p.exists():
            out.append(p)

    # unique stable
    uniq = {str(p.relative_to(ROOT)).replace("\\", "/"): p for p in out}
    return [uniq[k] for k in sorted(uniq.keys())]


SECTION_SRC = re.compile(r"(?m)^\- Source:\s*`([^`]+)`\s*$")


def extract_master_sources(master_text: str) -> list[str]:
    return sorted(set(SECTION_SRC.findall(master_text)))


def upsert_master_frontmatter(master_text: str, references: list[str]) -> str:
    # Master prompt currently has no frontmatter; we add/replace it.
    fm = ["type: Artifact", "creation date: 2026-02-09", "References:"]
    for r in references:
        fm.append(f"  - {r}")
    fm_txt = "---\n" + "\n".join(fm) + "\n---\n"

    m = FRONTMATTER_RE.match(master_text)
    if m:
        # replace
        return fm_txt + master_text[m.end() :]
    return fm_txt + master_text


def main() -> int:
    # 1) bump/add Version across all guideline files
    updated = 0
    added_frontmatter = 0
    for p in iter_guideline_files():
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        txt = p.read_text(encoding="utf-8", errors="ignore")
        fm, body = split_frontmatter(txt)
        if fm is None:
            fm = ""
            added_frontmatter += 1

        new_fm, _ver = upsert_version(fm, bump_if_present=True)
        new_txt = "---\n" + new_fm.rstrip() + "\n---\n" + body
        if new_txt != txt:
            p.write_text(new_txt, encoding="utf-8")
            updated += 1

    # 2) add References property to each Master Prompt frontmatter
    masters_updated = 0
    for mp_rel in MASTER_PROMPTS:
        mp = ROOT / mp_rel
        if not mp.exists():
            continue
        txt = mp.read_text(encoding="utf-8", errors="ignore")
        refs = extract_master_sources(txt)
        new_txt = upsert_master_frontmatter(txt, refs)
        if new_txt != txt:
            mp.write_text(new_txt, encoding="utf-8")
            masters_updated += 1

    print(f"Guidelines updated (Version): {updated}")
    print(f"Guidelines added frontmatter: {added_frontmatter}")
    print(f"Master Prompts updated (References): {masters_updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

