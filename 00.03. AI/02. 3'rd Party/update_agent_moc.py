"""
Update 04. Agent/_MOC_.md from folder structure (Map of Contents only).

Purpose:
- Keep _MOC_.md as a pure Map of Contents: index of roles and key links only.
- Regenerate the "### Active Roles" section from actual 04. Agent folder structure.
- Intended for future use: guideline update check, view changes, apply updates.

Usage:
  python update_agent_moc.py [--ai-root PATH] [--check | --diff | --write]
  --check   Report whether MOC is in sync with disk (exit 0 = in sync).
  --diff    Print the new Active Roles section (no file change).
  --write   Update 04. Agent/_MOC_.md with the new Active Roles section.
  Default: --check if no mode is given.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


def _ai_root_default() -> Path:
    return Path(__file__).resolve().parent.parent


def _list_role_folders(agent_root: Path) -> List[Path]:
    """Return 01. X, 02. Y, ... excluding 00. Template and 90. Shared Resources."""
    roles: List[Path] = []
    for p in agent_root.iterdir():
        if not p.is_dir():
            continue
        name = p.name
        if name.startswith("00. ") or name.startswith("90. "):
            continue
        if re.match(r"^\d+\.\s+.+", name):
            roles.append(p)
    return sorted(roles)


def _role_artifact_name(role_folder_name: str) -> str:
    """e.g. '01. Computer-Science Expert' -> 'Computer-Science Expert'."""
    return re.sub(r"^\d+\.\s+", "", role_folder_name).strip()


def _get_role_description(role_root: Path) -> str:
    """Extract one-line description from Role Rule.md (Domain or Role Name)."""
    rule = role_root / "Role Rule.md"
    if not rule.exists():
        return "(설명 없음)"
    text = rule.read_text(encoding="utf-8")
    for pattern in (r"-\s*\*\*Domain\*\*:\s*(.+)", r"-\s*\*\*Role Name\*\*:\s*(.+)"):
        m = re.search(pattern, text)
        if m:
            desc = m.group(1).strip()
            if desc:
                return desc
    return "(설명 없음)"


def _list_role_sub_items(role_root: Path, role_folder_name: str) -> List[str]:
    """List standard sub-items for MOC (Role Rule, Persona, Checklist, 99. Artifact)."""
    items: List[str] = []
    if (role_root / "Role Rule.md").exists():
        items.append("Role Rule")
    if (role_root / "Persona Profile.md").exists():
        items.append("Persona Profile")
    if (role_root / "Validation Checklist.md").exists():
        items.append("Validation Checklist")
    if (role_root / "Domain Knowledge.md").exists() or (role_root / "Domain Knowledge").exists():
        items.append("Domain Knowledge")
    artifact_dir = role_root / "99. Artifact"
    artifact_name = f"{_role_artifact_name(role_folder_name)}.md"
    if (artifact_dir / artifact_name).exists():
        items.append(f"99. Artifact/ - {artifact_name}")
    elif artifact_dir.exists():
        items.append("99. Artifact/")
    return items


def build_active_roles_section(agent_root: Path) -> str:
    """Build the ### Active Roles markdown block from disk."""
    lines: List[str] = ["### Active Roles"]
    for role_path in _list_role_folders(agent_root):
        name = role_path.name
        desc = _get_role_description(role_path)
        lines.append(f"- `{name}/` - {desc}")
        for sub in _list_role_sub_items(role_path, name):
            lines.append(f"  - {sub}")
        lines.append("")
    return "\n".join(lines).rstrip()


def parse_moc_active_role_folders(moc_text: str) -> List[str]:
    """Parse _MOC_.md and return list of role folder names in ### Active Roles."""
    folders: List[str] = []
    in_section = False
    for line in moc_text.splitlines():
        if line.strip() == "### Active Roles":
            in_section = True
            continue
        if in_section:
            if line.startswith("### ") or line.startswith("## "):
                break
            m = re.match(r"^-\s*`([^`]+)/`", line)
            if m:
                folders.append(m.group(1).strip())
    return folders


def get_moc_path(ai_root: Path) -> Path:
    return ai_root / "04. Agent" / "_MOC_.md"


def replace_active_roles_in_moc(moc_text: str, new_active_section: str) -> str:
    """Replace ### Active Roles section with new content; keep rest unchanged."""
    out: List[str] = []
    i = 0
    lines = moc_text.splitlines()
    while i < len(lines):
        if lines[i].strip() == "### Active Roles":
            out.append("### Active Roles")
            out.append("")
            for line in new_active_section.splitlines():
                if line.strip() == "### Active Roles":
                    continue
                out.append(line)
            out.append("")  # blank before next section
            # skip until next ### or ##
            i += 1
            while i < len(lines) and not re.match(r"^#{2,3}\s", lines[i]):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Update 04. Agent/_MOC_.md (Map of Contents) from folder structure"
    )
    ap.add_argument(
        "--ai-root",
        type=Path,
        default=None,
        help="Root of 00.03. AI (default: parent of script's parent)",
    )
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true", help="Report if MOC is in sync with disk")
    g.add_argument("--diff", action="store_true", help="Print new Active Roles section only")
    g.add_argument("--write", action="store_true", help="Write updated _MOC_.md")
    args = ap.parse_args()

    ai_root = args.ai_root or _ai_root_default()
    agent_root = ai_root / "04. Agent"
    moc_path = get_moc_path(ai_root)

    if not agent_root.exists():
        print("ERROR: 04. Agent not found under ai_root", file=sys.stderr)
        return 1
    if not moc_path.exists() and (args.write or args.check):
        print("ERROR: _MOC_.md not found", file=sys.stderr)
        return 1

    disk_folders = [p.name for p in _list_role_folders(agent_root)]
    new_section = build_active_roles_section(agent_root)

    if args.diff:
        print(new_section)
        return 0

    if args.write:
        moc_text = moc_path.read_text(encoding="utf-8")
        updated = replace_active_roles_in_moc(moc_text, new_section)
        moc_path.write_text(updated, encoding="utf-8")
        print("Updated 04. Agent/_MOC_.md (Active Roles section).")
        return 0

    # --check (default)
    if not moc_path.exists():
        print("MOC not found; run with --write to create from template (not implemented).")
        return 1
    moc_text = moc_path.read_text(encoding="utf-8")
    moc_folders = parse_moc_active_role_folders(moc_text)
    in_moc_not_disk = set(moc_folders) - set(disk_folders)
    in_disk_not_moc = set(disk_folders) - set(moc_folders)
    if not in_moc_not_disk and not in_disk_not_moc:
        print("OK: _MOC_.md is in sync with 04. Agent folder structure.")
        return 0
    if in_disk_not_moc:
        print("MOC missing role folders (on disk):", ", ".join(sorted(in_disk_not_moc)))
    if in_moc_not_disk:
        print("MOC lists role folders not on disk:", ", ".join(sorted(in_moc_not_disk)))
    print("Run with --write to update _MOC_.md.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
