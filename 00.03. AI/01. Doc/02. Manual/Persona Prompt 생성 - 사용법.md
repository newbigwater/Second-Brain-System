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
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/04. Agent - 설계서.md
  - 00. Second-Brain-System/00.03. AI/01. Doc/01. Design/03. Operation System - 설계서.md
  - 00. Second-Brain-System/00.03. AI/04. Agent/readme.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/90. Annex (Operational Standards)/00. Templates/OS Output Template.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/90. Annex (Operational Standards)/🧾 Organizer Contract Standard.md
---
---
# Persona Prompt 생성 — 사용법

## 00. 이 문서는 무엇인가?

이 문서는 **Persona(Role) prompt를 처음부터 생성**할 때 사용자가 따라야 할 **표준 절차**를 설명한다.  
새 Agent(역할)를 추가하고, Role Rule·Artifact를 준비한 뒤 Master Prompt까지 만드는 흐름을 한 권에 정리한다.

- **대상**: 새 Persona 또는 Role을 만들고 싶은 사용자
- **범위**: 템플릿 선택 → Role Rule 작성 → Artifact 폴더 구성 → Master Prompt 생성 → 검증

---

## 01. 언제 사용하나요?

다음 경우에 본 매뉴얼을 따른다.

- 새로운 **도메인 전문가 Persona**(예: 글쓰기 코치, 번역 전문가)를 추가할 때
- 새로운 **작업 유형 Role**(예: SRS 작성, 테스트)을 추가할 때
- 기존 Role/Persona가 없어 **처음부터 폴더·파일·규칙**을 잡을 때

---

## 02. 전제 조건

- **OS 이해**: `03. Operation System`이 기본 규칙·산출물 출력 방식을 정의하며, Persona는 이를 **확장만** 할 수 있다는 점을 알고 있을 것.
- **작업 디렉터리**: `00.03. AI` 루트(또는 `04. Agent` 폴더)에서 경로를 기준으로 진행한다.
- **참고 문서**: 필요 시 `01. Doc/01. Design/04. Agent - 설계서.md`, `04. Agent/readme.md`를 함께 본다.

---

## 03. Role vs Persona 선택

| 구분 | Role | Persona |
|------|------|---------|
| 목적 | 작업 유형/Stage별 확장 | 전문가 역할 기반 확장 |
| 구조 | 추가 제약/검증/템플릿 중심 | Role + Experience + Thinking Style + Domain Knowledge |
| 템플릿 | `04. Agent/00. Template/Role Rule Template.md` | `04. Agent/00. Template/Persona Template.md` |

**권장**: 도메인 전문가 성격이면 **Persona**, 작업 단계 성격이면 **Role**을 선택한다.

---

## 04. 표준 절차 (Step 1 ~ 6)

> **자동 생성(선택)**: `02. 3'rd Party/create_persona.py`를 사용하면 Step 1~5와 Persona Output Template까지 한 번에 생성할 수 있다.  
> 매뉴얼: `01. Doc/02. Manual/create_persona - 사용법.md`

### Step 1: 폴더 생성 및 템플릿 복사

**1.1 폴더 생성**

```powershell
cd "d:\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
mkdir "04. Agent\0X. <Role Name>"
```

- `0X`는 번호(예: `04`). 기존 Role 번호와 겹치지 않게 한다.

**1.2 템플릿 복사**

- **Role 타입**: `00. Template/Role Rule Template.md` → `0X. <Role Name>/Role Rule.md`
- **Persona 타입**: `00. Template/Persona Template.md` → `0X. <Role Name>/Role Rule.md`

```powershell
# Persona 예시
Copy-Item "04. Agent/00. Template/Persona Template.md" "04. Agent/0X. <Role Name>/Role Rule.md"
```

---

### Step 2: Role Rule 작성

**2.1 필수 포함 항목**

- **00. Role Definition**: Role Name, Domain, Applies To
- **01. OS 상속 선언 (강제)**: "본 Role은 OS Layer 0~4를 상속하며, 약화/무력화할 수 없다."
- **02. Extension Points**: 추가 제약, 추가 검증, **추가 산출물 템플릿**(내부 형식 확장)
- **03. Conflict Resolution**: OS Layer 0 > … > L4 > 본 Role
- **04. DoD**: 검증 가능한 완료 조건

**2.2 산출물 출력 형식 확장 (정리 요청 등 해당 시)**

- OS 기본 형식은 `03. Operation System/90. Annex (Operational Standards)/00. Templates/OS Output Template.md`를 따른다.
- **산출물 내부**의 섹션·테이블·템플릿은 **본 Role(Role Rule 또는 Organizer Contract)** 에서 확장·정의할 수 있다.
- 확장 시에도 OS 기본 형식(단일 코드 블록, 정리 시 #Tag·YAML 금지·Footnote 3요소 등)을 약화·대체하지 않는다.
- 정리 요청 특화 구조가 필요하면 `🧾 Organizer Contract`를 Role 폴더에 두고, Allowed Slots에 따라 내부 형식만 정의한다.

---

### Step 3: 추가 파일 생성 (선택)

```powershell
cd "04. Agent/0X. <Role Name>"

# Persona용: 사람이 읽기 쉬운 프로필
New-Item "Persona Profile.md"

# 검증 체크리스트
New-Item "Validation Checklist.md"

# 도메인 참조용
New-Item "Domain Knowledge.md"
```

- Role만 쓸 경우 Persona Profile은 생략 가능하다.

---

### Step 4: Artifact 폴더 및 파일 생성

```powershell
mkdir "99. Artifact"
New-Item "99. Artifact/readme.md"
New-Item "99. Artifact/<Role Name>.md"
```

- `<Role Name>`은 폴더명에서 번호만 뗀 이름(예: `01. Computer-Science Expert` → `Computer-Science Expert.md`).
- Compact·Applied는 필요 시 추가. **Master Prompt 본문은 스크립트로 생성**하는 것을 권장(Step 6).

---

### Step 5: _MOC_.md 업데이트

`04. Agent/_MOC_.md`의 **Active Roles** 섹션에 새 Role 한 줄을 추가한다.

```markdown
- `0X. <Role Name>/` — <한 줄 설명>
```

---

### Step 6: Master Prompt 생성 및 검증

**6.1 Master Prompt 생성 (권장: 스크립트)**

```powershell
cd "d:\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "0X. <Role Name>" --write
```

- **매뉴얼**: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`

**6.2 구조·OS 준수 검증**

```powershell
python "02. 3'rd Party/validate_agent_structure.py"
```

- Exit 0: 필수 파일·OS 상속 선언·Artifact References 통과.
- **매뉴얼**: `01. Doc/02. Manual/validate_agent_structure - 사용법.md`

---

## 05. 출력 형식 정리 (OS 기본 + Persona 확장)

- **기본**: 산출물 출력은 OS가 정한 **기본 형식**(`OS Output Template`)을 따른다. 단일 코드 블록, 정리 요청 시 #Tag 한 줄·YAML 금지·Footnote 3요소 등.
- **확장**: 각 Persona(Role)는 **내부 형식**(섹션·테이블·템플릿)을 Role Rule 또는 Organizer Contract에서 확장할 수 있다. OS 기본 형식을 **대체·약화하지 않는다**.
- **참고**: `01. Doc/01. Design/03. Operation System - 설계서.md` §02.06, `04. Artifact Engine/Artifact Engine.md` OS-ART-016, `🧾 Organizer Contract Standard.md` Allowed Slots.

---

## 06. 참고

| 문서 | 용도 |
|------|------|
| `01. Doc/00. Index.md` | 설계·매뉴얼 전체 목차 |
| `01. Doc/01. Design/04. Agent - 설계서.md` | Agent 구조·확장 원칙·할 수 있는 것/못 하는 것 |
| `04. Agent/readme.md` | 사용 가이드·새 Agent 만들기 요약 |
| `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md` | Master Prompt 자동 생성·갱신 |
| `01. Doc/02. Manual/validate_agent_structure - 사용법.md` | Role 폴더·OS 준수 검증 |
| `01. Doc/02. Manual/update_agent_moc - 사용법.md` | Agent _MOC_.md Active Roles 자동 갱신 |
| `03. Operation System/90. Annex/00. Templates/OS Output Template.md` | OS 기본 산출물 출력 형식 |
| `03. Operation System/90. Annex/🧾 Organizer Contract Standard.md` | 정리 요청 시 내부 형식 확장 계약 |
| `01. Doc/02. Manual/create_persona - 사용법.md` | Persona 스캐폴드 자동 생성 스크립트 |
