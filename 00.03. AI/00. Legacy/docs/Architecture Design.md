---
title: AI Project Suite – Architecture Design
last_updated: 2026-02-10
---
---

# 1. Overview
- **Purpose**: ChatGPT 기반 AI Agent가 “어떤 폴더에서 무엇을 참고해야 하는지”를 한눈에 이해하게 만드는 안내서이다.
- **Scope**: 레벨별 지침(`01. Core`, `10. Business`, `20. Personal`)과 이를 유지·배포하는 자동화 도구(`workspace/tools`).
- **Goals**
  1. **Up-only Link**: 하위 문서가 상위 규칙을 재정의하지 못하도록 구조화
  2. **Stage Skeleton 통일**: 모든 Stage가 `00 Index → 01 Rules → 02 Guides → 99 Artifact`를 갖추도록 강제
  3. **자동화 파이프라인**: Master Prompt·📌·Applied를 스크립트로 생성/검증/배포

> 초급자 Tip: “Core → Business → Personal” 순서로 내려가면서 폴더를 살펴보면 단계별 규칙이 어떻게 구체화되는지 쉽게 파악할 수 있다.

# 2. Level Architecture
| Level | 폴더 | 역할 | 핵심 산출물 |
| --- | --- | --- | --- |
| `00.00` | `01. Core/00. Charter` | Root Charter (🧠 Common Rule, StudyNote Rulebook, Standard Prompt Policy, Execution Gate) | Root 규칙 |
| `00.01` | `01. Core` | Operations / Standards / Frameworks / Core Custom Instructions | Stage 공통 운영 규칙 |
| `10.00` | `10. Business` | Helios/SRS, Aegis/SDS, Forge/SCS, Chronos/PM, LinguaBridge/Translation | 요구→설계→구현→운영 파이프라인 |
| `20.00` | `20. Personal` | Personal / English / Computer-Science / ISA-95 등 Mode 특화 Stage | 학습·도메인 지침 |
| `90.x` | `*/99. Artifact` | ChatGPT 등록용 Master Prompt / 📌 / Applied | Stage 산출물 |

**Link Policy (쉽게 보기)**
- `level` 숫자가 **작을수록 상위** 레벨이다. 예) `00.00` > `10.00` > `20.00`.
- 문서는 **동일 또는 상위 레벨**만 참조할 수 있다. (예: `10. Business` 문서는 `01. Core`는 참조 가능하지만 `20. Personal`은 참조 불가)
- `00 Layer`(Root)는 하위 Stage 내부 구조를 모른다는 가정으로 작성한다. 즉, Root 문서는 “Stage별 구체 지침”을 직접 언급하지 않는다.
- `_MOC_.md`는 “폴더 표지판” 역할만 한다. 세부 문서 링크는 해당 폴더 내부 문서에서 제공한다.

# 3. Stage Skeleton (공통)
| 디렉터리 | 내용 | 예시 |
| --- | --- | --- |
| `00. Index/` | Stage 목적, 상속 관계, 구조 요약 | `10. Business/00. Index/📘 Business Level Index.md` |
| `01. Rules/` | Stage 전용 최상위 지침, Traceability 계약, Custom Instructions | `10. Business/01. Rules/🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md` |
| `02. Guides/` | Prompt Template, Execution Checklist, Personal Instruction | `20. Personal/20.02 Computer-Science/02. Guides/📘 Computer-Science Study Rule.md` |
| `99. Artifact/` | Master Prompt, 📌 ChatGPT 맞춤형 지침, Applied (ChatGPT 등록) | `10. Business/10.01 Architect/10.01.01 SRS/99. Artifact/…` |

> (선택) “정리 요청(내용/용어/상세 정리)” 출력 형식을 Stage 전용 템플릿으로 특화하려면  
> `01. Rules/`에 `🧾 Organizer Contract...` 문서를 추가한다. (Root: `🧠 Common Rule 07.01.04-A`)

**사용 플로우 (예: Helios – SRS)**
1. `99. Artifact/Applied.md` 복사 → ChatGPT Custom Instructions에 붙여넣어 Stage 기본 규칙 등록
2. Helios 작업 시 `📌 ChatGPT 맞춤형 지침.md`를 열어 Snippet과 Self-check를 참고
3. 산출물(예: PRD, Traceability Matrix)을 작성한 뒤, 필요하면 `workspace/tools/artifact_master_prompt.py`를 실행하여 Master Prompt/📌/Applied를 최신 상태로 갱신
4. 최종 산출물은 항상 `99. Artifact` 폴더에서 관리 (중복 금지)

# 4. Domain Architecture
## 4.1 `01. Core` (AI Agent의 헌법과 중앙 운영국)
- **00. Charter**  
  - `🧠 Common Rule`: 사실성/불확실성 처리, 사고 모델(Manager/Worker/Evaluator), 출력 모드 판별 등 **모든 Stage가 준수해야 하는 최상위 규칙**.  
  - `🖋️ StudyNote Markdown Rulebook`: plainText fenced block, Tab bullet, Footnote 규칙을 정의.  
  - `🏗️ Standard Prompt Policy`: Role→Task→Context→Output 순서 등 Prompt 구조 강제.
- **01. Operations**  
  - Tag & Metadata, Stage Folder Skeleton, NG Fail Classification, Custom Instructions 등록 방법 등을 관리.  
  - Stage 폴더를 만들 때 “어떤 하위 폴더가 필요한지”를 알려주는 운영 매뉴얼에 해당.
- **02. Standards**  
  - 향후 Core Stage를 세분화할 때 사용할 표준 문서 자리. (현재는 비어있거나 Placeholder)
- **03. Frameworks**  
  - 📌 Genius Thinking Formula와 같은 사고 프레임워크. 전략/아이디어 요청 시 활성화한다.
- **04. Custom-Instructions**  
- (구) `04. Custom-Instructions`는 정리되었으며, ChatGPT 등록용 엔트리(`📌`/`Applied`)는 `99. Artifact/`에서 단일 관리한다.
- **99. Artifact**  
  - Core 전체를 하나로 묶은 Master Prompt. Stage별 Master Prompt는 여기서 선언된 규칙을 상속한다.

## 4.2 `10. Business` (요구→설계→구현 파이프라인)
- **공통 폴더**
  - `00. Index/📘 Business Level Index.md`: Business Stage 전체 구조 안내
  - `01. Rules/🔗 SRS ↔ SDS ↔ SCS Traceability Prompt Rules.md`: 세 Stage가 공유하는 Traceability 계약
  - `02. Guides/📘 Integrated Prompt Template Set.md`: SRS/SDS/SCS 공통 Prompt 템플릿
- **10.01 Architect**
  - **Helios(10.01.01 SRS)**: PRD/SRS/Traceability Matrix/Change Log 작성. Contract와 PRD Template이 필수.
  - **Aegis(10.01.02 SDS)**: Architecture/C4/PlantUML/ADR/Interface 설계. `SRS↔SDS`, `SDS↔SCS` 인터페이스 계약을 준수.
  - **Forge(10.01.03 SCS)**: 개발/테스트/CI/CD/배포. AI Coding Behavior Rule, Task Execution Playbook을 따라 구현.
- **10.02 Project**
  - **Chronos(10.02.01 PM)**: 일정/리스크/리소스/SLA 관리. WBS, Gantt, Risk Matrix가 주요 산출물.
  - **LinguaBridge(10.02.02 Translation)**: 다국어 번역/교정/QA 파이프라인. 입력 감지→전처리→번역→QA 4단계를 강제.
- **99. Artifact**  
  - Business Root 수준의 Master Prompt/📌/Applied를 보관. Stage 단위와 별개로 Business 전체에 대한 ChatGPT 세트를 가질 수 있다.

## 4.3 `20. Personal` (학습·연구·도메인 특화)
- **특징**
  - Mode 기반(예: English Grammar vs Podo, Computer-Science Study, ISA-95 Level 1~4 등).
  - 개인 학습/연구 영역이라도 Core/Business와 동일한 Skeleton·자동화를 따른다.
- **예시**
  - `20.01 English`: `01. Rules/Learn-English Priority Rules.md`, `02. Guides/Grammar/Template`, `99. Artifact/…`
  - `20.03 ISA-95` Level 1~4: 각 레벨마다 Index/Rules/Guides/Artifact 재배치 완료.
- **목표**: 개인용/연구용 지침도 Stage와 동일한 방식으로 ChatGPT에 등록할 수 있게 하는 것.

# 5. Automation Pipeline (`workspace/tools`)
| 카테고리 | 스크립트 | 기능 요약 |
| --- | --- | --- |
| Metadata & Structure | `apply_level_metadata.py` | front-matter에 `level`/`parent_level` 자동 삽입 |
|  | `replace_stage_paths.py` | Stage 리팩토링 후 경로 치환 |
| Stage 등록 | `workspace/tools/stage_targets.json` | JSON 배열. 신규 Stage를 추가하면 자동화 파이프라인이 해당 Stage의 `99. Artifact`를 생성 |
| Prompt Generation | `artifact_master_prompt.py` | Core/Business/Personal Master Prompt·📌·Applied 생성 (`stage_targets.json`을 읽어 확장) |
|  | `master_prompt_audit.py` | Master Prompt 단일 코드블록·Reference 완전성 검사 |
|  | `version_bump_and_master_references.py` | 지침 버전 관리 + Master Prompt Reference 주입 |
| Quality Assurance | `link_check.py` | 레포 전체 Markdown 링크 유효성 검사 |
|  | `check_level_links.py` | 레벨 위반(하위 참조) 탐지 |
| Archive | `workspace/tools/archive/*.py` | 과거 일회성 스크립트 (보관용) |

> 세부 사용법은 `docs/Tool Manual.md` 참고.

# 6. Artifact Lifecycle (단계별 흐름)
1. **규칙/가이드 수정**  
   - `apply_level_metadata.py` 로 level/parent_level 일치 여부 점검  
   - `link_check.py` 로 깨진 링크 탐지
2. **산출물 재생성**  
   - `artifact_master_prompt.py` 실행 → Stage `99. Artifact` 갱신
3. **감사**  
   - `master_prompt_audit.py` 로 코드블록·Reference 검증  
   - `check_level_links.py` 로 레벨 위반 탐지
4. **배포 & 기록**  
   - `version_bump_and_master_references.py` 로 Version/References 업데이트  
   - README, `docs/Architecture Design.md`, `docs/Tool Manual.md`에 변경사항 반영
5. **운영 보고**  
   - `link_integrity_report.md` 결과를 확인하고, 문제가 없으면 유지보수 로그에 첨부

# 7. Governance
- **Up-only Reference**: 하위 Stage는 상위 규칙을 재정의하지 않으며, 참조만 가능.
- **Stage Self-Containment**: Stage별 작업에 필요한 Rule/Guide/Checklist는 해당 Stage 디렉터리 안에 모두 존재해야 한다.
- **Artifact Singularity**: ChatGPT 등록용 문서는 `99. Artifact` 폴더에서만 관리 (중복 금지).
- **Automation First**: 수동 수정 전, 반드시 도구 파이프라인을 통해 산출물 생성·감사 후 배포.

# 8. Next Steps
1. 신규 Stage를 추가할 때는 `workspace/tools/stage_targets.json`에 `{ "title": "...", "base_dir": "...", "includes": [] }` 형태로 entry를 추가한 뒤, Skeleton과 자동화 절차를 복제한다.
2. `docs/Tool Manual.md`를 최신 상태로 유지해 AI Agent가 도구 사용법을 즉시 확보하도록 한다.
3. `link_check.py`와 `master_prompt_audit.py` 실행 결과를 README/Docs에 반영해 문서-산출물 간 신뢰도를 유지한다.