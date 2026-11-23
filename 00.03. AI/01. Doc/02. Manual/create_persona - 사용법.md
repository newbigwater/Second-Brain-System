---
type: Manual
creation date: 2026-02-21
tags:
  - 00__System
  - 00_03__AI
  - 01__Doc
  - 02__Manual
  - 04__Agent
Version: v1.0
Status: Active
References:
  - 00. Second-Brain-System/00.03. AI/01. Doc/00. Index.md
  - 00. Second-Brain-System/00.03. AI/02. 3'rd Party/create_persona.py
  - 00. Second-Brain-System/00.03. AI/01. Doc/02. Manual/Persona Prompt 생성 - 사용법.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/90. Annex (Operational Standards)/00. Templates/OS Output Template.md
---
---
# create_persona — 사용법

## 00. 이 문서는 무엇인가?

이 문서는 `create_persona.py`를 사용해서 **04. Agent 아래에 새 Persona(또는 Role) 스캐폴드를 자동 생성**하는 방법을 설명한다.

- **입력**: Persona Name, Persona Role(한 줄 설명)
- **생성**: 폴더·Role Rule·**Persona Output Template**(OS Output Template 복사)·Artifact 등
- **Persona Output Template**: 사용자가 편집 가능하며, Persona Agent는 이 형식을 기준으로 산출물 내부 구조를 출력한다.

---

## 01. 언제 사용하나요?

- 새 **Persona** 또는 **Role**을 추가할 때 수동 폴더/파일 생성 대신 스크립트로 한 번에 스캐폴드를 만들고 싶을 때
- **Persona Output Template**을 OS 기본 형식에서 시작해 Persona별로 수정해 쓰고 싶을 때

---

## 02. 무엇을 생성하나요?

| 대상 | 설명 |
|------|------|
| `04. Agent/<NN>. <Name>/` | 다음 번호 자동 부여(01, 02, 03 … 다음) |
| `Role Rule.md` | Persona Template(또는 Role Rule Template) 복사 + Name/Role 치환 + Persona Output Template 참조 문구 |
| `00. Template/Persona Output Template.md` | OS Output Template 복사 + "본 Persona 전용, 사용자 수정 가능" 안내 |
| `Persona Profile.md`, `Validation Checklist.md`, `Domain Knowledge.md` | 최소 스텁 |
| `99. Artifact/readme.md`, `99. Artifact/<Name>.md` | (기본 생성, --no-artifact 시 생략) |
| `_MOC_.md` | Active Roles에 새 한 줄 추가 |

---

## 03. 사용법(명령어)

작업 디렉터리는 **00.03. AI** 루트로 둔다.

### 03.01. 기본 실행 (Persona)

```powershell
cd "d:\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/create_persona.py" --name "My Persona" --role "한 줄 설명"
```

- `--name`: 폴더명·Artifact 파일명에 쓰는 이름(예: `Computer-Science Expert`)
- `--role`: 한 줄 설명(_MOC_·Role Definition용, 예: `CS 이론 전문가`)

### 03.02. Role 타입으로 생성

```powershell
python "02. 3'rd Party/create_persona.py" --name "Document Designer" --role "문서 설계" --type role
```

- `--type role`: Role Rule Template 기반으로 생성

### 03.03. Artifact 폴더 없이 생성

```powershell
python "02. 3'rd Party/create_persona.py" --name "My Persona" --role "한 줄 설명" --no-artifact
```

- 나중에 `agent_master_prompt_generator.py`로 Artifact만 생성할 때 사용

### 03.04. AI 루트 지정

```powershell
python "02. 3'rd Party/create_persona.py" --name "My Persona" --role "한 줄 설명" --ai-root "D:/경로/00.03. AI"
```

---

## 04. 생성 후 할 일

1. **Role Rule.md** 및 **00. Template/Persona Output Template.md** 필요에 따라 수정
2. (Artifact를 만든 경우) Master Prompt 생성:  
   `python "02. 3'rd Party/agent_master_prompt_generator.py" --role "<NN>. <Name>" --write`
3. 검증:  
   `python "02. 3'rd Party/validate_agent_structure.py"`

---

## 05. Persona Output Template

- **위치**: `04. Agent/<NN>. <Name>/00. Template/Persona Output Template.md`
- **내용**: OS Output Template과 동일한 형식에서 시작. 상단에 "본 Persona 전용, 사용자 수정 가능, Agent는 본 템플릿 내부 형식 기준 출력" 안내가 들어 있다.
- **역할**: 정리 요청·산출물 출력 시 **내부** 섹션·테이블·항목을 이 파일로 확장·정의. OS 래핑(단일 코드 블록, #Tag, Footnote 3요소 등)은 유지.

---

## 06. 참고

- **Persona Prompt 생성 절차 전체**: `01. Doc/02. Manual/Persona Prompt 생성 - 사용법.md`
- **Master Prompt 생성**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`
- **구조 검증**: `01. Doc/02. Manual/validate_agent_structure - 사용법.md`
- **OS 기본 출력 형식**: `03. Operation System/90. Annex/00. Templates/OS Output Template.md`
