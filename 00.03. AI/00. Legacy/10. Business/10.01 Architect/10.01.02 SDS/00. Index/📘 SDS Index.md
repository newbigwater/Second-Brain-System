---
type: Note
creation date: 2026-01-12 13:40
tags:
  - 00_03__AI
  - 00__System
  - 00__Index
  - 02__SDS
  - 02__Business
  - 02_02__SDS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.02 SDS/00. Index/_MOC_|00. Index]]"
outgoinglinks:
Version: v1.2
Audience: Architect / Designer / Dev Lead / AI Agent (Aegis)
Scope: Software Design Specification (SDS) 단계 전반
References:
level: 10.01.02
parent_level: 10.01
---
---
## 1. 목적

📘 SDS Index는 Stage 02(SDS)의 **단일 진입점**이다.  
SRS에서 확정된 요구사항(What)을 변경하지 않고 **설계 구조(How)** 로 전환하는 모든 활동은 본 문서의 우선순위를 따른다.

---

## 2. SDS 전체 구조

```
📘 Aegis – Architecture & Design Integration Guideline (v1.1)
├─ 🔗 SRS ↔ SDS Interface Contract
└─ 🔗 SDS ↔ SCS Interface Contract
```

---

## 3. Rule 문서

- 📘 **Aegis – Architecture & Design Integration Guideline**  
  → Stage 02의 최상위 헌법. 단순성·명확성·Traceability·ADR 기록을 강제하며 SRS 범위 확장을 전면 금지한다.
- 🔗 **SRS ↔ SDS Interface Contract**  
  → 요구사항 명세와 설계 산출물 간 매핑 규칙, 입·출력 인계 포맷을 정의한다.
- 🔗 **SDS ↔ SCS Interface Contract**  
  → 설계 산출물이 구현 단계로 전달될 때 유지해야 할 제약과 인계 검증 항목을 규정한다.

---

## 4. Guide 문서 (Human Reference)

- 📘 **Design Principles** – 품질 속성 중심의 설계 의사결정 기준
- 📘 **Modeling Guideline** – C4/PlantUML 표현 규칙 및 표기법
- 📘 **SDS Prompt Policy** – AI 설계 요청 시 필수 정책
- 🧭 **SDS Prompt Authoring Guide** – Human 전용 프롬프트 작성 절차

> Guide는 사람 전용 참고 자료이며 Rule을 대체하지 않는다.

---

## 5. Scope & Output 요약

- 📘 **SDS Scope Definition**  
  - 포함: 아키텍처 설계, 컴포넌트/인터페이스 구조, ADR  
  - 제외: 요구사항 변경, 구현 코드, 배포 상세
- 📘 **SDS Output Definition**  
  - 필수 산출물: Architecture Decision Record (ADR)  
  - 선택 산출물: SDS 문서, 다이어그램, 인터페이스 정의서  
  - 모든 산출물은 SRS 요구사항과 Traceability 유지

---

## 6. 사용 원칙 요약

- SRS의 What을 **확장 없이** How로 변환한다
- 설계 산출물은 항상 Traceable · Reviewable · Build-ready 상태를 유지한다
- 우선순위: Aegis Root Rule → Interface Contracts → Index → Guide
- 충돌·불확실 시 SRS/Helios 기준으로 재질문하거나 작업을 중단한다

---

## 7. 결론

📘 SDS Index는 설계 단계에서 사람과 AI가 동일한 기준으로 협업하기 위한 **유일한 공식 안내서**다.  
모든 SDS 작업은 본 문서가 정의한 구조와 우선순위를 기준으로 수행한다.
