---
type: MOC
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
level: 0
Version: v2.0
Status: Active
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/_MOC_.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/04. Agent - 설계서.md
---
---
## 00. What is this?

`04. Agent`는 **OS 기반 Role/Persona 확장 시스템**이다.  
모든 Role은 `03. Operation System`을 상속하며, OS를 약화/무력화할 수 없다.

## 01. Index

### Core
- `readme.md` — Agent 시스템 사용 가이드
- `00. Template/` — Role 생성 템플릿
  - `Role Rule Template.md` — 표준 Role 템플릿
  - `Persona Template.md` — Persona 특화 템플릿

### Active Roles

- `01. Computer-Science Expert/` - Computer Science Theory, Algorithms, Systems, Software Engineering
  - Role Rule
  - Persona Profile
  - Validation Checklist
  - 99. Artifact/ - Computer-Science Expert.md

- `02. LinguaBridge/` - 비즈니스 통역, 비즈니스 메일 번역·작성
  - Role Rule
  - Persona Profile
  - Validation Checklist
  - Domain Knowledge
  - 99. Artifact/ - LinguaBridge.md

- `03. English Learning Helper/` - 비기너 영어 주간 학습 정리(Podo), 책 기반 문법 학습 정리(Grammar)
  - Role Rule
  - Persona Profile
  - Domain Knowledge
  - 99. Artifact/ - English Learning Helper.md

### Shared Resources
- `90. Shared Resources/` — 공유 리소스
  - `readme.md` — 목적·사용 원칙·권장 하위 구조

## 02. Quick Navigation

### 새 Role 생성하기
1. `00. Template/Role Rule Template.md` 또는 `Persona Template.md` 복사
2. 새 폴더 생성: `0X. <Role Name>/`
3. `Role Rule.md` 작성 (OS 상속 선언 필수)
4. `99. Artifact/` 폴더 및 Master Prompt 생성
5. 본 `_MOC_.md`에 링크 추가

### Role 적용하기
1. OS 먼저 적용: `03. Operation System/99. Artifact/Master Prompt.md`
2. Role 적용: `04. Agent/<Role>/99. Artifact/<Role Name>.md`
3. ChatGPT/Gemini: 파일 첨부 (권장)
4. Cursor: `.cursor/rules/` 에 rule 파일 생성

## 03. Design Principles

- **OS 상속 강제**: 모든 Role은 Layer 0~4 상속
- **확장만 허용**: 추가 제약/검증/템플릿만 가능, 약화 금지
- **검증 가능성**: 모든 규칙은 검증 가능해야 함
- **단일 첨부 지원**: Master Prompt로 Plain 환경 지원

## 04. Version History

- v2.0 (2026-02-18): Computer-Science Expert 추가, 전체 구조 재설계
- v1.0 (2026-02-11): 초기 템플릿 구조 생성