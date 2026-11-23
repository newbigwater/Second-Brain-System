---
type: Manual
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 01__Doc
  - 02__Manual
  - 04__Agent
Version: v1.0
Status: Active
References:
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/04. Agent - 설계서.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/Artifact - 설계서.md
  - 00. Second-Brain-System/00.03. AI/02. 3'rd Party/agent_master_prompt_generator.py
  - 00. Second-Brain-System/00.03. AI/04. Agent/readme.md
---
---
# Agent Master Prompt Generator — 사용법

## 00. 이 문서는 무엇인가?

이 문서는 `agent_master_prompt_generator.py`를 사용해서  
`04. Agent/<Role>/99. Artifact/<Role Name>.md` (Agent별 단일 첨부용 Full 통합본)을 **자동으로 생성/갱신**하는 방법을 초보자도 따라할 수 있게 설명한다.

- **기본 동작**: `04. Agent/_MOC_.md`의 **Active Roles**를 읽어, 목록에 있는 **모든 Role**에 대해 한꺼번에 처리한다. (OS Master Prompt가 갱신된 뒤 전체 Agent 동기화에 유리하다.)
- **옵션**: `--role "01. Role Name"`을 지정하면 **해당 Role 하나만** 처리한다.

---

## 01. 언제 사용하나요?

다음 중 하나라도 해당하면 실행한다:

### 1.1 Role 규칙 수정 시
- `04. Agent/<Role>/Role Rule.md`를 수정했다
- `04. Agent/<Role>/Validation Checklist.md`를 수정했다
- `04. Agent/<Role>/Domain Knowledge.md`를 추가/수정했다

### 1.2 OS 업데이트 후
- `03. Operation System` 문서가 변경되어 OS Master Prompt가 갱신되었다
- 모든 Agent의 Master Prompt를 OS 최신 버전과 동기화해야 한다

### 1.3 새 Role 생성 후
- 새 Role을 만들고 Master Prompt를 처음 생성할 때
- `Role Rule.md` 작성 완료 후

### 1.4 검증 필요 시
- `<Role Name>.md`의 `References:` 목록과 실제 포함 원문이 일치하는지 확인하고 싶다

---

## 02. 무엇을 자동으로 해주나요?

### 2.1 자동 통합
다음 파일들을 **원문 그대로(Verbatim)** 단일 파일로 통합한다:

**필수 (항상 포함)**:
1. `03. Operation System/99. Artifact/Master Prompt.md` — OS 전체 규칙
2. `04. Agent/<Role>/Role Rule.md` — Role 핵심 규칙

**선택 (있으면 포함)**:
3. `04. Agent/<Role>/Validation Checklist.md` — Role 특화 검증
4. `04. Agent/<Role>/Domain Knowledge.md` — 도메인 지식 요약

### 2.2 자동 동기화
- `<Role Name>.md`의 frontmatter `References:`를 **실제 포함된 파일 목록으로 자동 동기화**한다
- 버전 번호 관리 (선택)
- 업데이트 날짜 기록 (선택)

### 2.3 형식 보존
각 파일을 다음 형태로 묶는다:
```
### Source: `<파일경로>`

`````text
(파일 원문 전체)
`````

**중요**:
- `<Role Name>.md`는 "수동 편집 문서"가 아니라 **생성 산출물(Artifact)** 로 다룬다
- 내용 변경은 `<Role Name>.md`를 직접 고치기보다, **원본 파일**(`Role Rule.md` 등)을 고치고 생성기를 다시 실행하는 것이 안전하다

---

## 03. 입력 (통합 대상) 범위

### 3.1 통합 순서
스크립트는 다음 순서로 파일을 통합한다:

```
1. OS Master Prompt (전체)
   ↓
2. Role Rule.md (필수)
   ↓
3. Validation Checklist.md (있으면)
   ↓
4. Domain Knowledge.md (있으면)
```

### 3.2 파일 존재 여부 확인
- **필수 파일이 없으면**: 오류 발생
  - `03. Operation System/99. Artifact/Master Prompt.md`
  - `04. Agent/<Role>/Role Rule.md`
- **선택 파일이 없으면**: 그냥 건너뛰기
  - `Validation Checklist.md`
  - `Domain Knowledge.md`

---

## 04. 출력 (생성 결과) 파일

출력 파일:
```
04. Agent/<Role>/99. Artifact/<Role Name>.md
```

**예시**:
```
04. Agent/01. Computer-Science Expert/99. Artifact/Computer-Science Expert.md
```

---

## 05. 실행 준비 (Windows / PowerShell)

### 05.01. Python 준비
- Python 3.x 설치 필요 (현재 레포는 Python 3.13에서도 동작)
- 외부 라이브러리 불필요 (Python 표준 라이브러리만 사용)

### 05.02. (권장) 콘솔 UTF-8 설정
파일명에 Emoji/한글이 포함되면 콘솔 출력이 깨질 수 있다. 아래를 먼저 실행하면 안정적이다.

```powershell
chcp 65001
powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
```

### 05.03. 작업 디렉토리 확인
명령은 `00. Second-Brain-System/00.03. AI/` 폴더 (= AI 루트)에서 실행한다고 가정한다.

```powershell
# 현재 위치 확인
pwd

# AI 루트로 이동 (필요 시)
cd "d:\03. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
```

### 05.04. 역할 목록 (기본: MOC / 옵션: 개별)

- **기본 (옵션 없음)**: `04. Agent/_MOC_.md`의 **### Active Roles** 섹션에서 Role 폴더 목록을 읽어 **모든 Role**을 대상으로 한다. MOC에 있지만 디스크에 없는 폴더는 건너뛴다.
- **개별만 처리**: `--role "01. Computer-Science Expert"` 처럼 `--role`을 지정하면 **그 Role 하나만** 처리한다.

---

## 06. 사용법 (명령어)

### 06.01. 변경 필요 여부만 확인 (체크)

**기본 (MOC 기준 전체 Role)**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --check
```

**개별 Role만**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --check
```

```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "02. LinguaBridge" --check
```

```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "03. English Learning Helper" --check
```

**결과 (콘솔 출력)**:
- **OK**: 해당 `<Role Name>.md`가 생성 결과와 동일 (업데이트 불필요). MOC 전체 시에는 Role별로 한 줄씩 출력 후 마지막에 "All N roles are up to date." 또는 "Next: run with ..." 안내.
- **DIFF**: 생성 결과와 다름 (업데이트 필요)

**예시 (MOC 전체 --check)**:
```text
OK: ...\01. Computer-Science Expert\99. Artifact\Computer-Science Expert.md (role: 01. Computer-Science Expert)
DIFF: ...\02. LinguaBridge\99. Artifact\LinguaBridge.md (role: 02. LinguaBridge)
...
Next: run with `--diff` to view changes or `--write` to update all.
```

**예시 (개별 --check)**:
```text
OK: D:\...\04. Agent\01. Computer-Science Expert\99. Artifact\Computer-Science Expert.md (role: 01. Computer-Science Expert)
```

```text
DIFF: D:\...\04. Agent\01. Computer-Science Expert\99. Artifact\Computer-Science Expert.md (role: 01. Computer-Science Expert)
Next: run with `--diff` to view changes or `--write` to update the file.
```

**Exit Code**:
- `0` (OK): 변경 없음
- `1` (DIFF): 변경 있음

#### PowerShell에서 exit code 확인 (선택)
```powershell
$LASTEXITCODE
```

#### CMD에서 exit code 확인 (선택)
```bat
echo %ERRORLEVEL%
```

---

### 06.02. 무엇이 달라지는지 diff 보기

**MOC 전체** (차이가 있는 Role마다 diff 출력):
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --check --diff
```

**개별 Role만**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --check --diff
```

**결과**:
- 기존 파일 vs 생성 결과의 **unified diff** 출력
- 변경된 줄 번호와 내용 표시

**주의**:
- diff 출력이 한글/이모지 때문에 깨지면 `--check`만 사용하고 `git diff`로 확인

---

### 06.03. 실제로 파일 갱신 (덮어쓰기)

**MOC 전체** (차이가 있는 Role만 덮어쓰기):
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --write
```

**개별 Role만**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --write
```

```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "02. LinguaBridge" --write
```

```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "03. English Learning Helper" --write
```

**결과**:
```text
Written: D:\...\04. Agent\01. Computer-Science Expert\99. Artifact\Computer-Science Expert.md
```

**권장 사항**:
- 덮어쓰기 전: `git status` / `git diff`로 변경사항 확인 또는 커밋으로 스냅샷 남기기
- 덮어쓰기 후: `git diff`로 결과 확인

---

### 06.04. (선택) 버전 자동 증가 / 업데이트 날짜 기록

**명령어**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --write --bump-version --stamp-updated
```

**옵션 설명**:
- `--bump-version`: `Version: vX.Y` 형태면 `vX.(Y+1)`로 증가
  - 예: `v1.0` → `v1.1`
- `--stamp-updated`: frontmatter에 `updated date: YYYY-MM-DD` 추가/갱신

**사용 시기**:
- Role Rule을 수정한 경우
- 중요한 업데이트를 기록하고 싶을 때

---

### 06.05. (고급) 다른 위치에서 실행할 때

기본값은 "이 스크립트의 상위 폴더"를 AI 루트로 사용한다.  
다른 위치에서 실행하면 `--ai-root`로 명시한다.

**명령어**:
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --ai-root "D:/03. Areas/Second-Brain-Area/00. Second-Brain-System/00.03. AI" \
  --role "01. Computer-Science Expert" \
  --write
```

---

## 07. 추천 작업 흐름 (안전 루틴)

### 07.01. Role Rule 수정 후 워크플로우

**Step 1**: Role Rule 수정
```powershell
# 파일 편집
code "04. Agent/01. Computer-Science Expert/Role Rule.md"
```

**Step 2**: 변경 확인
```powershell
git status
git diff
```

**Step 3**: (선택) 현재 상태 커밋
```powershell
git add "04. Agent/01. Computer-Science Expert/Role Rule.md"
git commit -m "feat(agent): Update CS Expert comparison rules"
```

**Step 4**: Master Prompt 재생성 필요 여부 확인
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --check
```

**Step 5**: Diff 확인 (필요 시)
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --check --diff
```

**Step 6**: Master Prompt 재생성
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --write --bump-version --stamp-updated
```

**Step 7**: 검증
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --check
# Exit code 0 확인 ✅
```

**Step 8**: Applied.md 업데이트 (선택)
```powershell
code "04. Agent/01. Computer-Science Expert/99. Artifact/Applied.md"
# 변경 이력 기록
```

**Step 9**: 변경사항 커밋
```powershell
git add "04. Agent/01. Computer-Science Expert/99. Artifact"
git commit -m "chore(agent): Regenerate CS Expert Master Prompt v1.1"
git tag "agent-cs-expert-v1.1.0"
```

---

### 07.02. OS 업데이트 후 전체 동기화

**배경**: OS Master Prompt가 갱신되면 모든 Agent의 Master Prompt도 재생성해야 한다.

**Step 1**: OS 업데이트 감지
```powershell
git diff --name-only | Select-String "03. Operation System"
```

**Step 2**: OS Master Prompt 재생성
```powershell
python "02. 3'rd Party/os_master_prompt_generator.py" --write --bump-version
```

**Step 3**: 모든 Agent Master Prompt 재생성
```powershell
# Computer-Science Expert
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --write --bump-version --stamp-updated

# 추가 Role이 있으면 반복
# python "02. 3'rd Party/agent_master_prompt_generator.py" \
#   --role "02. Another Role" \
#   --write --bump-version --stamp-updated
```

**Step 4**: 전체 검증
```powershell
# 각 Role별로 확인
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "01. Computer-Science Expert" \
  --check
# Exit code 0 확인
```

**Step 5**: 커밋
```powershell
git add "03. Operation System/99. Artifact" "04. Agent/*/99. Artifact"
git commit -m "chore: Sync all Agents with OS v1.2"
```

---

### 07.03. 새 Role 생성 후 워크플로우

**Step 1**: Role 폴더 및 기본 파일 생성
```powershell
mkdir "04. Agent/02. New Role"
mkdir "04. Agent/02. New Role/99. Artifact"

# 템플릿 복사
Copy-Item "04. Agent/00. Template/Role Rule Template.md" \
  "04. Agent/02. New Role/Role Rule.md"

# 또는 Persona 템플릿
Copy-Item "04. Agent/00. Template/Persona Template.md" \
  "04. Agent/02. New Role/Role Rule.md"
```

**Step 2**: Role Rule 작성
```powershell
code "04. Agent/02. New Role/Role Rule.md"
# OS 상속 선언, Extension Points, DoD 작성
```

**Step 3**: Validation Checklist 작성 (선택)
```powershell
code "04. Agent/02. New Role/Validation Checklist.md"
```

**Step 4**: Master Prompt 최초 생성
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "02. New Role" \
  --write
```

**Step 5**: 검증
```powershell
python "02. 3'rd Party/agent_master_prompt_generator.py" \
  --role "02. New Role" \
  --check
# Exit code 0 확인
```

**Step 6**: _MOC_.md 업데이트
```powershell
code "04. Agent/_MOC_.md"
# Active Roles에 "02. New Role" 추가
```

**Step 7**: 커밋
```powershell
git add "04. Agent/02. New Role" "04. Agent/_MOC_.md"
git commit -m "feat(agent): Add New Role v1.0"
git tag "agent-new-role-v1.0.0"
```

---

## 08. 자주 겪는 문제 (트러블슈팅)

### 08.01. "ERROR: Role path does not exist" / "ERROR: MOC not found" 오류

**Role path (--role 사용 시)**:
- `--role`에 지정한 폴더가 존재하지 않음

**해결**:
```powershell
# 폴더 존재 확인
Test-Path "04. Agent/01. Computer-Science Expert"

# Role 이름 확인 (정확한 폴더명 사용)
ls "04. Agent"
```

**MOC (--role 없이 실행 시)**:
- `04. Agent/_MOC_.md`가 없거나, **### Active Roles**에 항목이 없음  
→ `_MOC_.md`를 만들거나 `update_agent_moc.py --write`로 Active Roles를 갱신한 뒤 다시 실행한다.

**주의**:
- Role 이름은 **폴더명과 정확히 일치**해야 함
- 예: `"01. Computer-Science Expert"` (번호 + 공백 + 이름)

---

### 08.02. diff 출력이 깨지거나 오류가 난다

**원인**:
- Windows 콘솔 인코딩 문제 (한글/이모지 파일명)

**해결**:
```powershell
# UTF-8 설정 (05.02 참조)
chcp 65001
```

**대안**:
- `--diff` 없이 `--check`만 사용
- `git diff`로 변경 확인

---

### 08.03. diff가 너무 크다 (수천 줄)

**원인**:
- OS Master Prompt가 업데이트됨 (~1770줄)
- Role Rule이 대폭 수정됨
- 이전에 수동 편집했거나 통합 순서가 바뀜

**확인**:
```powershell
# OS Master Prompt 최신 여부 확인
python "02. 3'rd Party/os_master_prompt_generator.py" --check
```

**해결**:
- 정상적인 경우가 많음 (OS 통합이 대부분)
- `--write`로 갱신 후 `git diff`로 실제 변경 확인

**원칙**:
- Master Prompt는 생성 산출물로 두고, 변경은 원본 소스에서

---

### 08.04. 실행했는데 원하는 파일이 포함되지 않는다

**원인**:
- 파일 이름이 정확하지 않음
- 파일이 다른 위치에 있음

**확인**:
```powershell
# Role 폴더 구조 확인
ls "04. Agent/01. Computer-Science Expert" -Recurse
```

**포함 대상 (파일명 정확)**:
- ✅ `Role Rule.md` (필수)
- ✅ `Validation Checklist.md` (선택)
- ✅ `Domain Knowledge.md` (선택)

**제외 대상**:
- ❌ `Persona Profile.md` (사람용, 통합 안 함)
- ❌ `99. Artifact/` 폴더 내 파일
- ❌ `_MOC_.md`

---

### 08.05. "Role Rule.md가 없습니다" 오류

**원인**:
- Role 폴더에 `Role Rule.md` 파일이 없음 (필수 파일)

**해결**:
```powershell
# 파일 존재 확인
Test-Path "04. Agent/01. Computer-Science Expert/Role Rule.md"

# 템플릿에서 복사
Copy-Item "04. Agent/00. Template/Role Rule Template.md" \
  "04. Agent/01. Computer-Science Expert/Role Rule.md"

# 내용 작성
code "04. Agent/01. Computer-Science Expert/Role Rule.md"
```

---

### 08.06. 여러 Role을 한 번에 재생성하고 싶어요

**기본**: `--role` 없이 실행하면 `04. Agent/_MOC_.md`의 **Active Roles**에 있는 모든 Role을 한 번에 처리한다.

```powershell
# MOC 기준 전체 check
python "02. 3'rd Party/agent_master_prompt_generator.py" --check

# MOC 기준 전체 갱신
python "02. 3'rd Party/agent_master_prompt_generator.py" --write
```

**특정 Role 목록만 반복하고 싶을 때** (선택): PowerShell 반복문 예시

```powershell
# Role 목록 정의
$roles = @(
    "01. Computer-Science Expert",
    "02. Another Role",
    "03. Yet Another Role"
)

# 각 Role에 대해 실행
foreach ($role in $roles) {
    Write-Host "Processing: $role"
    python "02. 3'rd Party/agent_master_prompt_generator.py" `
        --role $role `
        --write --bump-version --stamp-updated
    
    # 검증
    python "02. 3'rd Party/agent_master_prompt_generator.py" `
        --role $role `
        --check
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ $role - OK" -ForegroundColor Green
    } else {
        Write-Host "❌ $role - FAILED" -ForegroundColor Red
    }
}
```

---

## 09. 고급 사용법

### 09.01. CI/CD 통합 (GitHub Actions)

**예시**: `.github/workflows/update-agents.yml`

```yaml
name: Update Agent Master Prompts

on:
  push:
    paths:
      - '00. Second-Brain-System/00.03. AI/03. Operation System/**'
      - '00. Second-Brain-System/00.03. AI/04. Agent/**/Role Rule.md'

jobs:
  update-prompts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.13'
      
      - name: Check OS Master Prompt
        working-directory: '00. Second-Brain-System/00.03. AI'
        run: |
          python "02. 3'rd Party/os_master_prompt_generator.py" --check
      
      - name: Update All Agents
        working-directory: '00. Second-Brain-System/00.03. AI'
        run: |
          python "02. 3'rd Party/agent_master_prompt_generator.py" \
            --role "01. Computer-Science Expert" \
            --write --bump-version
          
          # 추가 Role들...
      
      - name: Commit changes
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add "00. Second-Brain-System/00.03. AI/04. Agent/*/99. Artifact"
          git commit -m "chore: Auto-update Agent Master Prompts" || true
          git push
```

---

### 09.02. 배치 스크립트 작성

**파일**: `update_all_agents.ps1`

```powershell
# Agent Master Prompt 일괄 업데이트 스크립트
param(
    [switch]$Check,
    [switch]$Write
)

$aiRoot = "d:\03. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
Set-Location $aiRoot

$roles = @(
    "01. Computer-Science Expert"
    # 추가 Role들...
)

foreach ($role in $roles) {
    Write-Host "`n=== Processing: $role ===" -ForegroundColor Cyan
    
    if ($Check) {
        python "02. 3'rd Party/agent_master_prompt_generator.py" `
            --role $role --check
    }
    
    if ($Write) {
        python "02. 3'rd Party/agent_master_prompt_generator.py" `
            --role $role --write --bump-version --stamp-updated
    }
}

Write-Host "`n=== Complete ===" -ForegroundColor Green
```

**사용**:
```powershell
# 체크만
.\update_all_agents.ps1 -Check

# 갱신
.\update_all_agents.ps1 -Write

# 둘 다
.\update_all_agents.ps1 -Check -Write
```

---

## 10. 관련 도구

### 10.1 OS Master Prompt Generator

OS Master Prompt 생성은 별도 스크립트를 사용한다:
- **매뉴얼**: `01. Doc/02. Manual/OS Master Prompt Generator - 사용법.md`
- **스크립트**: `02. 3'rd Party/os_master_prompt_generator.py`

OS가 업데이트되면 OS Master Prompt를 먼저 재생성하고, 그 다음 Agent Master Prompt를 재생성한다.

### 10.2 validate_agent_structure.py

Agent 폴더 구조·OS 준수 검증 도구.  
- **전용 설명서**: `01. Doc/02. Manual/validate_agent_structure - 사용법.md`  
- **스크립트**: `02. 3'rd Party/validate_agent_structure.py`

**검증 항목**:
- 필수 파일 존재: 각 Role에 `Role Rule.md`, `99. Artifact/<RoleName>.md`
- OS 상속 선언: Role Rule.md 내 "OS 상속", "Layer 0~4", "약화/무력화" 금지 문구
- Artifact References: 첫 frontmatter의 References에 OS Master Prompt 및 본 Role Rule.md 포함

**실행**:
```powershell
cd "d:\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/validate_agent_structure.py"
```
Exit 0: 전부 통과. Exit 1: 일부 실패(출력 메시지 참고).

### 10.3 update_agent_moc.py

`04. Agent/_MOC_.md`의 **Active Roles** 섹션을 디스크 구조에 맞춰 자동 갱신한다.
- **매뉴얼**: `01. Doc/02. Manual/update_agent_moc - 사용법.md`
- **스크립트**: `02. 3'rd Party/update_agent_moc.py`

---

## 11. 참고 자료

### 11.1 설계 문서·목차
- **Doc 목차**: `01. Doc/00. Index.md` (설계·매뉴얼 전체 목록)
- **Agent 설계**: `01. Doc/01. Design/04. Agent - 설계서.md`
- **Artifact 설계**: `01. Doc/01. Design/Artifact - 설계서.md`
### 11.2 사용 가이드
- **Agent 사용법**: `04. Agent/readme.md`
- **Persona Prompt 생성**: `01. Doc/02. Manual/Persona Prompt 생성 - 사용법.md`
- **Template**: `04. Agent/00. Template/`

### 11.3 예시
- **CS Expert**: `04. Agent/01. Computer-Science Expert/`

---

## 12. 버전 이력

- **v1.2** (2026-02-21): 기본 동작을 _MOC_.md 기반(전체 Role)으로 변경, --role을 옵션(개별 Role)으로 문서화. §05.04, §06.01~06.03, §08.06 보강.
- **v1.1** (2026-02-21): Doc 목차(00. Index.md) 참조 추가, §10.3 update_agent_moc 추가, §11.1 설계·목차 정리
- **v1.0** (2026-02-18): 최초 작성
  - 기본 사용법
  - 워크플로우 3종 (Role 수정, OS 동기화, 새 Role)
  - 트러블슈팅 6종
  - 고급 사용법 (CI/CD, 배치 스크립트)
