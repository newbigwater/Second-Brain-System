from pathlib import Path
import re

ROOT = Path(r"D:/03. Areas/Second-Brain-Area/00. Second-Brain-System/00.03. AI")
TARGET = ROOT / "20. Personal/20.03 ISA-95/Level 3/99. Artifact/Master Prompt.md"

SOURCES = [
    "01. Core/00. Charter/01. Execution Gate/✅ Footnote Auto Checklis.md",
    "01. Core/00. Charter/01. Execution Gate/✅ Output Validation Checklist.md",
    "01. Core/00. Charter/🏗️ Standard Prompt Policy.md",
    "01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md",
    "01. Core/00. Charter/🧠 Common Rule.md",
    "01. Core/01. Operations/Operational Rules.md",
    "01. Core/01. Operations/❌ NG Fail Classification.md",
    "01. Core/01. Operations/🏷️ Tag & Metadata Governance.md",
    "01. Core/01. Operations/📎 Custom Instructions Registration Pack Standard.md",
    "01. Core/01. Operations/🧱 Stage Folder Skeleton Standard.md",
    "01. Core/01. Operations/🧷 Link Display Name Style Guide.md",
    "01. Core/03. Frameworks/📌 Genius Thinking Formula Prompt.md",
    "20. Personal/20.03 ISA-95/Level 3/00. Index/📘 Level 3 ISA-95 Index.md",
    "20. Personal/20.03 ISA-95/Level 3/02. Guides/02. 3L-MES 응답 자동 검증 체크리스트.md",
    "20. Personal/20.03 ISA-95/Level 3/01. Rules/01. Prompt - Project.md",
    "20. Personal/20.03 ISA-95/Level 3/01. Rules/03. Prompt - EDU.md",
    "20. Personal/20.03 ISA-95/Level 3/01. Rules/04. Prompt - ARCH.md",
    "20. Personal/20.03 ISA-95/Level 3/01. Rules/05. Prompt - PM.md",
    "20. Personal/20.03 ISA-95/Level 3/01. Rules/06. Prompt - SRS.md",
    "20. Personal/20.03 ISA-95/Level 3/99. Artifact/📌 ChatGPT 맞춤형 지침.md",
    "20. Personal/20.03 ISA-95/Level 3/99. Artifact/Applied.md",
]

MDLINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FENCE_LINE_RE = re.compile(r"(?m)^(\s*)```")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("\n")
    for idx in range(1, len(parts)):
        if parts[idx].strip() == "---":
            fm = "\n".join(parts[: idx + 1])
            body = "\n".join(parts[idx + 1 :])
            return fm, body
    return "", text


def sanitize_links_for_master(content: str) -> str:
    def repl_md(match: re.Match) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        return f"{label}: `{target}`"

    out = MDLINK_RE.sub(repl_md, content)
    out = WIKILINK_RE.sub(lambda m: f"⟦{m.group(1)}⟧", out)
    out = FENCE_LINE_RE.sub(lambda m: f"{m.group(1)}``\u200b`", out)
    return out


def main() -> None:
    sections = []
    for rel in SOURCES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        _fm, body = split_frontmatter(text)
        body = body.strip() or text.strip()
        content = sanitize_links_for_master(body)
        sections.append((Path(rel).name, rel.replace("\\", "/"), content))

    lines: list[str] = []
    lines.append("---")
    lines.append("type: Artifact")
    lines.append("creation date: 2026-02-10")
    lines.append("References:")
    for rel in SOURCES:
        lines.append(f"  - {rel}")
    lines.append("level: 20.03")
    lines.append("parent_level: 20")
    lines.append("---")
    lines.append("# Master Prompt — 20.03 ISA-95 Level 3")
    lines.append("")
    lines.append("아래 단일 코드 블록 전체를 ChatGPT Custom Instructions에 그대로 붙여넣는다.")
    lines.append("")
    lines.append("```")
    for title, rel, content in sections:
        lines.append(f"## {title}")
        lines.append(f"- Source: `{rel}`")
        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("---")
        lines.append("")
    if lines[-2:] == ["---", ""]:
        lines = lines[:-2]
    lines.append("```")

    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
