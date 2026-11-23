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
# 🧱 Stage Folder Skeleton Standard (OS 정본)

## Purpose

- `10. Business` 내 Stage 폴더(SRS/SDS/SCS)의 하위 구조를 “최소 공통 스켈레톤” 기준으로 표준화한다.
- 목표:
  - Stage별 구조 편차로 인한 혼란 감소
  - 필요할 때만 폴더를 추가하여 빈 폴더/불필요 계층 방지

## Naming / Numbering (강제)

- Stage 폴더 내부의 진입/요약/목차는 항상 `00. Index/`를 사용한다.
- ChatGPT 등록용 엔트리(📌/Applied)는 반드시 `99. Artifact/`에서만 관리한다.
  - `99. Artifact/📌 ChatGPT 맞춤형 지침.md`
  - `99. Artifact/Applied.md`
  - (권장) `99. Artifact/Master Prompt.md`
- Stage 루트에는 `_MOC_.md`가 존재해야 한다.
- (해당 시) “정리 요청”을 Stage 전용 템플릿으로 특화한다면 `01. Rules/`에 `🧾 Organizer Contract...` 문서를 추가한다.

## Minimum Skeleton (권장 표준)

모든 Stage는 아래를 “필요한 경우에만” 가진다(빈 폴더는 만들지 않는다).

- `00. Index/` (필수)
- `01. Rules/` (필수)
- `02. Contract/` (필요 시)
- `03. Guides/` (필요 시)
- `04. Outputs/` (필요 시)

## Why Stage Structures Differ (원칙)

- SRS: 산출물 템플릿 비중이 커서 `04. Outputs/`가 효과적일 수 있다.
- SDS: Index성 문서 활용도가 높다.
- SCS: 규율/실행 중심이므로 `Outputs` 강제가 항상 최선은 아니다.

## Enforcement (운영)

- 신규 Stage/프로젝트 생성 시:
  - 필수 3종 + `00. Index/` + Root Rule 폴더만 먼저 만든다.
  - Contract/Guides/Outputs는 필요 시 추가한다.
- 표시명/태그/링크는 아래 운영 표준을 따른다.
  - Registration Pack: `📎 Custom Instructions Registration Pack Standard`
  - Display name: `🧷 Link Display Name Style Guide`
  - Tags: `🏷️ Tag & Metadata Governance`

