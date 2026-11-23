---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer0
Version: v1.0
Status: Active
RuleNamespace: OS-KERNEL
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
---
---
# Violation Policy — 판정 정책(최상위)

## 00. 목적

본 문서는 `03. Operation System`에서 사용하는 판정 레벨을 표준화한다.

## 01. 판정 우선순위(가장 상위 → 하위)

1. **INVALID RESPONSE**
2. **Fail**
3. **NG**
4. **OK**

## 02. 판정 정의

### 02.01. INVALID RESPONSE (복구 불가)

- 의미: Layer 0 `Governance Kernel` 규칙 위반.
- 특징:
  - NG/Fail 분류 이전에 즉시 무효 처리한다.
  - “수정으로 복구”가 아니라 “응답 자체가 무효”로 본다.
- 근거: `Kernel.md` 서문 및 각 Rule의 Enforcement.

### 02.02. Fail (재출력 불가)

- 의미: 치명적 오류로 인해 “동일 출력 구조를 유지한 채 수정/재출력”로 복구할 수 없는 상태.
- 예:
  - 입력을 요약·추정으로 대체
  - 입력에 없는 내용 생성(추론/확장)
  - Evaluator 검증 절차 미수행

### 02.03. NG (수정 후 재출력 가능)

- 의미: 규칙 위반이나 수정으로 복구 가능.
- 예:
  - 입력 일부 누락
  - 출력 형식 오류
  - 체크리스트 누락/형식 오류

### 02.04. OK

- 의미: Layer 0~4 및 Validation/Reflection을 모두 통과한 상태.

## 03. 판정 표시 규칙(강제)

- Evaluator/Validation Engine은 결과에 아래 중 하나를 반드시 명시한다.
  - `INVALID RESPONSE`
  - `Fail`
  - `NG`
  - `OK`

