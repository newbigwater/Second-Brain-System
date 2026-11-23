from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}

# Folder-name redesign (keep numeric prefixes, change semantic names only)
REPLACEMENTS = [
    # plain (non-encoded)
    ("00. Core/02. Contract/", "00. Core/02. Contracts/"),
    ("00. Core/04. Human-Guides/", "00. Core/04. Standards/"),
    ("00. Core/05. Optional-Frameworks/", "00. Core/05. Frameworks/"),
    ("00. Core/06. Guides/", "00. Core/06. Custom-Instructions/"),
    # percent-encoded (used in many md links)
    ("00.%20Core/02.%20Contract/", "00.%20Core/02.%20Contracts/"),
    ("00.%20Core/04.%20Human-Guides/", "00.%20Core/04.%20Standards/"),
    ("00.%20Core/05.%20Optional-Frameworks/", "00.%20Core/05.%20Frameworks/"),
    ("00.%20Core/06.%20Guides/", "00.%20Core/06.%20Custom-Instructions/"),
    # relative inside 00. Core docs (no "00. Core/" prefix)
    ("../02. Contract/", "../02. Contracts/"),
    ("../04. Human-Guides/", "../04. Standards/"),
    ("../05. Optional-Frameworks/", "../05. Frameworks/"),
    ("../06. Guides/", "../06. Custom-Instructions/"),
    ("../02.%20Contract/", "../02.%20Contracts/"),
    ("../04.%20Human-Guides/", "../04.%20Standards/"),
    ("../05.%20Optional-Frameworks/", "../05.%20Frameworks/"),
    ("../06.%20Guides/", "../06.%20Custom-Instructions/"),
]


def iter_md_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


def apply_replacements(text: str) -> tuple[str, int]:
    n = 0
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
            n += 1
    return text, n


def main() -> int:
    changed_files = 0
    changed_total = 0

    for f in iter_md_files():
        original = f.read_text(encoding="utf-8", errors="ignore")
        updated, n = apply_replacements(original)
        if n:
            f.write_text(updated, encoding="utf-8")
            changed_files += 1
            changed_total += n

    print(f"Updated files: {changed_files}")
    print(f"Replacement hits: {changed_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

