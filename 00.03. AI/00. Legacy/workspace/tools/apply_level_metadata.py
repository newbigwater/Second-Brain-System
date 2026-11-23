#!/usr/bin/env python3
"""Populate level metadata in front matter based on folder prefixes."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Ordered from most specific to least specific so that longer prefixes win.
LEVEL_MAP = [
    ("01. Core/00. Charter", "00.00"),
    ("01. Core/01. Operations", "00.01"),
    ("01. Core/02. Standards", "00.01"),
    ("01. Core/03. Frameworks", "00.01"),
    ("01. Core/04. Custom-Instructions", "00.01"),
    ("01. Core/99. Artifact", "90.00"),
    ("10. Business/10.01 Architect/10.01.01 SRS", "10.01.01"),
    ("10. Business/10.01 Architect/10.01.02 SDS", "10.01.02"),
    ("10. Business/10.01 Architect/10.01.03 SCS", "10.01.03"),
    ("10. Business/10.01 Architect", "10.01"),
    ("10. Business/10.02 Project/10.02.01 PM", "10.02.01"),
    ("10. Business/10.02 Project/10.02.02 Translation", "10.02.02"),
    ("10. Business/10.02 Project", "10.02"),
    ("10. Business/01. Rules", "10.00"),
    ("10. Business/02. Guides", "10.00"),
    ("10. Business/99. Artifact", "90.00"),
    ("10. Business", "10.00"),
    ("20. Personal/20.01 English/01. Rules/20.01.01 Podo English", "20.01.01"),
    ("20. Personal/20.01 English/01. Rules/20.01.02 Grammar", "20.01.02"),
    ("20. Personal/20.01 English/01. Rules", "20.01"),
    ("20. Personal/20.01 English", "20.01"),
    ("20. Personal/20.02 Computer-Science", "20.02"),
    ("20. Personal/20.03 ISA-95", "20.03"),
    ("20. Personal/20.00 Personal", "20.00"),
    ("20. Personal", "20.00"),
    ("99. Backup", "90.01"),
    ("01. Core", "00.01"),
]

SKIP_DIRS = {"workspace", "tools", ".git", ".obsidian", "node_modules"}


def find_level(rel_path: Path) -> str | None:
    posix = rel_path.as_posix()
    for prefix, level in LEVEL_MAP:
        if posix.startswith(prefix):
            return level
    return None


def compute_parent(level: str) -> str | None:
    if "." not in level:
        return None
    parts = level.split(".")
    if len(parts) <= 1:
        return None
    parent = ".".join(parts[:-1])
    if len(parent) <= 2:
        return None
    return parent


def update_front_matter(path: Path, level: str) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return False

    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return False

    fm_lines = lines[1:end_idx]
    body = lines[end_idx + 1 :]

    desired_parent = compute_parent(level)
    changed = False

    new_fm = []
    found_level = False
    found_parent = False
    for line in fm_lines:
        if line.startswith("level:"):
            found_level = True
            if line != f"level: {level}":
                new_fm.append(f"level: {level}")
                changed = True
            else:
                new_fm.append(line)
        elif line.startswith("parent_level:"):
            found_parent = True
            if desired_parent and line != f"parent_level: {desired_parent}":
                new_fm.append(f"parent_level: {desired_parent}")
                changed = True
            elif not desired_parent:
                # remove stale parent_level
                changed = True
                continue
            else:
                new_fm.append(line)
        else:
            new_fm.append(line)

    fm_lines = new_fm

    if not found_level:
        fm_lines.append(f"level: {level}")
        changed = True

    if desired_parent:
        if not found_parent:
            fm_lines.append(f"parent_level: {desired_parent}")
            changed = True
    else:
        if found_parent:
            # already removed above
            pass
    if not changed:
        return False

    new_text = "\n".join(["---", *fm_lines, "---", *body])
    if text.endswith("\n"):
        new_text += "\n"
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    updated = 0
    skipped = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        level = find_level(rel)
        if not level:
            skipped.append(rel.as_posix())
            continue
        if update_front_matter(path, level):
            updated += 1
    print(f"Updated level metadata in {updated} files.")
    if skipped:
        print("Skipped (no level mapping):")
        for item in skipped:
            safe = item.encode("unicode_escape").decode()
            print(f"  - {safe}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
