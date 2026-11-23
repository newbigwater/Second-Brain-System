---
type: Note
creation date: 2026-01-12 12:41
tags:
  - 00_03__AI
  - 00__System
  - 01__SRS
  - 02__Contract
  - 02__Business
  - 02_01__SRS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.01 SRS/02. Contract/_MOC_|02. Contract]]"
outgoinglinks:
Version: v1.1
References:
level: 10.01.01
parent_level: 10.01
---
---
## 0. 목적

본 문서는 SRS 단계에서 정의된 요구사항이  
SDS → SCS 단계로 전달될 때 **추적성(Traceability)** 을 보장하기 위한 강제 규칙을 정의한다.

본 문서는 가이드가 아닌 **Contract(계약)** 이며,  
모든 요구사항은 반드시 다음 단계로 추적 가능해야 한다.

---

## 1. 기본 원칙

- 모든 요구사항은 **고유 ID**를 가진다
- 요구사항 변경은 **Change Request Log**를 통한 승인만 허용된다
- 상위 단계 산출물을 하위 단계에서 **수정·추론·확장하지 않는다**
- 모든 하위 단계는 상위 단계의 ID를 **참조만** 한다

---

## 2. Traceability 체계

```
SRS (Requirement ID) → SDS (Design ID) → SCS (Implementation ID)
```

### 2.1 ID 형식 규칙

- **SRS**: `REQ-xxx`
- **SDS**: `DES-xxx`
- **SCS**: `IMP-xxx`

> `FR/NFR`, `COMP/INTF`, `CODE/TEST` 등의 분류는 ID Prefix로 분기하지 않는다.  
> 필요 시 각 항목의 **Type 필드/속성**으로만 표현한다. (예: `Type: Functional`, `Type: Non-Functional`)

### 2.2 매핑 규칙

- 하나의 SRS 요구사항은 여러 SDS 설계 요소로 매핑될 수 있다
- 하나의 SDS 설계 요소는 여러 SCS 구현 항목으로 매핑될 수 있다
- 역방향 추적(하위 → 상위)도 항상 가능해야 한다

---

## 3. 단계별 Traceability 규칙

### 3.1 SRS → SDS

#### 허용
- SRS Requirement ID 참조
- 요구사항을 설계 요소로 매핑
- 설계 결정 근거로 요구사항 ID 명시

#### 금지
- 새로운 요구사항 생성
- 요구사항 의미 변경 또는 재해석
- SRS에 없는 기능 추가

#### 검증 기준
- 모든 설계 항목이 최소 하나의 SRS ID와 연결되어야 함
- 설계 문서에 "Traceability Matrix" 또는 "Requirement Mapping" 포함

---

### 3.2 SDS → SCS

#### 허용
- SDS Component / Interface ID 참조
- 설계 기반 구현 구조화
- 구현 결정 근거로 설계 ID 명시

#### 금지
- 설계에 없는 로직 추가
- 임의의 기술 선택 (ADR 없이)
- 설계 범위를 벗어난 구현

#### 검증 기준
- 모든 구현 항목이 최소 하나의 SDS ID와 연결되어야 함
- 코드 주석 또는 문서에 설계 ID 참조 포함

---

## 4. 변경 관리 규칙

### 4.1 요구사항 변경 절차

1. **Change Request Log**에 변경 사유 기록
2. **Product Owner 또는 PM** 승인
3. 승인 후 SRS 업데이트
4. 영향받는 SDS/SCS 항목 재검토 및 업데이트
5. Traceability Matrix 갱신

### 4.2 승인 없는 변경 금지

- 승인되지 않은 변경은 SRS에 반영될 수 없다
- 하위 단계에서 상위 단계 변경을 요구할 수 없다
- 변경은 항상 상위 → 하위 방향으로만 전파된다

---

## 5. AI 출력 검증 규칙

- 각 결과물에 상위 ID 참조 표 포함
- 참조 불가 항목은 "추적 불가(Traceability Not Available)"로 명시
- Traceability Matrix는 모든 산출물에 포함되어야 함

---

## 6. 결론

본 규칙은 AI 기반 문서 자동화 환경에서  
요구사항 왜곡 및 설계 오염을 방지하기 위한 **필수 정책**이다.

모든 Stage의 AI Agent와 Human 사용자는  
본 Contract를 준수하여 **무결한 Traceability**를 유지해야 한다.
