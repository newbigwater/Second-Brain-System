from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [ROOT / "02. Business", ROOT / "03. Project"]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}


REPLACEMENTS = [
    ("../../01.%20Core/", "../../../01.%20Core/"),
    ("../../01. Core/", "../../../01. Core/"),
    ("../../02.%20Business/", "../../../02.%20Business/"),
    ("../../02. Business/", "../../../02. Business/"),
    ("../../03.%20Project/", "../../../03.%20Project/"),
    ("../../03. Project/", "../../../03. Project/"),
]


def iter_md_files():
    for base in TARGET_DIRS:
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            rel = p.relative_to(ROOT)
            if any(part in EXCLUDE_DIRS for part in rel.parts):
                continue
            yield p


def main() -> int:
    changed_files = 0
    hits_total = 0
    for f in iter_md_files():
        original = f.read_text(encoding="utf-8", errors="ignore")
        updated = original
        hits = 0
        for old, new in REPLACEMENTS:
            if old in updated:
                updated = updated.replace(old, new)
                hits += 1
        if hits:
            f.write_text(updated, encoding="utf-8")
            changed_files += 1
            hits_total += hits

    print(f"Updated files: {changed_files}")
    print(f"Replacement hits: {hits_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

