---
type: Note
creation date: 2026-01-12 13:44
tags:
  - 00_03__AI
  - 00__System
  - 01__Rules
  - 02__SDS
  - 02__Business
  - 02_02__SDS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.02 SDS/01. Rules/_MOC_|01. Rules]]"
outgoinglinks:
Version: v1.1
References:
level: 10.01.02
parent_level: 10.01
---
---
## 0. 목적

본 문서는 **SDS → SCS 핸드오프** 시 설계 산출물이 구현 단계로 전달될 때 유지해야 할 제약을 정의한다.

본 문서는 가이드가 아닌 **강제 규칙(Contract)** 이며,  
위반 시 구현 승인이 불가하다.

---

## 1. 기본 원칙

- SDS는 구현 상세를 포함하지 않는다
- 클래스, 함수, 코드 구조는 SCS 책임이다
- SCS는 SDS 설계를 **수정·추론·확장하지 않는다**

---

## 2. 허용 사항

- SDS Component / Interface ID 참조
- 설계 기반 구현 구조화
- 구현 결정 근거로 설계 ID 명시
- Traceability Matrix 작성

---

## 3. 금지 사항

- 설계에 없는 로직 추가
- 임의의 기술 선택 (ADR 없이)
- 설계 범위를 벗어난 구현
- 설계 재해석 또는 의미 변경

---

## 4. 검증 기준

- 모든 구현 항목이 최소 하나의 SDS ID와 연결되어야 함
- 코드 주석 또는 문서에 설계 ID 참조 포함
- 참조 불가 항목은 "추적 불가"로 명시

---

## 5. 결론

본 Contract를 준수하여 **무결한 SDS → SCS Traceability**를 유지해야 한다.
