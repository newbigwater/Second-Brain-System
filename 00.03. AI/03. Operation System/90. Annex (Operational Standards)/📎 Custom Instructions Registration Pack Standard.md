---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Annex
Version: v1.0
Status: Active
RuleNamespace: OS-OPS
References: []
---
---
# 📎 Custom Instructions Registration Pack Standard (OS 정본)

## Purpose

- ChatGPT Custom Instructions 등록(또는 세션 시작 시 적용)에 필요한 최소 파일 세트(Registration Pack)를 표준화한다.
- 목표:
  - 모델/환경이 달라도 동일한 규칙 우선순위가 재현되게 한다.
  - `Applied.md`는 “참조 포인터”이며, 필요 시 첨부 파일로 보완한다.

## 용어

- **📌 ChatGPT 맞춤형 지침(메인)**: Custom Instructions에 직접 입력할 메인 지침 문서
- **Applied**: 메인 지침이 길이 제한을 넘을 때 사용하는 대체 등록용 문서
- **Registration Pack**: 특정 작업을 시작하기 위해 반드시 등록/첨부해야 하는 문서 묶음

## 환경별 규칙(중요)

### A) Repo-Access 환경 (Cursor/Agent)

- 가능하면 `📌 ChatGPT 맞춤형 지침.md`를 Custom Instructions에 직접 입력한다.
- 길이 제한이면 `Applied.md`를 입력하고 `📌` 문서를 함께 첨부한다.

### B) Plain ChatGPT 환경 (파일 접근 불가)

- `Applied.md`만으로는 참조 포인터를 따라갈 수 없으므로 Stage별 최소 첨부 세트를 대화에 첨부(또는 본문 포함)한다.

## 공통 Registration Pack (항상)

- 필수
  - `03. Operation System/00. Governance Kernel/Kernel.md`
  - `03. Operation System/01. Cognitive Engine/Cognitive Engine.md`
  - `03. Operation System/02. Validation Engine/Validation Engine.md`
  - `03. Operation System/03. Self-Reflection Loop/Reflection Loop.md`
  - `03. Operation System/04. Artifact Engine/Artifact Engine.md`
  - 작업 대상(Stage/Project)의 `99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - (필요 시) 작업 대상(Stage/Project)의 `99. Artifact/Applied.md`
- 권장(정리/EDU 성격 출력물 포함 시)
  - 본 Annex의 정리·EDU 산출물 기본 규칙: `03. Operation System/90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md`
  - (해당 시) 작업 대상(Stage/Project)의 `🧾 Organizer Contract...` 문서
  - 표준: `03. Operation System/90. Annex (Operational Standards)/🧾 Organizer Contract Standard.md`

## Stage별 최소 첨부 세트 (Plain ChatGPT 기준)

### SRS

- `.../99. Artifact/Applied.md`
- `.../99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `.../01. Rules/<SRS Root Rule>`
- `.../02. Contract/<Traceability Rules>`
- (필요 시) `.../02. Contract/<Domain Contract>`

### SDS

- `.../99. Artifact/Applied.md`
- `.../99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `.../01. Rules/<SDS Root Rule>`
- `.../02. Contract/<Interface Contracts>`

### SCS

- `.../99. Artifact/Applied.md`
- `.../99. Artifact/📌 ChatGPT 맞춤형 지침.md`
- `.../01. Rules/<SCS Root Rule & Playbooks>`

### PM / Translation / Application

- 원칙은 동일하다.
  - `Applied.md` + `📌 ...` 기본 세트
  - 프로젝트가 전용 모드/체크리스트/템플릿을 갖는다면 해당 문서도 함께 첨부

## 우선순위(Conflict Resolution)

- 충돌 시 기본 우선순위:
  - OS Layer 0~4
  - 해당 Stage/Project Root Rule
  - Contracts
  - `📌 ChatGPT 맞춤형 지침(메인)` → `Applied.md`(대체용)

