import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}


def iter_mocs():
    for p in ROOT.rglob("_MOC_.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


def has_any_outgoing_wikilink(text: str) -> bool:
    # YAML key may exist, but actual items are lines like: - "[[...|...]]"
    return bool(re.search(r'(?m)^\s*-\s*"\[\[', text))


def outgoinglinks_is_empty_block(text: str) -> bool:
    # Typical pattern in this repo:
    # outgoinglinks:
    # ---
    # ---
    stripped = text.strip()
    return bool(re.search(r"(?ms)^outgoinglinks:\s*\n---\s*\n---\s*$", stripped))


def main() -> int:
    empty = []
    for p in iter_mocs():
        txt = p.read_text(encoding="utf-8", errors="ignore")
        if "outgoinglinks:" not in txt:
            continue
        if outgoinglinks_is_empty_block(txt) or not has_any_outgoing_wikilink(txt):
            empty.append(str(p.relative_to(ROOT)).replace("\\", "/"))

    empty.sort()
    print("\n".join(empty))
    print("count", len(empty))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

