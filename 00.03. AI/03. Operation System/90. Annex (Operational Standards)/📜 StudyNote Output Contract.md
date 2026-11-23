---
type: Contract
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Annex
Version: v1.0
Status: Active
RuleNamespace: OS-OPS
References:
  - 03. Operation System/04. Artifact Engine/Output Modes.md
  - 03. Operation System/90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md
---
---
# 📜 StudyNote Output Contract (정리 요청 전용)

본 문서는 **정리 요청(내용 정리/용어 정리/학습 정리/EDU)** 처리 시 출력 형식을 강제하는 **Output Contract**이다.  
OS-ART-020(StudyNote Output Mode)과 동일 내용을 계약 형태로 명문화한다.

---

## 01. 적용 조건

- 요청 유형: 내용 정리 요청, 용어 정리, 상세 정리, 학습 정리(StudyNote), EDU 성격 출력물
- 정리 요청 감지 시 본 Contract가 활성화되며, 출력은 아래 조항을 **전부** 준수해야 한다.

---

## 02. 계약 조항 (강제)

**적용 계층**

- **출력 래핑(최우선)**: 정리 산출물은 반드시 단일 코드 블록으로 감싼다. 코드 블록 없이 본문만 출력하는 것은 **미준수**이다.
- **코드 블록 내부 구조**: 아래 3) #Tag 한 줄, 4) YAML 금지, 5) Footnote는 모두 **코드 블록 내부** 내용에 대한 규칙이다.
- 정리 전용 문서 구조 규칙은 **단일 코드 블록 래핑을 대체하지 않는다.**

### 1) 단일 코드 블록

- 전체 문서는 **단일** ` ```markdown ` 또는 ` ```text ` 코드 블록으로 감싼다. 닫는 ``` 는 **전체 산출물 맨 끝에 한 번만** 둔다.
- 코드 블록 **내부** 본문에는 닫는 백틱(```) 한 줄을 넣지 않는다. 넣으면 마크다운 파서가 그 위치에서 블록을 종료해 그 뒤 내용이 블록 밖으로 빠진다(블록 조기 종료).
- 복수 코드 블록 또는 코드 블록 없이 본문만 출력하는 것은 **미준수**이다.
- 정리 전용 문서 구조(#Tag, YAML 금지 등)는 이 **래핑**을 대체하지 않는다.

### 2) 코드 블록 외 텍스트 금지

- 코드 블록 **밖**에 설명·요약·부가 문단·해설을 두지 않는다.
- 출력은 “코드 블록 하나 + (선택) 블록 직전 안내 문장 없음”이 원칙이다.

### 3) 코드 블록 내부 첫 줄 — #Tag 한 줄

- 블록 **내부** 첫 줄은 풋노트에서 추출한 용어를 **각각 `#TagName` 또는 `$TagName`**(구동사 등) 형태로, **띄어쓰기 한 줄**에 나열한다(개행 금지). **금지**: `#Tag: word1 word2` 형태.
- 둘째 줄은 빈 줄, 셋째 줄부터 본문 첫 헤더(`# 1. ...` 등).

### 4) YAML frontmatter 금지

- 내용 정리 산출물에는 `---` 로 감싼 YAML frontmatter( title, date, tags 등)를 **사용하지 않는다**.
- 문서는 #Tag 한 줄로만 시작한다.

### 5) Footnote 3요소 구조 필수 (Obsidian 호환 형식)

- 핵심 용어·약어는 **Footnote**로 정의하며, OS-ART-015 **To-Be(Obsidian 호환)** 형식을 따른다.
- **형식**: `[^n]: **용어(English term)**` 한 줄 → 탭 들여쓰기 후 정의 서술 문단 → `- **Scope**:` 불릿(필수 권장) → 해당 시 `- **Exclusion/Caution**:` 불릿. 라벨을 빈칸으로 두지 않는다.
- 예: `[^1]: **통합된 데이터(Integrated data)**` 다음 줄에 탭 들여쓰기된 정의 문단, 이어서 `- **Scope**: 데이터 중복 최소화, 무결성 유지`

---

## 03. 검증 연계

- Output Validation Checklist에서 다음 항목으로 검증한다:
  - 단일 코드 블록 존재 여부
  - 코드 블록 외 텍스트 부재 여부
  - 코드 블록 내 첫 줄 #Tag(띄어쓰기 한 줄) 여부
  - YAML frontmatter 부재 여부
  - Footnote 3요소 및 풋노트 형식 준수 여부

---

## 04. 우선순위

- 본 Contract는 Layer 4(Artifact Engine) 및 Annex 운영 표준 내에서 적용된다.
- OS Layer 0(Governance Kernel) 위반 시 본 Contract와 무관하게 INVALID RESPONSE이다.
- Stage/Project별 Organizer Contract가 있으면 **템플릿/구조**는 해당 Contract를 따르되, **출력 형식**(단일 코드 블록, #Tag 한 줄, YAML 금지)은 본 Contract를 따른다.
