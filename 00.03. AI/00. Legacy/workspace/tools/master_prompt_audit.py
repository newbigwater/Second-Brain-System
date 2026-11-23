from __future__ import annotations

import re
from artifact_master_prompt import (
    ROOT,
    TARGETS,
    collect_md_files_under,
    business_common_dirs_for,
)


def expected_relpaths_for_target(base: str, includes: list[str]) -> list[str]:
    base_dir = ROOT / base
    core_dirs = [
        ROOT / "01. Core/00. Charter",
        ROOT / "01. Core/01. Operations",
        ROOT / "01. Core/02. Standards",
        ROOT / "01. Core/03. Frameworks",
    ]
    common_dirs = business_common_dirs_for(base)

    rel_paths: list[str] = []
    rel_paths.extend(collect_md_files_under(core_dirs + common_dirs, exclude_exact_relpaths=set()))

    if includes:
        for inc in includes:
            path = ROOT / inc
            if path.exists():
                rel_paths.append(inc)
    else:
        exclude_exact = {
            f"{base}/📌 ChatGPT 맞춤형 지침.md",
            f"{base}/Applied.md",
        }
        rel_paths.extend(collect_md_files_under([base_dir], exclude_exact_relpaths=exclude_exact))

    return list(dict.fromkeys(rel_paths))


FENCE_LINE = re.compile(r"^```[a-zA-Z0-9_-]*\s*$")
SECTION_SRC = re.compile(r"^\- Source:\s*`([^`]+)`\s*$")


def audit_single_fence(master_text: str) -> tuple[bool, str]:
    lines = master_text.splitlines()
    fence_idxs = [i for i, ln in enumerate(lines) if FENCE_LINE.match(ln.strip())]
    if len(fence_idxs) != 2:
        return False, f"Expected exactly 2 fence lines, found {len(fence_idxs)} ({fence_idxs[:10]})"
    if fence_idxs[0] >= fence_idxs[1]:
        return False, "Fence order invalid"
    # Ensure no other line starts with ``` (escaped by generator)
    for i, ln in enumerate(lines):
        if i in fence_idxs:
            continue
        if ln.startswith("```"):
            return False, f"Found unescaped fence at line {i+1}"
    return True, "OK"


def audit_completeness(master_text: str, expected_relpaths: list[str]) -> tuple[bool, str]:
    lines = master_text.splitlines()
    found: list[str] = []
    for i, ln in enumerate(lines):
        m = SECTION_SRC.match(ln.strip())
        if m:
            found.append(m.group(1))

    found_set = set(found)
    expected_set = set(expected_relpaths)

    missing = sorted(expected_set - found_set)
    extra = sorted(found_set - expected_set)

    if missing or extra:
        msg = []
        if missing:
            msg.append(f"Missing sections: {len(missing)} (first 10: {missing[:10]})")
        if extra:
            msg.append(f"Extra sections: {len(extra)} (first 10: {extra[:10]})")
        return False, " | ".join(msg)
    return True, f"OK ({len(expected_set)} sections)"


def main() -> int:
    failures: list[str] = []
    for title, base, includes in TARGETS:
        master = ROOT / base / "99. Artifact" / "Master Prompt.md"
        if not master.exists():
            failures.append(f"{title}: missing Master Prompt.md at {master.relative_to(ROOT)}")
            continue

        txt = master.read_text(encoding="utf-8", errors="ignore")
        ok_fence, fence_msg = audit_single_fence(txt)
        expected = expected_relpaths_for_target(base, includes)
        ok_comp, comp_msg = audit_completeness(txt, expected)

        if not ok_fence or not ok_comp:
            failures.append(f"{title}: fence={ok_fence}({fence_msg}), completeness={ok_comp}({comp_msg})")

    if failures:
        for msg in failures:
            print(msg.encode("unicode_escape").decode())
        print("failures", len(failures))
        return 2

    print("OK: all master prompts passed fence + completeness checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

