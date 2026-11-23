---
type: Manual
creation date: 2026-02-21
tags:
  - 00__System
  - 00_03__AI
  - 01__Doc
  - 02__Manual
Version: v1.0
Status: Active
References:
  - 00. Second-Brain-System/00.03. AI/01. Doc/00. Index.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/04. Agent - 설계서.md
  - 00. Second-Brain-System/00.03. AI/02. 3'rd Party/validate_agent_structure.py
  - 00. Second-Brain-System/00.03. AI/04. Agent/readme.md
---
---
## 00. 이 문서는 무엇인가?

이 문서는 `validate_agent_structure.py`를 사용해서  
`04. Agent` 아래 각 Role의 **폴더 구조**와 **OS 준수 여부**를 자동으로 검증하는 방법을 설명한다.

- **대상**: `01. Computer-Science Expert`, `02. LinguaBridge`, `03. English Learning Helper` 등 `04. Agent` 내 번호 붙은 Role 폴더
- **목적**: 필수 파일 존재, OS 상속 선언, Artifact References 포함 여부를 한 번에 점검

## 01. 언제 사용하나요?

다음 중 하나라도 해당하면 실행한다.

- 새 Role을 추가한 뒤 표준 구조를 지켰는지 확인하고 싶을 때
- Role Rule 또는 `99. Artifact/*.md`를 수정한 뒤 References/선언이 빠지지 않았는지 확인할 때
- CI/배치에서 Agent 구조·OS 준수 검증을 자동화할 때

## 02. 무엇을 검증하나요?

스크립트는 **각 Role 폴더마다** 아래 3가지 검사를 수행한다.

### 02.01. 필수 파일(Required files)

- `Role Rule.md` — 해당 Role 루트에 존재해야 함
- `99. Artifact/<RoleName>.md` — 폴더명에서 번호·앞 공백을 뗀 이름의 마크다운 파일  
  - 예: `01. Computer-Science Expert` → `99. Artifact/Computer-Science Expert.md`

### 02.02. OS 상속 선언(OS inheritance declaration)

- `Role Rule.md` 본문에 다음이 **둘 다** 포함되어야 함:
  - OS 상속(또는 Layer 0 / Layer 1 등)을 나타내는 문구
  - "약화" 또는 "무력화" 금지 문구

### 02.03. Artifact References

- `99. Artifact/<RoleName>.md`의 **첫 번째 YAML frontmatter**에 `References:`가 있어야 함
- `References:` 목록에 다음이 **둘 다** 포함되어야 함:
  - OS Master Prompt: `03. Operation System` 경로와 `Master Prompt.md`를 포함한 항목
  - 본 Role Rule: 해당 Role 폴더명과 `Role Rule.md`를 포함한 항목

## 03. 검증 대상(Role 폴더 범위)

- **포함**: `04. Agent` 아래 이름이 `숫자. `로 시작하는 폴더 (`01. ...`, `02. ...`, …)
- **제외**: `00. Template`, `90. Shared Resources`

Role이 하나도 없으면 "No role folders found" 메시지 후 종료 코드 0으로 종료한다.

## 04. 실행 준비(Windows / PowerShell)

### 04.01. Python

- Python 3.x 필요(스크립트는 표준 라이브러리만 사용)

### 04.02. (권장) 콘솔 UTF-8 설정

경로에 한글/Emoji가 있으면 출력이 깨질 수 있다. 실행 전에 아래를 실행하면 안정적이다.

```powershell
chcp 65001
powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
```

## 05. 사용법(명령어)

아래는 작업 디렉터리를 **`00.03. AI` 루트**로 두고 실행한다고 가정한다.

### 05.01. 기본 실행(권장)

```powershell
cd "d:\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/validate_agent_structure.py"
```

- **종료 코드 0**: 모든 Role에서 3가지 검사 통과
- **종료 코드 1**: 하나라도 실패(콘솔에 FAIL 항목 출력)

### 05.02. AI 루트를 다른 경로로 지정

`00.03. AI`가 다른 드라이브/경로에 있을 때:

```powershell
python "02. 3'rd Party/validate_agent_structure.py" --ai-root "D:/경로/00.03. AI"
```

- `--ai-root`를 주지 않으면 스크립트 파일 기준 **상위 폴더**가 AI 루트로 사용된다.

## 06. 출력 예시

### 06.01. 전부 통과

```text
--- 04. Agent/01. Computer-Science Expert ---
  OK: Required files
  OK: OS inheritance declaration
  OK: Artifact References

--- 04. Agent/02. LinguaBridge ---
  OK: Required files
  OK: OS inheritance declaration
  OK: Artifact References

--- 04. Agent/03. English Learning Helper ---
  OK: Required files
  OK: OS inheritance declaration
  OK: Artifact References

All checks passed.
```

### 06.02. 일부 실패

```text
--- 04. Agent/03. English Learning Helper ---
  OK: Required files
  OK: OS inheritance declaration
  FAIL: English Learning Helper.md: References에 OS Master Prompt 없음

Some checks failed.
```

## 07. 실패 시 조치

| FAIL 메시지 | 조치 |
|-------------|------|
| `Missing: Role Rule.md` | 해당 Role 루트에 `Role Rule.md` 생성(템플릿은 `04. Agent/00. Template/` 참고) |
| `Missing: 99. Artifact/<RoleName>.md` | `99. Artifact/` 아래에 폴더명에서 번호만 뗀 이름의 `.md` 파일 생성(또는 Agent Master Prompt Generator로 생성) |
| `OS 상속 선언(또는 Layer 0~4) 문구 없음` | `Role Rule.md`에 OS Layer 0~4 상속 문구 추가 |
| `OS 약화/무력화 금지 문구 없음` | `Role Rule.md`에 "OS를 약화/무력화할 수 없다"류 문구 추가 |
| `References에 OS Master Prompt 없음` | 해당 Role의 `99. Artifact/<RoleName>.md` frontmatter `References:`에 `03. Operation System/99. Artifact/Master Prompt.md` 경로 추가 |
| `References에 본 Role Rule.md 없음` | 동일 frontmatter `References:`에 해당 Role의 `Role Rule.md` 경로 추가(예: `04. Agent/03. English Learning Helper/Role Rule.md`) |
| `frontmatter 없음` / `frontmatter 종료 없음` | Artifact 파일 상단에 `---`로 시작·종료하는 YAML frontmatter 블록 추가 |

수정 후 스크립트를 다시 실행해 모든 항목이 OK인지 확인한다.

## 08. 참고

- **Agent 설계**: `01. Doc/01. Design/04. Agent - 설계서.md`
- **Agent 사용 가이드**: `04. Agent/readme.md`
- **Agent Master Prompt Generator 매뉴얼(§10.2)**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md` — 동일 스크립트 요약 및 실행 예시 포함
- **Agent MOC 갱신**: `01. Doc/02. Manual/update_agent_moc - 사용법.md` — `04. Agent/_MOC_.md` Active Roles 자동 갱신
