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
  - "[[🏷️ Tag & Metadata Governance|🏷️ Tag & Metadata Governance]]"
Version: v1.1
References:
level: 0.01
---
---

## Purpose

- 본 문서는 Obsidian wikilink의 표시명(예: `⟦path|display⟧`)을 **일관된 규칙**으로 고정한다.
- 목표:
  - 폴더 이동/리네이밍 이후에도 문서 네비게이션이 **혼동 없이 유지**
  - “구 트리 표기(legacy display name)”가 새 레이어 구조를 오염시키는 문제 방지

---

## Core Rules (강제)

### 1) Stage/Layer 표시명은 “현 구조”를 기준으로 한다

- `10.01.01 SRS`, `10.01.02 SDS`, `10.01.03 SCS`, `10.02.01 PM`, `10.02.02 Translation`, `20. Personal` 같은 **현 레이어 표기**를 사용한다.
- 금지(예): `|01. SRS`, `|04. PM`, `|05. Translation`, `|07. Application`

### 2) `_MOC_` 링크는 “폴더 진입” 표시명으로 통일한다

- 권장:
  - `\[\[10. Business/10.01 Architect/10.01.01 SRS/_MOC_|10.01.01 SRS\]\]`
  - `\[\[10. Business/10.02 Project/_MOC_|10.02 Project\]\]`

### 3) 문서 링크는 “문서 제목 그대로”를 표시명으로 사용한다

- 예:
  - `[[.../📘 Integrated Prompt Template Set|📘 Integrated Prompt Template Set]]`
  - `[[.../📎 Custom Instructions Registration Pack Standard|📎 Registration Pack Standard]]`

---

## Migration/Repair Rule (운영)

- 기존 문서에서 legacy 표시명이 발견되면:
  - **경로(path)는 그대로 유지**
  - **표시명(display)만 현 구조 기준으로 교체**
- 이 작업은 링크 무결성에 영향을 주지 않으며, “혼동 제거” 목적의 유지보수다.

