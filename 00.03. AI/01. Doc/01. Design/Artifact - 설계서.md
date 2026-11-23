---
type: Design
creation date: 2026-02-11
tags:
  - 00_03__AI
  - 00__System
  - 03__OperationSystem
Version: v1.1
Status: Active
Updated: 2026-02-21
References:
  - 00. Second-Brain-System/00.03. AI/01. Doc/00. Index.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/03. Operation System - 설계서.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/04. Agent - 설계서.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/02. Manual/OS Master Prompt Generator - 사용법.md
---
---
## 00. 목적

본 문서는 `03. Operation System/99. Artifact`를 “설계 레벨”에서 정의한다.  
또한 본 문서 자체를 **첨부 파일로 제공**했을 때, 모델이 **“이 파일을 지침으로 삼아 처리”** 할 수 있도록 운영 문구/규칙을 포함한다.

## 00-A. 첨부 기반 적용 방식(이 문서를 ‘지침’으로 쓰는 법)

### 00-A-01. 사용자(사람)가 모델에게 제공하는 1줄 지시문(권장)

아래 문장을 “시스템/맞춤지침/추가 지침” 입력란에 함께 제공한다.

```text
첨부된 "Artifact - 설계서.md"의 내용을 최상위 지침으로 적용하고, 그 규칙에 따라 작업을 진행하라.
```

### 00-A-02. Plain 환경(레포 경로 접근 불가)에서의 필수 동작

- 이 문서에 등장하는 레포 경로는 “설계상의 위치”이며, Plain 환경에서는 **경로를 따라가서 파일을 열 수 없다고 가정**한다.
- 따라서 **필요한 원문 규칙이 첨부되지 않았다면**:
  - 임의 추정으로 진행하지 말고,
  - 필요한 파일의 “추가 첨부”를 요청한다.

예:

- OS 전체 적용이 필요하면: “OS Master Prompt (Full, Attachment)” **첨부 1개**를 요청
- 텍스트-only 환경이면: “OS Master Prompt (Compact, Paste-only)” **코드블록 붙여넣기**를 요청

## 01. 배경(왜 99. Artifact가 필요한가)

LLM 환경은 크게 2가지로 나뉜다.

- **A) Repo-Access 환경**: Cursor 같은 도구에서 레포 파일을 직접 읽을 수 있다.
- **B) Plain 환경**: ChatGPT/Gemini처럼 “레포 경로를 따라가서 파일을 열어볼 수 없는” 환경이 많다.

Plain 환경에서는 `03. Operation System`이 여러 파일로 나뉘어 있으면, “지침을 적용하려면 파일을 여러 개 첨부해야 하는 문제”가 발생한다.  
`99. Artifact`는 이 문제를 해결하기 위해 **등록/첨부/복붙을 위한 패키지(Artifact)** 를 제공한다.

## 02. 설계 원칙(Design Principles)

### 02.01. 단일 첨부(1-file attachment) 우선

- 가능하면 **`Master Prompt.md` 1개 파일만 첨부**해도 OS가 적용되도록 한다.

### 02.02. 원문 통합(Verbatim) + 명시적 References

- 첨부용 통합본은 “요약본”이 아니라 **원문 지침을 그대로 포함**한다.
- 어떤 파일이 통합에 포함되었는지 frontmatter `References:`에 **정확히 나열**한다.

### 02.03. 대안 경로 제공(붙여넣기-only)

- 어떤 플랫폼은 파일 첨부가 불가능하거나, 맞춤지침 입력란이 짧을 수 있다.
- 이 경우를 위해 **Compact(요약/부트스트랩)** 를 제공한다.

## 03. 표준 구조(안)

```text
03. Operation System/
  99. Artifact/
    readme.md                         # 사용 가이드
    Master Prompt.md                  # Full, Attachment (원문 통합)
    Master Prompt (Compact).md        # Paste-only (요약/부트스트랩)
```

## 04. 파일 역할 정의

### 04.01. `readme.md` (가이드)

- `99. Artifact`의 목적/사용 방법을 요약한다.
- “첨부 1개(권장)” vs “텍스트 붙여넣기(대안)”를 구분한다.
- OS + Role 등록 순서를 안내한다.

### 04.02. `Master Prompt.md` (Full, Attachment)

- **단일 첨부용 통합본**이다.
- `03. Operation System/00. Governance Kernel` ~ `90. Annex (Operational Standards)`의 지침을 **원문 그대로 포함**한다.
- frontmatter `References:`는 “통합에 실제로 포함된 파일 목록”이다.

### 04.03. `Master Prompt (Compact).md` (Paste-only)

- **텍스트만 붙여넣기 가능한 환경**을 위한 요약/부트스트랩이다.
- Full 원문 통합을 대체하지 않는다.
- 목적은 “최소한의 OS 핵심 규칙/흐름을 강제”하여 드리프트를 줄이는 것이다.

## 05. 운영 적용 시나리오(초급자용)

### 05.01. ChatGPT / Gemini에 “첨부 파일 1개”로 등록(권장)

- 첨부 파일: “OS Master Prompt (Full, Attachment)”
- 텍스트 입력이 필요한 경우(선택):
  - “첨부 파일의 모든 규칙을 최상위로 적용하라” 같은 한 줄을 함께 제공한다.

### 05.02. 텍스트만 붙여넣기 가능한 경우(대안)

- 붙여넣기: “OS Master Prompt (Compact, Paste-only)”의 코드 블록 전체

## 06. OS + Role(Agent) 결합 원칙(요약)

- Role은 OS를 **약화/무력화/재정의**할 수 없다(확장만 가능).
- OS를 먼저 적용하고, 그 다음 Role을 적용한다.
- Role도 Plain 환경에서 단일 등록이 필요하면, **각 Role 폴더의 `99. Artifact/`** 에 “Role Prompt”를 제공한다.

## 07. 유지보수(운영) 규칙

### 07.01. 변경 발생 지점

OS 문서가 변경되면 `Master Prompt.md`는 다음 조건을 만족하도록 갱신되어야 한다.

- 통합본이 최신 원문을 포함한다.
- `References:`가 최신 포함 목록과 일치한다.

### 07.02. 운영 도구(자동화)

- 운영 표준(Annex)에 “자동 점검/생성/검증” 도구가 정의되어 있다면, 해당 표준을 우선 적용한다.

## 08. 완료 조건(DoD)

- `Master Prompt.md` 단일 첨부로 OS 적용이 가능하다.
- `Master Prompt.md` frontmatter `References:`가 “실제 포함 원문 파일”과 1:1로 일치한다.
- `readme.md`가 “첨부(권장) / 붙여넣기(대안)”를 초급자도 따라할 수 있게 설명한다.

