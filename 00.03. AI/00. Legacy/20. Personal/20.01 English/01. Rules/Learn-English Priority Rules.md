---
type: Note
creation date: 2026-01-26 12:14
tags:
  - 00__System
  - 00_03__AI
  - 06__Learn
  - 01__English
  - 04__Application
Version: v1.1
level: 20.01
---
---
# Learn-English Priority Rules (Stage Rule)

> 본 문서는 “ChatGPT 등록용 Artifact(📌/Applied)”가 아니라,  
> `20.01 English` Stage의 **우선순위/모드/출력 정책**을 정의하는 **Rule 문서**이다.

---

## 0. 프로젝트 최상위 개요 (MOC · Root Rule)

**Learn - English** 프로젝트는 영어 비기너 학습자를 위해 **완전히 분리된 두 학습 모드**를 제공한다.

- 문법을 이해하기 위한 **Grammar 모드**
- 실제로 말하고 쓰기 위한 **Podo 모드**

최상위 규칙(Root Rule)은 항상 `01. Core/00. Charter/🧠 Common Rule.md`이며,  
본 문서는 Root Rule을 대체하지 않고 **정리 요청(학습 산출물) 템플릿을 특화**하기 위한 규칙만 제공한다.

본 프로젝트에서 **정리 요청/학습 산출물 출력**은  
“설명을 잘한 답변”이 아니라  
**“정의된 규칙과 계약(🧾 Organizer Contract + Execution Gate)을 정확히 통과한 학습 산출물”**만을 유효한 결과로 인정한다.

자유 질문/설명 요청은 🧠 Common Rule의 일반 설명 규칙을 따른다.

---

## 1. 학습 모드 선택 (필수 · 절대 규칙)

학습을 시작하기 전에 아래 중 하나를 반드시 선택한다.

- `Mode: Grammar`
- `Mode: Podo`

- 모드 선택 없이 학습 요청 불가
- 하나의 채팅에서는 하나의 모드만 유지
- 모드 변경 시 새 채팅 시작을 원칙으로 한다

---

## 2. 우선순위 규칙 (Conflict Resolution)

충돌 시 아래 우선순위를 따른다.

1. `01. Core/00. Charter/🧠 Common Rule.md`
2. `01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md` (정리 요청 해당 시)
3. `01. Rules/🧾 Organizer Contract - Learn English.md` (정리 요청/학습 산출물 해당 시)
4. 선택된 학습 모드의 Prompt/Template/Execution Gate
	- Grammar → `20.01.02 Grammar/*`
	- Podo → `20.01.01 Podo English/*`

---

## 3. 적용 범위 및 출력 정책

- 본 프로젝트는 교육·학습 프로젝트이며, “정리 요청/학습 산출물”은 **계산된 결과물(Contract)** 로 취급한다.
- “정리 요청/학습 산출물”에 해당하면:
	- 적용 트리거/해석/출력 형식은 `01. Rules/🧾 Organizer Contract - Learn English.md`가 **단일 진실 소스(SSOT)** 다.
	- Mode 기반 Template로 출력하며, 해당 Mode의 Execution Gate를 통과하지 못하면 출력은 Fail로 처리한다.
- 자유 질문/설명 요청은:
	- 🧠 Common Rule의 일반 설명 규칙을 따른다.
	- 단, 사용자가 “산출물 형태(정리/템플릿)”를 요구하면 Organizer Contract로 전환한다.

---

## 4. Grammar 모드 전용 규칙

### 목적

- 영어 문법을 비기너 눈높이에서 이해
- 책 기반 학습 내용을 정확·일관·누적 정리

### 적용 지침

- `01. Prompt - Grammer`

### 허용 범위

- Concept / Why / Form 중심 구조
- 짧은 예문, 현재형 위주
- Practice는 사용자 입력 정리 전용

### 금지 항목

- AI 임의 예문 생성
- 회화 중심 출력
- Weekly Study 구조

※ 예문은 교재 또는 사용자 입력을 정리·재배치하는 경우에만 허용하며,  
AI가 새 예문을 임의 생성하는 행위는 허용되지 않는다.

---

## 5. Podo 모드 전용 규칙

### 목적

- 단어·문장·회화를 실제로 말하고 쓰기 위한 훈련
- 주간 단위 학습 내용을 구조화·누적 관리

### 적용 지침

- `01. Prompt - Podo English`

### 허용 범위

- Weekly Study 구조
- Words / Conversation / Practice 중심
- Grammar는 학습 로그 내 보조 섹션으로만 허용

### 금지 항목

- Grammar 개념 설명
- 규칙 요약
- 평가·피드백·다음 단계 제안

---

## 6. 모드 혼합 금지 원칙 (강제)

다음 행위는 프로젝트 전역에서 금지된다.

- Grammar 모드에서 Weekly Study 출력
- Podo 모드에서 Grammar Template 출력
- Grammar / Podo Practice 규칙 상호 침범
- 하나의 출력에 두 모드 규칙 혼합

---

## 7. 출력 형식 공통 규칙

- (정리 요청/학습 산출물 해당 시) 출력 형식은 `01. Rules/🧾 Organizer Contract - Learn English.md`를 따른다.

---

## 8. 용어 해석 고정 규칙 (시스템 트리거 포함)

- `<오늘의 문법>`
	- Grammar 모드 자동 전환으로 해석 금지
	- 학습 로그의 섹션명으로만 해석한다

---

## 9. 위반 감지 시 처리 규칙

- 출력이 본 지침을 위반한 경우:
	- 사용자의 지적을 즉시 최우선 반영
	- 변명·설명 없이 전체 재출력
	- 지침 재해석 또는 완화 시도 금지

---

## 10. 다음 진입용 고정 문구

학습은 반드시 아래 문구 중 하나로 시작한다.

- `Mode: Grammar`
- `Mode: Podo`

본 문구 없이 진행되는 학습 요청은 Learn - English 프로젝트 규칙상 처리 불가로 간주한다.

