---
type: Note
creation date: 2026-02-09
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 01__Core
  - 03__Operations
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/01. Operations/_MOC_|01. Operations]]"
outgoinglinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/00. Charter/🧠 Common Rule|🧠 Common Rule]]"
Version: v1.1
References:
level: 0.01
---
---

# NG / Fail Classification

## 01. Purpose

본 문서는 AI 출력 결과에 대해 **NG와 Fail을 명확히 구분**하여,  
재작업 가능 여부와 즉시 중단 여부를 일관되게 판정하기 위한 기준 문서다.

---

## 02. Classification Overview

|구분|의미|재출력 가능|비고|
|---|---|---|---|
|NG|규칙 위반이나 수정으로 복구 가능|가능|보완 후 재출력 허용|
|Fail|Root Contract 위반 또는 치명적 오류|불가|즉시 중단|

---

## 03. NG Criteria (수정 가능)

다음 중 하나라도 해당하면 결과는 **NG**로 판정한다.

- 입력 항목 일부 누락
- 출력 형식 오류 (Markdown 규칙 일부 위반 등)
- Footnote 누락 또는 불완전 정의
- Input Coverage Declaration 누락 또는 형식 오류
- Trace Mapping 표는 있으나 일부 매핑 불일치

> 조치
>
> - Evaluator는 NG 사유를 명시한다.
> - Worker는 동일 형식으로 전체 재출력을 수행한다.

---

## 04. Fail Criteria (재출력 불가)

다음 중 하나라도 해당하면 결과는 **Fail**로 판정한다.

- Complete Input Read Rule 위반
- 입력을 요약·추정으로 대체한 경우
- 입력에 없는 내용 생성 (추론/확장)
- Traceability Contract 위반 (신규 ID 생성 등)
- Evaluator 검증 절차 미수행

> 조치
>
> - 즉시 출력 무효 처리
> - 동일 요청에 대한 재출력 금지

---

## 05. Evaluator Responsibility

- Evaluator는 NG/Fail 중 하나를 반드시 명시한다.
- 판정 근거를 최소 1줄 이상 서술한다.

---

## 06. Execution Gate

- 본 분류 기준은 03.Operations 영역의 모든 Gate 판단에 우선 적용된다.
- 충돌 시 🧠 Common Rule이 최상위 기준이다.

