---
type: Guide
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
Version: v1.0
Status: Active
References:
  - 03. Operation System/_MOC_.md
---
---
## 00. What is this?

`03. Operation System`은 AI 응답/산출물 생성의 **정본(SSOT)** 이다.  
모든 Role/Stage/Project는 본 OS를 상속하며, OS를 약화/무력화할 수 없다.

## 01. Quick Start (읽는 순서)

1. Layer 0 (불변): `00. Governance Kernel/Kernel.md`
2. Layer 1 (절차): `01. Cognitive Engine/Cognitive Engine.md`
3. Layer 2 (검증): `02. Validation Engine/Validation Engine.md`
4. Layer 3 (Reflection): `03. Self-Reflection Loop/Reflection Loop.md`
5. Layer 4 (산출): `04. Artifact Engine/Artifact Engine.md` + `04. Artifact Engine/Output Modes.md`

## 02. Operational Flow (강제)

사용자 입력
→ RA
→ Manager
→ Worker
→ Evaluator
→ Validation Engine
→ Self-Reflection Loop
→ Artifact Engine
→ 최종 출력

## 03. Modes

- Normal Mode: Reflection 1회
- Critical Mode: Reflection 최대 2회
- Fast Mode: Reflection 생략

## 04. Core Contracts (항상 지켜야 하는 것)

- **Kernel 위반 금지**: 위반 시 `INVALID RESPONSE`
- **Input Coverage Declaration**: 입력 기반 작업 출력에 “입력 반영 현황” 포함
- **Output Mode 준수**: 설명/산출물/파일 생성 모드 혼합 금지(기본)

## 05. Registration Pack (세션 시작 시 최소 세트)

- `90. Annex (Operational Standards)/📎 Custom Instructions Registration Pack Standard.md` 참고

## 05-A. Mode Selection (키워드 기반)

- “생성”, “파일 생성”, “실제 파일로” → File Generation Mode
- “출력”, “문서로 출력”, “md로 내보내” → Artifact Output Mode
- “내용 정리”, “용어 정리”, “상세 정리” → Organizer Mode
- “설명”, “해설”, “분석” → Explanation Mode

## 05-B. Session Start Flow (운영)

- OS 적용(필수) → Stage/Project Root Rule 적용 → Contract 적용 → Role 확장 규칙 적용
- 산출물 생성 전: Output Mode 판별 및 적용 규칙 세트(Manager) 확정

## 06. Where do Role rules live?

- Role 확장 규칙은 `04. Agent/`에 위치한다.
- 템플릿: `04. Agent/00. Template/Role Rule Template.md`

## 07. Single Registration (단일 등록) — Copy & Paste 가이드

### 07.01. OS만 등록(권장: 첨부 파일 1개)

- **첨부용 통합본(권장)**: `99. Artifact/Master Prompt.md`
  - `00. Governance Kernel` ~ `90. Annex (Operational Standards)`까지의 **원문 지침을 단일 파일로 통합**한 파일이다.
  - ChatGPT 맞춤지침 / Gemini GEM 등에 **파일 1개만 첨부**하는 목적에 맞춘다.

방법(첨부 기반):

1. `99. Artifact/Master Prompt.md`를 **첨부 파일로 등록**한다.
2. (텍스트 입력이 필요하면) “이 첨부 파일의 모든 규칙을 최상위로 적용하라”는 문장을 함께 제공한다.

### 07.02. OS만 등록(대안: 텍스트 입력만 가능한 경우)

- **붙여넣기용 요약본(길이 제한 대응)**: `99. Artifact/Master Prompt (Compact).md`

방법(붙여넣기 기반):

1. `Master Prompt (Compact).md`를 열고, 안내된 **단일 코드 블록 전체**를 복사한다.
2. Custom Instructions(또는 동등한 “전역 지침” 입력란)에 그대로 붙여넣는다.

### 07.03. OS + Role 동시 등록(개인 프로젝트 등)

권장 순서(상속/적용 순서):

1. **OS**를 먼저 등록한다.
2. 그 다음 **Role**을 등록한다.

Role Rule 위치(예):

- `04. Agent/<Role Name>/Role Rule.md`

주의:

- Role은 OS를 **약화/무력화/재정의**할 수 없다(확장만 가능).
- Role Rule을 붙여넣을 때도, “외부 파일을 참조해야만 동작하는 지침” 형태로 작성하지 않는다(단일 등록 목적 위반).

### 07.04. 언제 Compact를 쓰나?

- Custom Instructions 길이 제한이 있거나, 여러 Role을 함께 넣어야 해서 공간이 부족할 때만 `Master Prompt (Compact).md`를 사용한다.
- 제한이 없다면 항상 `Master Prompt.md`(표준)를 우선 사용한다.

## 08. 단순 학습·내용 정리 시 사용 방법 (OS만)

Role 없이 **학습 정리·내용 정리·정리 요청**만 사용할 때의 최소 등록 방법이다.

### Step 1: OS 첨부

```
파일: 99. Artifact/Master Prompt.md
위치: Custom Instructions 파일 첨부
```

### Step 2: 프로젝트 지침 입력 (권장)

아래 문단을 **Custom Instructions / 프로젝트 지침**란에 그대로 붙여 넣는다. 채팅창이 아니라 **지침 설정 화면**에 넣어야 한다.

```
첨부된 Master Prompt의 모든 규칙을 최상위 지침으로 적용하라. 우선순위는 OS Layer 0 → L1 → L2 → L3 → L4이다.

학습 내용 정리·내용 정리·정리 요청이 들어오면 반드시 첨부된 지침을 참고한 뒤 작업한다. 출력 시 다음을 준수한다: (1) 정리 산출물은 반드시 단일 fenced code block(마크다운 또는 text)으로 감싼다. (2) 핵심 용어·약어는 Markdown 풋노트 형식으로 정의한다(OS-ART-015 To-Be·Obsidian 호환). 본문에는 [^1], [^2]처럼 참조를 두고, 문서 하단 풋노트는 `[^n]: **용어(English)**` 한 줄 → 탭 들여쓰기 정의 문단 → `- **Scope**:` 불릿(필수 권장) 형식으로 쓴다. 위첨자 숫자(¹²³)나 "1. 2. 3." 번호 목록만으로 대체하지 않는다. (3) 풋노트에 등록된 용어는 문서 최상단에 #Tag로 띄어쓰기 한 줄로만 나열한다. 개행하지 않는다. (4) 내용 정리 산출물에는 YAML frontmatter(--- 블록)를 사용하지 않는다. 문서는 #Tag 한 줄 → 빈 줄 → 본문 첫 헤더 순으로 시작한다. (5) 문서 제목이 'NN. 제목' 형식으로 주어진 경우 헤더 계층 구조를 준수한다. H1(#)은 상위 토픽(이미지 또는 제목에서 자동 유도), H2(##)는 'NN. 제목'(사용자 제공 값 그대로, 변경 금지), H3(###)은 'NN.MM. 소절'(두 자리 번호)로 표기한다. '## 1.' 또는 '### 3.1' 등 임의 번호 체계로 바꾸지 않는다.
```

