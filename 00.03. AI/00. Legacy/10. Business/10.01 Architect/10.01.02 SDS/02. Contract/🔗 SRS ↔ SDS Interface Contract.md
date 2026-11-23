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

본 문서는 **SRS → SDS 핸드오프** 시 요구사항 명세와 설계 산출물 간 매핑 규칙을 정의한다.

본 문서는 가이드가 아닌 **강제 규칙(Contract)** 이며,  
위반 시 설계 승인이 불가하다.

---

## 1. 기본 원칙

- SDS는 SRS를 **입력물로만** 사용한다
- SRS Requirement ID는 모든 설계 항목에 **참조되어야** 한다
- SRS 요구사항을 **수정·추론·확장하지 않는다**

---

## 2. 허용 사항

- SRS Requirement ID 참조
- 요구사항을 설계 요소로 매핑
- 설계 결정 근거로 요구사항 ID 명시
- Traceability Matrix 작성

---

## 3. 금지 사항

- 새로운 요구사항 생성
- 요구사항 의미 변경 또는 재해석
- SRS에 없는 기능 추가
- 요구사항 범위 확장

---

## 4. 검증 기준

- 모든 설계 항목이 최소 하나의 SRS ID와 연결되어야 함
- 설계 문서에 "Traceability Matrix" 또는 "Requirement Mapping" 포함
- 참조 불가 항목은 "추적 불가"로 명시

---

## 5. 결론

본 Contract를 준수하여 **무결한 SRS → SDS Traceability**를 유지해야 한다.
