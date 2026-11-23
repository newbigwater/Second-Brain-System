from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}


REPLACEMENTS = [
    # Core folder rename (00 -> 01)
    ("00. Core/", "01. Core/"),
    ("00.%20Core/", "01.%20Core/"),
    ("00. Second-Brain-System/00.03. AI/00. Core/", "00. Second-Brain-System/00.03. AI/01. Core/"),
    (r"00. System\00.03. AI\00. Core\\", r"00. System\00.03. AI\01. Core\\"),

    # Stage folders moved under Business
    ("01. SRS/", "02. Business/02.01. SRS/"),
    ("01.%20SRS/", "02.%20Business/02.01.%20SRS/"),
    ("00. Second-Brain-System/00.03. AI/01. SRS/", "00. Second-Brain-System/00.03. AI/02. Business/02.01. SRS/"),
    (r"00. System\00.03. AI\01. SRS\\", r"00. System\00.03. AI\02. Business\02.01. SRS\\"),

    ("02. SDS/", "02. Business/02.02. SDS/"),
    ("02.%20SDS/", "02.%20Business/02.02.%20SDS/"),
    ("00. Second-Brain-System/00.03. AI/02. SDS/", "00. Second-Brain-System/00.03. AI/02. Business/02.02. SDS/"),
    (r"00. System\00.03. AI\02. SDS\\", r"00. System\00.03. AI\02. Business\02.02. SDS\\"),

    ("03. SCS/", "02. Business/02.03. SCS/"),
    ("03.%20SCS/", "02.%20Business/02.03.%20SCS/"),
    ("00. Second-Brain-System/00.03. AI/03. SCS/", "00. Second-Brain-System/00.03. AI/02. Business/02.03. SCS/"),
    (r"00. System\00.03. AI\03. SCS\\", r"00. System\00.03. AI\02. Business\02.03. SCS\\"),

    # Project folders
    ("04. PM/", "03. Project/03.01. PM/"),
    ("04.%20PM/", "03.%20Project/03.01.%20PM/"),
    ("00. Second-Brain-System/00.03. AI/04. PM/", "00. Second-Brain-System/00.03. AI/03. Project/03.01. PM/"),
    (r"00. System\00.03. AI\04. PM\\", r"00. System\00.03. AI\03. Project\03.01. PM\\"),

    ("05. Translation/", "03. Project/03.02. Translation/"),
    ("05.%20Translation/", "03.%20Project/03.02.%20Translation/"),
    ("00. Second-Brain-System/00.03. AI/05. Translation/", "00. Second-Brain-System/00.03. AI/03. Project/03.02. Translation/"),
    (r"00. System\00.03. AI\05. Translation\\", r"00. System\00.03. AI\03. Project\03.02. Translation\\"),

    # Application folder rename
    ("07. Application/", "04. Application/"),
    ("07.%20Application/", "04.%20Application/"),
    ("00. Second-Brain-System/00.03. AI/07. Application/", "00. Second-Brain-System/00.03. AI/04. Application/"),
    (r"00. System\00.03. AI\07. Application\\", r"00. System\00.03. AI\04. Application\\"),

    # Backtick mentions (best-effort)
    ("`00. Core`", "`01. Core`"),
]


def iter_md_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


def main() -> int:
    changed_files = 0
    changed_hits = 0

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
            changed_hits += hits

    print(f"Updated files: {changed_files}")
    print(f"Replacement hits: {changed_hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

