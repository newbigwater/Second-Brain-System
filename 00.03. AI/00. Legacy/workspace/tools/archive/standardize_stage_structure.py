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


def safe_rename_dir(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        raise RuntimeError(f"Destination already exists: {dst}")
    src.rename(dst)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_moc_if_missing(dir_path: Path, *, tags: list[str], backlinks: list[str], outgoinglinks: list[str]) -> None:
    moc = dir_path / "_MOC_.md"
    if moc.exists():
        return
    tags_block = "\n".join([f"  - {t}" for t in tags])
    backlinks_block = "\n".join([f"  - \"{b}\"" for b in backlinks]) if backlinks else ""
    outgoing_block = "\n".join([f"  - \"{o}\"" for o in outgoinglinks]) if outgoinglinks else ""
    text = (
        "---\n"
        "type: MOC\n"
        "creation date: 2026-02-09\n"
        "tags:\n"
        f"{tags_block}\n"
        "backlinks:\n"
        f"{backlinks_block}\n"
        "outgoinglinks:\n"
        f"{outgoing_block}\n"
        "---\n"
        "---\n"
    )
    moc.write_text(text, encoding="utf-8")


def apply_replacements(text: str, replacements: list[tuple[str, str]]) -> str:
    for a, b in replacements:
        text = text.replace(a, b)
    return text


def fix_tags_frontmatter(text: str, tag_replacements: list[tuple[str, str]]) -> str:
    # simple string-based tag replacements; safe in this repo because tags are stable tokens
    for a, b in tag_replacements:
        text = re.sub(rf"(?m)^\s*-\s*{re.escape(a)}\s*$", f"  - {b}", text)
    return text


def main() -> int:
    # 1) Folder renames to unify skeleton:
    renames = [
        ("02. Business/02.01. SRS/01. Constitution", "02. Business/02.01. SRS/01. Rules"),
        ("02. Business/02.02. SDS/02. Guides", "02. Business/02.02. SDS/03. Guides"),
        ("02. Business/02.03. SCS/02. Guides", "02. Business/02.03. SCS/03. Guides"),
    ]
    for s, d in renames:
        safe_rename_dir(ROOT / s, ROOT / d)

    # 2) Ensure missing skeleton folders exist with MOC placeholders
    # Target skeleton: 00. Index / 01. Rules / 02. Contract / 03. Guides / 04. Outputs
    srs = ROOT / "02. Business/02.01. SRS"
    sds = ROOT / "02. Business/02.02. SDS"
    scs = ROOT / "02. Business/02.03. SCS"

    for stage_dir in (srs, sds, scs):
        ensure_dir(stage_dir / "00. Index")
        ensure_dir(stage_dir / "01. Rules")
        ensure_dir(stage_dir / "02. Contract")
        ensure_dir(stage_dir / "03. Guides")
        ensure_dir(stage_dir / "04. Outputs")

    # 3) Move SDS interface contracts into 02. Contract (to match skeleton)
    sds_rules_dir = sds / "01. Rules"
    sds_contract_dir = sds / "02. Contract"
    for fname in [
        "🔗 SRS ↔ SDS Interface Contract.md",
        "🔗 SDS ↔ SCS Interface Contract.md",
    ]:
        src = sds_rules_dir / fname
        dst = sds_contract_dir / fname
        if src.exists() and not dst.exists():
            src.rename(dst)

    # 4) Create missing MOCs where needed (only for newly created folders)
    # We keep this conservative: only ensure Contract/Outputs MOCs exist for SDS/SCS if absent.
    write_moc_if_missing(
        sds / "02. Contract",
        tags=["00__System", "00_03__AI", "02__SDS", "02__Contract", "02__Business", "02_02__SDS"],
        backlinks=[f"[[00. Second-Brain-System/00.03. AI/02. Business/02.02. SDS/_MOC_.md|02.02. SDS]]"],
        outgoinglinks=[
            "[[00. Second-Brain-System/00.03. AI/02. Business/02.02. SDS/02. Contract/🔗 SRS ↔ SDS Interface Contract|🔗 SRS ↔ SDS Interface Contract]]",
            "[[00. Second-Brain-System/00.03. AI/02. Business/02.02. SDS/02. Contract/🔗 SDS ↔ SCS Interface Contract|🔗 SDS ↔ SCS Interface Contract]]",
        ],
    )
    write_moc_if_missing(
        sds / "04. Outputs",
        tags=["00__System", "00_03__AI", "02__SDS", "04__Outputs", "02__Business", "02_02__SDS"],
        backlinks=[f"[[00. Second-Brain-System/00.03. AI/02. Business/02.02. SDS/_MOC_.md|02.02. SDS]]"],
        outgoinglinks=[],
    )
    write_moc_if_missing(
        scs / "02. Contract",
        tags=["00__System", "00_03__AI", "03__SCS", "02__Contract", "02__Business", "02_03__SCS"],
        backlinks=[f"[[00. Second-Brain-System/00.03. AI/02. Business/02.03. SCS/_MOC_.md|02.03. SCS]]"],
        outgoinglinks=[],
    )
    write_moc_if_missing(
        scs / "04. Outputs",
        tags=["00__System", "00_03__AI", "03__SCS", "04__Outputs", "02__Business", "02_03__SCS"],
        backlinks=[f"[[00. Second-Brain-System/00.03. AI/02. Business/02.03. SCS/_MOC_.md|02.03. SCS]]"],
        outgoinglinks=[],
    )

    # 5) Global link/path replacements
    replacements = [
        # SRS constitution -> rules
        ("02. Business/02.01. SRS/01. Constitution/", "02. Business/02.01. SRS/01. Rules/"),
        ("02. Business/02.01. SRS/01. Constitution", "02. Business/02.01. SRS/01. Rules"),
        # SDS guides folder rename
        ("02. Business/02.02. SDS/02. Guides/", "02. Business/02.02. SDS/03. Guides/"),
        ("02. Business/02.02. SDS/02. Guides", "02. Business/02.02. SDS/03. Guides"),
        # SCS guides folder rename
        ("02. Business/02.03. SCS/02. Guides/", "02. Business/02.03. SCS/03. Guides/"),
        ("02. Business/02.03. SCS/02. Guides", "02. Business/02.03. SCS/03. Guides"),
        # SDS interface contracts moved to 02. Contract
        ("02. Business/02.02. SDS/01. Rules/🔗 SRS ↔ SDS Interface Contract", "02. Business/02.02. SDS/02. Contract/🔗 SRS ↔ SDS Interface Contract"),
        ("02. Business/02.02. SDS/01. Rules/🔗 SDS ↔ SCS Interface Contract", "02. Business/02.02. SDS/02. Contract/🔗 SDS ↔ SCS Interface Contract"),
        ("02. Business/02.02. SDS/01. Rules/🔗 SRS ↔ SDS Interface Contract.md", "02. Business/02.02. SDS/02. Contract/🔗 SRS ↔ SDS Interface Contract.md"),
        ("02. Business/02.02. SDS/01. Rules/🔗 SDS ↔ SCS Interface Contract.md", "02. Business/02.02. SDS/02. Contract/🔗 SDS ↔ SCS Interface Contract.md"),
    ]

    tag_replacements = [
        ("01__Constitution", "01__Rules"),
        ("02__Guides", "03__Guides"),
        ("01__Index", "00__Index"),
    ]

    changed = 0
    for f in iter_md_files():
        txt = f.read_text(encoding="utf-8", errors="ignore")
        new = apply_replacements(txt, replacements)
        new = fix_tags_frontmatter(new, tag_replacements)
        if new != txt:
            f.write_text(new, encoding="utf-8")
            changed += 1

    print(f"Updated files (text/tag refs): {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

