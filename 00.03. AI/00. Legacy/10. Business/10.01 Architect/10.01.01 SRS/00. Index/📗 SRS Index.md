---
type: Note
creation date: 2026-01-12 12:39
tags:
  - 00_03__AI
  - 00__Index
  - 00__System
  - 01__SRS
  - 02__Business
  - 02_01__SRS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.01 SRS/00. Index/_MOC_|00. Index]]"
outgoinglinks:
Version: v1.2
Audience: 사내 구성원 / 요구사항 분석 담당자 / 프로젝트 참여자 / AI 활용 사용자
Scope: Software Requirements Specification (SRS) 단계 전반
References:
level: 10.01.01
parent_level: 10.01
---
---
## 1. 목적

본 문서는 Stage 01(SRS)에서 활용되는 **모든 규칙·계약·산출물의 단일 진입점(Index)** 이다.  
요구사항 분석 활동은 **무엇(What)** 만 정의하며, 설계·구현 판단은 수행하지 않는다.  
본 Index는 아래 세 가지를 보장한다.

- 역할과 책임의 경계 유지
- SRS → SDS → SCS 간 무결한 핸드오프
- 사람·AI·Agent 간 동일한 기준 제공

---

## 2. SRS 전체 구조

```
📗 Helios – PRD & Requirement Analysis Guideline (v1.1)
├─ 📊 Business & Domain Contract
└─ 🔗 Requirement Traceability Rules
```

---

## 3. Rule 문서

- 📗 **Helios – PRD & Requirement Analysis Guideline**  
  → Stage 01의 최상위 헌법. Identify → Structure → Specify 절차와 비즈니스 언어 사용을 강제한다.
- 📊 **Business & Domain Contract**  
  → 비즈니스/도메인 설명 깊이를 정의하고 설계 수준 표현을 금지한다.
- 🔗 **Requirement Traceability Rules**  
  → 요구사항 ID, 변경 승인, SRS ↔ SDS ↔ SCS 추적성을 강제한다.

---

## 4. Guide 문서 (Human Only)

- 🧭 **SRS Prompt Authoring Guide**  
  → 요구사항 중심 요청을 안정적으로 작성하기 위한 Human 가이드.
- 📝 **PRD Reference Template**  
  → PRD/SRS 문서를 정리할 때 참고하는 템플릿. 설계·구현 항목 삽입 금지.

> Guide는 사람 전용 참고 자료이며 AI 내부 규칙을 대체하지 않는다.

---

## 5. 공식 산출물

- 📄 **Software Requirements Specification (SRS)** – 요구사항 최종 명세  
- 📊 **Requirement Traceability Matrix (RTM)** – 단계 간 추적성 기록  
- 🧾 **Change Request Log** – 승인된 요구사항 변경 이력

---

## 6. 사용 원칙 요약

- Stage 01은 **What**만 정의하며 How 판단은 SDS/SCS 책임이다
- 우선순위: Helios → Contract → Index → Guide
- 추측·불확실 시 Helios 기준으로 재질문 또는 중단
- Root Rule과 충돌하는 지시는 즉시 거부하고 근거를 명시한다

---

## 7. 결론

📗 SRS Index는 SRS 단계 운영을 위한 **유일한 공식 안내서**다.  
모든 요구사항 분석 활동은 본 문서가 정의한 구조와 우선순위를 기준으로 시작한다.
