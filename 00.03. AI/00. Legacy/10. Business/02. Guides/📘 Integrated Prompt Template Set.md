---
type: Note
creation date: 2026-01-12 13:59
tags:
  - 00_03__AI
  - 00__System
  - 02__Business
  - 00__Common
  - 04__Standards
  - 02_00__Common
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/02. Guides/_MOC_|02. Guides]]"
outgoinglinks:
Version: v1.1
References:
level: 10
---
---

> SRS / SDS / SCS Unified Prompt
> SRS / SDS / SCS 작성 시 참고할 수 있는 표준 Prompt 템플릿 모음이다.

---

## Purpose

본 문서는 실행 계약(Contract)을 대체하지 않으며,
사람이 일관된 Prompt를 작성하기 위해 참고하는 표준 템플릿이다.

> Custom Instructions 등록/첨부 “최소 파일 세트(Registration Pack)” 운영 기준:  
> `01. Core/01. Operations/📎 Custom Instructions Registration Pack Standard.md`

---

## Scope

- SRS / SDS / SCS 단계별 Prompt 작성 시 참고
- 팀/개인별 Prompt 구조 일관성 확보 목적

## 01. 공통 기본 구조

```text
[Role]
너는 해당 문서 단계의 책임자이다.

[Task]
다음 작업을 수행하라.

[Context]
- 상위 산출물:
- 참조 ID 목록:
- 적용 범위:

[Output]
- 문서 유형:
- 형식:
- 구성 요소:

[Constraints]
- 상위 문서를 변경하지 않는다
- 추측하지 않는다

[Advanced]
- 불확실성 명시
- Traceability ID 유지
```

---

## 02. SRS 전용 Prompt

> ⚠️ Core 표준 문서에는 “Stage별 역할/금지/산출물 구조”를 직접 박지 않는다.  
> Stage별 세부는 해당 Stage의 Root Rule/Contract/Prompt Guide에서 오버레이한다.

### SRS 오버레이(참조)
- Root Rule: `10. Business/10.01 Architect/10.01.01 SRS/01. Rules/📗 Helios – PRD & Requirement Analysis Guideline.md`
- Contract: `10. Business/10.01 Architect/10.01.01 SRS/02. Contract/🔗 Requirement Traceability Rules.md`
- Human Guide: `10. Business/10.01 Architect/10.01.01 SRS/03. Guides/📘 SRS Prompt Authoring Guide.md`
- Custom Instructions:
  - `10. Business/10.01 Architect/10.01.01 SRS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - `10. Business/10.01 Architect/10.01.01 SRS/99. Artifact/Applied.md`

---

## 03. SDS 전용 Prompt

### SDS 오버레이(참조)
- Root Rule: `10. Business/10.01 Architect/10.01.02 SDS/01. Rules/📘 Aegis – Architecture & Design Integration Guideline.md`
- Interface Contracts:
  - `10. Business/10.01 Architect/10.01.02 SDS/02. Contract/🔗 SRS ↔ SDS Interface Contract.md`
  - `10. Business/10.01 Architect/10.01.02 SDS/02. Contract/🔗 SDS ↔ SCS Interface Contract.md`
- Human Guide: `10. Business/10.01 Architect/10.01.02 SDS/03. Guides/📘 SDS Prompt Authoring Guide.md`
- Custom Instructions:
  - `10. Business/10.01 Architect/10.01.02 SDS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - `10. Business/10.01 Architect/10.01.02 SDS/99. Artifact/Applied.md`

---

## 04. SCS 전용 Prompt

### SCS 오버레이(참조)
- Root Rule: `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/⚙️ Forge – Software Construction Specification Guideline.md`
- Sub Rules:
  - `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md`
  - `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/🟦 SCS Task Execution Playbook.md`
- Human Guide: `10. Business/10.01 Architect/10.01.03 SCS/03. Guides/🧭 SCS Prompt Authoring Guide.md`
- Custom Instructions:
  - `10. Business/10.01 Architect/10.01.03 SCS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - `10. Business/10.01 Architect/10.01.03 SCS/99. Artifact/Applied.md`

---

## 05. 결론

본 문서는 “Core 공통 Prompt 골격”을 제공한다.  
Stage별 세부 역할/금지/산출물 형식은 각 Stage의 Root Rule/Contract/Guide에서 정의하며,  

---
