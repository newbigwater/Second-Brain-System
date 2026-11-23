---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer2
Version: v1.0
Status: Active
RuleNamespace: OS-VAL
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Violation Policy.md
  - 03. Operation System/02. Validation Engine/Validation Engine.md
---
---
# NG / Fail Policy (Layer 2)

## 00. 목적

본 문서는 Validation/Evaluator가 `NG`와 `Fail`을 일관되게 판정하기 위한 기준이다.

## 01. 우선순위

- `INVALID RESPONSE`(Layer 0 위반)가 최상위다.
- 그 외에 `Fail` vs `NG`를 분류한다.

## 02. NG 기준(수정 가능)

다음 중 하나라도 해당하면 결과는 **NG**다.

- 입력 항목 일부 누락
- 출력 형식 오류(마크다운 규칙 일부 위반 등)
- 체크리스트 누락 또는 형식 오류
- Trace Mapping 표는 있으나 일부 매핑 불일치

## 03. Fail 기준(재출력 불가)

다음 중 하나라도 해당하면 결과는 **Fail**이다.

- 입력을 요약·추정으로 대체
- 입력에 없는 내용 생성(추론/확장)
- Evaluator 검증 절차 미수행

## 04. Evaluator 책임(강제)

- Evaluator는 `NG/Fail` 중 하나를 반드시 명시한다.
- 판정 근거를 최소 1줄 이상 서술한다.

