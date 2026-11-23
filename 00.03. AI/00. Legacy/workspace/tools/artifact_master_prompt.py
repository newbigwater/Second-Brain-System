from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules"}
CONFIG_PATH = Path(__file__).with_name("stage_targets.json")


def iter_md_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def split_frontmatter(text: str) -> tuple[str, str]:
    # returns (frontmatter_or_empty, body)
    m = re.match(r"(?s)\A---\n.*?\n---\n", text)
    if not m:
        return "", text
    return m.group(0), text[m.end() :]


def extract_first_fenced_block(text: str) -> str | None:
    # triple backticks, no language required. Return content inside the first fenced block.
    m = re.search(r"(?s)```[^\n]*\n(.*?)\n```", text)
    if not m:
        return None
    return m.group(1).strip("\n")


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def move_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    ensure_dir(dst.parent)
    if dst.exists():
        # keep dst as authoritative; convert src into deprecated stub later
        return False
    src.rename(dst)
    return True


def write_file(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


def mirror_artifact_to_workspace(base: str) -> None:
    """
    Mirror generated artifacts into `workspace/<base>/99. Artifact/`.
    This prevents drift for users who consume artifacts from the `workspace/` subtree.
    """
    src_dir = ROOT / base / "99. Artifact"
    dst_dir = ROOT / "workspace" / base / "99. Artifact"
    ensure_dir(dst_dir)

    for fname in ["Master Prompt.md", "📌 ChatGPT 맞춤형 지침.md", "Applied.md", "_MOC_.md"]:
        src = src_dir / fname
        if not src.exists():
            continue
        write_file(dst_dir / fname, read_text(src))


def mk_deprecated_stub(to_rel: str) -> str:
    return (
        "---\n"
        "type: Deprecated\n"
        "creation date: 2026-02-09\n"
        "---\n"
        "\n"
        "# Deprecated\n"
        "\n"
        "이 문서는 `99. Artifact/`로 이동되었습니다.\n"
        "\n"
        f"- 최신 문서: `{to_rel}`\n"
    )


def mk_artifact_moc(stage_name: str, links: list[str]) -> str:
    outgoing = "\n".join([f"  - \"{l}\"" for l in links])
    return (
        "---\n"
        "type: MOC\n"
        "creation date: 2026-02-09\n"
        "tags:\n"
        "  - 99__Artifact\n"
        f"  - {stage_name}\n"
        "backlinks:\n"
        "outgoinglinks:\n"
        f"{outgoing}\n"
        "---\n"
        "---\n"
    )


def mk_master_prompt(title: str, sections: list[tuple[str, str]], references: list[str]) -> str:
    # sections: (label, content) - content already plain text
    # references: list of source file relpaths included in this master prompt
    fm = []
    fm.append("---")
    fm.append("type: Artifact")
    fm.append("creation date: 2026-02-09")
    fm.append("References:")
    for r in references:
        fm.append(f"  - {r}")
    fm.append("---")

    body = []
    body.extend(fm)
    body.append(f"# Master Prompt — {title}")
    body.append("")
    body.append("아래 단일 코드 블록 전체를 ChatGPT Custom Instructions에 그대로 붙여넣는다.")
    body.append("")
    # NOTE: Keep triple-backtick for broad compatibility, but we must escape any embedded ``` inside content.
    body.append("```")
    for label, content in sections:
        fname = Path(label).name
        body.append(f"## {fname}")
        body.append(f"- Source: `{label}`")
        body.append("")
        body.append(content.strip())
        body.append("")
        body.append("---")
        body.append("")
    # drop trailing --- block
    if body[-2:] == ["---", ""]:
        body = body[:-2]
    body.append("```")
    body.append("")
    return "\n".join(body)


def mk_applied_from_master(title: str) -> str:
    # Applied is the minimal Custom Instructions content when the 📌 doc exceeds the input limit.
    # Format: Role + "Follow the attached 📌 ChatGPT 맞춤형 지침"
    role_hint = {
        "01. Core": "전 Stage 공통 운영/출력 규칙을 집행하는 Root AI Agent",
        "10. Business": "SRS→SDS→SCS→PM→Translation 체계의 Business 공통 규칙을 적용하는 AI Agent",
        "10.01.01 SRS": "Helios(SRS/PRD/Traceability) 작성/검증을 돕는 AI Agent",
        "10.01.02 SDS": "Aegis(SDS/C4/ADR/Interface) 설계를 돕는 AI Agent",
        "10.01.03 SCS": "Forge(구현/테스트/CI/CD) 실행을 돕는 AI Agent",
        "10.02.01 PM": "Chronos(PM/WBS/Risk/Report) 운영을 돕는 AI Agent",
        "10.02.02 Translation": "LinguaBridge(교정/번역/QA) 파이프라인을 적용하는 AI Agent",
        "20.00 Personal": "개인 생활(회고/루틴/의사결정) 지원 AI Agent",
        "20.01 English": "영어 학습(Mode: Grammar/Podo) 산출물을 계약 기반으로 출력하는 AI Agent",
        "20.02 Computer-Science": "CS 학습/연구/설명/코딩을 구조화해 돕는 AI Agent",
        "20.03 ISA-95": "ISA-95 학습/도메인 정리를 돕는 AI Agent",
        "20.03 ISA-95 Level 3": "ISA-95 Level 3 도메인 정리를 돕는 AI Agent",
    }.get(title, "해당 Stage/Project를 지원하는 AI Agent")

    snippet_lines = [
        f"Applied ({title})",
        "",
        "Role",
        f"- {role_hint}",
        "",
        "Instruction",
        "- 첨부된 `📌 ChatGPT 맞춤형 지침` 문서의 **형식/규칙을 그대로** 따른다.",
        "- 첨부가 없으면, 먼저 해당 `📌 ChatGPT 맞춤형 지침` 문서 첨부/제공을 요청한다.",
    ]
    snippet = "\n".join(snippet_lines).strip() + "\n"

    return (
        "---\n"
        "type: Note\n"
        "creation date: 2026-02-11\n"
        "---\n"
        "---\n"
        "```\n"
        f"{snippet}"
        "```\n"
    )


def mk_pin_from_master(title: str) -> str:
    # 📌 doc is the primary Custom Instructions content when it fits the input limit.
    # Format (fixed): Role / Rule Set / Scope / Non-negotiables / Output modes / Pre-process / Process / Post-process
    role_hint = {
        "01. Core": "전 Stage 공통 운영/출력 규칙을 집행하는 Root AI Agent",
        "10. Business": "SRS→SDS→SCS→PM→Translation 체계의 Business 공통 규칙을 적용하는 AI Agent",
        "10.01.01 SRS": "Helios(SRS/PRD/Traceability) 작성/검증을 돕는 AI Agent",
        "10.01.02 SDS": "Aegis(SDS/C4/ADR/Interface) 설계를 돕는 AI Agent",
        "10.01.03 SCS": "Forge(구현/테스트/CI/CD) 실행을 돕는 AI Agent",
        "10.02.01 PM": "Chronos(PM/WBS/Risk/Report) 운영을 돕는 AI Agent",
        "10.02.02 Translation": "LinguaBridge(교정/번역/QA) 파이프라인을 적용하는 AI Agent",
        "20.00 Personal": "개인 생활(회고/루틴/의사결정) 지원 AI Agent",
        "20.01 English": "영어 학습(Mode: Grammar/Podo) 산출물을 계약 기반으로 출력하는 AI Agent",
        "20.02 Computer-Science": "CS 학습/연구/설명/코딩을 구조화해 돕는 AI Agent",
        "20.03 ISA-95": "ISA-95 학습/도메인 정리를 돕는 AI Agent",
        "20.03 ISA-95 Level 3": "ISA-95 Level 3 도메인 정리를 돕는 AI Agent",
    }.get(title, "해당 Stage/Project를 지원하는 AI Agent")

    scope_hint = {
        "01. Core": "Core 운영/출력 규칙(최상위 Charter/Operations) 집행",
        "10. Business": "Business 공통(Traceability/템플릿) + Stage 파이프라인(SRS→SDS→SCS→PM→Translation)",
        "10.01.01 SRS": "SRS/PRD/Traceability 산출 및 검증(Helios)",
        "10.01.02 SDS": "SDS/C4/ADR/Interface 설계 산출(Aegis)",
        "10.01.03 SCS": "구현/테스트/CI/CD 산출(Forge)",
        "10.02.01 PM": "WBS/Gantt/Risk/Report 산출(Chronos)",
        "10.02.02 Translation": "교정/번역/QA 산출(LinguaBridge)",
        "20.00 Personal": "개인 생활 지원(회고/루틴/의사결정)",
        "20.01 English": "영어 학습 산출(Mode: Grammar/Podo) 및 정리/학습 산출물 계약 준수",
        "20.02 Computer-Science": "CS 학습/연구/설명/코딩",
        "20.03 ISA-95": "ISA-95 학습/도메인 정리",
        "20.03 ISA-95 Level 3": "ISA-95 Level 3 도메인 정리",
    }.get(title, "Stage 규칙 적용")

    stage_specific_nonneg = {
        "20.01 English": [
            "- 학습은 `Mode: Grammar` 또는 `Mode: Podo`가 없으면 먼저 모드 선택을 요구한다.",
            "- 모드 혼합 금지. '정리/학습 산출물'은 Organizer Contract + Execution Gate를 통과하는 형식으로 출력한다.",
        ],
        "10. Business": [
            "- Traceability: REQ-### / DES-### / IMP-###. 하위 단계는 상위 ID를 참조만 한다.",
        ],
        "20.00 Personal": [
            "- 공감/비판단 톤. 사실 vs 조언을 분리하고, 과도한 단정/훈계 금지.",
            "- 의료/법률/투자 주제는 위험 고지 + 전문가 상담 권유.",
        ],
        "20.02 Computer-Science": [
            "- 모호하면 Mode(Explain/Study/Design/Code)를 먼저 확인한다.",
            "- 코드 요청은 요구→의사코드→확인→완성코드 흐름을 따른다.",
        ],
    }.get(title, [])

    nonneg_lines = [
        "- 사실/가정/추측을 분리하고, 불확실하면 명시(알 수 없음/추측 등).",
        "- 모호하면 먼저 질문해서 입력/목표/범위를 확정한다.",
        "- 출력은 기본 Markdown. 사용자가 정한 헤더/구조를 임의로 바꾸지 않는다.",
        "- 입력 누락/요약 대체/스캔 금지(입력 커버리지 100%).",
        *stage_specific_nonneg,
    ]

    output_mode_lines = [
        "- 요청을 (생성 > 출력 > 정리(내용/용어/상세) > 일반 설명) 우선순위로 판별한다.",
        "- '정리' 요청: 입력 누락 없이 커버 + 순수 Markdown + (EDU 성격이면) 용어/약어 Footnote 정의.",
        "- '산출물 출력' 요청: 결과물은 한 번에 완결되게 출력(중간 스캔/요약 대체 금지).",
        "- 코드/구현 요청: 요구→의사코드→확인→완성코드 흐름(상위 규칙 준수).",
    ]

    # Keep formatting deterministic and compact.
    lines: list[str] = []
    lines.extend(
        [
            "---",
            "type: Note",
            "creation date: 2026-02-11",
            "---",
            "---",
            f"# 📌 ChatGPT 맞춤형 지침 — {title}",
            "",
            "## Role",
            "",
            f"- {role_hint}",
            "",
            "## Rule Set",
            "",
            "- **SSOT(단일 진실 소스)**: `99. Artifact/Master Prompt.md`",
            "- 상위 규칙(공통 운영/출력 규칙) → Stage/Project 규칙 → 템플릿/가이드 순으로 적용한다.",
            "",
            "## Scope",
            "",
            f"- {scope_hint}",
            "",
            "## Non-negotiables",
            "",
            *nonneg_lines,
            "",
            "## Output modes",
            "",
            *output_mode_lines,
            "",
            "## Pre-process",
            "",
            "- 입력에서 요청 타입/목표/산출물 형태를 판별한다.",
            "- 모호하면 질문으로 전제/범위/제약(모드 포함)을 확정한다.",
            "",
            "## Process",
            "",
            "- 확정된 요청 타입에 맞는 출력 모드로 결과를 작성한다.",
            "- Stage/Project 전용 규칙(Organizer Contract/Execution Gate/Traceability 등)이 있으면 우선 적용한다.",
            "",
            "## Post-process",
            "",
            "- 입력 누락 0, 형식 위반 0, 사용자 요구 반영 100%를 자체 점검한다.",
            "- 사실성/불확실성 표기/금지 사항 위반 여부를 최종 점검한다.",
            "",
        ]
    )
    return "\n".join(lines)


DEFAULT_TARGETS = [
    # (title, base_dir, include_files_relative_to_root)
    (
        "01. Core",
        "01. Core",
        [],
    ),
    (
        "10. Business",
        "10. Business",
        [
            "10. Business/00. Index/📘 Business Level Index.md",
            "10. Business/01. Rules/🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md",
            "10. Business/02. Guides/📘 Integrated Prompt Template Set.md",
        ],
    ),
    (
        "10.01.01 SRS",
        "10. Business/10.01 Architect/10.01.01 SRS",
        [],
    ),
    (
        "10.01.02 SDS",
        "10. Business/10.01 Architect/10.01.02 SDS",
        [],
    ),
    (
        "10.01.03 SCS",
        "10. Business/10.01 Architect/10.01.03 SCS",
        [],
    ),
    (
        "10.02.01 PM",
        "10. Business/10.02 Project/10.02.01 PM",
        [],
    ),
    (
        "10.02.02 Translation",
        "10. Business/10.02 Project/10.02.02 Translation",
        [],
    ),
    (
        "20.00 Personal",
        "20. Personal/20.00 Personal",
        [
            "20. Personal/20.00 Personal/00. Index/📘 Personal Level Index.md",
            "20. Personal/20.00 Personal/01. Rules/Personal Stage Behavior Rules.md",
        ],
    ),
    (
        "20.01 English",
        "20. Personal/20.01 English",
        [
            "20. Personal/20.01 English/00. Index/📘 English Level Index.md",
            "20. Personal/20.01 English/01. Rules/Learn-English Priority Rules.md",
            "20. Personal/20.01 English/01. Rules/🧾 Organizer Contract - Learn English.md",
            "20. Personal/20.01 English/01. Rules/20.01.01 Podo English/00. Output Contract Concept.md",
            "20. Personal/20.01 English/01. Rules/20.01.01 Podo English/01. Prompt - Podo English.md",
            "20. Personal/20.01 English/01. Rules/20.01.01 Podo English/02. Template - Podo English.md",
            "20. Personal/20.01 English/01. Rules/20.01.01 Podo English/03. Execution gate - Podo English.md",
            "20. Personal/20.01 English/01. Rules/20.01.02 Grammar/01. Prompt - Grammer.md",
            "20. Personal/20.01 English/01. Rules/20.01.02 Grammar/02. Template - Grammer.md",
            "20. Personal/20.01 English/01. Rules/20.01.02 Grammar/03. Execution gate - Grammer.md",
        ],
    ),
    (
        "20.02 Computer-Science",
        "20. Personal/20.02 Computer-Science",
        [
            "20. Personal/20.02 Computer-Science/00. Index/📘 CS Level Index.md",
            "20. Personal/20.02 Computer-Science/01. Rules/Computer-Science Stage Behavior Rules.md",
            "20. Personal/20.02 Computer-Science/02. Guides/📘 Computer-Science Study Rule.md",
        ],
    ),
    (
        "20.03 ISA-95",
        "20. Personal/20.03 ISA-95",
        [],
    ),
]


def load_external_targets(config_path: Path = CONFIG_PATH) -> list[tuple[str, str, list[str]]]:
    if not config_path.exists():
        return []
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[stage_targets] invalid JSON: {config_path} ({exc})") from exc

    if not isinstance(data, list):
        raise SystemExit(f"[stage_targets] top-level must be a list: {config_path}")

    entries: list[tuple[str, str, list[str]]] = []
    for entry in data:
        if not isinstance(entry, dict):
            raise SystemExit(f"[stage_targets] each entry must be an object: {config_path}")
        title = entry.get("title")
        base_dir = entry.get("base_dir")
        includes = entry.get("includes", [])
        if not title or not base_dir:
            raise SystemExit(f"[stage_targets] 'title' and 'base_dir' required for each entry: {entry}")
        if includes is None:
            includes = []
        if not isinstance(includes, list):
            raise SystemExit(f"[stage_targets] 'includes' must be a list for entry {title}")
        entries.append((title, base_dir, includes))
    return entries


TARGETS = DEFAULT_TARGETS + load_external_targets()


MDLINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FENCE_LINE_RE = re.compile(r"(?m)^(\s*)```")


def sanitize_links_for_master(content: str) -> str:
    """
    Master Prompt is intended for pasting into ChatGPT, not for repository navigation.
    Convert Markdown links into plain text so link_check doesn't treat them as repo links.
    """

    def _repl(m: re.Match) -> str:
        label = m.group(1).strip()
        target = m.group(2).strip()
        return f"{label}: `{target}`"

    out = MDLINK_RE.sub(_repl, content)
    # Replace Obsidian wikilinks with a non-link marker so link_check doesn't treat them as links.
    out = WIKILINK_RE.sub(lambda m: f"⟦{m.group(1)}⟧", out)
    # Escape any embedded triple-backtick fence lines so the master prompt's single fence never breaks.
    # We inject a zero-width space between the 2nd and 3rd backtick: ``\u200b`
    out = FENCE_LINE_RE.sub(lambda m: f"{m.group(1)}``\u200b`", out)
    return out


def collect_md_files_under(dirs: list[Path], *, exclude_exact_relpaths: set[str]) -> list[str]:
    files: list[Path] = []
    for d in dirs:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            rel = p.relative_to(ROOT)
            if any(part in EXCLUDE_DIRS for part in rel.parts):
                continue
            # never embed artifacts into master (avoid recursion and stubs)
            if "99. Artifact" in rel.parts:
                continue
            if p.name == "_MOC_.md":
                continue
            rel_s = str(rel).replace("\\", "/")
            if rel_s in exclude_exact_relpaths:
                continue
            files.append(p)

    # stable order: path string
    uniq: dict[str, Path] = {}
    for p in files:
        uniq[str(p.relative_to(ROOT)).replace("\\", "/")] = p
    return sorted(uniq.keys())


def business_common_dirs_for(base: str) -> list[Path]:
    if base.startswith("10. Business/10.01") or base.startswith("10. Business/10.02"):
        candidates = [
            ROOT / "10. Business/01. Rules",
            ROOT / "10. Business/02. Guides",
        ]
        return [p for p in candidates if p.exists()]
    return []


def main() -> int:
    # 0) Create 99. Artifact and move files
    moved_count = 0
    for title, base, _includes in TARGETS:
        base_dir = ROOT / base
        artifact_dir = base_dir / "99. Artifact"
        ensure_dir(artifact_dir)

        for fname in ["📌 ChatGPT 맞춤형 지침.md", "Applied.md"]:
            src = base_dir / fname
            dst = artifact_dir / fname
            did = move_if_exists(src, dst)
            if did:
                moved_count += 1
            # IMPORTANT: Do NOT keep deprecated stubs at the old location.
            # Single source of truth is under 99. Artifact/.

        pin = artifact_dir / "📌 ChatGPT 맞춤형 지침.md"
        applied = artifact_dir / "Applied.md"
        # Always rewrite entrypoint artifacts to prevent drift.
        write_file(pin, mk_pin_from_master(title))
        write_file(applied, mk_applied_from_master(title))

    # 1) Update internal references across repo to new artifact paths for the moved filenames
    # We do simple safe replacements for absolute-ish strings used in this repo.
    rep_pairs = []
    for _title, base, _includes in TARGETS:
        # Only for paths where these files can exist
        rep_pairs.append((f"{base}/📌 ChatGPT 맞춤형 지침.md", f"{base}/99. Artifact/📌 ChatGPT 맞춤형 지침.md"))
        rep_pairs.append((f"{base}/Applied.md", f"{base}/99. Artifact/Applied.md"))
        rep_pairs.append((f"{base}/📌 ChatGPT 맞춤형 지침", f"{base}/99. Artifact/📌 ChatGPT 맞춤형 지침"))
        rep_pairs.append((f"{base}/Applied", f"{base}/99. Artifact/Applied"))

    changed_refs = 0
    for f in iter_md_files():
        txt = read_text(f)
        new = txt
        for a, b in rep_pairs:
            new = new.replace(a, b)
        if new != txt:
            f.write_text(new, encoding="utf-8")
            changed_refs += 1

    # 2) Generate Master Prompt per target (after moves/stubs)
    master_count = 0
    for title, base, includes in TARGETS:
        base_dir = ROOT / base
        artifact_dir = base_dir / "99. Artifact"
        ensure_dir(artifact_dir)

        # Include ALL guideline files for this project:
        # - Core 01..05 areas
        # - Business common (SRS/SDS/SCS only)
        # - Entire target project/stage folder
        core_dirs = [
            ROOT / "01. Core/00. Charter",
            ROOT / "01. Core/01. Operations",
            ROOT / "01. Core/02. Standards",
            ROOT / "01. Core/03. Frameworks",
        ]

        common_dirs = business_common_dirs_for(base)

        # Exclude legacy root filenames if they exist (we want 99. Artifact as the only entrypoint)
        exclude_exact = {
            f"{base}/📌 ChatGPT 맞춤형 지침.md",
            f"{base}/Applied.md",
        }

        rel_paths: list[str] = []
        rel_paths.extend(collect_md_files_under(core_dirs + common_dirs, exclude_exact_relpaths=set()))
        if includes:
            for inc in includes:
                path = ROOT / inc
                if path.exists():
                    rel_paths.append(inc)
        else:
            rel_paths.extend(collect_md_files_under([base_dir], exclude_exact_relpaths=exclude_exact))
        rel_paths = list(dict.fromkeys(rel_paths))

        sections: list[tuple[str, str]] = []
        for inc in rel_paths:
            p = ROOT / inc
            txt = read_text(p)
            _fm, body = split_frontmatter(txt)
            content = sanitize_links_for_master(body.strip())
            sections.append((inc, content))

        master_text = mk_master_prompt(title, sections, rel_paths)
        write_file(artifact_dir / "Master Prompt.md", master_text)
        master_count += 1

        # write a small artifact MOC for convenience
        write_file(
            artifact_dir / "_MOC_.md",
            mk_artifact_moc(
                stage_name=title.replace(" ", "_").replace(".", "_"),
                links=[
                    f"[[00. Second-Brain-System/00.03. AI/{base}/99. Artifact/Master Prompt|Master Prompt]]",
                    f"[[00. Second-Brain-System/00.03. AI/{base}/99. Artifact/📌 ChatGPT 맞춤형 지침|📌 ChatGPT 맞춤형 지침]]",
                    f"[[00. Second-Brain-System/00.03. AI/{base}/99. Artifact/Applied|Applied]]",
                ],
            ),
        )

        # mirror artifacts into workspace/ (optional consumption path)
        mirror_artifact_to_workspace(base)

    print(f"Moved original files: {moved_count}")
    print(f"Updated files (reference rewrites): {changed_refs}")
    print(f"Generated Master Prompts: {master_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

