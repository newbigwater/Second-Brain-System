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
# 🧷 Link Display Name Style Guide (OS 정본)

## Purpose

- Obsidian wikilink의 표시명(`[[path|display]]`)을 일관된 규칙으로 고정한다.
- 목표:
  - 폴더 이동/리네이밍 이후에도 네비게이션 혼동 방지
  - legacy display name이 신규 레이어 구조를 오염시키는 문제 방지

## Core Rules (강제)

### 1) Stage/Layer 표시명은 “현 구조”를 기준으로 한다

- 허용 예:
  - `10.01.01 SRS`, `10.01.02 SDS`, `10.01.03 SCS`
  - `10.02.01 PM`, `10.02.02 Translation`
  - `20. Personal`
- 금지 예:
  - `|01. SRS`, `|04. PM`, `|05. Translation`, `|07. Application`

### 2) `_MOC_` 링크는 “폴더 진입” 표시명으로 통일한다

- 권장:
  - `[[10. Business/10.01 Architect/10.01.01 SRS/_MOC_|10.01.01 SRS]]`
  - `[[10. Business/10.02 Project/_MOC_|10.02 Project]]`

### 3) 문서 링크는 “문서 제목 그대로”를 표시명으로 사용한다

- 예:
  - `[[.../📘 Integrated Prompt Template Set|📘 Integrated Prompt Template Set]]`
  - `[[.../📎 Custom Instructions Registration Pack Standard|📎 Registration Pack Standard]]`

## Migration/Repair Rule (운영)

- 기존 문서에서 legacy 표시명이 발견되면:
  - 경로(path)는 그대로 유지한다.
  - 표시명(display)만 현 구조 기준으로 교체한다.
- 이 작업은 링크 무결성에 영향을 주지 않으며, 혼동 제거 목적의 유지보수다.

