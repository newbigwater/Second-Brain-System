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
  - 00. Second-Brain-System/00.03. AI/02. 3'rd Party/update_agent_moc.py
  - 00. Second-Brain-System/00.03. AI/04. Agent/_MOC_.md
  - 00. Second-Brain-System/00.03. AI/04. Agent/readme.md
---
---
## 00. 이 문서는 무엇인가?

이 문서는 `update_agent_moc.py`를 사용해서  
`04. Agent/_MOC_.md`의 **Active Roles** 섹션을 **실제 폴더 구조에 맞춰 자동으로 갱신**하는 방법을 설명한다.

- **대상**: `04. Agent/_MOC_.md` (Map of Contents)
- **목적**: MOC를 “목차/인덱스만 담는 문서”로 유지하고, Role 추가·삭제·설명 변경 시 **Active Roles**만 스크립트로 동기화

차후 이 스크립트·파일을 기준으로 “지침 업데이트 체크”, “변경 사항 보기”, “변경 사항 업데이트” 기능을 확장할 수 있도록 설계되어 있다.

## 01. 언제 사용하나요?

다음 중 하나라도 해당하면 실행한다.

- `04. Agent` 아래에 **새 Role 폴더**를 추가했을 때 (`0X. <Role Name>/`)
- Role 폴더를 **삭제**했을 때 (MOC에서도 제거하고 싶을 때)
- **Role Rule.md**의 Domain / Role Name을 수정했을 때 (MOC 한 줄 설명 반영)
- Role 폴더 내 **Role Rule, Persona Profile, Validation Checklist, Domain Knowledge, 99. Artifact** 등 구조가 바뀌었을 때
- MOC와 디스크가 **일치하는지 점검**만 하고 싶을 때 (`--check`)

## 02. 무엇을 자동으로 해주나요?

- **`### Active Roles` 섹션만** 디스크 기준으로 다시 만든다.
- 각 Role의 **한 줄 설명**은 해당 Role의 `Role Rule.md`에서 **Domain** 또는 **Role Name** 항목을 읽어 쓴다.
- 각 Role 아래 **하위 항목**은 실제로 존재하는 파일/폴더만 나열한다.
  - Role Rule, Persona Profile, Validation Checklist, Domain Knowledge, 99. Artifact/ (및 메인 Artifact 파일명)
- **Core**, **Shared Resources**, **Quick Navigation**, **Design Principles**, **Version History** 등 **다른 섹션은 건드리지 않는다.**

즉, `_MOC_.md`는 “Map of Contents” 역할만 하도록 유지하고, **Active Roles**만 자동 갱신된다.

## 03. 갱신 대상(Role 폴더 범위)

- **포함**: `04. Agent` 아래 이름이 `숫자. `로 시작하는 폴더 (`01. ...`, `02. ...`, …)
- **제외**: `00. Template`, `90. Shared Resources`

스크립트는 위 조건에 맞는 폴더만 스캔해 Active Roles 목록을 만든다.  
MOC에만 있고 디스크에 없는 Role(예: 삭제한 폴더)은 `--write` 시 목록에서 빠진다.

## 04. 한 줄 설명·하위 항목 출처

| 항목 | 출처 |
|------|------|
| 한 줄 설명 | `Role Rule.md`의 `- **Domain**:` 또는 `- **Role Name**:` (먼저 찾은 것 사용) |
| 없을 때 | `(설명 없음)` |
| 하위 항목 | 디스크에 존재하는 것만: Role Rule.md, Persona Profile.md, Validation Checklist.md, Domain Knowledge(.md 또는 폴더), 99. Artifact/ 및 `99. Artifact/<RoleName>.md` |

## 05. 실행 준비(Windows / PowerShell)

### 05.01. Python

- Python 3.x 필요(스크립트는 표준 라이브러리만 사용)

### 05.02. (권장) 콘솔 UTF-8 설정

경로·설명에 한글이 있으면 콘솔 출력이 깨질 수 있다. 실행 전에 아래를 실행하면 안정적이다.

```powershell
chcp 65001
powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
```

## 06. 사용법(명령어)

아래는 작업 디렉터리를 **`00.03. AI` 루트**로 두고 실행한다고 가정한다.

### 06.01. MOC와 디스크 일치 여부만 확인(체크, 기본 동작)

```powershell
python "02. 3'rd Party/update_agent_moc.py" --check
```

- **결과**:
  - **OK**: MOC에 적힌 Role 폴더 목록과 디스크의 Role 폴더 목록이 같음 → exit code 0
  - **불일치**: MOC에만 있거나 디스크에만 있는 Role이 있음 → exit code 1, 메시지로 어떤 폴더가 다른지 출력

예시(일치):

```text
OK: _MOC_.md is in sync with 04. Agent folder structure.
```

예시(불일치):

```text
MOC missing role folders (on disk): 04. New Role
Run with --write to update _MOC_.md.
```

```text
MOC lists role folders not on disk: 04. Deleted Role
Run with --write to update _MOC_.md.
```

- 옵션을 주지 않으면 **`--check`**가 기본이다.

### 06.02. 갱신될 Active Roles 내용만 보기(diff, 파일 수정 없음)

```powershell
python "02. 3'rd Party/update_agent_moc.py" --diff
```

- **결과**: 현재 디스크 기준으로 만들어진 **`### Active Roles`** 블록 전체를 콘솔에 출력한다.  
  파일은 수정하지 않는다.

### 06.03. 실제로 _MOC_.md 갱신(쓰기)

```powershell
python "02. 3'rd Party/update_agent_moc.py" --write
```

- **결과**: `04. Agent/_MOC_.md`를 열어 **`### Active Roles`** 섹션만 새 내용으로 교체하고 저장한다.  
  나머지 섹션(Core, Shared Resources, Quick Navigation 등)은 그대로 둔다.

권장:

- 갱신 전 `git status` / `git diff`로 변경 예정 범위를 확인하거나, 커밋으로 스냅샷을 남긴다.
- 갱신 후 `git diff 04. Agent/_MOC_.md`로 결과를 확인한다.

### 06.04. (고급) 다른 위치에서 실행할 때

기본값은 “스크립트 파일의 상위 폴더”를 AI 루트(`00.03. AI`)로 사용한다.  
다른 경로를 쓰려면 `--ai-root`를 지정한다.

```powershell
python "02. 3'rd Party/update_agent_moc.py" --ai-root "D:/Second-Brain-Area/00. Second-Brain-System/00.03. AI" --write
```

## 07. 추천 작업 흐름

1. Role 폴더 추가/삭제 또는 Role Rule 등 수정
2. `git status`로 변경 확인 (선택: 커밋)
3. `--check`로 MOC와 디스크 일치 여부 확인
4. 필요 시 `--diff`로 갱신될 Active Roles 내용 확인
5. `--write`로 `_MOC_.md` 갱신
6. `--check` 다시 실행해 exit code 0인지 확인
7. `git diff 04. Agent/_MOC_.md`로 diff 확인 후 커밋

## 08. 자주 겪는 문제(트러블슈팅)

### 08.01. --diff 출력이 깨진다

- “05.02. 콘솔 UTF-8 설정”을 먼저 실행한다.
- 그래도 깨지면 `--diff` 없이 `--check`만 쓰고, 실제 변경은 `--write` 후 `git diff`로 확인한다.

### 08.02. MOC에만 있는 Role이 사라졌다

- `--write`는 **디스크에 있는 Role 폴더만** Active Roles에 넣는다.  
  디스크에 없는 Role(예: 아직 만들지 않은 “04. 인플루언서랩”)은 MOC에서 제거된다.  
  해당 Role을 다시 쓰려면 폴더를 만든 뒤 다시 `--write`를 실행하면 된다.

### 08.03. 한 줄 설명이 "(설명 없음)"으로 나온다

- 해당 Role 폴더에 `Role Rule.md`가 있는지 확인한다.
- `Role Rule.md` 본문에 `- **Domain**:` 또는 `- **Role Name**:` 항목이 있는지 확인한다.  
  스크립트는 이 두 항목 중 먼저 찾은 것을 한 줄 설명으로 쓴다.

### 08.04. _MOC_.md가 없다고 나온다

- `04. Agent/_MOC_.md` 파일이 실제로 있는지 확인한다.
- `--ai-root`를 쓴다면, 지정한 경로 아래에 `04. Agent/_MOC_.md`가 있어야 한다.

## 09. 관련 도구

| 도구 | 용도 | 매뉴얼 / 스크립트 |
|------|------|-------------------|
| validate_agent_structure | Role 폴더 구조·OS 준수 검증 | `validate_agent_structure - 사용법.md`, `validate_agent_structure.py` |
| Agent Master Prompt Generator | Role별 Master Prompt 생성 | `Agent Master Prompt Generator - 사용법.md`, `agent_master_prompt_generator.py` |
| create_persona | Persona 스캐폴드 생성 | `Persona Prompt 생성 - 사용법.md`, `create_persona.py` |

- **update_agent_moc**: MOC의 **목차(Active Roles)** 만 디스크와 동기화한다.  
- **validate_agent_structure**: 각 Role의 필수 파일·OS 상속·Artifact References를 검증한다.  
- **Agent Master Prompt Generator**: OS + Role Rule을 합친 Master Prompt 파일을 생성한다.

## 10. 버전 이력

- **v1.0** (2026-02-21): 최초 작성
