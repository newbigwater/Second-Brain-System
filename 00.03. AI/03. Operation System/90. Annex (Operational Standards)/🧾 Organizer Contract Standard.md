---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Annex
Version: v1.0
Status: Active
RuleNamespace: OS-OPS
References: []
---
---
# 🧾 Organizer Contract Standard (OS 정본)

## Purpose

- “내용·용어·용어 상세 정리 요청”에서 Stage/Project가 **특화 템플릿을 합법적으로 적용**할 수 있도록 Organizer Contract의 표준을 정의한다.
- 목표:
  - Root Rule(불변 조건)을 유지한 채 “형식 다형성(템플릿 특화)”만 허용한다.
  - Stage별 “재정의/무력화(Disable)” 선언을 차단한다.

## Definition

- Organizer Contract: 정리 요청(내용/용어/상세 정리)에만 적용되는 템플릿/구조 계약
- Organizer Contract는 Root Rule을 대체하지 않으며 하위 특화 규칙으로만 동작한다.

## Location / Naming (표준)

- 위치(권장): 해당 Stage/Project의 `01. Rules/`
- 파일명(권장): `🧾 Organizer Contract.md` 또는 `🧾 Organizer Contract - <StageName>.md`

## Priority (Conflict Resolution)

- OS Layer 0~4
- 정리·EDU 산출물 기본 규칙 (본 Annex: `90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md`)
- 🧾 Organizer Contract (해당 시)
- Stage/Project의 기타 Prompt/Template/Execution Gate

## Mandatory Invariants (절대 불변 조건)

Organizer Contract는 아래 항목을 완화/무력화/재정의할 수 없다.

- 입력 커버리지(누락/요약 대체/스캔 금지)
- 사용자 제공 헤더/구조 변경 금지
- 순수 Markdown 및 출력 환경 규칙 준수
- 약어/전문용어 개념 판별 및 Footnote 정의 책임(EDU 성격 출력물 해당 시)
- Execution Gate(검증) 체계와의 호환(검증 가능한 규칙만 추가)

## Allowed Slots (특화 허용 범위)

- **산출물 내부 형식**(섹션 구성/순서/명칭, 테이블, 항목) 정의 — 이는 OS 기본 형식(`00. Templates/OS Output Template.md`)을 **확장**하는 것이며, OS 기본 형식(단일 코드 블록, #Tag 한 줄, YAML 금지, Footnote 3요소 등)을 **대체하지 않는다**.
- 도메인 전용 섹션 추가(예: Practice, Mistake Pattern, Flashcards)
- “정리 요청” 트리거 해석의 고정(예: ‘정리=요약’ 금지 등)

단, Slots 특화로 인해 Invariants가 훼손되면 NG/Fail이다.

## Minimum Sections (문서 필수 섹션)

- Purpose
- Applies To
- Output Template
- Execution Gate Hook
- Invariants Declaration

## Registration Pack (첨부) 규칙

- Repo-Access 환경: “등록”은 필수가 아니나, Stage `Applied.md` 또는 `📌` 문서에서 Organizer Contract 존재를 명시적으로 가리켜야 한다.
- Plain ChatGPT 환경: `Applied.md` + `📌` + Organizer Contract를 함께 첨부한다.

