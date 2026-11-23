# CLAUDE.md (00. Second-Brain-System/00.03. AI)

`00. Second-Brain-System/00.03. AI/` 아래 파일을 다룰 때 자동으로 로드되는 지침이다. 루트 `CLAUDE.md`와 함께 적용된다.

## 명령: AI Operation System 스크립트

모두 `00. Second-Brain-System/00.03. AI/02. 3'rd Party/`에서 실행한다. 공통적으로 `--check`(동기화 여부 판정, exit code로 보고) / `--diff`(변경 미리보기) / `--write`(실제 반영) 3모드를 따르며, 기본값은 비파괴 모드다. **먼저 `--check` 또는 `--diff`로 확인한 뒤 `--write`한다.**

```bash
cd "00. Second-Brain-System/00.03. AI/02. 3'rd Party"

# OS Master Prompt 재생성 (Kernel/Engine 문서를 하나로 합성)
python os_master_prompt_generator.py --diff
python os_master_prompt_generator.py --write --stamp-updated   # --bump-version 으로 vX.Y 증가

# Agent별 Master Prompt 재생성 (OS Master Prompt + Role Rule + Checklist + Domain Knowledge)
python agent_master_prompt_generator.py --diff
python agent_master_prompt_generator.py --write
python agent_master_prompt_generator.py --role "01. Computer-Science Expert" --write  # 단일 Role만

# 04. Agent/_MOC_.md 의 Active Roles 섹션을 실제 폴더 구조와 동기화
python update_agent_moc.py --check
python update_agent_moc.py --write

# Agent 폴더 구조/OS 상속 선언 검증 (통과 0, 실패 1) — 사실상 이 저장소의 유일한 테스트
python validate_agent_structure.py

# 신규 Persona/Role 스캐폴딩
python create_persona.py --name "My Persona" --role "한 줄 설명"
```

`validate_agent_structure.py`는 각 Role 폴더에 `Role Rule.md`와 `99. Artifact/<RoleName>.md`가 있는지, Role Rule에 OS 상속 선언이 있는지, Artifact가 OS Master Prompt와 Role Rule을 참조하는지 검사한다. Agent 관련 파일을 수정한 뒤에는 이 스크립트를 돌린다.

## 구조: AI Operation System

문서를 조립해 LLM 마스터 프롬프트를 생성하는 파이프라인이다. 계층은 **엔진 문서 → OS Master Prompt → Agent Master Prompt** 순으로 흐른다.

```
03. Operation System/          # OS 정본 (사람이 편집하는 소스)
  00. Governance Kernel/       # Kernel.md, Violation Policy.md
  01. Cognitive Engine/        # Cognitive Engine.md, Traceability Scheme.md
  02. Validation Engine/       # Validation Engine.md, NG-Fail Policy.md, Checklists/
  03. Self-Reflection Loop/
  04. Artifact Engine/         # Output Modes.md
  90. Annex (Operational Standards)/   # 태그·링크·산출물 표준
  99. Artifact/Master Prompt.md        # ← 생성물. 직접 편집 금지

04. Agent/                     # Role별 페르소나
  00. Template/                # Role Rule / Persona 뼈대
  NN. <Role Name>/
    Role Rule.md               # OS 상속 선언 필수
    Persona Profile.md, Validation Checklist.md, Domain Knowledge.md
    99. Artifact/<RoleName>.md # ← 생성물. 직접 편집 금지
  90. Shared Resources/
  _MOC_.md                     # Active Roles 목록 — update_agent_moc.py가 관리

01. Doc/                       # 설계서 및 스크립트 사용법 매뉴얼
02. 3'rd Party/                # 위 파이프라인을 구동하는 Python 스크립트
```

핵심 규칙: **`99. Artifact/` 하위 파일은 전부 생성물이다.** 내용을 바꾸려면 소스 문서(Kernel/Engine/Annex/Role Rule)를 고치고 제너레이터를 `--write`로 다시 돌린다. Artifact를 직접 편집하면 다음 생성 시 사라진다. Artifact frontmatter의 `Version`/`References`도 제너레이터가 관리한다.

스크립트별 상세 사용법은 `00. Second-Brain-System/00.03. AI/01. Doc/02. Manual/`에, 설계 의도는 `01. Doc/01. Design/`에 있다.
