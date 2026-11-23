#!/usr/bin/env python3
"""Verify that markdown links follow level ordering rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"workspace", "tools", ".git", ".obsidian", "node_modules"}

WIKI_LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def read_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fm = {}
    for idx in range(1, len(lines)):
        line = lines[idx].strip()
        if line == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fm[key.strip()] = value.strip()
    return fm


def level_to_tuple(level: str) -> tuple[int, ...]:
    parts = []
    for part in level.split("."):
        digits = ""
        for ch in part:
            if ch.isdigit():
                digits += ch
            else:
                break
        if not digits:
            digits = "0"
        parts.append(int(digits))
    return tuple(parts)


from urllib.parse import unquote


def normalize_link(link: str) -> str:
    link = link.strip()
    if link.startswith("<") and link.endswith(">"):
        link = link[1:-1]
    return unquote(link)


def resolve_target(source: Path, link: str) -> Path | None:
    link = normalize_link(link)
    if not link or "://" in link or link.startswith("#") or link.startswith("mailto:"):
        return None
    candidate: Path
    if link.startswith("/"):
        candidate = ROOT / link[1:]
    elif link.startswith("."):
        candidate = (source.parent / link)
    else:
        candidate = ROOT / link
    if not candidate.suffix:
        candidate = candidate.with_suffix(".md")
    return candidate


def resolve_wiki_target(source: Path, link: str) -> Path | None:
    link = normalize_link(link)
    if not link:
        return None
    rel = source.parent / link
    if not rel.suffix:
        rel = rel.with_suffix(".md")
    if rel.exists():
        return rel
    rel = ROOT / link
    if not rel.suffix:
        rel = rel.with_suffix(".md")
    return rel


def collect_levels() -> tuple[dict[Path, str], dict[Path, str]]:
    level_map: dict[Path, str] = {}
    type_map: dict[Path, str] = {}
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        fm = read_front_matter(path)
        level = fm.get("level")
        if level:
            level_map[path] = level
            doc_type = fm.get("type", "")
            if doc_type:
                type_map[path] = doc_type.strip().lower()
    return level_map, type_map


def strip_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text
    lines = text.splitlines()
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return text
    return "\n".join(lines[end_idx + 1 :])


def main() -> int:
    level_map, type_map = collect_levels()
    violations: list[str] = []

    for path, level in level_map.items():
        if path.name == "_MOC_.md":
            continue
        if type_map.get(path, "") == "moc":
            continue
        src_tuple = level_to_tuple(level)
        text = strip_front_matter(path.read_text(encoding="utf-8"))

        for match in WIKI_LINK_RE.finditer(text):
            target = resolve_wiki_target(path, match.group(1))
            if target and target in level_map:
                tgt_tuple = level_to_tuple(level_map[target])
                if tgt_tuple > src_tuple:
                    violations.append(f"{path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")

        for match in MD_LINK_RE.finditer(text):
            target = resolve_target(path, match.group(2))
            if target and target.exists() and target in level_map:
                tgt_tuple = level_to_tuple(level_map[target])
                if tgt_tuple > src_tuple:
                    violations.append(f"{path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")

    if violations:
        print("Level link violations detected:")
        for item in violations:
            print(f"  - {item!a}")
        return 1

    print("No level link violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
