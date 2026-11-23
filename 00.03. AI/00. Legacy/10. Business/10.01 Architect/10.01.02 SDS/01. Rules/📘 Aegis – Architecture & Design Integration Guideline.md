---
type: Note
creation date: 2026-01-12 13:40
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
Version: v1.1 - 01. Core/03. Frameworks/📌 Genius Thinking Formula Prompt.md
References:
  - 01. Core/00. Charter/🧠 Common Rule.md
  - 01. Core/02. Standards/🏗️ Standard Prompt Policy.md
  - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
  - 01. Core/03. Frameworks/📌 Genius Thinking Formula Prompt.md
level: 10.01.02
parent_level: 10.01
---
---
## 1. 프로젝트 개요
Aegis는 **시스템 설계 및 아키텍처 정의(SDS)** 단계의 표준을 관리합니다.  
Helios에서 정의된 요구사항을 기술적 구조로 전환하여 설계, 모델링, 문서화를 수행합니다.

### ※기본 중요 참고 지침
- [🧠 Common Rule](🧠%20Common%20Rule.md)n%20[📌 Genius Thinking Formula Prompt](📌%20Genius%20Thinking%20Formula%20Prompt.md)g%20[🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)0Stu[🏗️ Standard Prompt Policy](🏗️%20Standard%20Prompt%20Policy.md)%8F%97%EF%B8%8F%20Standard%20Prompt%20Policy.md)

---

## 2. 역할 및 책임
| 역할 | 주요 책임 |
|------|------------|
| Architect | 시스템 전체 구조 설계 및 품질 속성 관리 |
| Designer | 모듈/컴포넌트 수준 상세 설계 |
| AI Agent (Aegis) | 설계 자동화, 다이어그램 생성, 검증 수행 |
| Developer (Forge 연동) | 구현 피드백 제공 및 설계 검증 |

---

## 3. 주요 산출물
→ SDS (Software Design Specification)  
→ C4 Model / PlantUML Diagram  
→ ADR (Architecture Decision Record)  
→ Design Pattern Catalog  
→ Interface Definition Document  

---

## 4. 문서 구조
```md
# System Overview
# Architecture Diagram
# Module Design
# Data Model
# Interface Specification
# Design Review Checklist
```

---

## 5. 설계 원칙
→ 단순성과 명확성을 우선  
→ SOLID, DRY, KISS, YAGNI 원칙 준수  
→ 높은 응집도, 낮은 결합도 유지  
→ 변경에 유연하고 확장 가능한 구조 유지  

---

## 6. 절대 금지 사항 (Absolute Prohibitions)

SDS 단계에서 다음 행위는 **절대 금지**된다.

- **SRS 범위 확장 금지**  
  → SRS에 정의되지 않은 요구사항을 추가하거나 확장하지 않는다

- **요구사항 추가/수정 금지**  
  → SRS 요구사항의 의미를 변경하거나 새로운 기능을 임의로 추가하지 않는다

- **구현 코드 작성 금지**  
  → 클래스, 함수, 코드 구조 등 구현 상세는 SCS 단계에서만 수행한다

- **설계 재해석 금지**  
  → SRS 요구사항을 설계 관점에서 재해석하거나 의미를 변경하지 않는다

- **임의 기술 선택 금지**  
  → 기술 스택 선택은 ADR을 통해 근거를 명시하고, SRS 비기능 요구사항과 일치해야 한다

---

## 8. 하위 규칙 체계 (Sub Rules)

Aegis Root Rule 하위에는 다음 Interface Contract 문서들이 존재한다.

- 🔗 **SRS ↔ SDS Interface Contract**  
  → 요구사항 명세와 설계 산출물 간 매핑 규칙 정의

- 🔗 **SDS ↔ SCS Interface Contract**  
  → 설계 산출물이 구현 단계로 전달될 때 유지해야 할 제약 정의

하위 Contract는:
- 본 문서를 **보완**할 수 있으나
- **우선하거나 충돌할 수 없다**

하위 Contract와 본 문서 간 해석 또는 적용 충돌이 발생할 경우, **AI Agent는 판단을 중단하고 Aegis Root Rule 기준 위반으로 즉시 재질문하거나 실행을 중단한다.**

---

## 9. 검증 체크리스트
| 항목       | 기준                     | 상태  |
| -------- | ---------------------- | --- |
| 설계 명확성   | 주요 컴포넌트 구조 정의          | ☐   |
| 품질 속성 정의 | 성능/보안/확장성 고려           | ☐   |
| ADR 기록   | 모든 설계 결정 문서화           | ☐   |
| 리뷰 수행    | Peer/ARB 검토 완료         | ☐   |
| SRS Traceability | 모든 설계 항목이 SRS ID와 연결됨 | ☐   |