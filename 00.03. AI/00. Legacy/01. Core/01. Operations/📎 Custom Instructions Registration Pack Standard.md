---
type: Note
creation date: 2026-02-09
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 01__Core
  - 03__Operations
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/01. Operations/_MOC_|01. Operations]]"
outgoinglinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/00. Charter/🧠 Common Rule|🧠 Common Rule]]"
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/99. Artifact/Applied|01. Core Applied]]"
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/02. Guides/📘 Integrated Prompt Template Set|📘 Integrated Prompt Template Set]]"
Version: v1.1
References:
level: 0.01
---
---

## Purpose

- 본 문서는 “ChatGPT Custom Instructions 등록(또는 세션 시작 시 적용)”에 필요한 **최소 파일 세트(Registration Pack)** 를 표준화한다.
- 목표:
  - 모델/환경이 달라도(레포 접근 가능/불가) **동일한 규칙 우선순위**가 재현되게 한다.
  - `Applied.md`가 “참조 포인터” 역할임을 명확히 하고, 필요 시 **첨부 파일**로 보완한다.

---

## 용어

- **📌 ChatGPT 맞춤형 지침(메인)**: Custom Instructions에 직접 입력할 “메인 지침” 문서(정식 포맷: Role/Rule Set/Scope/Non-negotiables/Output modes/Pre-process/Process/Post-process).
- **Applied**: 위 `📌 ChatGPT 맞춤형 지침`이 1,500자 제한을 넘는 경우 사용하는 “대체 등록용” 문서(최소 구성: Role + “첨부된 📌 지침을 따르라”).
- **Registration Pack**: 특정 작업을 시작하기 위해 *반드시* 등록/첨부해야 하는 문서 묶음.

---

## 환경별 규칙 (중요)

### A) Repo-Access 환경 (Cursor/Agent 등)

- 모델이 워크스페이스 파일을 직접 읽을 수 있다면,
  - 가능하면 **`📌 ChatGPT 맞춤형 지침.md`를 Custom Instructions에 직접 입력**한다.
  - 만약 입력 길이 제한으로 `📌`를 넣을 수 없으면 **`Applied.md`를 입력**하고, `📌` 문서를 함께 첨부한다.

### B) Plain ChatGPT 환경 (파일 접근 불가)

- 모델이 파일을 직접 읽을 수 없다면,
  - `Applied.md`만으로는 “참조 포인터”를 따라갈 수 없으므로,
  - 아래의 “Stage별 최소 첨부 세트”를 **대화에 첨부**(또는 본문에 포함)해야 한다.

---

## 공통 Registration Pack (항상)

- **필수**
  - `01. Core/00. Charter/🧠 Common Rule.md`
  - 작업 대상(Stage/Project)의 `99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - (필요 시) 작업 대상(Stage/Project)의 `99. Artifact/Applied.md`

- **권장(정리/EDU 성격 출력물 포함 시)**
  - `01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md`
  - (해당 시) 작업 대상(Stage/Project)의 `🧾 Organizer Contract...` 문서
  - 표준: `01. Core/01. Operations/🧾 Organizer Contract Standard.md`

---

## Stage별 최소 첨부 세트 (Plain ChatGPT 기준)

### SRS (10. Business/10.01 Architect/10.01.01 SRS)

- `10. Business/10.01 Architect/10.01.01 SRS/99. Artifact/Applied.md`
- `10. Business/10.01 Architect/10.01.01 SRS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `10. Business/10.01 Architect/10.01.01 SRS/01. Rules/📗 Helios – PRD & Requirement Analysis Guideline.md`
- `10. Business/10.01 Architect/10.01.01 SRS/02. Contract/🔗 Requirement Traceability Rules.md`
- (도메인/용어 계약이 필요한 경우) `10. Business/10.01 Architect/10.01.01 SRS/02. Contract/📊 Business & Domain Contract.md`

### SDS (10. Business/10.01 Architect/10.01.02 SDS)

- `10. Business/10.01 Architect/10.01.02 SDS/99. Artifact/Applied.md`
- `10. Business/10.01 Architect/10.01.02 SDS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `10. Business/10.01 Architect/10.01.02 SDS/01. Rules/📘 Aegis – Architecture & Design Integration Guideline.md`
- `10. Business/10.01 Architect/10.01.02 SDS/02. Contract/🔗 SRS ↔ SDS Interface Contract.md`
- `10. Business/10.01 Architect/10.01.02 SDS/02. Contract/🔗 SDS ↔ SCS Interface Contract.md`

### SCS (10. Business/10.01 Architect/10.01.03 SCS)

- `10. Business/10.01 Architect/10.01.03 SCS/99. Artifact/Applied.md`
- `10. Business/10.01 Architect/10.01.03 SCS/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/⚙️ Forge – Software Construction Specification Guideline.md`
- `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md`
- `10. Business/10.01 Architect/10.01.03 SCS/01. Rules/🟦 SCS Task Execution Playbook.md`

### PM (10. Business/10.02 Project/10.02.01 PM)

- `10. Business/10.02 Project/10.02.01 PM/99. Artifact/Applied.md`
- `10. Business/10.02 Project/10.02.01 PM/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `10. Business/10.02 Project/10.02.01 PM/01. Rules/📚 Chronos – Project Management & Coordination Guideline.md`

### Translation (10. Business/10.02 Project/10.02.02 Translation)

- `10. Business/10.02 Project/10.02.02 Translation/99. Artifact/Applied.md`
- `10. Business/10.02 Project/10.02.02 Translation/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `10. Business/10.02 Project/10.02.02 Translation/01. Rules/🌐 LinguaBridge – Multilingual Translation Guideline.md`

---

## Application 프로젝트 (20. Personal)

- 원칙은 동일하다.
  - `Applied.md` + `📌 ... Custom Instructions.md`가 기본 세트
  - 프로젝트가 “전용 모드/체크리스트/템플릿”을 갖는다면 해당 문서도 함께 첨부

예시(ISA-95):
- `20. Personal/20.03 ISA-95/99. Artifact/Applied.md`
- `20. Personal/20.03 ISA-95/99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- (작업 Level에 맞는 Prompt/Checklist 문서)

---

## 우선순위(Conflict Resolution)

- 충돌 시 기본 우선순위:
  - **🧠 Common Rule**
  - 해당 Stage/Project Root Rule (예: Helios/Aegis/Forge/Chronos/LinguaBridge)
  - Contracts (Traceability/Interface/Domain 등)
  - `📌 ChatGPT 맞춤형 지침(메인)` → `Applied.md`(대체용)

> `Applied.md`는 길이 제한 시 사용하는 “대체 등록용”이다.  
> 원칙적으로는 `📌 ChatGPT 맞춤형 지침.md`를 메인으로 사용한다.

