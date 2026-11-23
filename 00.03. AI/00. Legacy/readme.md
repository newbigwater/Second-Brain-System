---
Version: v1.0
---
---
# 🤖 AI Project Suite – Integrated Framework (2026 Refresh)

## 🧭 개요
→ 본 Suite는 ChatGPT 기반 AI Agent가 **요구사항(SRS) → 설계(SDS) → 개발(SCS) → 관리(PM) → 번역(Translation)** 전 주기를 자동화하도록 설계된 메타 가이드입니다.  
→ 모든 단계는 `01. Core`에서 정의된 사고·운영·출력 규칙을 상속하며, Project별 Prompt/Traceability/체크리스트가 상호 호환되도록 통합되었습니다.  
→ 이번 리프레시는 Canvas vs plainText, 링크 무결성, Traceability 자동화를 해결하기 위한 보조 정책 제안까지 포함합니다.

> 📘 전체 구조 개요: [ChatGPT Custom Instructions – AI Project Suite](docs/ChatGPT%20Custom%20Instructions%20%E2%80%93%20AI%20Project%20Suite.md)  
> 📎 ChatGPT 등록 시: 각 Stage `99. Artifact/Applied.md`를 붙여넣고, 자세한 규칙은 같은 폴더의 `📌 ChatGPT 맞춤형 지침.md`에서 확인하세요.
>
> 구조/용어 정합화의 SSOT: [Architecture Design](docs/Architecture%20Design.md)

## 🏗 프로젝트 계층
| 레이어 | 프로젝트 | 의미 | 역할 |
| --- | --- | --- | --- |
| 00 Root | `01. Core/00. Charter` | 최상위 규약/Charter | Common Rule, Operational Rules, Execution Gate |
| 00.01 Core | `01. Core` ([MOC](01.%20Core/_MOC_.md)) | 전 프로젝트 공통 지침 | Operations/Standards/Frameworks/Custom Instructions |
| 10. Business | `10. Business` ([MOC](10.%20Business/_MOC_.md)) | SRS/SDS/SCS 및 Business Common | `00. Index` + `01. Rules`(Traceability) + `02. Guides`(템플릿) + Stage별 `99. Artifact` |
| 10. Project | `10. Business/10.02 Project` ([MOC](10.%20Business/10.02%20Project/_MOC_.md)) | PM/Translation | Chronos·LinguaBridge Stage와 공통 구조(00~02 + 99) |
| 20. Personal | `20. Personal` ([MOC](20.%20Personal/_MOC_.md)) | 학습/개인/도메인 특화 프로젝트 | Stage Skeleton(00 Index / 01 Rules / 02 Guides / 99 Artifact) |

---

## 🏗 프로젝트 구조 및 역할
| 프로젝트                           | 이름의 의미 및 선정 이유                                                            |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| **📗 Helios**                  | ‘Helios(헬리오스)’는 그리스 신화의 태양신으로, 모든 것을 밝히는 빛의 상징. → 프로젝트의 출발점으로서 **요구사항의 방향과 시야를 밝히는 역할** |
| **📘 Aegis**                   | ‘Aegis(이지스)’는 제우스의 방패로, 보호·방어·안정의 상징. → 시스템의 **안정적 설계와 견고한 구조**를 의미                     |
| **⚙️ Forge**                   | ‘Forge(포지)’는 대장간 또는 단련의 장소. → 설계를 실제 코드로 구현하는 **창조의 현장**을 상징                            |
| **📚 Chronos**                 | ‘Chronos(크로노스)’는 시간의 신으로, 모든 흐름을 통제하는 존재. → 프로젝트의 **일정·리스크·품질을 통합 관리**하는 역할             |
| **🌐 LinguaBridge**            | ‘Lingua’(언어) + ‘Bridge’(다리)의 합성어. → **언어 장벽을 넘는 커뮤니케이션의 연결 고리**                         |
| **📌 Genius Thinking Formula** | 창의적 사고와 문제 정의를 체계화하는 **지적 인프라의 중심**                                                     |

| 구분 | 프로젝트 | 역할 | 주요 문서 | Core Reference |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------- | --------------------------------------------- |
| **10.01.01 – SRS** | [📗 Helios – PRD & Requirement Analysis Guideline](10.%20Business/10.01%20Architect/10.01.01%20SRS/01.%20Rules/%F0%9F%93%97%20Helios%20%E2%80%93%20PRD%20&%20Requirement%20Analysis%20Guideline.md) | 요구사항 분석 및 기획 | PRD / SRS / Traceability Matrix | 📊 Business & Domain Contract / 📌 Genius Formula |
| **10.01.02 – SDS** | [📘 Aegis – Architecture & Design Integration Guideline](10.%20Business/10.01%20Architect/10.01.02%20SDS/01.%20Rules/%F0%9F%93%98%20Aegis%20%E2%80%93%20Architecture%20&%20Design%20Integration%20Guideline.md) | 시스템 아키텍처 및 설계 | SDS / C4 Model / ADR / Data Model | 📌 Genius Formula / 🧠 AI Programming Rule |
| **10.01.03 – SCS** | [⚙️ Forge – Software Construction Specification Guideline](10.%20Business/10.01%20Architect/10.01.03%20SCS/01.%20Rules/%E2%9A%99%EF%B8%8F%20Forge%20%E2%80%93%20Software%20Construction%20Specification%20Guideline.md) | 개발·코드 구현 및 테스트 | SCS / Source Code / Build Script | 🧠 AI Programming Rule / 📌 Genius Formula |
| **10.02.01 – PM** | [📚 Chronos – Project Management & Coordination Guideline](10.%20Business/10.02%20Project/10.02.01%20PM/01.%20Rules/%F0%9F%93%9A%20Chronos%20%E2%80%93%20Project%20Management%20&%20Coordination%20Guideline.md) | 일정·리스크·리소스 관리 | WBS / Gantt / Risk Matrix | 📊 Business Rule / 📌 Genius Formula |
| **10.02.02 – Translation** | [🌐 LinguaBridge – Multilingual Translation Guideline](10.%20Business/10.02%20Project/10.02.02%20Translation/01.%20Rules/%F0%9F%8C%90%20LinguaBridge%20%E2%80%93%20Multilingual%20Translation%20Guideline.md) | 다국어 번역 및 커뮤니케이션 품질 관리 | Multilingual Translation Guideline | 📌 Genius Formula |
| **Core (00.01)**            | [📌 Genius Thinking Formula Prompt](01.%20Core/03.%20Frameworks/%F0%9F%93%8C%20Genius%20Thinking%20Formula%20Prompt.md) | 사고 프레임워크 및 창의적 문제 해결 | Idea Generation / Analytical Thinking | — |

---

## 🔗 프로젝트 상호 관계

```
📗 Helios (SRS)
    ↓ 요구사항 전달
📘 Aegis (SDS)
    ↓ 설계 전개
⚙️ Forge (SCS)
    ↓ 코드 구현 및 테스트
────────────────────────────
📚 Chronos → 일정·리스크·리소스 제어
🌐 LinguaBridge → 다국어 협업/품질
📌 Core Set → 사고·출력·프롬프트 기반
📊 Business Rule / 🧠 AI Rule → 도메인·코드 품질 상속
```

## 📌 Core Directive Set (Level 00~00.01)
| 문서 | 포커스 | 핵심 규정 |
| --- | --- | --- |
| [📌 Genius Thinking Formula Prompt](01.%20Core/03.%20Frameworks/%F0%9F%93%8C%20Genius%20Thinking%20Formula%20Prompt.md) | 사고 프레임 | 역할 확인 → 10개 공식 중 2개 혼합 → 분석 1500자·아이디어 3000자 → Canvas 산출 |
| [🧠 Common Rule](01.%20Core/00.%20Charter/%F0%9F%A7%A0%20Common%20Rule.md) | 최상위 운영 | 사실 검증, 불확실성 표기, Manager/Worker/Evaluator 사고, 요청 타입별 출력 모드(설명/출력/생성/정리) 및 Artifact 강제 |
| [🖋️ StudyNote Markdown Rulebook](01.%20Core/00.%20Charter/%F0%9F%96%8B%EF%B8%8F%20StudyNote%20Markdown%20Rulebook.md) | 순수 Markdown | 사용자 헤더 존중, plainText fenced block, Tab 기반 bullet, 약어 최초 정의, Footnote 표준, Canvas 금지 |
| [🏗️ Standard Prompt Policy](01.%20Core/00.%20Charter/%F0%9F%8F%97%EF%B8%8F%20Standard%20Prompt%20Policy.md) | Prompt 구조 | Role→Task→Context→Output→Constraints→Advanced 6단, 품질 체크리스트, 명령 재현성 |
| [🏷️ Tag & Metadata Governance](01.%20Core/01.%20Operations/%F0%9F%8F%B7%EF%B8%8F%20Tag%20&%20Metadata%20Governance.md) | 운영(Obsidian) | 레이어 태그 정규 체계, legacy 병행 유지, 쿼리 권장 방식, 정리/제거 정책 |
| [📘 Integrated Prompt Template Set](10.%20Business/02.%20Guides/%F0%9F%93%98%20Integrated%20Prompt%20Template%20Set.md) | Business Common | 공통 템플릿 + Stage 오버레이 참조 |
| [🔗 Traceability Prompt Rules](10.%20Business/01.%20Rules/%F0%9F%94%97%20SRS%20%E2%86%94%20SDS%20%E2%86%94%20SCS%20Traceability%20Prompt%20Rules.md) | Business Common | REQ/DES/IMP, 상위 산출물 불변, ID 참조만 허용, Trace Table 필수 |

> 정리 요청(내용/용어/상세 정리)은 기본적으로 StudyNote 규칙을 따르되,  
> Stage/Project가 `🧾 Organizer Contract(정리 요청 전용 Output Contract)`를 제공하는 경우 `🧠 Common Rule 07.01.04-A`에 따라 템플릿을 특화할 수 있다.

## 📚 Stage Guidance
### 📗 Helios – SRS
→ PRD/SRS/Traceability/Change Log 산출, 구조: Overview → Core Functionalities → System Context → References → Validation Checklist.  
→ [📊 Business & Domain Contract](10.%20Business/10.01%20Architect/10.01.01%20SRS/02.%20Contract/%F0%9F%93%8A%20Business%20&%20Domain%20Contract.md)로 도메인 기준/용어/계약 관점 정렬.  
→ [🔗 Requirement Traceability Rules](10.%20Business/10.01%20Architect/10.01.01%20SRS/02.%20Contract/%F0%9F%94%97%20Requirement%20Traceability%20Rules.md)로 REQ/DES/IMP 추적 규칙을 고정.  
→ [📝 PRD Reference Template](10.%20Business/10.01%20Architect/10.01.01%20SRS/03.%20Guides/%F0%9F%93%9D%20PRD%20Reference%20Template.md)로 섹션별 기대치를 표준화.

### 📘 Aegis – SDS
→ Architect/Designer/AI Agent/Developer 역할, SDS/C4/PlantUML/ADR/Interface 산출.  
→ SOLID/DRY/KISS/YAGNI, 높은 응집·낮은 결합, 품질 속성 정의, ADR 기록, Peer/ARB 리뷰 의무.

### ⚙️ Forge – SCS
→ Developer/Reviewer/DevOps/AI Agent/Architect 책임, SCS/Source/Test/CI/CD/Deploy 문서화.  
→ 의사코드 승인 후 구현, TODO 금지, import/예외/테스트 필수, 자동화 우선.  
→ [📘 AI Coding Behavior Rule](10.%20Business/10.01%20Architect/10.01.03%20SCS/01.%20Rules/%F0%9F%93%98%20AI%20Coding%20Behavior%20Rule.md)와 [🟦 SCS Task Execution Playbook](10.%20Business/10.01%20Architect/10.01.03%20SCS/01.%20Rules/%F0%9F%9F%A6%20SCS%20Task%20Execution%20Playbook.md)이 “요구 분석 → 의사코드 → 승인 → 구현” 실행 규율을 강제.

### 📚 Chronos – PM
→ PM/AI Coordinator/Stakeholder/Aegis·Forge Agent 협업, 목표/범위→요구 추적→리스크→진행→품질 프로세스.  
→ 산출물: WBS, Gantt, Risk Matrix, Progress Report(Markdown/CSV/Excel), Canvas 보고 가능.  
→ 리스크 매트릭스·QA·보고 주기 체크리스트 내재.

### 🌐 LinguaBridge – Translation
→ 한국어 입력 시 교정→격식체 변환→한국어/English/Русский 병렬 출력, 존칭·톤 일관성.  
→ 입력 감지→전처리→번역→QA 4단계, 출력은 Canvas/Markdown 구조 유지.  
→ 품질표: 언어 감지 정확도, 교정 품질, 번역 정확성, 어투, 포맷.

## 🧰 Backup Role Guides
→ [📋 Project Management Group Rule](99.%20Backup/%F0%9F%93%8B%20Project%20Management%20Group%20Rule.md): 목표/범위/일정/비용 정의, 리스크·보고·자원 관리, Canvas 산출.  
→ [📐 Architect Group Rule](99.%20Backup/%F0%9F%93%90%20Architect%20Group%20Rule.md): 품질 속성 우선순위, ADR 필수, PlantUML·Canvas 문서, Peer Review.  
→ [🧩 Designer Group Rule](99.%20Backup/%F0%9F%A7%A9%20Designer%20Group%20Rule.md): SOLID/DRY/KISS/YAGNI, 패턴 근거 기록, 클래스/시퀀스/컴포넌트 다이어그램, 변경 이력.

## 🧱 Prompt & Traceability 플랫폼
→ Stage별 Prompt Policy가 공통 템플릿을 상속하여 Role/Task/Constraints를 잠금 처리, 추론 오염을 차단합니다.  
→ REQ-### / DES-### / IMP-### ID를 `Helios → Aegis → Forge` 매핑 테이블로 관리하고, 산출물마다 상위 ID 참조 표를 필수 포함합니다.  
→ Prompt 실행 전에 “역할 미확정 → 재질문” 규칙과 “분석 1500자 / 아이디어 3000자” 규칙을 미들웨어에서 검증하는 것을 권장합니다.

## 🗂 Output 거버넌스 (Canvas vs PlainText)
→ Common Rule §7이 자연어 트리거(설명/출력/생성/정리)를 판별해 적절한 모드(Markdown Plain Text, Artifact Output, Artifact File Generation, StudyNote 규격)를 자동 적용합니다.  
→ 기본값은 StudyNote Rulebook에 따라 **plainText fenced block + Tab bullet**이며, Helios/Aegis/Forge/Chronos/LinguaBridge/Backup 문서가 Canvas를 요구할 경우 dual-output(plain + Canvas) 또는 전용 변환 파이프라인을 사용합니다.  
→ 권장 정책: front-matter에 `output_mode=plain|canvas|dual`, `canvas_reason`, `plain_reason`을 선언하고 “Output Mode Arbiter” 스크립트가 Agent 응답 전에 우선순위를 결정하도록 합니다.  
→ 변환 도구 제안: Markdown AST 기반 CLI가 plainText 규칙 검증, Canvas 템플릿 생성을 자동화하여 Core ↔ Stage 간 충돌을 제거합니다.

## 🔗 링크 무결성 & 자동화
→ 상대 경로 링크가 많으므로 Git Hook 또는 GitHub Actions로 Markdown/Obsidian 링크를 파싱해 존재 여부를 검사하고, 실패 시 PR 차단 및 Chronos 리포트에 이슈를 등록합니다.  
→ `links.yaml` 형태의 Canonical Registry를 유지해 경로 변경 시 alias를 제공, Traceability ID와 함께 대시보드에서 상태를 시각화합니다.  
→ Helios/Aegis/Forge 검증표·LinguaBridge 3언어 출력 등 반복 구조는 템플릿화하여 링크·포맷 비정합을 조기에 탐지합니다.

## 📂 디렉터리 맵
```
./
├── 01. Core
│   ├── 00. Charter/
│   │   ├── 🧠 Common Rule.md
│   │   ├── 🖋️ StudyNote Markdown Rulebook.md
│   │   └── 🏗️ Standard Prompt Policy.md
│   ├── 01. Operations/
│   ├── 02. Standards/
│   ├── 03. Frameworks/
│   │   └── 📌 Genius Thinking Formula Prompt.md
│   └── 99. Artifact/
│       ├── Master Prompt.md
│       ├── 📌 ChatGPT 맞춤형 지침.md
│       └── Applied.md
├── 10. Business
│   ├── 00. Index/
│   │   └── 📘 Business Level Index.md
│   ├── 01. Rules/
│   │   └── 🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md
│   ├── 02. Guides/
│   │   └── 📘 Integrated Prompt Template Set.md
│   ├── 10.01 Architect/
│   │   ├── 10.01.01 SRS/
│   │   ├── 10.01.02 SDS/
│   │   └── 10.01.03 SCS/
│   └── 10.02 Project/
│       ├── 10.02.01 PM/
│       └── 10.02.02 Translation/
├── 20. Personal
│   ├── 20.00 Personal/
│   ├── 20.01 English/
│   ├── 20.02 Computer-Science/
│   └── 20.03 ISA-95/
└── 99. Backup
```

## ⚙️ 운영 원칙
1. 연계 자동화 → Helios→Aegis→Forge 데이터 파이프라인, Chronos의 일정/리스크 통제, LinguaBridge의 글로벌 커뮤니케이션 지원.  
2. 문서 표준화 → plainText 기본, 필요 시 Canvas 변환, PlantUML/CSV 일관성, 약어 최초 정의.  
3. Core 상속 → Core 변경 시 Stage/Support 문서가 자동 갱신되도록 메타데이터와 검증 파이프라인을 함께 유지.  
4. 추적성과 검증 → 모든 산출물에 Trace Table/체크리스트 포함, Link Integrity/Output Lint 파이프라인으로 품질 보증.
5. Stage 확장 → `workspace/tools/stage_targets.json`에 신규 Stage(`title`, `base_dir`, `includes`)를 추가하면 자동화 스크립트가 해당 Stage `99. Artifact`를 생성·검증한다.

## ✅ 운영 목적
→ 요구→설계→구현→운영→번역의 지식 흐름을 AI 중심으로 자동화  
→ PM(Chronos) 기반 통합 거버넌스와 다국어 협업 지원  
→ Traceability·출력·링크 품질을 자동 검증하는 보조 정책으로 지침 상충을 제거  
→ “Helios가 빛을 비추고, Aegis가 구조를 세우며, Forge가 현실을 만든다. Chronos가 시간을 관리하고, LinguaBridge가 세계를 잇는다. 그리고 Genius Formula가 모든 생각의 출발점이다.”
