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
References:
  - 03. Operation System/90. Annex (Operational Standards)/📘 Operational Rules.md
---
---
# 🏗️ Business Stage Integration Standard (SRS / SDS / SCS)

## 00. 목적

본 문서는 `10. Business`의 Stage(SRS/SDS/SCS) 작업에서 OS가 요구하는 “상위 산출물 불변성 + 신규 판단 금지”를 운영 표준으로 고정한다.

## 01. 적용 범위

- 사용자가 SRS/SDS/SCS를 명시하거나,
- 산출물이 SRS/SDS/SCS 성격을 갖는 경우

## 02. Stage별 핵심 운영 규칙(운영 표준)

### 02.01. SRS Handling Rule

- 요구사항은 반드시 단일 의미 단위로 분리한다.
- 복합 요구사항은 허용하지 않는다.

### 02.02. SDS Derivation Rule

- SDS는 SRS 문장을 재해석하지 않는다.
- 구조 변환만 허용된다.

### 02.03. SCS Implementation Rule

- 구현 단계에서 신규 판단은 금지된다.
- 설계에서 정의된 요소만 코드로 변환한다.

## 03. 충돌 처리

- Stage의 Root Rule/Contract가 존재하면 해당 문서가 우선한다.
- 단, OS Layer 0(불변 규칙)을 약화할 수는 없다.

