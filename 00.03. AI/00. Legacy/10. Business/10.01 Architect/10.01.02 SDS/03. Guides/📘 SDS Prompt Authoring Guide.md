---
type: Note
creation date: 2026-01-12 13:44
tags:
  - 00_03__AI
  - 00__System
  - 02__SDS
  - 03__Guides
  - 02__Business
  - 02_02__SDS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.02 SDS/03. Guides/_MOC_|03. Guides]]"
outgoinglinks:
Version: v1.1
Audience: Architect / Designer / Tech Lead / AI 사용자
Purpose: SRS 요구사항을 만족하는 설계 요청을 일관된 형식으로 작성하기 위한 Human 전용 가이드 - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
References:
  - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
level: 10.01.02
parent_level: 10.01
---
---
## 1. 목적

본 문서는 Stage 02(SDS)에서 AI에게 설계 업무를 지시하려는 **Human 사용자**를 위한 프롬프트 작성 기준이다.  
SRS 요구사항을 **How**로 전환할 때 범위를 벗어나지 않도록 역할·입력·제약을 명확히 정의한다.

---

## 2. 언제 참고해야 하는가

- 신규 모듈/컴포넌트 설계를 작성하거나 보완할 때
- 인터페이스, 데이터 흐름, ADR 작성을 AI에 위임할 때
- SRS → SDS 핸드오프 범위를 명확히 해야 할 때
- 기존 설계를 리뷰·정비하고 싶을 때

---

## 3. SDS 사고 원칙

- **Traceable**: 모든 설계 결정은 SRS Requirement ID, NFR, ADR로 추적 가능해야 한다
- **Constrained**: SRS 범위를 확장하거나 임의 기능을 추가하지 않는다
- **Documented**: 출력물 형식(텍스트 C4, 표, ADR 등)을 명확히 지정한다
- **Review-ready**: 결과물은 즉시 검토·승인 가능한 세부 정보를 포함한다

### 3.1 출력 모드 판별 규칙 (중요)

요청을 작성하기 전에, 먼저 “원하는 결과 유형”을 아래 우선순위로 판별한다.

```
생성 요청 > 출력 요청 > 내용·용어 정리 요청 > 일반 설명
```

- **생성 요청**: `.md` 파일로 “생성”되길 원함(파일 단위 결과)
- **출력 요청**: 복사/저장 가능한 “Artifact” 형태로 출력되길 원함(코드 블록 기반)
- **내용·용어 정리 요청**: 학습/EDU 정리처럼 구조·Footnote 규칙을 강하게 적용
- **일반 설명**: 설명 중심(필요한 부분만 코드/표)

### 3.2 StudyNote(정리/EDU) 출력 규칙 (필수 조건으로 명시 권장)

정리/EDU 문서(설계 검토 노트, 비교표, 용어 정리 등)를 요구하는 경우, Output/Constraints에 아래 조건을 **명시적으로 포함**하는 것을 권장한다.

- 문서 **첫 줄에 `#Tag`** 등록
- Footnote는 **정의 대상 용어 토큰 바로 뒤**에 직접 매핑(문장 끝/괄호 전체 부착 금지)
- Bold 용어 뒤에는 **공백 1칸** 유지(예: `**용어[^1]** 을`)
- 표준은 `🖋️ StudyNote Markdown Rulebook`을 따른다
  - 참고: [🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)Rulebook.md)

---

## 4. 권장 프롬프트 기본 구조 (5요소)

1. **역할(Role)** – 시스템 아키텍트, 설계 리뷰어 등 SDS 역할  
2. **작업(Task)** – 생성 / 보완 / 비교 / 리뷰 / 모델링 중 어떤 활동인지 명시  
3. **맥락(Context)** – 참조해야 할 SRS ID, 품질 속성 목표, 기존 산출물 링크  
4. **제약(Constraints)** – Helios/Aegis 준수, 금지 대상, 성능·보안 기준  
5. **출력(Output)** – 기대 산출물 형태(C4 Level, ADR, 표 필드 정의 등)

### 예시
```
당신은 시스템 아키텍트입니다.
SRS-ID REQ-12, REQ-13을 충족하는 서비스 구성도를 텍스트로 설계해주세요.
입력은 첨부된 요구사항 요약이며 SDS 범위를 넘어서는 기능 추가는 금지입니다.
C4 Level-2 기준으로 컴포넌트/인터페이스를 설명하고 ADR 초안을 함께 작성해주세요.

출력은 StudyNote 규칙을 따르는 설계 문서로 작성해주세요.
- 문서 첫 줄에 #Tag를 등록해주세요.
- 전문 용어/약어는 최초 등장 시 Footnote로 정의하고, 용어 토큰 바로 뒤에 [^n]을 직접 부착해주세요.
- Bold 용어 뒤에는 공백 1칸을 유지해주세요. (예: **용어[^1]** 을)
- 문서 마지막에 ## Footnotes 섹션을 포함해주세요.
```

---

## 5. 좋은 SDS 프롬프트 작성 원칙

### 5.1 역할/관점을 설계 레벨로 고정
- ✅ 시스템 아키텍트 / 설계 리뷰어 / 인터페이스 디자이너  
- ❌ 개발자 / 구현 엔지니어 (SCS 지시로 혼동됨)

### 5.2 맥락은 구체적이고 추적 가능하게
- 필수: SRS Requirement ID, 기존 ADR 링크, 품질 속성/비기능 목표  
- 금지: "이런 느낌" 같은 추상 표현, SRS에 없는 가정

### 5.3 출력 범위·표현을 명확히
- C4 수준, PlantUML, 표 항목(이름/책임/인터페이스/제약) 등 구체화  
- 산출물에 포함해야 할 필수 필드와 설명 깊이를 미리 지정

### 5.4 설계·구현 경계 유지
- “코드 작성” 대신 “설계 구조 설명”으로 한정  
- 배포 스크립트, 코드 세부 결정, 테스트 구현은 SCS에서 처리

---

## 6. 요청 유형별 작성 예시

### 6.1 시스템 구성 설계
```
당신은 시스템 아키텍트입니다.
REQ-07 주문 처리 요구사항을 만족하는 C4 Level-3 설계를 작성해주세요.
각 컴포넌트의 책임, 사용 데이터, 상호작용을 표로 정리하고
보안/장애 대비 품질 속성을 어떻게 충족하는지 설명해주세요.

출력은 StudyNote 규칙을 따르며, 첫 줄에 #Tag를 포함하고, 전문 용어/약어는 Footnote 직접 매핑으로 정의해주세요.
```

### 6.2 인터페이스 정의
```
API-05 요구사항을 기준으로 Order Service ↔ Inventory Service 인터페이스를 설계해주세요.
요청/응답 필드, 데이터 계약, 오류 처리 규칙, SLA 제약을 포함해주세요.

출력은 StudyNote 규칙을 따르며, 첫 줄에 #Tag를 포함해주세요.
약어/전문 용어(API, SLA 등)는 최초 1회 Footnote로 정의하고 용어 토큰 바로 뒤에 [^n]을 직접 부착해주세요.
```

### 6.3 ADR 생성
```
메시지 브로커 선택에 대한 ADR을 작성해주세요.
SRS REQ-02(Non-Functional: Performance) 요구사항을 근거로 선택지 비교와 최종 결정을 기록하고,
관련 요구사항 ID를 명시하여 Traceability를 확보해주세요.

출력은 StudyNote 규칙을 따르며, 첫 줄에 #Tag를 포함해주세요.
전문 용어/약어는 Footnote 직접 매핑으로 정의하고, 문서 마지막에 ## Footnotes 섹션을 포함해주세요.
```

---

## 7. 피해야 할 요청 방식

- “알아서 설계해줘” 같은 맥락 없는 포괄 지시
- SRS ID 없이 “재고 관리 느낌으로” 등 모호한 요구
- 구현/코드 생성을 동시에 요구(Playbook Type A 혼합)  
- “요구사항이 부족하면 추가해줘”처럼 범위를 확장시키는 표현
- 설계 출력 형식을 지정하지 않고 결과를 맡기는 방식

---

## 8. AI 내부 규칙과의 관계

- AI는 **📘 Aegis Root Rule** 및 **Interface Contracts** 를 최우선 적용한다
- 본 가이드는 Human 참고용이며 Rule과 충돌 시 항상 Rule이 우선한다
- Playbook/Behavior Rule에 따라 Pseudocode나 코드 생성을 요구하지 않는다

---

## 9. 결론

정확한 설계 산출물은 **구조화된 요청**에서 출발한다.  
본 가이드를 활용해 Traceable 한 설계 지시를 작성하면 AI와 사람이 같은 기준으로 SDS 단계를 수행할 수 있다.
