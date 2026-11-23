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
  - "[[📎 Custom Instructions Registration Pack Standard|📎 Registration Pack Standard]]"
  - "[[🧷 Link Display Name Style Guide|🧷 Link Display Name Style Guide]]"
  - "[[🏷️ Tag & Metadata Governance|🏷️ Tag & Metadata Governance]]"
Version: v1.1
References:
level: 0.01
---
---

## Purpose

- 본 문서는 `10. Business` 내 Stage 폴더(SRS/SDS/SCS)의 하위 구조를 “최소 공통 스켈레톤” 기준으로 정리한다.
- 목표:
  - Stage마다 다르게 생겨서 생기는 혼란을 줄이고
  - 실제로 필요한 경우에만 폴더를 추가해 “빈 폴더/불필요한 계층”을 방지한다.

---

## Naming / Numbering (강제)

- Stage 폴더 내부의 “진입/요약/목차”는 **항상 `00. Index/`** 를 사용한다.
- ChatGPT 등록용 엔트리(📌/Applied)는 **반드시 `99. Artifact/`에서만** 관리한다.
  - `99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - `99. Artifact/Applied.md`
  - (권장) `99. Artifact/Master Prompt.md`
- Stage 루트에는 `_MOC_.md`가 존재해야 한다.
- (해당 시) “정리 요청(내용/용어/상세 정리)”을 Stage 전용 템플릿으로 특화한다면,
  - `01. Rules/`에 `🧾 Organizer Contract...` 문서를 추가한다.

---

## Minimum Skeleton (권장 표준)

모든 Stage는 아래를 “필요한 경우에만” 가진다(빈 폴더는 만들지 않는다).

- `00. Index/` (필수)
  - 단계 진입점 문서(예: `SDS Index`, Scope/Output 정의 등)
- `01. Rules/` (필수)
  - Root Rule(예: Helios/Aegis/Forge)
  - 단계의 금지/허용/품질 규정
- `02. Contract/` (필요 시)
  - 도메인/추적성/인터페이스 같은 “실행 계약”
- `03. Guides/` (필요 시)
  - 사람용 작성 가이드, 템플릿, 예시
- `04. Outputs/` (필요 시)
  - 문서 템플릿(특히 SRS처럼 산출물 템플릿 세트가 고정적일 때)

---

## Why Stage Structures Differ (원칙)

- **SRS**: 산출물 템플릿(SRS/RTM/CR Log) 비중이 커서 `04. Outputs/`를 두는 것이 효과적이다.
- **SDS**: Index성 문서(범위/산출물 정의 등)가 분화되기 쉬워 `00. Index/` 활용도가 높다.
- **SCS**: 규율/실행(playbook) 중심이며 산출물이 코드/테스트로 이어지므로 `Outputs`를 Stage 표준으로 강제하지 않는 편이 낫다.

---

## Enforcement (운영)

- 신규 Stage/프로젝트 생성 시:
  - “필수 3종 + `00. Index/` + Root Rule 폴더”만 먼저 만든다.
  - Contract/Guides/Outputs는 필요가 생길 때만 추가한다.
- 표시명/태그/링크는 아래 운영 표준을 따른다.
  - Registration Pack: `📎 Custom Instructions Registration Pack Standard`
  - Display name: `🧷 Link Display Name Style Guide`
  - Tags: `🏷️ Tag & Metadata Governance`

