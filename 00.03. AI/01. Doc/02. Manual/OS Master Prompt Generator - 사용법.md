---
type: Manual
creation date: 2026-02-12
tags:
  - 00__System
  - 00_03__AI
  - 01__Doc
  - 02__Manual
Version: v1.1
Status: Active
Updated: 2026-02-18
References:
  - 00. Second-Brain-System/00.03. AI/01. Doc/00. Index.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/Artifact - 설계서.md
  - 00. Second-Brain-System/00.03. AI/02. 3'rd Party/os_master_prompt_generator.py
---
---
## 00. 이 문서는 무엇인가?

이 문서는 `os_master_prompt_generator.py`를 사용해서  
`03. Operation System/99. Artifact/Master Prompt.md`(OS 단일 첨부용 Full 통합본)을 **자동으로 생성/갱신**하는 방법을 초보자도 따라할 수 있게 설명한다.

## 01. 언제 사용하나요?

다음 중 하나라도 해당하면 실행한다.

- `03. Operation System`의 규칙/체크리스트/부록/템플릿을 수정했다
- `Master Prompt.md`를 “첨부 1개”로 최신 상태로 만들고 싶다
- `Master Prompt.md`의 `References:` 목록과 실제 포함 원문이 어긋난 것 같다

## 02. 무엇을 자동으로 해주나요?

- OS 원문 파일들을 스캔해 **원문 그대로(Verbatim)** 통합한다.
- `Master Prompt.md`의 frontmatter `References:`를 **실제 포함된 파일 목록으로 자동 동기화**한다.
- 각 파일을 다음 형태로 묶는다.
  - `### Source: <파일경로>`
  - (코드블록) 해당 파일 원문 전체

중요:

- `Master Prompt.md`는 “수동 편집 문서”가 아니라 **생성 산출물(Artifact)** 로 다룬다.
- 내용 변경은 `Master Prompt.md`를 직접 고치기보다, **원본 OS 문서**를 고치고 생성기를 다시 실행하는 것이 안전하다.

## 03. 입력(통합 대상) 범위

생성기는 `03. Operation System` 아래의 다음 영역을 통합 대상으로 삼는다.

- `00. Governance Kernel/`
- `01. Cognitive Engine/`
- `02. Validation Engine/`
- `02. Validation Engine/Checklists/`
- `03. Self-Reflection Loop/`
- `04. Artifact Engine/`
- `90. Annex (Operational Standards)/`
- `90. Annex (Operational Standards)/00. Templates/`

기본 제외:

- `99. Artifact/` (출력/산출물 폴더)
- `_MOC_.md` (인덱스)

## 04. 출력(생성 결과) 파일

- 출력 파일(고정): `03. Operation System/99. Artifact/Master Prompt.md`

## 05. 실행 준비(Windows / PowerShell)

### 05.01. Python 준비

- Python 3.x 설치 필요(현재 레포는 Python 3.13에서도 동작)

### 05.02. (권장) 콘솔 UTF-8 설정

파일명에 Emoji/한글이 포함되면 콘솔 출력이 깨질 수 있다. 아래를 먼저 실행하면 안정적이다.

```powershell
chcp 65001
powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
```

## 06. 사용법(명령어)

아래 명령은 `00. Second-Brain-System/00.03. AI/` 폴더(= AI 루트)에서 실행한다고 가정한다.

### 06.01. 변경 필요 여부만 확인(체크)

```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --check
```

- 결과(콘솔 출력):
  - **OK**: `Master Prompt.md`가 생성 결과와 동일(업데이트 불필요)
  - **DIFF**: 생성 결과와 다름(업데이트 필요)

예시:

```text
OK: .../03. Operation System/99. Artifact/Master Prompt.md is up to date.
```

```text
DIFF: .../03. Operation System/99. Artifact/Master Prompt.md differs from generated output.
Next: run with `--diff` to view changes or `--write` to update the file.
```

추가 확인(선택):

- `--check`는 exit code도 유지한다.
  - **exit code 0**: OK
  - **exit code 1**: DIFF

#### PowerShell에서 exit code 확인(선택)

```powershell
$LASTEXITCODE
```

#### CMD에서 exit code 확인(선택)

```bat
echo %ERRORLEVEL%
```

### 06.02. 무엇이 달라지는지 diff 보기

```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --check --diff
```

### 06.03. 실제로 파일 갱신(덮어쓰기)

```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --write
```

권장:

- 덮어쓰기 전에는 `git status`/`git diff`로 변경사항을 확인하거나 커밋으로 스냅샷을 남긴다.
- 덮어쓰기 후 결과 확인은 `git diff`로 한다.

### 06.04. (선택) 버전 자동 증가 / 업데이트 날짜 기록

```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --write --bump-version --stamp-updated
```

- `--bump-version`: `Version: vX.Y` 형태면 `vX.(Y+1)`로 증가
- `--stamp-updated`: frontmatter에 `updated date:`를 추가/갱신

### 06.05. (고급) 다른 위치에서 실행할 때

기본값은 “이 스크립트의 상위 폴더”를 AI 루트로 사용한다.  
다른 위치에서 실행하면 `--ai-root`로 명시한다.

```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --ai-root "D:/03. Areas/Second-Brain-Area/00. Second-Brain-System/00.03. AI" --write
```

## 07. 추천 작업 흐름(안전 루틴)

1. OS 문서 수정
2. `git status`로 변경 확인
3. (선택) 현재 상태 커밋
4. `--check`로 업데이트 필요 여부 확인
5. `--check --diff`로 변화 확인
6. `--write`로 갱신
7. 다시 `--check` 실행해서 0인지 확인
8. 변경사항 커밋

## 08. 자주 겪는 문제(트러블슈팅)

### 08.01. diff 출력이 깨지거나 오류가 난다

- 위의 “콘솔 UTF-8 설정”을 먼저 실행한다.
- 그래도 깨지면 `--diff` 없이 `--check`만 쓰고, 변경은 `git diff`로 확인한다.

### 08.02. diff가 너무 크다(수천 줄)

- 정상일 수 있다.
  - 이전에 `Master Prompt.md`를 수동 편집했거나,
  - 통합 순서/공백/펜스 처리 규칙이 바뀐 경우 diff가 크게 나온다.
- 원칙: `Master Prompt.md`는 생성 산출물로 두고, 변경은 원문 소스에서 한다.

### 08.03. 실행했는데 원하는 파일이 포함되지 않는다

- 해당 파일이 통합 대상 디렉토리(03번) 안에 있는지 확인한다.
- 파일이 `_MOC_.md`이거나 `99. Artifact/` 아래면 기본적으로 제외된다.

---

## 09. 관련 도구

### Agent Master Prompt Generator

Agent별 Master Prompt 생성은 별도 스크립트를 사용한다:
- **매뉴얼**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`
- **스크립트**: `02. 3'rd Party/agent_master_prompt_generator.py`

Agent Master Prompt는 OS Master Prompt + Role Rule을 통합한다.

---

## 10. 버전 이력

- **v1.1** (2026-02-18): 관련 도구 섹션 추가, References 업데이트
- **v1.0** (2026-02-12): 최초 작성
