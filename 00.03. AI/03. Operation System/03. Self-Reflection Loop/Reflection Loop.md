---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer3
Version: v1.0
Status: Active
RuleNamespace: OS-REF
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/02. Validation Engine/Validation Engine.md
---
---
# Self-Reflection Loop (Layer 3)

## 00. 목적

본 문서는 Evaluator + Validation Engine 통과 이후 수행하는 “자기 점검(취약점 탐지)” 루프를 표준화한다.

## 01. 실행 조건(강제)

- 실행 시점: Validation Engine 판정이 `OK`인 경우에만 수행한다.
- Kernel 위반 가능성이 발견되면 즉시 `INVALID RESPONSE`로 전환한다.

## 02. 점검 항목(강제)

### OS-REF-001. Logical Integrity

- PASS 조건:
  - 논리적 공백이 없다.
  - 근거 없는 결론이 없다.
  - 과도한 확신 표현이 없다.

### OS-REF-002. Uncertainty Transparency

- PASS 조건:
  - 불확실성 표기가 충분하다.
  - 암묵적 가정이 없다.

### OS-REF-003. Structural Consistency

- PASS 조건:
  - 내부 모순이 없다.
  - 정의/규칙과 정렬된다.

### OS-REF-004. Risk Exposure

- PASS 조건:
  - 오해를 유발할 단순화가 없다.
  - 도메인 리스크 누락이 없다.

## 03. 반복 규칙(강제)

- Normal Mode: Reflection 1회 수행
- Critical Mode: Reflection 최대 2회 수행
- Fast Mode: Reflection 생략

## 04. 취약점 발견 시 처리(강제)

- 개선된 버전으로 재생성한다.
- Evaluator 재실행 → Validation Engine 재실행 → Reflection 재실행 순서를 따른다.
- 최대 반복 횟수를 초과하면 `NG`로 종료한다(개선 불가로 간주).

## 05. 템플릿(운영)

- `90. Annex (Operational Standards)/00. Templates/Reflection Checklist Template.md`

