---
type: Guide
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - CS__Expert
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

`99. Artifact`는 Computer-Science Expert Persona를 **AI 플랫폼에 등록하기 위한 통합 파일**을 보관한다.

---

## 01. 파일 구성

### `Computer-Science Expert.md` (권장)
- **목적**: OS + CS Expert Role 전체 통합본
- **방법**: 파일 첨부
- **환경**: ChatGPT, Gemini, Claude (파일 첨부 가능한 모든 환경)
- **크기**: 제한 없음 (Full 버전)

### `Computer-Science Expert (Compact).md` (대안)
- **목적**: 길이 제한 대응 요약본
- **방법**: 복사 & 붙여넣기
- **환경**: 텍스트 입력란만 가능한 경우
- **크기**: ~1000~1500 토큰 목표

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

**Step 2**: CS Expert Role 첨부
```
파일: 04. Agent/01. Computer-Science Expert/99. Artifact/Computer-Science Expert.md
위치: Custom Instructions 파일 첨부 (추가)
```

**Step 3**: 프로젝트 지침 입력 (필수 권장)

아래 문단을 **Custom Instructions / 프로젝트 지침**란에 그대로 붙여 넣는다. 채팅창이 아니라 **지침 설정 화면**에 넣어야 한다.

```
위 두 첨부 파일(Master Prompt, Computer-Science Expert)의 모든 규칙을 최상위 지침으로 적용하라. 우선순위는 OS Layer 0 → L1 → L2 → L3 → L4 → CS Expert 확장 규칙이다.

학습 내용 정리·내용 정리·정리 요청이 들어오면 반드시 첨부된 지침을 참고한 뒤 작업한다. 출력 시 다음을 준수한다: (1) 정리 산출물은 반드시 단일 fenced code block(마크다운 또는 text)으로 감싼다. (2) 핵심 용어·약어는 Markdown 풋노트로 정의한다(OS-ART-015 To-Be·Obsidian 호환). 본문에는 [^1], [^2] 참조를 두고, 문서 하단 풋노트는 `[^n]: **용어(English)**` 한 줄 → 탭 들여쓰기 정의 문단 → `- **Scope**:` 불릿(필수 권장) 형식으로 쓴다. 위첨자 숫자(¹²³)나 "1. 2. 3." 번호 목록만으로 대체하지 않는다. (3) 풋노트에 등록된 용어는 문서 최상단에 #Tag로 띄어쓰기 한 줄로만 나열한다. 개행하지 않는다. (4) 내용 정리 산출물에는 YAML frontmatter(--- 블록)를 사용하지 않는다. 문서는 #Tag 한 줄 → 빈 줄 → 본문 첫 헤더 순으로 시작한다. (5) 문서 제목이 'NN. 제목' 형식으로 주어진 경우 헤더 계층 구조를 준수한다. H1(#)은 상위 토픽(이미지 또는 제목에서 자동 유도), H2(##)는 'NN. 제목'(사용자 제공 값 그대로, 변경 금지), H3(###)은 'NN.MM. 소절'(두 자리 번호)로 표기한다. '## 1.' 또는 '### 3.1' 등 임의 번호 체계로 바꾸지 않는다.
```

---

### 방법 2: Gemini GEM

**Step 1**: 새 GEM 생성

**Step 2**: Knowledge 등록
- OS Master Prompt 업로드
- CS Expert Master Prompt 업로드

**Step 3**: Instructions 입력
```
본 Knowledge의 모든 문서는 전체 지침으로 적용한다.
우선순위: OS Layer 0 > L1 > L2 > L3 > L4 > CS Expert 확장 규칙
```

---

### 방법 3: Cursor AI

**Step 1**: `.cursor/rules/` 폴더 생성

**Step 2**: `computer-science-expert.mdrule` 파일 생성

**Step 3**: 내용 작성
- OS 핵심 규칙 (Layer 0~4 요약)
- CS Expert Role Rule 전체
- ~2000줄 목표

---

### 방법 4: 텍스트만 가능 (길이 제한)

**Step 1**: `Computer-Science Expert (Compact).md` 열기

**Step 2**: 코드 블록 전체 복사

**Step 3**: Custom Instructions 입력란에 붙여넣기

---

## 03. Master Prompt 생성 방법

### 자동 생성 (권장)

```powershell
cd "d:\20. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --write
```

- 전체 Agent 일괄 재생성: `--role` 없이 `--write` 실행. 매뉴얼: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`

### 수동 생성 (임시)

**Step 1**: OS Master Prompt 복사
```powershell
Copy-Item "03. Operation System/99. Artifact/Master Prompt.md" `
  "04. Agent/01. Computer-Science Expert/99. Artifact/Computer-Science Expert.md"
```

**Step 2**: Role Rule 추가
- `Role Rule.md` 내용을 Computer-Science Expert.md 하단에 추가

**Step 3**: frontmatter References 업데이트
- References에 포함된 모든 파일 나열

---

## 04. 업데이트 주기

### OS 업데이트 시
- `02. 3'rd Party/os_master_prompt_generator.py --write` → `agent_master_prompt_generator.py --write`(전체 Role). 상세: `04. Agent/readme.md` §05-A.

### Role Rule 수정 시
- `agent_master_prompt_generator.py --role "01. Computer-Science Expert" --write`

---

## 05. 버전 관리

### 버전 번호 체계
```
vMAJOR.MINOR.PATCH

MAJOR: OS 호환성 깨지는 변경
MINOR: Role 기능 추가
PATCH: 버그 수정, 문서 개선
```

### 현재 버전
- **CS Expert Artifact**: v1.1
- **OS Master Prompt**: `03. Operation System/99. Artifact/` 참고

---

## 06. 문제 해결

### Q1: Master Prompt가 너무 커요
**A**: 
- ChatGPT/Gemini: 파일 첨부 제한 없음 (Full 사용)
- 텍스트만: Compact 버전 사용

### Q2: 적용이 안 되는 것 같아요
**A**:
1. 세션 초기화 (새 대화 시작)
2. 명시적 적용 요청: "Computer-Science Expert Persona를 적용해주세요"
3. OS 규칙 우선 확인: "OS Layer 0 Kernel 규칙을 절대 위반하지 마세요"

### Q3: Role Rule을 수정했는데 반영이 안 돼요
**A**:
1. Master Prompt 재생성 확인
2. 파일 재첨부 (캐시 문제)
3. 버전 확인

---

## 07. 참고 자료

- **Agent 사용 가이드**: `04. Agent/readme.md`
- **Role Rule**: `../Role Rule.md`
- **Persona Profile**: `../Persona Profile.md`
- **Validation Checklist**: `../Validation Checklist.md`
- **OS Master Prompt**: `03. Operation System/99. Artifact/Master Prompt.md`
- **Master Prompt 생성 매뉴얼**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`
