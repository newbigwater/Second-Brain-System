---
type: Note
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 01__Core
  - 03__Operations
Version: v1.0
References:
  - 01. Core/00. Charter/🧠 Common Rule.md
  - 01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md
level: 00.01
parent_level: 00.00
---
---

## Purpose

- 본 문서는 “내용·용어·용어 상세 정리 요청”에서 Stage/Project가 **특화 템플릿을 합법적으로 적용**할 수 있도록,
  - Organizer Contract(정리 요청 전용 Output Contract)의 **위치/명명/선언/필수 요건**을 표준화한다.
- 목표:
  - Root Rule(🧠 Common Rule)의 불변 조건을 유지한 채 “형식 다형성(템플릿 특화)”을 허용한다.
  - Stage별 “재정의/무력화(Disable)” 선언 대신, **특화(Specialize) + 확장 지점(Extension Point)** 기반으로 충돌을 방지한다.

---

## Definition

- **Organizer Contract**: “정리 요청(내용/용어/상세 정리)”에만 적용되는 **템플릿/구조 계약**.
- Organizer Contract는 Root Rule을 대체하지 않으며, `🧠 Common Rule 07.01.04-A`의 하위 특화 규칙으로만 동작한다.

---

## Location / Naming (표준)

- 위치(권장): 해당 Stage/Project의 `01. Rules/` 폴더
- 파일명(권장): `🧾 Organizer Contract.md` 또는 `🧾 Organizer Contract - <StageName>.md`
- 문서가 존재하면, 해당 Stage/Project는 “정리 요청”에 대해 **StudyNote Base Template 대신 특화 템플릿을 적용할 수 있다.**

---

## Priority (Conflict Resolution)

충돌 시 우선순위는 아래를 따른다.

- 🧠 Common Rule
- 🖋️ StudyNote Markdown Rulebook
- 🧾 Organizer Contract (해당 시)
- Stage/Project의 기타 Prompt/Template/Execution Gate

---

## Mandatory Invariants (절대 불변 조건)

Organizer Contract는 아래 항목을 완화/무력화/재정의할 수 없다.

- 입력 커버리지(누락/요약 대체/스캔 금지)
- 사용자 제공 헤더/구조 변경 금지
- 순수 Markdown 및 출력 환경 규칙 준수(Canvas/HTML 등 금지 정책 포함)
- 약어/전문용어 개념 판별 및 Footnote 정의 책임(EDU 성격 출력물 해당 시)
- Execution Gate(검증) 체계와의 호환(검증 가능한 규칙만 추가)

---

## Allowed Slots (특화 허용 범위)

- 섹션 구성/순서/명칭(Template) 정의
- 도메인 전용 섹션 추가(예: Practice, Mistake Pattern, Flashcards)
- “정리 요청” 트리거 해석의 고정(예: ‘정리=요약’ 금지 등)

단, 위 Slots 특화로 인해 Invariants가 훼손되면 NG/Fail이다.

---

## Minimum Sections (문서 필수 섹션)

Organizer Contract 문서는 최소 아래 섹션을 포함해야 한다.

- Purpose
- Applies To (어떤 요청/모드/문서에 적용되는지)
- Output Template (필수 섹션/순서/형식)
- Execution Gate Hook (어떤 Gate로 무엇을 검증하는지)
- Invariants Declaration (상위 불변 조건 준수 선언)

---

## Registration Pack (첨부) 규칙

- Repo-Access 환경에서는 Organizer Contract를 “등록”할 필요는 없지만,
  - Stage `Applied.md` 또는 `📌 ...` 문서에서 **Organizer Contract 존재를 명시적으로 가리켜야 한다.**
- Plain ChatGPT 환경에서는 Organizer Contract가 작업에 필수라면,
  - `Applied.md` + `📌` + Organizer Contract를 함께 첨부한다.
