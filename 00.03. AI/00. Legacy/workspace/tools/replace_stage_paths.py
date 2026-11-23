#!/usr/bin/env python3
"""One-off helper to rewrite markdown references after level restructure."""

from __future__ import annotations

from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parents[2]
REPLACEMENTS = OrderedDict([
    ("02. Business/02.01. SRS", "10. Business/10.01 Architect/10.01.01 SRS"),
    ("02. Business/02.02. SDS", "10. Business/10.01 Architect/10.01.02 SDS"),
    ("02. Business/02.03. SCS", "10. Business/10.01 Architect/10.01.03 SCS"),
    ("02. Business/00. Common/📘 Integrated Prompt Template Set.md", "10. Business/02. Guides/📘 Integrated Prompt Template Set.md"),
    ("02. Business/00. Common/🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md", "10. Business/01. Rules/🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md"),
    ("02. Business/00. Common", "10. Business/01. Rules"),
    ("02. Business", "10. Business"),
    ("03. Project/03.01. PM", "10. Business/10.02 Project/10.02.01 PM"),
    ("03. Project/03.02. Translation", "10. Business/10.02 Project/10.02.02 Translation"),
    ("03. Project", "10. Business/10.02 Project"),
    ("04. Application/01. Learn/01. Podo", "20. Personal/20.01 English/01. Rules/20.01.01 Podo English"),
    ("04. Application/01. Learn/02. Grammer", "20. Personal/20.01 English/01. Rules/20.01.02 Grammar"),
    ("04. Application/01. Learn/01. English", "20. Personal/20.01 English/01. Rules"),
    ("04. Application/01. Learn", "20. Personal/20.01 English"),
    ("04. Application/02. Computer-Science", "20. Personal/20.02 Computer-Science"),
    ("04. Application/03. ISA-95", "20. Personal/20.03 ISA-95"),
    ("04. Application/00. Personal", "20. Personal/20.00 Personal"),
    ("04. Application", "20. Personal"),
    ("02.%20Business/02.01.%20SRS", "10.%20Business/10.01%20Architect/10.01.01%20SRS"),
    ("02.%20Business/02.02.%20SDS", "10.%20Business/10.01%20Architect/10.01.02%20SDS"),
    ("02.%20Business/02.03.%20SCS", "10.%20Business/10.01%20Architect/10.01.03%20SCS"),
    ("02.%20Business/00.%20Common/%F0%9F%93%98%20Integrated%20Prompt%20Template%20Set.md", "10.%20Business/02.%20Guides/%F0%9F%93%98%20Integrated%20Prompt%20Template%20Set.md"),
    ("02.%20Business/00.%20Common/%F0%9F%94%97%20SRS%20%E2%86%94%20SDS%20%E2%86%94%20SCS%20Traceability%20Prompt%20Rules.md", "10.%20Business/01.%20Rules/%F0%9F%94%97%20SRS%20%E2%86%94%20SDS%20%E2%86%94%20SCS%20Traceability%20Prompt%20Rules.md"),
    ("02.%20Business/00.%20Common", "10.%20Business/01.%20Rules"),
    ("02.%20Business", "10.%20Business"),
    ("03.%20Project/03.01.%20PM", "10.%20Business/10.02%20Project/10.02.01%20PM"),
    ("03.%20Project/03.02.%20Translation", "10.%20Business/10.02%20Project/10.02.02%20Translation"),
    ("03.%20Project", "10.%20Business/10.02%20Project"),
    ("04.%20Application/01.%20Learn/01.%20Podo", "20.%20Personal/20.01%20English/01.%20Rules/20.01.01%20Podo%20English"),
    ("04.%20Application/01.%20Learn/02.%20Grammer", "20.%20Personal/20.01%20English/01.%20Rules/20.01.02%20Grammar"),
    ("04.%20Application/01.%20Learn/01.%20English", "20.%20Personal/20.01%20English/01.%20Rules"),
    ("04.%20Application/01.%20Learn", "20.%20Personal/20.01%20English"),
    ("04.%20Application/02.%20Computer-Science", "20.%20Personal/20.02%20Computer-Science"),
    ("04.%20Application/03.%20ISA-95", "20.%20Personal/20.03%20ISA-95"),
    ("04.%20Application/00.%20Personal", "20.%20Personal/20.00%20Personal"),
    ("04.%20Application", "20.%20Personal"),
])

SKIP_DIRS = {"workspace", "tools", ".git", ".obsidian", "node_modules"}


def main() -> int:
    updated = 0
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in REPLACEMENTS.items():
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
    print(f"Rewrote paths in {updated} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
