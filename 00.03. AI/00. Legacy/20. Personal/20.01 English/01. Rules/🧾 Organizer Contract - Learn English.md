---
type: Note
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 06__Learn
  - 01__English
  - 04__Application
Version: v1.0
Purpose: Learn - English 프로젝트의 “정리 요청(학습 산출물)” 출력 템플릿을 강제하는 Organizer Contract
References:
  - 01. Core/00. Charter/🧠 Common Rule.md
  - 01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md
  - 20. Personal/20.01 English/01. Rules/Learn-English Priority Rules.md
  - 20. Personal/20.01 English/01. Rules/20.01.01 Podo English/00. Output Contract Concept.md
  - 20. Personal/20.01 English/01. Rules/20.01.01 Podo English/02. Template - Podo English.md
  - 20. Personal/20.01 English/01. Rules/20.01.01 Podo English/03. Execution gate - Podo English.md
  - 20. Personal/20.01 English/01. Rules/20.01.02 Grammar/02. Template - Grammer.md
  - 20. Personal/20.01 English/01. Rules/20.01.02 Grammar/03. Execution gate - Grammer.md
level: 20.01
parent_level: 20
---
---

## Purpose

- 본 문서는 Learn - English 프로젝트에서 “정리 요청(내용/용어/상세 정리)”이 들어왔을 때,
  - 🧠 Common Rule이 지정한 StudyNote Base 형식 대신
  - **Learn - English 전용 Template + Execution Gate**로 출력되도록 강제하는 Organizer Contract이다.
- 본 문서는 Learn - English의 “정리 요청/학습 산출물”에 대한 다음 항목의 **단일 진실 소스(SSOT)** 로 취급한다.
	- 적용 트리거(무엇이 ‘정리 요청/산출물’인지)
	- 트리거 해석(‘정리=요약’ 오해 방지)
	- 산출물 출력 형식(단일 코드 블록 등)

---

## Applies To

다음 요청(트리거)에 본 Contract를 적용한다.

- “정리 요청”
- “학습 내용 출력”
- “금주 학습 완료, 내용 정리 요청”
- Template 기반 출력 요청

> 자유 질문/설명 요청에는 적용하지 않는다. (그 경우 🧠 Common Rule의 일반 출력 규칙을 따른다.)

---

## Trigger Interpretation (트리거 해석 고정)

- “정리 요청”은 **요약**이 아니다.
- “정리 요청”은 **기록 재배치 / 압축**이며, Learn - English에서는 “학습 산출물(Contract)” 출력 트리거로 취급한다.

---

## Mode Selection (필수)

학습 산출물 출력 전에 아래 중 하나가 반드시 명시되어야 한다.

- `Mode: Grammar`
- `Mode: Podo`

모드가 없으면 Manager는 모드 선택을 요구하고, 산출물 출력을 진행하지 않는다.

---

## Output Template (특화 템플릿)

- Mode = `Grammar`
	- Template: `20.01.02 Grammar/02. Template - Grammer.md`
	- Gate: `20.01.02 Grammar/03. Execution gate - Grammer.md`
- Mode = `Podo`
	- Template: `20.01.01 Podo English/02. Template - Podo English.md`
	- Gate: `20.01.01 Podo English/03. Execution gate - Podo English.md`

---

## Output Format (공통 강제)

- 산출물은 **단일 Markdown 코드 블록**으로만 출력한다.
- 코드 블록 외 텍스트 출력은 금지한다.
- 선택된 Mode의 Template 외 형식은 금지한다.

---

## Invariants Declaration (상위 불변 조건 준수)

본 Organizer Contract는 다음 상위 불변 조건을 준수한다.

- 입력 커버리지(누락/요약 대체/스캔 금지)
- 사용자 제공 헤더/구조 변경 금지(Template가 요구하는 구조 내에서만 채움)
- 순수 Markdown 및 출력 환경 규칙 준수(HTML/Canvas 금지 정책 포함)

---

## Execution Gate Hook

- 출력 전, 해당 Mode의 Execution Gate를 통과하지 못하면 **출력 차단(Fail)** 로 처리한다.
- 수정 요청이 들어오면 부분 수정은 금지하며, **전체 재출력 + 재검증**을 수행한다.
