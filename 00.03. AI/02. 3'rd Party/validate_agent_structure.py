"""
Validate Agent folder structure and OS compliance.

Purpose:
- Check each Role under 04. Agent for:
  1. Required files: Role Rule.md, 99. Artifact/<RoleName>.md
  2. OS inheritance declaration in Role Rule.md
  3. References in main Artifact include OS Master Prompt and Role Rule

Usage:
  python validate_agent_structure.py [--ai-root PATH]
  Exit 0 if all pass, 1 if any check fails.
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


def check_required_files(role_root: Path, role_name: str) -> Tuple[bool, List[str]]:
    """Check Role Rule.md and 99. Artifact/<RoleName>.md exist."""
    errors: List[str] = []
    rule = role_root / "Role Rule.md"
    if not rule.exists():
        errors.append(f"Missing: {rule.relative_to(role_root.parent)}")
    artifact_dir = role_root / "99. Artifact"
    artifact_name = f"{_role_artifact_name(role_name)}.md"
    artifact_file = artifact_dir / artifact_name
    if not artifact_file.exists():
        errors.append(f"Missing: 99. Artifact/{artifact_name}")
    return len(errors) == 0, errors


def check_os_inheritance(role_root: Path) -> Tuple[bool, List[str]]:
    """Check Role Rule.md contains OS inheritance and no-weakening declaration."""
    errors: List[str] = []
    rule = role_root / "Role Rule.md"
    if not rule.exists():
        return False, ["Role Rule.md missing"]
    text = rule.read_text(encoding="utf-8")
    if "OS" not in text or ("상속" not in text and "Layer 0" not in text and "Layer 1" not in text):
        errors.append("Role Rule.md: OS 상속 선언(또는 Layer 0~4) 문구 없음")
    if "약화" not in text and "무력화" not in text:
        errors.append("Role Rule.md: OS 약화/무력화 금지 문구 없음")
    return len(errors) == 0, errors


def check_artifact_references(ai_root: Path, role_root: Path, role_name: str) -> Tuple[bool, List[str]]:
    """Check main Artifact References (first frontmatter only) include OS Master Prompt and Role Rule."""
    errors: List[str] = []
    artifact_name = f"{_role_artifact_name(role_name)}.md"
    artifact_file = role_root / "99. Artifact" / artifact_name
    if not artifact_file.exists():
        return False, [f"99. Artifact/{artifact_name} 없음"]
    text = artifact_file.read_text(encoding="utf-8")
    if not text.strip().startswith("---"):
        errors.append(f"{artifact_name}: frontmatter 없음")
        return False, errors
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{artifact_name}: frontmatter 종료 없음")
        return False, errors
    fm = text[4:end]
    refs: List[str] = []
    in_refs = False
    for line in fm.splitlines():
        if line.strip() == "References:":
            in_refs = True
            continue
        if in_refs:
            if line.strip().startswith("- "):
                refs.append(line.strip()[2:].strip())
            elif line.strip() and not line.startswith(" "):
                in_refs = False
    if not any("Master Prompt.md" in r and "03. Operation System" in r for r in refs):
        errors.append(f"{artifact_name}: References에 OS Master Prompt 없음")
    if not any("Role Rule.md" in r and role_root.name in r for r in refs):
        errors.append(f"{artifact_name}: References에 본 Role Rule.md 없음")
    return len(errors) == 0, errors


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate 04. Agent structure and OS compliance")
    ap.add_argument(
        "--ai-root",
        type=Path,
        default=None,
        help="Root of 00.03. AI (default: parent of script's parent)",
    )
    args = ap.parse_args()
    ai_root = args.ai_root or _ai_root_default()
    agent_root = ai_root / "04. Agent"
    if not agent_root.exists():
        print("ERROR: 04. Agent not found under ai_root")
        return 1

    roles = _list_role_folders(agent_root)
    if not roles:
        print("No role folders found under 04. Agent")
        return 0

    all_ok = True
    for role_path in roles:
        role_name = role_path.name
        rel = role_path.relative_to(ai_root)
        print(f"\n--- {rel} ---")

        ok1, err1 = check_required_files(role_path, role_name)
        if not ok1:
            all_ok = False
            for e in err1:
                print(f"  FAIL: {e}")
        else:
            print("  OK: Required files")

        ok2, err2 = check_os_inheritance(role_path)
        if not ok2:
            all_ok = False
            for e in err2:
                print(f"  FAIL: {e}")
        else:
            print("  OK: OS inheritance declaration")

        ok3, err3 = check_artifact_references(ai_root, role_path, role_name)
        if not ok3:
            all_ok = False
            for e in err3:
                print(f"  FAIL: {e}")
        else:
            print("  OK: Artifact References")

    print()
    if all_ok:
        print("All checks passed.")
        return 0
    print("Some checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
