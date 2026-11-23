import re
import urllib.parse
from pathlib import Path


# When scripts live under workspace/tools/, repo root is two levels up.
ROOT = Path(__file__).resolve().parents[2]
EXCLUDE_DIRS = {"99. Backup", ".git", ".obsidian", "node_modules", "workspace"}

# Treat only these as real file extensions. Many notes here include dots in the
# title (e.g., "01. Foo"), which would otherwise be misinterpreted as an extension.
KNOWN_EXTS = {
    ".md",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".pdf",
    ".csv",
    ".xlsx",
    ".xls",
}

# Some files use vault-root-prefixed paths inside wikilinks.
OBSIDIAN_PREFIXES = [
    "00. Second-Brain-System/00.03. AI/",
    r"00. Second-Brain-System\00.03. AI\\",
]

WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")
MDLINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def iter_markdown_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        yield p


def normalize_target(t: str) -> str:
    t = t.strip()
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1].strip()
    if (t.startswith('"') and t.endswith('"')) or (t.startswith("'") and t.endswith("'")):
        t = t[1:-1]
    return t.strip()


def parse_wikilink(payload: str) -> str:
    return payload.split("|", 1)[0].strip()


def is_scheme_link(t: str) -> bool:
    return bool(re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", t))


def strip_obsidian_prefix(t: str) -> str:
    for pref in OBSIDIAN_PREFIXES:
        if t.startswith(pref):
            return t[len(pref) :]
    return t


def candidate_paths(base_dir: Path, target: str):
    target = target.replace("\\", "/")

    # remove heading/block refs
    target_no_anchor = target.split("#", 1)[0].split("^", 1)[0].strip()
    if not target_no_anchor:
        return []

    # strip common vault prefix if present
    target_no_anchor = strip_obsidian_prefix(target_no_anchor)

    variants = {target_no_anchor, urllib.parse.unquote(target_no_anchor)}
    cands = []

    for v in variants:
        v = v.strip()
        if not v:
            continue
        if is_scheme_link(v):
            continue

        # ignore absolute drive paths
        if re.match(r"^[A-Za-z]:[\\/]", v):
            continue

        # relative to file, and vault-root relative
        if v.startswith("/"):
            cands.append(ROOT / v.lstrip("/"))
        else:
            cands.append((base_dir / v).resolve())
            cands.append((ROOT / v).resolve())

        # If the link does not end with a known extension, also try appending ".md".
        # (note: titles like "01. Foo" would otherwise be misread as having an extension)
        if Path(v).suffix.lower() not in KNOWN_EXTS:
            if v.startswith("/"):
                cands.append(ROOT / (v.lstrip("/") + ".md"))
            else:
                cands.append((base_dir / (v + ".md")).resolve())
                cands.append((ROOT / (v + ".md")).resolve())

    uniq = []
    seen = set()
    for c in cands:
        try:
            rel = c.relative_to(ROOT)
        except Exception:
            continue
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if c not in seen:
            uniq.append(c)
            seen.add(c)
    return uniq


def exists_any(cands) -> bool:
    return any(c.exists() for c in cands)


def main() -> int:
    broken = []  # (src_rel, kind, target)
    scanned_files = 0
    checked_links = 0

    for f in iter_markdown_files():
        scanned_files += 1
        txt = f.read_text(encoding="utf-8", errors="ignore")
        base = f.parent

        for m in WIKILINK_RE.finditer(txt):
            raw_inner = m.group(1)
            target = normalize_target(parse_wikilink(raw_inner))
            if not target or target.startswith("#"):
                continue
            cands = candidate_paths(base, target)
            if not cands:
                continue
            checked_links += 1
            if not exists_any(cands):
                broken.append((str(f.relative_to(ROOT)), "wikilink", raw_inner))

        for m in MDLINK_RE.finditer(txt):
            raw = normalize_target(m.group(1))
            if not raw or raw.startswith("#") or is_scheme_link(raw):
                continue
            cands = candidate_paths(base, raw)
            if not cands:
                continue
            checked_links += 1
            if not exists_any(cands):
                broken.append((str(f.relative_to(ROOT)), "mdlink", raw))

    broken.sort()

    out = []
    out.append("# Link Integrity Report (excluding 99. Backup)")
    out.append("")
    out.append(f"- Scanned markdown files: **{scanned_files}**")
    out.append(f"- Checked links: **{checked_links}**")
    out.append(f"- Broken links found: **{len(broken)}**")
    out.append("")

    if not broken:
        out.append("## Broken links")
        out.append("")
        out.append("None ✅")
    else:
        by_src = {}
        for src, kind, tgt in broken:
            by_src.setdefault(src, []).append((kind, tgt))

        for src in sorted(by_src):
            out.append(f"## {src}")
            for kind, tgt in by_src[src]:
                out.append(f"- **{kind}**: `{tgt}`")
            out.append("")

    report_path = ROOT / "link_integrity_report.md"
    report_text = "\n".join(out) + "\n"
    report_path.write_text(report_text, encoding="utf-8")

    # Mirror for workspace consumers (report excludes workspace/ by design)
    workspace_report_path = ROOT / "workspace" / "link_integrity_report.md"
    workspace_report_path.write_text(report_text, encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {workspace_report_path}")
    print(f"Scanned {scanned_files} files; checked {checked_links} links; broken {len(broken)}")
    return 0 if not broken else 2


if __name__ == "__main__":
    raise SystemExit(main())

