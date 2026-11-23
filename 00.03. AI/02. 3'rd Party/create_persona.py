"""
Create a new Persona (or Role) under 04. Agent with scaffold and Persona Output Template.

Purpose:
- User inputs: Persona Name, Persona Role (one-line description)
- Creates 04. Agent/<NN>. <Name>/ with Role Rule, 00. Template/Persona Output Template.md,
  optional Persona Profile, Validation Checklist, Domain Knowledge, 99. Artifact/
- Persona Output Template is a copy of OS Output Template; user can edit it for internal format.
- Role Rule references 00. Template/Persona Output Template.md for output format.

Usage:
  python create_persona.py --name "My Persona" --role "한 줄 설명"
  python create_persona.py --name "My Persona" --role "한 줄 설명" --type role
  python create_persona.py --name "My Persona" --role "한 줄 설명" --no-artifact
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional


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


def _next_role_number(agent_root: Path) -> int:
    """Return next available role number (e.g. 4 if 01, 02, 03 exist)."""
    roles = _list_role_folders(agent_root)
    if not roles:
        return 1
    numbers: List[int] = []
    for r in roles:
        m = re.match(r"^(\d+)\.\s+.+", r.name)
        if m:
            numbers.append(int(m.group(1)))
    return max(numbers) + 1 if numbers else 1


def _role_folder_name(number: int, name: str) -> str:
    """e.g. 4, 'My Persona' -> '04. My Persona'."""
    return f"{number:02d}. {name}"


def create_persona(
    ai_root: Path,
    name: str,
    role_description: str,
    persona_type: str = "persona",
    create_artifact: bool = True,
) -> int:
    agent_root = ai_root / "04. Agent"
    if not agent_root.exists():
        print("ERROR: 04. Agent not found under ai_root")
        return 1

    nn = _next_role_number(agent_root)
    folder_name = _role_folder_name(nn, name)
    role_root = agent_root / folder_name
    if role_root.exists():
        print(f"ERROR: Folder already exists: {role_root}")
        return 1

    # Paths to templates (relative to ai_root)
    if persona_type == "role":
        rule_src = ai_root / "04. Agent" / "00. Template" / "Role Rule Template.md"
    else:
        rule_src = ai_root / "04. Agent" / "00. Template" / "Persona Template.md"

    os_output_tpl = ai_root / "03. Operation System" / "90. Annex (Operational Standards)" / "00. Templates" / "OS Output Template.md"

    if not rule_src.exists():
        print(f"ERROR: Template not found: {rule_src}")
        return 1
    if not os_output_tpl.exists():
        print(f"ERROR: OS Output Template not found: {os_output_tpl}")
        return 1

    role_root.mkdir(parents=True)

    # 1. Role Rule.md from template + placeholder replacement
    rule_text = rule_src.read_text(encoding="utf-8")
    # Replace 00. Role section (Persona)
    rule_text = re.sub(
        r"- \*\*Role Name\*\*: \(예:[^\)]+\)",
        f"- **Role Name**: {name}",
        rule_text,
        count=1,
    )
    rule_text = re.sub(
        r"- \*\*Audience/Domain\*\*: \(예:[^\)]+\)",
        f"- **Audience/Domain**: {role_description}",
        rule_text,
        count=1,
    )
    rule_text = re.sub(
        r"- \*\*Applies To\*\*: \(예:[^\)]+\)",
        "- **Applies To**: (사용자 정의)",
        rule_text,
        count=1,
    )
    # Inject Persona Output Template reference (after "추가 산출물 템플릿" example lines)
    output_tpl_line = (
        "- 정리 요청·산출물 출력 시 **내부 형식**은 본 Role의 "
        "`00. Template/Persona Output Template.md`를 따른다. "
        "OS 기본 형식(단일 코드 블록, #Tag 한 줄, YAML 금지, Footnote 3요소)은 유지한다."
    )
    if "00. Template/Persona Output Template.md" not in rule_text:
        # Insert after output template example line (Persona or Role template)
        if "- (예) 분석/설계/정리 템플릿" in rule_text:
            rule_text = rule_text.replace(
                "- (예) 분석/설계/정리 템플릿\n",
                f"- (예) 분석/설계/정리 템플릿\n- {output_tpl_line}\n",
                1,
            )
        elif "- (예) 도메인 전용 섹션/표/매핑 포맷" in rule_text:
            rule_text = rule_text.replace(
                "- (예) 도메인 전용 섹션/표/매핑 포맷\n",
                f"- (예) 도메인 전용 섹션/표/매핑 포맷\n- {output_tpl_line}\n",
                1,
            )
        elif "- 도메인 전용 섹션/표/매핑 포맷" in rule_text:
            rule_text = rule_text.replace(
                "- 도메인 전용 섹션/표/매핑 포맷\n",
                f"- 도메인 전용 섹션/표/매핑 포맷\n- {output_tpl_line}\n",
                1,
            )
    (role_root / "Role Rule.md").write_text(rule_text, encoding="utf-8")

    # 2. 00. Template/Persona Output Template.md
    template_dir = role_root / "00. Template"
    template_dir.mkdir(parents=True)
    os_content = os_output_tpl.read_text(encoding="utf-8")
    intro = (
        f"> 본 문서는 **{name}** 전용 산출물 출력 형식 템플릿이다. "
        "OS Output Template을 확장하며, **아래 본문 구조(섹션·테이블·항목)는 사용자가 수정**할 수 있다. "
        "Persona Agent는 정리 요청·산출물 출력 시 OS 래핑(단일 코드 블록, #Tag, Footnote 3요소 등)을 유지한 채, "
        "본 템플릿의 내부 형식을 기준으로 출력한다.\n\n"
    )
    # Insert after first --- (after frontmatter) or after "# OS Output Template"
    if "---\n\n## 01." in os_content:
        persona_content = os_content.replace(
            "---\n\n## 01.",
            "---\n\n" + intro + "## 01.",
            1,
        )
    else:
        persona_content = intro + os_content
    # Change title to Persona Output Template
    persona_content = persona_content.replace(
        "# OS Output Template (기본 산출물 출력 형식)",
        f"# Persona Output Template — {name}",
        1,
    )
    (template_dir / "Persona Output Template.md").write_text(persona_content, encoding="utf-8")

    # 3. Stub files
    (role_root / "Persona Profile.md").write_text(
        f"---\ntype: Persona Profile\n---\n\n# {name} — Persona Profile\n\n(사용자 작성)\n",
        encoding="utf-8",
    )
    (role_root / "Validation Checklist.md").write_text(
        f"---\ntype: Checklist\n---\n\n# {name} — Validation Checklist\n\n(사용자 작성)\n",
        encoding="utf-8",
    )
    (role_root / "Domain Knowledge.md").write_text(
        f"---\ntype: Reference\n---\n\n# {name} — Domain Knowledge\n\n(참조용, 사용자 작성)\n",
        encoding="utf-8",
    )

    # 4. 99. Artifact
    if create_artifact:
        artifact_dir = role_root / "99. Artifact"
        artifact_dir.mkdir(parents=True)
        artifact_name = f"{name}.md"
        (artifact_dir / "readme.md").write_text(
            f"---\ntype: Guide\n---\n\n# 99. Artifact — 사용 가이드\n\n"
            f"`99. Artifact`는 **{name}** Persona를 AI 플랫폼에 등록하기 위한 통합 파일을 보관한다.\n\n"
            f"- **Master Prompt**: `{artifact_name}` — OS + Role 통합본 (스크립트로 생성 권장)\n"
            f"- 생성: `python \"02. 3'rd Party/agent_master_prompt_generator.py\" --role \"{folder_name}\" --write`\n",
            encoding="utf-8",
        )
        (artifact_dir / artifact_name).write_text(
            f"<!-- Master Prompt는 agent_master_prompt_generator.py로 생성 -->\n",
            encoding="utf-8",
        )

    # 5. _MOC_.md update
    moc_path = agent_root / "_MOC_.md"
    if moc_path.exists():
        moc_text = moc_path.read_text(encoding="utf-8")
        new_line = f"- `{folder_name}/` — {role_description}\n"
        # Insert before "### Shared Resources" or at end of last role block
        if "### Shared Resources" in moc_text:
            moc_text = moc_text.replace(
                "\n### Shared Resources",
                f"\n{new_line}\n### Shared Resources",
                1,
            )
        else:
            # Append before "## 02. Quick Navigation"
            moc_text = moc_text.replace(
                "\n## 02. Quick Navigation",
                f"\n{new_line}\n## 02. Quick Navigation",
                1,
            )
        moc_path.write_text(moc_text, encoding="utf-8")

    print(f"Created: {role_root.relative_to(ai_root)}")
    print(f"  Role Rule.md (from {'Persona' if persona_type == 'persona' else 'Role'} template)")
    print(f"  00. Template/Persona Output Template.md (OS Output Template + 편집 가능)")
    print(f"  Persona Profile.md, Validation Checklist.md, Domain Knowledge.md")
    if create_artifact:
        print(f"  99. Artifact/readme.md, 99. Artifact/{name}.md")
    print(f"  _MOC_.md updated")
    print()
    print("Next steps:")
    print(f"  1. Edit Role Rule.md and 00. Template/Persona Output Template.md as needed.")
    if create_artifact:
        print(f'  2. python "02. 3\'rd Party/agent_master_prompt_generator.py" --role "{folder_name}" --write')
        print(f'  3. python "02. 3\'rd Party/validate_agent_structure.py"')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Create a new Persona (or Role) under 04. Agent with Persona Output Template"
    )
    ap.add_argument("--name", required=True, help="Persona name (e.g. 'Computer-Science Expert')")
    ap.add_argument("--role", required=True, help="One-line role description (e.g. 'CS 이론 전문가')")
    ap.add_argument(
        "--type",
        choices=("persona", "role"),
        default="persona",
        help="Base template: persona (default) or role",
    )
    ap.add_argument("--ai-root", type=Path, default=None, help="Root of 00.03. AI")
    ap.add_argument(
        "--no-artifact",
        action="store_true",
        help="Do not create 99. Artifact folder and files",
    )
    args = ap.parse_args()
    ai_root = args.ai_root or _ai_root_default()
    return create_persona(
        ai_root=ai_root,
        name=args.name.strip(),
        role_description=args.role.strip(),
        persona_type=args.type,
        create_artifact=not args.no_artifact,
    )


if __name__ == "__main__":
    sys.exit(main())
