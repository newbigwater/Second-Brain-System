---
type: Guide
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - EnglishLearning
  - Artifact
Version: v1.1
Status: Active
References:
  - 04. Agent/readme.md
  - 01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md
---
---
# 99. Artifact — 사용 가이드

## 00. 이 폴더는 무엇인가?

`99. Artifact`는 **English Learning Helper Persona**를 AI 플랫폼에 등록하기 위한 통합 파일을 보관한다.

---

## 01. 파일 구성

### `English Learning Helper.md` (권장)
- **목적**: OS + English Learning Helper Role 전체 통합본 (Podo/Grammar 모드, 출력 형식 포함)
- **방법**: 파일 첨부
- **환경**: ChatGPT, Gemini, Claude (파일 첨부 가능한 모든 환경)
- **출력**: 학습 정리 노트는 **항상 단일 코드 블록**으로 출력
- **출력 형식 정의**: 섹션·테이블 구조는 `../00. Template/Persona Output Template.md`에 정의되어 있으며, Podo 모드는 해당 템플릿의 구조를 따른다.

---

## 02. 사용 방법

### 방법 1: ChatGPT Custom Instructions (권장)

**Step 1**: OS 먼저 첨부
```
파일: 03. Operation System/99. Artifact/Master Prompt.md
위치: Custom Instructions 파일 첨부
```

**Step 2**: English Learning Helper 첨부
```
파일: 04. Agent/03. English Learning Helper/99. Artifact/English Learning Helper.md
위치: Custom Instructions 파일 첨부 (추가)
```

**Step 3**: 프로젝트 지침 입력 (권장)

```
위 첨부 파일(OS Master Prompt, English Learning Helper)의 모든 규칙을 최상위 지침으로 적용하라. 우선순위는 OS Layer 0 → L1 → L2 → L3 → L4 → English Learning Helper 확장 규칙이다.

학습 정리 노트(Podo·Grammar)는 반드시 단일 코드 블록(```markdown ... ```)으로만 출력한다. 코드 블록 밖에 설명·메타 문장을 두지 않는다.

모드: Podo(주간 학습 정리) 또는 Grammar(문법 정리). "Podo", "금주 학습 완료, 내용 정리 요청" 등 → Podo. "Grammar", "문법 정리" 등 → Grammar. 모호하면 한 번만 "Podo 모드와 Grammar 모드 중 어떤 것을 원하시나요?"로 재질문한다.
```

---

### 방법 2: Gemini GEM

**Step 1**: 새 GEM 생성  
**Step 2**: Knowledge에 OS Master Prompt + English Learning Helper.md 업로드  
**Step 3**: Instructions에 "본 Knowledge 전체 지침 적용. 우선순위 OS > English Learning Helper. 학습 정리 노트는 단일 코드 블록만. 모드: Podo 또는 Grammar, 불명확 시 한 번만 재질문."

---

## 03. ChatGPT 사용 시 모드별 참고 문서 (필수)

각 모드 사용 시 아래 문서를 **첨부·참고**하여 작성한다.

### Grammar Mode
- 사용자 첨부 문법 교재/PDF
→ [Concept], [Why], [Form], [Examples] 등 작성 시 참고. 예문은 교재/사용자 입력만.

### Podo Mode
- 사용자 첨부 어원/구동사 학습 자료 — **[Etymology] 작성 시 필수 참고**
→ Podo 출력 시 참고. **Etymology**는 4컷 영단어 PDF를 반드시 참고.

### Podo 출력 형식 (필수)
- **형식 정의(레포 내)**: `../00. Template/Persona Output Template.md` — Podo/Grammar 출력 구조·테이블 형식 정본.
- **Podo 구조·예시**: 사용자 첨부 Podo 템플릿/출력 예시 문서 — Podo 모드 출력 시 동일한 섹션 순서·테이블 헤더를 유지.
- **입력 예시**: 사용자 첨부 학습지 원문 유형 문서 참고.
- (레포 외) `language/Podo/01.Standard/Start2/04. 조동사를 활용한 정보 요청 표현.md`와 동일한 구조로 작성하는 것도 가능.

### Podo 규칙 정본 (필수)
- Podo 상세 규칙 문서를 사용자가 **별도 첨부**하여 **필수** 준수.

---

## 04. 출력 형식 (강제)

- **Podo / Grammar 모두**: 최종 학습 정리 노트는 **단일** ` ```markdown ` 또는 ` ```text ` 코드 블록으로 감싼다.
- **풋노트(정리 시)**: OS 정리 요청 시 풋노트가 필요하면 OS-ART-015 **To-Be(Obsidian 호환)** 형식(`[^n]: **용어(English)**` → 탭 들여쓰기 정의 문단 → `- **Scope**:` 불릿)을 따른다.
- 코드 블록 **밖**에 설명·요약·메타 문장을 출력하지 않는다. (Obsidian에 바로 붙여넣기 가능.)
- 코드 블록 **내부** 본문에는 닫는 백틱(```) 한 줄을 넣지 않는다. 넣으면 마크다운이 그 위치에서 블록을 종료해 그 뒤 내용이 블록 밖으로 빠진다(블록 조기 종료).
- **내부 구조**(섹션·테이블)는 `../00. Template/Persona Output Template.md` 기준.
- 수정 요청 시 부분 수정 없이 **전체 문서 재출력**만 수행한다.

### Podo 출력 검증(체크)

Podo 출력 후 아래를 확인한다.

1. **[Conversation]** — 제공된 학습 대화가 **원문 그대로**인가? (오타·문법 수정 금지)
2. **[Practice] User Table** — 사용자 오류 문장이 입력에 있으면 **반드시** 포함되었는가?
3. **[Practice] Word Table** — [Words] **모든 단어 × 1문장(1:1)**이 **생략 없이 전부** 출력되었는가? ("이하 동일" 등 대체 금지)
4. **단일 코드 블록** — 전체 노트가 하나의 ` ```markdown ` … ` ``` ` 로만 감싸져 있는가? 블록 **내부**에 닫는 ``` 가 없어 조기 종료가 발생하지 않았는가?

---

## 05. Master Prompt 생성 방법

### 자동 생성 (권장)

```powershell
cd "d:\20. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "03. English Learning Helper" --write
```

- 전체 Agent 일괄 재생성: `--role` 없이 `--write`. 매뉴얼: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`

### 업데이트 주기

- **OS 업데이트 시**: `04. Agent/readme.md` §05-A에 따라 OS 재생성 후 `agent_master_prompt_generator.py --write`
- **Role Rule 수정 시**: `--role "03. English Learning Helper" --write`로 해당 Artifact만 재생성

---

## 06. 참고

- **Agent 사용 가이드**: `04. Agent/readme.md`
- **Persona 프로필**: `../Persona Profile.md`
- **Role Rule**: `../Role Rule.md`
- **모드별 참고 문서**: 사용자 첨부 자료 목록 문서
- **출력 형식 템플릿**: `../00. Template/Persona Output Template.md` — Podo/Grammar 출력 구조·섹션·테이블 정의.
- **Podo 구조·예시·입력**: 사용자 첨부 Podo 템플릿/예시/입력 문서
- **OS Master Prompt**: `03. Operation System/99. Artifact/Master Prompt.md`
- **Master Prompt 생성 매뉴얼**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`
- Podo/Grammar 상세 규칙·Gate는 Role Rule 04·05절 및 필요 시 사용자가 **별도 첨부**한 문서로 준수한다.
