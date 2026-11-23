"""
Agent Master Prompt Generator

Purpose:
- Auto-generate Agent-specific Master Prompt by combining:
  1. OS Master Prompt (full)
  2. Role Rule.md
  3. Validation Checklist.md (optional)
  4. Domain Knowledge.md (optional)

Design:
- Default: uses 04. Agent/_MOC_.md to discover Active Roles and processes all of them.
- Optional: --role "01. Role Name" to process a single role only.
- Similar to os_master_prompt_generator.py
- Python stdlib only (no dependencies)
- Preserves frontmatter, updates References
- Supports --check, --diff, --write, --bump-version
"""

from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass(frozen=True)
class Config:
    ai_root: Path
    role_path: str  # e.g., "01. Computer-Science Expert"
    agent_root_rel: Path = Path("04. Agent")
    os_artifact_rel: Path = Path("03. Operation System/99. Artifact/Master Prompt.md")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def _max_backtick_run(s: str) -> int:
    return max((len(m.group(0)) for m in re.finditer(r"`+", s)), default=0)


def _fence_for_content(content: str) -> str:
    n = max(3, _max_backtick_run(content) + 1)
    return "`" * n


def _rel_from_ai_root(ai_root: Path, path: Path) -> str:
    return path.relative_to(ai_root).as_posix()


def _get_moc_path(ai_root: Path) -> Path:
    return ai_root / "04. Agent" / "_MOC_.md"


def _list_roles_from_moc(moc_path: Path) -> List[str]:
    """Parse _MOC_.md and return list of role folder names in ### Active Roles."""
    if not moc_path.exists():
        return []
    text = moc_path.read_text(encoding="utf-8")
    folders: List[str] = []
    in_section = False
    for line in text.splitlines():
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


def _collect_role_sources(cfg: Config) -> List[Path]:
    """Collect sources for Agent Master Prompt.
    
    Order:
    1. OS Master Prompt (full)
    2. Role Rule.md
    3. Validation Checklist.md (if exists)
    4. Domain Knowledge.md (if exists)
    5. 00. Template/Persona Output Template.md (if exists)
    """
    sources: List[Path] = []
    
    # 1. OS Master Prompt (full)
    os_artifact = cfg.ai_root / cfg.os_artifact_rel
    if os_artifact.exists():
        sources.append(os_artifact)
    
    # 2. Role Rule
    role_root = cfg.ai_root / cfg.agent_root_rel / cfg.role_path
    role_rule = role_root / "Role Rule.md"
    if role_rule.exists():
        sources.append(role_rule)
    
    # 3. Validation Checklist (optional)
    checklist = role_root / "Validation Checklist.md"
    if checklist.exists():
        sources.append(checklist)
    
    # 4. Domain Knowledge (optional)
    domain = role_root / "Domain Knowledge.md"
    if domain.exists():
        sources.append(domain)
    
    # 5. Persona Output Template (optional) — 출력 형식 정의, 첨부 시 단일 파일로 완결
    persona_template = role_root / "00. Template" / "Persona Output Template.md"
    if persona_template.exists():
        sources.append(persona_template)
    
    return sources


def _parse_frontmatter(doc: str) -> Tuple[dict, str]:
    """Returns (frontmatter_dict, body_text)."""
    if not doc.startswith("---\n"):
        return {}, doc
    end = doc.find("\n---\n", 4)
    if end == -1:
        return {}, doc
    fm_text = doc[4:end]
    body = doc[end + len("\n---\n") :]

    fm: dict = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def _render_frontmatter(
    existing: str | None,
    references: List[str],
    version_bump: bool,
    stamp_updated: bool,
    role_name: str,
) -> str:
    now = _dt.date.today().isoformat()

    existing_fm: dict = {}
    if existing:
        existing_fm, _ = _parse_frontmatter(existing)

    def pick(key: str, default: str) -> str:
        return existing_fm.get(key, default)

    version = pick("Version", "v1.0")
    if version_bump:
        version = _bump_version(version)

    lines: List[str] = []
    lines.append("---")
    lines.append(f"type: {pick('type','Artifact')}")
    lines.append(f"creation date: {pick('creation date', now)}")
    lines.append("tags:")
    lines.append("  - 00__System")
    lines.append("  - 00_03__AI")
    lines.append("  - 04__Agent")
    # Role-specific tag
    role_tag = role_name.replace(" ", "_").replace("-", "_")
    lines.append(f"  - {role_tag}")
    lines.append(f"Version: {version}")
    lines.append(f"Status: {pick('Status','Active')}")
    lines.append(
        f"Purpose: {pick('Purpose', f'Single-file attachment (OS + {role_name} Role)')}"
    )
    if stamp_updated:
        lines.append(f"updated date: {now}")
    lines.append("References:")
    for r in references:
        lines.append(f"  - {r}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _bump_version(v: str) -> str:
    m = re.match(r"^v(\d+)\.(\d+)$", v.strip())
    if not m:
        return v
    major = int(m.group(1))
    minor = int(m.group(2)) + 1
    return f"v{major}.{minor}"


def generate_agent_master_prompt(
    cfg: Config, *, version_bump: bool, stamp_updated: bool
) -> str:
    role_root = cfg.ai_root / cfg.agent_root_rel / cfg.role_path
    
    # Extract role name (e.g., "01. Computer-Science Expert" -> "Computer-Science Expert")
    role_name = cfg.role_path.split("/")[-1]  # e.g., "01. Computer-Science Expert"
    # Remove numbering prefix (e.g., "01. " or "02. ")
    role_name_clean = re.sub(r'^\d+\.\s*', '', role_name)  # e.g., "Computer-Science Expert"
    
    # Output file name with role name
    out_path = role_root / "99. Artifact" / f"{role_name_clean}.md"
    existing_text = _read_text(out_path) if out_path.exists() else ""

    sources = _collect_role_sources(cfg)
    references = [_rel_from_ai_root(cfg.ai_root, p) for p in sources]

    fm = _render_frontmatter(
        existing_text,
        references,
        version_bump=version_bump,
        stamp_updated=stamp_updated,
        role_name=role_name_clean,
    )

    title = f"# {role_name_clean} — Master Prompt (OS + Role)\n"
    intro = (
        "\n"
        "## 00. 목적\n\n"
        f"이 문서는 **{role_name_clean} Role**을 위한 마스터 파일이다.  \n"
        "`03. Operation System` 전체 + Role 확장 규칙을 **단일 파일로 통합**한다.\n\n"
        "## 01. 적용 방식 (중요)\n\n"
        "- 본 파일의 모든 내용(아래의 모든 블록 포함)은 **규칙/지침으로 간주**한다.\n"
        "- 상위 우선순위:\n"
        "  - OS Layer 0 (Governance Kernel) → Layer 1 → Layer 2 → Layer 3 → Layer 4 → Role 확장 규칙\n\n"
        "## 02. 통합 원문 (Verbatim Sources)\n\n"
        "아래는 OS 및 Role 구성 문서들의 원문을 그대로 포함한다.\n"
    )

    blocks: List[str] = []
    for p in sources:
        rel = _rel_from_ai_root(cfg.ai_root, p)
        content = _read_text(p)
        fence = _fence_for_content(content)
        # Python 3.9 호환: f-string 표현식 안에서 백슬래시를 쓸 수 없으므로 미리 계산한다.
        tail = "" if content.endswith("\n") else "\n"
        blocks.append(
            f"\n### Source: `{rel}`\n\n"
            f"{fence}text\n"
            f"{content}{tail}"
            f"{fence}\n"
        )

    return fm + "---\n" + title + intro + "".join(blocks)


def _unified_diff(a: str, b: str, fromfile: str, tofile: str) -> str:
    a_lines = a.splitlines(keepends=True)
    b_lines = b.splitlines(keepends=True)
    return "".join(difflib.unified_diff(a_lines, b_lines, fromfile=fromfile, tofile=tofile))


def _print_check_tree(
    agent_root: Path, role_results: List[Tuple[str, bool]]
) -> None:
    """Print --check results as a tree (04. Agent / Role / 99. Artifact / file  OK|DIFF)."""
    root_name = agent_root.name  # "04. Agent"
    lines: List[str] = [root_name]
    for i, (role_path, differs) in enumerate(role_results):
        role_name = role_path.split("/")[-1]
        role_name_clean = re.sub(r"^\d+\.\s*", "", role_name)
        artifact_rel = f"99. Artifact/{role_name_clean}.md"
        status = "DIFF" if differs else "OK"
        is_last_role = i == len(role_results) - 1
        branch = "└── " if is_last_role else "├── "
        lines.append(f"{branch}{role_path}/")
        prefix = "    " if is_last_role else "│   "
        lines.append(f"{prefix}└── {artifact_rel}  {status}")
    print("\n".join(lines))


def _process_one_role(
    cfg: Config,
    *,
    check: bool,
    diff: bool,
    write: bool,
    version_bump: bool,
    stamp_updated: bool,
) -> Tuple[bool, str]:
    """
    Process a single role: generate, then check/diff/write.
    Returns (differs, out_path_str).
    """
    role_root = cfg.ai_root / cfg.agent_root_rel / cfg.role_path
    role_name = cfg.role_path.split("/")[-1]
    role_name_clean = re.sub(r"^\d+\.\s*", "", role_name)
    out_path = role_root / "99. Artifact" / f"{role_name_clean}.md"

    if not role_root.exists():
        return True, str(out_path)  # treat missing as "differs"

    generated = generate_agent_master_prompt(
        cfg, version_bump=version_bump, stamp_updated=stamp_updated
    )
    existing = _read_text(out_path) if out_path.exists() else ""
    differs = existing != generated

    if differs and diff:
        print(
            _unified_diff(
                existing,
                generated,
                fromfile=str(out_path),
                tofile=str(out_path) + " (generated)",
            )
        )
    if write and differs:
        _write_text(out_path, generated)
        print(f"Written: {out_path}")

    return differs, str(out_path)


def main() -> int:
    # Windows console robustness
    try:
        import sys

        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass

    ap = argparse.ArgumentParser(
        description="Generate Agent Master Prompt (OS + Role). Default: all roles from 04. Agent/_MOC_.md."
    )
    ap.add_argument(
        "--ai-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to 00.03. AI folder",
    )
    ap.add_argument(
        "--role",
        default=None,
        help='Single role only (e.g., "01. Computer-Science Expert"). If omitted, use all roles from _MOC_.md.',
    )
    ap.add_argument("--write", action="store_true", help="Write output file(s)")
    ap.add_argument(
        "--check", action="store_true", help="Exit non-zero if output differs"
    )
    ap.add_argument(
        "--diff", action="store_true", help="Print diff if output differs"
    )
    ap.add_argument(
        "--bump-version", action="store_true", help="Bump Version vX.Y -> vX.(Y+1)"
    )
    ap.add_argument(
        "--stamp-updated",
        action="store_true",
        help="Add/refresh updated date in frontmatter",
    )
    args = ap.parse_args()

    ai_root = Path(args.ai_root)
    agent_root = ai_root / "04. Agent"
    moc_path = _get_moc_path(ai_root)

    # Resolve role list: from --role (single) or from _MOC_.md (all)
    if args.role is not None:
        roles_to_process = [args.role.strip()]
    else:
        if not moc_path.exists():
            print(f"ERROR: MOC not found: {moc_path}")
            print("Either create 04. Agent/_MOC_.md or use --role to process a single role.")
            return 1
        roles_to_process = _list_roles_from_moc(moc_path)
        if not roles_to_process:
            print("ERROR: No Active Roles found in _MOC_.md.")
            return 1
        # Filter to roles that actually exist on disk
        existing_roles = [r for r in roles_to_process if (agent_root / r).exists()]
        if not existing_roles:
            print("ERROR: No role folders from _MOC_.md exist on disk.")
            return 1
        if len(existing_roles) < len(roles_to_process):
            missing = set(roles_to_process) - set(existing_roles)
            print(f"Note: Skipping roles not on disk: {', '.join(sorted(missing))}")
        roles_to_process = existing_roles

    # Default (no --check, --diff, --write): just print output path(s)
    if not (args.check or args.diff or args.write):
        for role_path in roles_to_process:
            role_name = role_path.split("/")[-1]
            role_name_clean = re.sub(r"^\d+\.\s*", "", role_name)
            out_path = agent_root / role_path / "99. Artifact" / f"{role_name_clean}.md"
            print(str(out_path))
        return 0

    any_differs = False
    role_results: List[Tuple[str, bool]] = []
    for role_path in roles_to_process:
        cfg = Config(ai_root=ai_root, role_path=role_path)
        differs, _ = _process_one_role(
            cfg,
            check=args.check,
            diff=args.diff,
            write=args.write,
            version_bump=args.bump_version,
            stamp_updated=args.stamp_updated,
        )
        if differs:
            any_differs = True
        role_results.append((role_path, differs))

    if args.check and not args.diff:
        _print_check_tree(agent_root, role_results)
        if any_differs:
            suffix = " all." if len(roles_to_process) > 1 else ""
            print(f"\nNext: run with `--diff` to view changes or `--write` to update{suffix}")
        else:
            n = len(roles_to_process)
            print(f"\nOK: {'All ' + str(n) + ' roles are' if n > 1 else 'Role is'} up to date.")
        return 1 if any_differs else 0

    if args.diff and any_differs:
        return 1
    if args.write:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
