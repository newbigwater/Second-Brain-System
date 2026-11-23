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
# 📘 Operational Rules (OS 정본)

> 본 문서는 `03. Operation System`의 실무 운영 규칙(How-to)을 제공한다.  
> 본 문서는 Governance Kernel(Layer 0) 및 OS Layer 1~4를 수정/약화하지 않는다.

## 00. Governance Index (운영 허브)

- Tag/메타데이터 운영 표준: `90. Annex (Operational Standards)/🏷️ Tag & Metadata Governance.md`
- Custom Instructions 등록/첨부 최소 세트(Registration Pack): `90. Annex (Operational Standards)/📎 Custom Instructions Registration Pack Standard.md`
- Obsidian wikilink 표시명(display) 스타일: `90. Annex (Operational Standards)/🧷 Link Display Name Style Guide.md`
- Stage 폴더 스켈레톤 표준: `90. Annex (Operational Standards)/🧱 Stage Folder Skeleton Standard.md`
- Organizer Contract 표준: `90. Annex (Operational Standards)/🧾 Organizer Contract Standard.md`

## 01. 자동 점검(스크립트)

**현행 스크립트** (`02. 3'rd Party/`):
- OS Master Prompt 생성: `02. 3'rd Party/os_master_prompt_generator.py`
- Agent Master Prompt 생성: `02. 3'rd Party/agent_master_prompt_generator.py`
- Agent 구조·OS 준수 검증: `02. 3'rd Party/validate_agent_structure.py`
- Persona 스캐폴드 생성: `02. 3'rd Party/create_persona.py`

**과거 스크립트(참조 전용)**: 링크 무결성, Master Prompt 검증, MOC 품질, 태그 정규화 등은 참조 전용 영역에 있으며, 필요 시 동일 기능을 `02. 3'rd Party/`로 이전할 수 있다.

## 02. Windows/PowerShell UTF-8 출력 표준(모지바케 방지)

Unicode 경로(한글/Emoji)에서 `git diff`/스크립트 출력이 깨지면 아래를 먼저 실행한다.

```text
chcp 65001
powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
```

## 03. Input Handling Rules (Layer 1로 승격됨)

- 입력 분해/혼합 입력 차단 규칙은 OS Layer 1 `Cognitive Engine.md`에 정본으로 존재한다.
  - Input Segmentation Rule
  - Mixed Input Detection Rule

## 04. StudyNote Operational Rules (조건부 적용)

> 정리/EDU 성격 출력물에서만 적용한다.

- Practice 영역은 입력 단어를 100% 포함해야 한다(해당 템플릿/계약 존재 시).
- 약어·전문용어·교육 개념은 Footnote로 정의한다.
  - Footnote는 OS-ART-015 To-Be(Obsidian 호환) 형식(정의 문단 + Scope 필수 권장).
- 검증은 OS Layer 2 체크리스트(`Footnote Auto Checklist`)로 수행한다.

## 05. SRS / SDS / SCS Operational Rules (Stage 규칙 우선)

- 본 규칙은 Business Stage의 Root Rule/Contract가 우선이며, 충돌 시 Stage 규칙을 따른다.
- 단, “재해석 금지/신규 판단 금지”는 OS Kernel/Engine의 불변 조건과 정렬되어야 한다.

## 06. Output Validation Rules (Layer 2로 승격됨)

- Output Validation은 OS Layer 2 `Validation Engine` 및 `Output Validation Checklist`로 수행한다.
- NG/Fail 판정은 OS Layer 2 `NG-Fail Policy.md` 및 Layer 0 `Violation Policy.md`를 따른다.

