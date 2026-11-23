"""
OS Master Prompt Generator

Purpose:
- Auto-generate `03. Operation System/99. Artifact/Master Prompt.md`
  by concatenating verbatim sources from:
    - 00. Governance Kernel
    - 01. Cognitive Engine
    - 02. Validation Engine (+ Checklists)
    - 03. Self-Reflection Loop
    - 04. Artifact Engine
    - 90. Annex (Operational Standards) (+ Templates)

Design notes:
- Uses only Python stdlib (no dependencies).
- Preserves existing Master Prompt frontmatter fields where possible,
  but rewrites `References:` to reflect actual included sources.
- Embeds each source file verbatim in a fenced code block using a fence
  length greater than any backtick run in the content.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


@dataclass(frozen=True)
class Config:
    ai_root: Path
    os_root_rel: Path = Path("03. Operation System")
    out_rel: Path = Path("03. Operation System/99. Artifact/Master Prompt.md")


def _read_text(path: Path) -> str:
    # Normalize to LF for deterministic embedding/diffs
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Force LF newlines on Windows as well
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def _max_backtick_run(s: str) -> int:
    return max((len(m.group(0)) for m in re.finditer(r"`+", s)), default=0)


def _fence_for_content(content: str) -> str:
    # At least 3 backticks; strictly longer than any run inside content.
    n = max(3, _max_backtick_run(content) + 1)
    return "`" * n


def _rel_from_ai_root(ai_root: Path, path: Path) -> str:
    return path.relative_to(ai_root).as_posix()


def _collect_sources(cfg: Config) -> List[Path]:
    os_root = cfg.ai_root / cfg.os_root_rel

    include_dirs = [
        os_root / "00. Governance Kernel",
        os_root / "01. Cognitive Engine",
        os_root / "02. Validation Engine",
        os_root / "02. Validation Engine" / "Checklists",
        os_root / "03. Self-Reflection Loop",
        os_root / "04. Artifact Engine",
        os_root / "90. Annex (Operational Standards)",
        os_root / "90. Annex (Operational Standards)" / "00. Templates",
    ]

    # Collect all Markdown files under those directories, excluding:
    # - 99. Artifact (output artifacts)
    # - _MOC_.md (index)
    # - any hidden/system files
    sources: List[Path] = []
    for d in include_dirs:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            if any(part.startswith(".") for part in p.parts):
                continue
            # Exclusions
            if "99. Artifact" in p.parts:
                continue
            if p.name == "_MOC_.md":
                continue
            sources.append(p)

    # Deduplicate while preserving deterministic ordering by custom priority.
    seen = set()
    unique: List[Path] = []
    for p in sorted(sources, key=lambda x: _sort_key(cfg.ai_root, x)):
        if p in seen:
            continue
        seen.add(p)
        unique.append(p)
    return unique


def _sort_key(ai_root: Path, p: Path) -> Tuple:
    rel = _rel_from_ai_root(ai_root, p)

    # Explicit priority order matching OS reading flow
    priority_prefixes = [
        "03. Operation System/00. Governance Kernel/Kernel.md",
        "03. Operation System/00. Governance Kernel/Violation Policy.md",
        "03. Operation System/01. Cognitive Engine/Cognitive Engine.md",
        "03. Operation System/01. Cognitive Engine/Traceability Scheme.md",
        "03. Operation System/02. Validation Engine/Validation Engine.md",
        "03. Operation System/02. Validation Engine/NG-Fail Policy.md",
        "03. Operation System/02. Validation Engine/Checklists/Output Validation Checklist.md",
        "03. Operation System/02. Validation Engine/Checklists/Footnote Auto Checklist.md",
        "03. Operation System/03. Self-Reflection Loop/Reflection Loop.md",
        "03. Operation System/04. Artifact Engine/Artifact Engine.md",
        "03. Operation System/04. Artifact Engine/Output Modes.md",
        # Keep same order as current Master Prompt references
        "03. Operation System/90. Annex (Operational Standards)/📎 Custom Instructions Registration Pack Standard.md",
        "03. Operation System/90. Annex (Operational Standards)/📘 Operational Rules.md",
        "03. Operation System/90. Annex (Operational Standards)/🏷️ Tag & Metadata Governance.md",
        "03. Operation System/90. Annex (Operational Standards)/🧷 Link Display Name Style Guide.md",
        "03. Operation System/90. Annex (Operational Standards)/🧱 Stage Folder Skeleton Standard.md",
        "03. Operation System/90. Annex (Operational Standards)/🧾 Organizer Contract Standard.md",
        "03. Operation System/90. Annex (Operational Standards)/📜 StudyNote Output Contract.md",
        "03. Operation System/90. Annex (Operational Standards)/🖋️ StudyNote & EDU Integration Standard.md",
        "03. Operation System/90. Annex (Operational Standards)/🏗️ Business Stage Integration Standard (SRS-SDS-SCS).md",
        # Templates (stable order)
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/Input Coverage Declaration Template.md",
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/Trace Mapping Table Template.md",
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/RA Template.md",
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/Manager Plan Template.md",
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/Evaluator Report Template.md",
        "03. Operation System/90. Annex (Operational Standards)/00. Templates/Reflection Checklist Template.md",
    ]
    try:
        idx = priority_prefixes.index(rel)
        return (0, idx)
    except ValueError:
        # Fallback: sort by path to be deterministic
        return (1, rel)


def _parse_frontmatter(doc: str) -> Tuple[dict, str]:
    """
    Returns (frontmatter_dict, body_text).
    If no frontmatter, returns ({}, original_doc).
    """
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


def _render_frontmatter(existing: str | None, references: List[str], version_bump: bool, stamp_updated: bool) -> str:
    now = _dt.date.today().isoformat()

    existing_fm: dict = {}
    if existing:
        existing_fm, _ = _parse_frontmatter(existing)

    def pick(key: str, default: str) -> str:
        return existing_fm.get(key, default)

    # Keep existing values if present.
    version = pick("Version", "v1.0")
    if version_bump:
        version = _bump_version(version)

    lines: List[str] = []
    lines.append("---")
    lines.append(f"type: {pick('type','Artifact')}")
    lines.append(f"creation date: {pick('creation date', now)}")
    # Keep tags if they exist; else add minimal defaults
    if "tags" in existing_fm:
        # This parser doesn't handle yaml lists; keep a minimal default
        pass
    lines.append("tags:")
    lines.append("  - 00__System")
    lines.append("  - 00_03__AI")
    lines.append("  - 03__OperationSystem")
    lines.append(f"Version: {version}")
    lines.append(f"Status: {pick('Status','Active')}")
    lines.append(f"Purpose: {pick('Purpose','Single-file attachment (full OS guidance, verbatim sources)')}")
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


def generate_master_prompt(cfg: Config, *, version_bump: bool, stamp_updated: bool) -> str:
    out_path = cfg.ai_root / cfg.out_rel
    existing_text = _read_text(out_path) if out_path.exists() else ""

    sources = _collect_sources(cfg)
    references = [_rel_from_ai_root(cfg.ai_root, p) for p in sources]

    fm = _render_frontmatter(existing_text, references, version_bump=version_bump, stamp_updated=stamp_updated)

    title = "# Master Prompt — 03. Operation System (Full, Attachment)\n"
    intro = (
        "\n"
        "## 00. 목적\n\n"
        "이 문서는 `03. Operation System`의 **전체 지침을 단일 파일로 통합**한 “첨부용 마스터 파일”이다.  \n"
        "목적: ChatGPT 맞춤지침 / Gemini GEM 등에서 **파일 1개만 첨부**하여 OS를 적용하기 위함이다.\n\n"
        "## 01. 적용 방식(중요)\n\n"
        "- 본 파일의 모든 내용(아래의 모든 블록 포함)은 **규칙/지침으로 간주**한다.\n"
        "- 상위 우선순위:\n"
        "  - `Governance Kernel`(Layer 0) → Layer 1 → Layer 2 → Layer 3 → Layer 4 → Annex(운영 표준/템플릿)\n\n"
        "## 02. 통합 원문(Verbatim Sources)\n\n"
        "아래는 OS 구성 문서들의 원문을 그대로 포함한다.\n"
    )

    blocks: List[str] = []
    for p in sources:
        rel = _rel_from_ai_root(cfg.ai_root, p)
        content = _read_text(p)
        fence = _fence_for_content(content)
        # Ensure content ends with a single LF before closing fence.
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


def main() -> int:
    # Windows consoles may default to cp949 and fail on emoji filenames.
    # Make stdout robust for diff printing.
    try:
        import sys

        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--ai-root", default=str(Path(__file__).resolve().parents[1]), help="Path to 00.03. AI folder")
    ap.add_argument("--write", action="store_true", help="Write output file")
    ap.add_argument("--check", action="store_true", help="Exit non-zero if output differs")
    ap.add_argument("--diff", action="store_true", help="Print diff if output differs")
    ap.add_argument("--bump-version", action="store_true", help="Bump Version vX.Y -> vX.(Y+1)")
    ap.add_argument("--stamp-updated", action="store_true", help="Add/refresh updated date in frontmatter")
    args = ap.parse_args()

    cfg = Config(ai_root=Path(args.ai_root))
    out_path = cfg.ai_root / cfg.out_rel

    generated = generate_master_prompt(cfg, version_bump=args.bump_version, stamp_updated=args.stamp_updated)
    existing = _read_text(out_path) if out_path.exists() else ""

    if args.check or args.diff:
        differs = existing != generated

        # For beginners: print an explicit status line in --check mode.
        if args.check and not args.diff:
            if differs:
                print(f"DIFF: {out_path} differs from generated output.")
                print("Next: run with `--diff` to view changes or `--write` to update the file.")
            else:
                print(f"OK: {out_path} is up to date.")

        if differs:
            if args.diff:
                print(_unified_diff(existing, generated, fromfile=str(out_path), tofile=str(out_path) + " (generated)"))
            return 1 if args.check else 0
        return 0

    if args.write:
        _write_text(out_path, generated)
        return 0

    # Default: print where output would go
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

