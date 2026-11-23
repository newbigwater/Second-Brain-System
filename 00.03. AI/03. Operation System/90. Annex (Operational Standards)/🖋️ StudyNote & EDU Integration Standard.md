---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Annex
Version: v1.1
Status: Active
RuleNamespace: OS-OPS
References:
  - 03. Operation System/02. Validation Engine/Checklists/Footnote Auto Checklist.md
  - 03. Operation System/90. Annex (Operational Standards)/🧾 Organizer Contract Standard.md
  - 03. Operation System/90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md
  - 03. Operation System/90. Annex (Operational Standards)/📘 Operational Rules.md
---
---
# 🖋️ StudyNote & EDU Integration Standard (OS 연계 표준)

## 00. 목적

본 문서는 "정리/EDU 성격 출력물"에서 OS(레이어 0~4)와 **본 Annex의 정리·EDU 산출물 기본 규칙**, Organizer Contract, Validation Checklist의 관계를 표준화한다.

## 01. 우선순위(강제)

1. OS Layer 0~4
2. 정리·EDU 산출물 기본 규칙 (본 Annex: `90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md`)
3. 🧾 Organizer Contract (해당 Stage/Project에 존재하는 경우)

## 02. 적용 트리거

다음 중 하나라도 해당하면 "정리/EDU 성격 출력물"로 간주한다.

- 사용자가 "내용 정리/용어 정리/상세 정리"를 요청
- 교육용 문서(EDU), 학습 정리(StudyNote) 산출

## 03. 핵심 용어·약어 Footnote 필수 (강제 · Obsidian 호환 형식)

**모든 내용 정리 작업 시 핵심 용어 및 약어는 footnote로 상세 기술한다.**

- 약어·전문용어·교육 개념은 Footnote로 정의한다.
- OS-ART-015 **To-Be(Obsidian 호환)** 형식: `[^n]: **용어(English)**` → 탭 들여쓰기 정의 문단 → `- **Scope**:` (필수 권장) → 해당 시 `- **Exclusion/Caution**:`
- 최소 포함: 정의 문단 + Scope.

## 04. 검증(Execution Gate 연계)

- Footnote 표기/위치/금지 패턴/3요소 검증은 OS Layer 2 체크리스트로 수행한다.
  - `02. Validation Engine/Checklists/Footnote Auto Checklist.md`

## 05. 풋노트 기반 Tag 자동 생성(정리 요청 시)

- 정리/EDU 산출물에 풋노트가 포함된 경우, 풋노트에 등록된 용어·약어·전문 개념을 추출하여 문서 최상단에 **각각** `#TagName` 또는 `$TagName`(구동사 등) 형식으로 일괄 등록한다. Tag는 띄어쓰기로 한 줄에 나열하며 개행하지 않는다. `#Tag: word1 word2` 형태는 사용하지 않는다.
- 상세 규칙: 정리·EDU 산출물 기본 규칙 **06. 풋노트 기반 Tag 자동 생성 규칙** 준수.

## 06. Practice(연습) 섹션 규칙(조건부)

- Practice 섹션이 포함되는 템플릿(Organizer Contract/Stage Template)이 존재하는 경우:
  - Practice 영역은 입력 단어를 100% 포함해야 한다.
- Practice 섹션의 존재 여부는 Organizer Contract 또는 Stage 템플릿에 의해 결정된다(OS가 임의로 생성하지 않는다).
