---
type: Note
creation date: 2026-01-12 14:00
tags:
  - 00_03__AI
  - 00__System
  - 02__Business
  - 00__Common
  - 02__Contracts
  - 02_00__Common
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/01. Rules/_MOC_|01. Rules]]"
outgoinglinks:
Version: v1.1
References:
level: 10
---
---
# 🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules

## 01. Purpose
본 문서는 SRS → SDS → SCS 전 과정에서 **추적성(Traceability)** 을 강제하기 위한 Business Common 실행 계약이다.
Stage/Project 문서는 본 계약을 **보강(추가 제약/절차/템플릿)** 할 수 있으나,
본 계약과 **모순되는 규칙으로 완화/재정의할 수 없다.**

---

## 02. Scope
- 요구사항(SRS)
- 설계(SDS)
- 구현(SCS)

---

## 03. Fundamental Rules
- 상위 산출물을 하위 산출물이 수정·해석·추론하는 행위는 금지한다.
- 하위 단계는 상위 단계 ID를 **참조만** 한다.
- FR/NFR은 ID Prefix가 아니라 **속성(Attribute)** 으로 취급한다. (ID Prefix는 REQ/DES/IMP만 사용)

---

## 04. Stage Mapping Rules

### 04.01. SRS → SDS

#### Allowed
- SRS Requirement ID 참조
- 요구사항-설계 매핑

#### Forbidden
- 신규 요구사항 생성
- 의미 확장

---

### 04.02. SDS → SCS

#### Allowed
- SDS Component / Interface ID 참조
- 설계 기반 구현

#### Forbidden
- 설계 외 로직 추가
- 임의 기술 선택

---

## 05. Trace ID Convention

```plainText
REQ-xxx   (SRS)
DES-xxx   (SDS)
IMP-xxx   (SCS)
```

---

## 06. Input–Output Trace Mapping Rule
- 모든 출력 요소는 입력 항목과 매핑되어야 한다.
- 매핑 불가 항목은 반드시 **추적 불가**로 명시한다.
- Trace Mapping 표(Trace Table)가 없는 출력은 규칙 위반이다.
- Trace Table은 최소한 다음 열을 포함한다:
  - `Input ID` / `Output ID` / `Mapping Rationale` / `Status(OK|추적 불가)`

---

## 07. Evaluator Verification
- 입력 ID 전체 반영 여부 검증
- 신규 ID 생성 여부 검증
- 위반 시 즉시 **NG**

---

## 08. Execution Gate
- Trace 규칙 미준수 시 산출물은 **무효**다.
