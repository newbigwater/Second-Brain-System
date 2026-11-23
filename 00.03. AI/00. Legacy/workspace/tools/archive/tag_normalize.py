from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}


def iter_md_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


FRONTMATTER_RE = re.compile(r"(?s)\A---\n(.*?)\n---\n")


def infer_layer_tags(rel_posix: str) -> list[str]:
    # Add stable layer tags (keep legacy tags intact).
    if rel_posix.startswith("01. Core/"):
        return ["01__Core"]
    if rel_posix.startswith("02. Business/"):
        tags = ["02__Business"]
        if rel_posix.startswith("02. Business/00. Common/"):
            tags.append("02_00__Common")
        elif rel_posix.startswith("02. Business/02.01. SRS/"):
            tags.append("02_01__SRS")
        elif rel_posix.startswith("02. Business/02.02. SDS/"):
            tags.append("02_02__SDS")
        elif rel_posix.startswith("02. Business/02.03. SCS/"):
            tags.append("02_03__SCS")
        return tags
    if rel_posix.startswith("03. Project/"):
        tags = ["03__Project"]
        if rel_posix.startswith("03. Project/03.01. PM/"):
            tags.append("03_01__PM")
        elif rel_posix.startswith("03. Project/03.02. Translation/"):
            tags.append("03_02__Translation")
        return tags
    if rel_posix.startswith("04. Application/"):
        return ["04__Application"]
    return []


def parse_tags_block(frontmatter: str) -> tuple[list[str], int, int] | None:
    """
    Return (tags, start_idx, end_idx) for the tags list in the frontmatter *body*.
    Indices are relative to the frontmatter body string.
    """
    m = re.search(r"(?m)^tags:\s*\n", frontmatter)
    if not m:
        return None

    start = m.end()
    # tags block is consecutive lines starting with optional spaces + '-' until a non-list line or EOF
    lines = frontmatter[start:].splitlines(True)
    block = []
    consumed = 0
    for line in lines:
        if re.match(r"^\s*-\s+", line):
            block.append(line)
            consumed += len(line)
            continue
        break

    if consumed == 0:
        return ([], start, start)

    tags = []
    for line in block:
        t = re.sub(r"^\s*-\s+", "", line).strip()
        if t:
            tags.append(t)
    return (tags, start, start + consumed)


def rewrite_frontmatter(frontmatter_body: str, add_tags: list[str]) -> tuple[str, bool]:
    parsed = parse_tags_block(frontmatter_body)
    if not parsed:
        return frontmatter_body, False

    existing, s, e = parsed
    merged = list(dict.fromkeys(existing + [t for t in add_tags if t not in existing]))
    if merged == existing:
        return frontmatter_body, False

    new_block = "".join([f"  - {t}\n" for t in merged])
    updated = frontmatter_body[:s] + new_block + frontmatter_body[e:]
    return updated, True


def main() -> int:
    changed = 0
    for f in iter_md_files():
        rel = str(f.relative_to(ROOT)).replace("\\", "/")
        add = infer_layer_tags(rel)
        if not add:
            continue

        txt = f.read_text(encoding="utf-8", errors="ignore")
        fm = FRONTMATTER_RE.match(txt)
        if not fm:
            continue

        body = fm.group(1)
        new_body, did = rewrite_frontmatter(body, add)
        if not did:
            continue

        new_txt = "---\n" + new_body + "\n---\n" + txt[fm.end() :]
        f.write_text(new_txt, encoding="utf-8")
        changed += 1

    print(f"Updated files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

