---
type: Guide
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - LinguaBridge
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

`99. Artifact`는 **LinguaBridge Persona**를 AI 플랫폼에 등록하기 위한 통합 파일을 보관한다.

---

## 01. 파일 구성

### `LinguaBridge.md` (권장)
- **목적**: OS + LinguaBridge Role 전체 통합본
- **방법**: 파일 첨부
- **환경**: ChatGPT, Gemini, Claude (파일 첨부 가능한 모든 환경)
- **크기**: 제한 없음 (Full 버전)

### `LinguaBridge (Compact).md` (대안)
- **목적**: 길이 제한 대응 요약본
- **방법**: 복사 & 붙여넣기
- **환경**: 텍스트 입력란만 가능한 경우

### `Applied.md`
- **목적**: 실제 적용 이력 기록
- **내용**: 적용 환경, 버전, 날짜, 변경 사항

---

## 02. 사용 방법

### 방법 1: ChatGPT Custom Instructions (권장)

**Step 1**: OS 먼저 첨부
```
파일: 03. Operation System/99. Artifact/Master Prompt.md
위치: Custom Instructions 파일 첨부
```

**Step 2**: LinguaBridge Role 첨부
```
파일: 04. Agent/02. LinguaBridge/99. Artifact/LinguaBridge.md
위치: Custom Instructions 파일 첨부 (추가)
```

**Step 3**: 프로젝트 지침 입력 (필수 권장)

아래 문단을 **Custom Instructions / 프로젝트 지침**란에 그대로 붙여 넣는다. **지침 설정 화면**에 넣어야 한다.

```
위 두 첨부 파일(Master Prompt, LinguaBridge)의 모든 규칙을 최상위 지침으로 적용하라. 우선순위는 OS Layer 0 → L1 → L2 → L3 → L4 → LinguaBridge 확장 규칙이다.

사용자 선택에 의한 모드 선택을 적용한다. 통역이 필요하면 "Mode 1" 또는 "통역 모드", "통역해 줘" 등으로 요청하면 통역만 출력한다(대답하지 않음). 메일이 필요하면 **"메일"**, "Mode 2", "메일 모드", "메일 번역/작성" 등으로 요청하면 해당 언어쌍으로 메일 본문만 출력한다. **"메일"만 적어도 Mode 2가 동작한다.** 모드가 불명확하면 한 번만 재질문한다.

내용 정리·용어 정리·정리 요청이 들어오면 OS StudyNote 규칙을 준수한다. 정리 산출물은 단일 코드 블록(마크다운 또는 text)으로 감싸고, 블록 내부에서 #Tag 한 줄·YAML 금지·풋노트(OS-ART-015 To-Be·Obsidian 호환 형식)를 적용한다.
```

---

### 방법 2: Gemini GEM

**Step 1**: 새 GEM 생성  
**Step 2**: Knowledge에 OS Master Prompt + LinguaBridge.md 업로드  
**Step 3**: Instructions에 "본 Knowledge의 모든 문서는 전체 지침으로 적용. 우선순위: OS > LinguaBridge. 모드 선택: Mode 1 통역만 / Mode 2 메일."

---

### 방법 3: Cursor AI

- `.cursor/rules/` 에 rule 파일 생성
- OS 핵심 규칙 + LinguaBridge Role Rule 요약
- 모드 선택 규칙(Mode 1 통역만, Mode 2 메일) 포함

---

### 방법 4: 텍스트만 가능 (길이 제한)

- `LinguaBridge (Compact).md` 내용을 복사하여 Custom Instructions 입력란에 붙여넣기. 제한이 없으면 방법 1(파일 첨부) 권장.

---

## 03. 모드 선택 안내

| 모드 | 요청 예시 | 동작 |
|------|-----------|------|
| **Mode 1 (통역)** | "통역 모드", "Mode 1", "통역해 줘" | 한국인↔외국인 대화 통역. 대상어: EN, RU, JP, ZH. **통역만** 출력, 대답 금지. |
| **Mode 2 (메일)** | **"메일"**, "메일 모드", "Mode 2", "메일 번역/작성" | **한국어** → 비즈니스 해석·재작성 → EN, RU / **영어** → KO, RU(재작성 없음) / **러시아어** → KO, EN(재작성 없음). 본문은 **코드 블록**으로 출력(Outlook 붙여넣기용). **"메일"만 적어도 Mode 2.** |

---

## 04. Master Prompt 생성 방법

### 자동 생성 (권장)

```powershell
cd "d:\20. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "02. LinguaBridge" --write
```

- 전체 Agent 일괄 재생성: `--role` 없이 `--write`. 매뉴얼: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`

### 수동 생성 (임시)

1. OS Master Prompt 복사 → `LinguaBridge.md`로 저장  
2. Role Rule.md 내용을 하단에 추가  
3. frontmatter References 업데이트  

---

## 05. 업데이트 주기

- **OS 업데이트 시**: `04. Agent/readme.md` §05-A에 따라 OS Master Prompt 재생성 후 `agent_master_prompt_generator.py --write`
- **Role Rule 수정 시**: `--role "02. LinguaBridge" --write`로 해당 Artifact만 재생성

---

## 06. 참고 자료

- **Agent 사용 가이드**: `04. Agent/readme.md`
- **Role Rule**: `../Role Rule.md`
- **Persona Profile**: `../Persona Profile.md`
- **Validation Checklist**: `../Validation Checklist.md`
- **Domain Knowledge**: `../Domain Knowledge.md`
- **OS Master Prompt**: `03. Operation System/99. Artifact/Master Prompt.md`
- **Master Prompt 생성 매뉴얼**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`
