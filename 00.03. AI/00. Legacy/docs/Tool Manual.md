---
title: AI Project Suite – Tool Manual
last_updated: 2026-02-10
---
---

# 1. 개요
- **위치**: `workspace/tools/`
- **목적**: Stage 지침과 Artifact를 재생성·검증·배포하는 자동화 스크립트를 문서화한다.
- **누구를 위한 문서인가요?**  
  초급 개발자도 이 문서만 보면 “어떤 스크립트를 언제, 왜 실행해야 하는지” 이해할 수 있도록 작성했습니다.
- **운영 원칙**
  1. 모든 스크립트는 저장소 루트(`D:/…/00.03. AI`)에서 실행한다.  
     → VS Code 터미널/PowerShell에서 `cd "D:/03. Areas/Second-Brain-Area/00. Second-Brain-System/00.03. AI"` 후 명령 실행.
  2. 실행 전/후 `git status`와 `link_integrity_report.md`를 확인하여 변경 사항과 품질 리포트를 기록한다.
  3. 사용 빈도가 낮은 스크립트는 `workspace/tools/archive/`로 이동해 루트 디렉터리를 단순화했다.

# 2. 핵심 스크립트
## 2.1 산출물 & 품질 파이프라인
| 스크립트 | 입력/의존성 | 출력/효과 | 사용 시점 |
| --- | --- | --- | --- |
| `artifact_master_prompt.py` | Stage Rules/Guides/Contracts, `docs/ChatGPT Custom Instructions – AI Project Suite.md` | Stage별 `99. Artifact/`에 Master Prompt + 📌 + Applied 재생성 | Stage 지침 변경 후 |
| `master_prompt_audit.py` | Master Prompt 파일 | 단일 코드 블록/Reference 누락 여부 보고 | Master Prompt 생성 직후 |
| `version_bump_and_master_references.py` | 모든 지침 파일 | front-matter `Version` 자동 증가, Master Prompt `References` 주입 | 배포 직전 |

### 상세 설명 (Step-by-Step)
#### a. `artifact_master_prompt.py`
1. **왜 실행하나요?**  
   Stage 문서(Helios, Aegis 등)를 수정한 뒤 ChatGPT에 붙여넣을 Master Prompt/📌/Applied를 다시 만들어야 합니다.
2. **무엇을 하나요?**  
   - Core/Business/Personal Stage 경로 + 공통 디렉터리(`01. Core/00. Charter`, `10. Business/01. Rules`, `10. Business/02. Guides`)를 읽어 하나의 Master Prompt를 구성합니다.  
   - `99. Artifact/` 폴더에 Master Prompt, 📌, Applied를 덮어씁니다.  
   - `docs/ChatGPT Custom Instructions – AI Project Suite.md` 경로도 포함하여 참조 체인을 일치시킵니다.
3. **실행 예시**  
   ```
   cd "D:/03. Areas/Second-Brain-Area/00. Second-Brain-System/00.03. AI"
   python workspace/tools/artifact_master_prompt.py
   ```
4. **출력 확인**  
   - 터미널에 `Generated Master Prompts: N` 메시지 표시  
   - 각 Stage `99. Artifact/`에 Master Prompt, 📌, Applied가 갱신됩니다.

#### b. `master_prompt_audit.py`
1. **왜 실행하나요?**  
   Master Prompt 형식이 깨진 상태로 배포되지 않도록 자동 검사합니다.
2. **무엇을 하나요?**  
   - `- Source: \`...\`` 목록과 실제 파일 집합을 비교하여 누락/초과를 보고합니다.  
   - Fence 검사: 시작·끝 2개의 코드 블록 라인만 허용 (중간에 ```가 추가되면 실패).
3. **실행 예시**  
   ```
   python workspace/tools/master_prompt_audit.py
   ```
4. **결과 해석**  
   - `OK: all master prompts passed fence + completeness checks` → 정상  
   - 실패 메시지가 Stage 이름과 함께 출력되면 해당 Stage Master Prompt를 다시 생성하거나 수동 수정해야 합니다.

#### c. `version_bump_and_master_references.py`
1. **왜 실행하나요?**  
   Stage 지침을 업데이트하면 `Version` 필드를 올리고, Master Prompt front-matter에 최신 `References` 리스트를 주입해야 합니다.
2. **무엇을 하나요?**  
   - front-matter `Version` 키가 있으면 소수점 단위 +0.1로 증가(예: v1.3 → v1.4).  
   - Master Prompt에는 `References` 배열을 삽입하여 `artifact_master_prompt.py`가 수집한 파일 경로를 명시합니다.
3. **실행 예시**  
   ```
   python workspace/tools/version_bump_and_master_references.py
   ```
4. **주의**  
   `docs/ChatGPT Custom Instructions – AI Project Suite.md`도 대상에 포함되므로, 이동/삭제 여부를 미리 확인하세요.

## 2.2 메타데이터 & 구조
| 스크립트 | 기능 | 사용 예시 |
| --- | --- | --- |
| `apply_level_metadata.py` | 폴더 Prefix → `level` / `parent_level` 매핑을 front-matter에 자동 주입. Up-only 정책 근거 데이터를 유지. | Stage 리팩토링 후 `python workspace/tools/apply_level_metadata.py` |
| `replace_stage_paths.py` | Markdown 내 Stage 경로를 일괄 치환 (예: `02. Business/02.01 SRS` → `10. Business/10.01.01 SRS`). | 구조 대규모 변경 시 `python workspace/tools/replace_stage_paths.py` |

### 주의 사항 / 실수 방지 팁
- `apply_level_metadata.py`
  - `LEVEL_MAP`이 **가장 구체적인 경로 → 덜 구체적인 경로** 순서로 나열되어 있어야 합니다.  
  - 예) `20. Personal/20.01 English/01. Rules/20.01.01 Podo English` 항목이 `20. Personal/20.01 English`보다 먼저 나와야 합니다.
- `replace_stage_paths.py`
  - OrderedDict 기반이라 **긴 경로에서 짧은 경로 순**으로 선언되어 있습니다.  
  - 명령 실행 전에는 반드시 `git status`로 변경 범위를 확인하고, 필요하면 `git diff`로 결과를 검토하세요.

## 2.3 검증 유틸리티
| 스크립트 | 기능 | 비고 |
| --- | --- | --- |
| `link_check.py` | Markdown/Obsidian 링크 (WikiLink 포함) 유효성 검사. `.gitignore` + `workspace/` 제외. | 결과는 루트 `link_integrity_report.md` 에 기록 (동일 내용이 `workspace/link_integrity_report.md`로 미러링됨) |
| `check_level_links.py` | 문서 간 레벨 위반(하위가 상위 참조)을 탐지. | `_MOC_` 제외 / Stage 99 Artifact 미검사 옵션 포함 |

### 실행 팁
- `link_check.py`
  - Emoji/한글 경로도 검증하므로 PowerShell 출력이 깨질 수 있습니다.  
  - 실패 메시지가 뜨면 루트 `link_integrity_report.md`를 직접 열어 어떤 링크가 깨졌는지 확인하세요.
- `check_level_links.py`
  - CP949 인코딩 문제를 피하려면 아래처럼 환경 변수를 지정하고 실행하면 좋습니다.  
    ```
    set PYTHONIOENCODING=utf-8
    python workspace/tools/check_level_links.py
    ```
  - Git/PowerShell 출력(예: `git diff`)이 한글/Emoji에서 깨질 경우:
    - 표준 스니펫은 `01. Core/01. Operations/Operational Rules.md`의 “Windows/PowerShell UTF-8 출력 표준”을 따른다.

## 2.4 Stage 등록 (`stage_targets.json`)
- **위치**: `workspace/tools/stage_targets.json`
- **용도**: 내장 Stage 외에 *신규 Stage*를 자동화 파이프라인에 등록할 때 사용.
- **형식 (JSON 배열)**:
  ```json
  [
    {
      "title": "20.04 NewStage",
      "base_dir": "20. Personal/20.04 NewStage",
      "includes": [
        "20. Personal/20.04 NewStage/00. Index/📘 NewStage Index.md"
      ]
    }
  ]
  ```
  - `title`: Master Prompt 제목에 사용.
  - `base_dir`: Stage 루트 경로 (`.../StageName`).
  - `includes`: Stage 외부의 공통 문서를 추가로 포함하고 싶을 때만 작성. 생략하면 `base_dir` 하위의 모든 `.md`를 자동 수집합니다.
- **동작**: `artifact_master_prompt.py`, `master_prompt_audit.py`, `version_bump_and_master_references.py`가 이 파일을 읽어 새로운 Stage의 `99. Artifact/`를 생성/검증/버전 관리합니다.

> **권장 실행 순서**  
> 1) `apply_level_metadata.py` → 2) `artifact_master_prompt.py` → 3) `master_prompt_audit.py` → 4) `link_check.py` → 5) `version_bump_and_master_references.py`

# 3. 예시 워크플로 (초급 개발자용)
> 시나리오: Helios(10.01.01 SRS) Stage의 규칙 문서를 수정했고, ChatGPT에 최신 규칙을 반영해야 합니다.

1. **레벨/링크 검증**
   ```
   python workspace/tools/apply_level_metadata.py
   python workspace/tools/link_check.py
   ```
   - 실패 메시지가 나오면 해당 파일을 열어 front-matter나 링크를 수정합니다.
2. **Master Prompt 재생성 + 감사**
   ```
   python workspace/tools/artifact_master_prompt.py
   python workspace/tools/master_prompt_audit.py
   ```
   - `OK` 메시지가 뜨면 Pass, 실패 시 Stage명을 참고해 해당 Master Prompt를 다시 확인합니다.
3. **버전 및 Reference 갱신**
   ```
   python workspace/tools/version_bump_and_master_references.py
   ```
4. **커밋 전 확인**
   - `git status`로 변경 파일 확인 → `git diff`로 주요 변경 사항 검토
   - README 혹은 Docs에 반영이 필요하면 수정 후 `link_check.py`를 한 번 더 실행합니다.

# 4. 아카이브 스크립트
- **경로**: `workspace/tools/archive/`
- **포함 파일**: `fix_relative_link_depth.py`, `migrate_core_structure.py`, `migrate_top_layers.py`, `moc_audit.py`, `rebuild_references_from_links.py`, `standardize_stage_structure.py`, `tag_normalize.py`, `tmp_generate_master.py`
- **용도**: 과거 리팩토링/마이그레이션용 일회성 스크립트. 필요 시 `python workspace/tools/archive/<script>.py`로 실행 가능하나 기본 플로우에는 포함되지 않는다.

# 5. 운영 체크리스트
1. **규칙 수정 직후** → `apply_level_metadata.py` + `link_check.py`
2. **Stage 산출물 갱신** → `artifact_master_prompt.py` 실행 → `master_prompt_audit.py` 검사
3. **배포 전** → `version_bump_and_master_references.py` 로 Version/Reference 동기화
4. **품질 보고** → `link_integrity_report.md` 확인 후 README/Docs 업데이트

# 6. 트러블슈팅
- **Unicode 경로 문제**: PowerShell이 Emoji/한글 경로를 처리하지 못하면 Python `Path.replace()` 사용.
- **Workspace 제외**: `link_check.py` 는 `workspace/`를 기본 제외 → 실제 경로 반영 후 재검사.
- **Archive 복구**: 필요 시 `archive/`에서 스크립트를 루트로 복사해 사용한 뒤 다시 보관.

# 7. FAQ
- **Q. Master Prompt에 새 문서를 포함하려면?**  
  A. 해당 Stage 폴더 구조(예: `10. Business/10.01 Architect/10.01.01 SRS/01. Rules/`) 안에 문서를 추가하면 `artifact_master_prompt.py`가 자동으로 수집합니다. 특정 파일을 제외하고 싶다면 스크립트 내 TARGET 설정을 수정해야 합니다.
- **Q. `link_check.py` 실행이 길어지면?**  
  A. 우선 Git diff로 변경 범위를 확인해 수동 검증 후 전체 검사를 실행합니다. 현재는 전체 검사에 30~40초가 걸립니다.
- **Q. Archive 스크립트는 언제 사용하나요?**  
  A. 과거 구조 리팩토링이 다시 필요할 때만 사용합니다. 예를 들어, Stage Skeleton을 대량 수정할 경우 `standardize_stage_structure.py`를 참조할 수 있습니다.

---
본 매뉴얼과 `docs/Architecture Design.md`, `readme.md`를 함께 참고하면 어떤 AI Agent도 현재 지침 체계와 자동화 도구를 이해하고 추가 작업을 수행할 수 있다.
