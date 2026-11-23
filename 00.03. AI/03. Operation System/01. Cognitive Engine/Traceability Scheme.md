---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer1
Version: v1.0
Status: Active
RuleNamespace: OS-TRACE
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/02. Validation Engine/Validation Engine.md
  - 03. Operation System/_MOC_.md
---
---
# Traceability Scheme (Layer 1)

## 00. 목적

본 문서는 OS 및 하위 Stage/Project 산출물에서 **추적성(Traceability)** 을 유지하기 위한 ID/매핑 규칙을 정의한다.

## 01. 적용 범위

- OS 문서(레이어 0~4)
- 문서 산출물(SRS/SDS/SCS/PM/Translation/StudyNote 등)

## 02. ID 체계(표준)

### OS-TRACE-001. OS Requirements ID

- 형식: `REQ-OS-###`
- 사용처: OS 설계/규칙/검증 항목의 요구사항 추적

### OS-TRACE-002. OS Rule ID Namespace

- Kernel: `OS-KERNEL-###`
- Cognitive: `OS-COG-###`
- Validation: `OS-VAL-###`
- Reflection: `OS-REF-###`
- Artifact: `OS-ART-###`
- Annex(운영 표준): `OS-OPS-###`

## 03. 매핑(Trace Mapping) 규칙

### OS-TRACE-010. Trace Mapping Table (해당 시 필수)

다음 중 하나라도 해당하면, “입력 → 출력” 매핑 표를 제공해야 한다.

- 입력이 장문/복합 구조(헤더/목록/표/예시 포함)
- 요구사항/설계/사양 문서(SRS/SDS/SCS)
- 검증/감사 목적 출력

### OS-TRACE-011. 추적 불가 처리(강제)

- 특정 출력 요소가 입력에 매핑되지 않으면 해당 항목을 **"추적 불가"** 로 명시한다.
- “그럴듯한 추정으로 매핑”은 금지한다(=Kernel 위반 가능성).

## 04. ID 생성/변경 정책

### OS-TRACE-020. 신규 ID 생성 제한

- 사용자가 ID 체계를 지정하지 않은 경우:
  - OS 문서 내부에서는 `REQ-OS-###`, `OS-*-###`만 사용한다.
  - Stage/Project 산출물에서는 해당 Stage의 공식 Rule/Contract가 정의한 ID 체계를 우선한다.

### OS-TRACE-021. 상위 산출물 ID 불변

- 상위 산출물(요구사항 ID 등)의 의미/번호/텍스트를 재해석하거나 변경하지 않는다.
- 구조 변환만 허용되는 경우(예: SRS→SDS)에는 “재해석 금지”를 우선한다.

## 05. Validation 연계(필수)

- Traceability 검증은 Layer 2 `Validation Engine`에서 수행한다.
- “매핑 표 누락/불일치/추적 불가 미표시”는 최소 `NG`다.

