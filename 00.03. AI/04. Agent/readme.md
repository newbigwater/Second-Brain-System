---
type: Guide
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
Version: v1.1
Status: Active
References:
  - 04. Agent/_MOC_.md
---
---
# 04. Agent — 사용 가이드

## 00. Agent란 무엇인가?

`04. Agent`는 **역할(Role) 기반 AI 동작 확장 시스템**이다.

### 핵심 개념
- **OS (Operation System)**: 공통 헌법 + 실행 엔진 (`03. Operation System`)
- **Agent (Role)**: 특정 업무/도메인에 특화된 확장 규칙
- **가장 중요한 원칙**: Role은 OS를 **약화할 수 없다** (확장만 가능)

### OS vs Agent
| 구분 | OS | Agent |
|------|-----|-------|
| 목적 | 모든 작업에 공통 적용되는 불변 규칙 | 특정 Role/Domain 전용 추가 규칙 |
| 적용 범위 | 전역 (모든 요청) | 해당 Role 활성화 시에만 |
| 우선순위 | 최상위 (Layer 0~4) | OS 다음 |
| 예시 | 거짓 생성 금지, 입력 전체 읽기, 검증 절차, 풋노트 To-Be 형식 | CS 학습 정리 4요소, 통역/메일 모드, Podo·Grammar 학습 정리 |

### 현재 등록된 Agent (Active Roles)

| Role | 용도 | Artifact (첨부용) |
|------|------|-------------------|
| `01. Computer-Science Expert/` | CS 이론·알고리즘·시스템·소프트웨어 공학 | `99. Artifact/Computer-Science Expert.md` |
| `02. LinguaBridge/` | 비즈니스 통역(Mode 1), 비즈니스 메일 번역·작성(Mode 2) | `99. Artifact/LinguaBridge.md` |
| `03. English Learning Helper/` | 비기너 영어 주간 정리(Podo), 책 기반 문법 정리(Grammar) | `99. Artifact/English Learning Helper.md` |

상세 목록·Quick Navigation: `04. Agent/_MOC_.md`

---

## 01. 언제 Agent를 만드나?

다음 경우에 Agent(Role)를 만든다:

✅ **만들어야 하는 경우**
- 특정 도메인(CS, 영어, 글쓰기 등)에 반복적으로 작업
- 도메인 특화 규칙/체크리스트/템플릿이 필요
- 일관된 응답 품질을 보장하고 싶을 때
- 여러 플랫폼(ChatGPT, Gemini, Cursor)에서 동일한 동작 필요

❌ **만들지 않아도 되는 경우**
- 일회성 요청
- OS 기본 규칙만으로 충분한 작업
- 도메인 특화 규칙이 없는 경우

---

## 02. Role vs Persona 차이

### Role
- **목적**: 작업 유형/Stage별 확장 (예: SRS 작성, 번역, 테스트)
- **구조**: 추가 제약/검증/템플릿 중심
- **템플릿**: `00. Template/Role Rule Template.md`

### Persona
- **목적**: 전문가 역할 기반 확장 (예: CS Expert, 글쓰기 코치)
- **구조**: Role + Experience + Thinking Style + Domain Knowledge
- **템플릿**: `00. Template/Persona Template.md`

**권장**: 도메인 전문가 성격이면 Persona, 작업 단계 성격이면 Role

---

## 03. 새 Agent 만들기 (표준 절차)

> **상세 매뉴얼**: `01. Doc/02. Manual/Persona Prompt 생성 - 사용법.md` — 단계별 절차·출력 형식 확장·검증까지 정리.

### Step 1: 템플릿 선택 및 복사

```powershell
# 폴더 생성
mkdir "d:\03. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI\04. Agent\0X. <Role Name>"
```

**Role 타입**:
```powershell
# 템플릿 복사
Copy-Item "00. Template/Role Rule Template.md" "0X. <Role Name>/Role Rule.md"
```

**Persona 타입**:
```powershell
Copy-Item "00. Template/Persona Template.md" "0X. <Role Name>/Role Rule.md"
```

### Step 2: Role Rule 작성

필수 포함 항목:
```markdown
## 00. Role Definition
- Role Name: <이름>
- Domain: <도메인>
- Applies To: <적용 범위>

## 01. OS 상속 선언 (강제)
본 Role은 OS Layer 0~4를 상속하며, 약화/무력화할 수 없다.

## 02. Extension Points

### 02.01. 추가 제약 (Constraints)
- (예) CS 이론 범위로 제한
- (예) 4요소 단위 필수

### 02.02. 추가 검증 (Validation Hooks)
- (예) XXX-VAL-001: 완결성 검증
- (예) XXX-VAL-002: 용어 정의 검증

### 02.03. 추가 산출물 템플릿 (Output Templates)
- (예) 학습 정리 템플릿
- (예) 비교표 템플릿

## 03. Conflict Resolution
OS Layer 0 > L1 > L2 > L3 > L4 > 본 Role

## 04. DoD (완료 조건)
- [ ] 검증 가능한 조건 1
- [ ] 검증 가능한 조건 2
```

### Step 3: 추가 파일 생성 (선택)

```powershell
# Persona Profile (사람이 읽기 쉬운 버전)
New-Item "0X. <Role Name>/Persona Profile.md"

# Validation Checklist
New-Item "0X. <Role Name>/Validation Checklist.md"

# Domain Knowledge (참조용)
New-Item "0X. <Role Name>/Domain Knowledge.md"
```

### Step 4: Artifact 폴더 생성

```powershell
mkdir "0X. <Role Name>/99. Artifact"

# Artifact 파일들 (필수: readme.md, <Role Name>.md)
New-Item "0X. <Role Name>/99. Artifact/readme.md"
New-Item "0X. <Role Name>/99. Artifact/<Role Name>.md"

# 선택: Compact(길이 제한 대응), Applied(적용 이력)
# New-Item "0X. <Role Name>/99. Artifact/<Role Name> (Compact).md"
# New-Item "0X. <Role Name>/99. Artifact/Applied.md"
```

### Step 5: _MOC_.md 업데이트

`04. Agent/_MOC_.md`의 "Active Roles" 섹션에 추가:
```markdown
- `0X. <Role Name>/` — <설명>
```

### Step 6: Master Prompt 생성

**수동 방식** (임시):
1. `03. Operation System/99. Artifact/Master Prompt.md` 복사
2. `0X. <Role Name>/Role Rule.md` 내용 추가
3. frontmatter References 업데이트

**자동 방식** (권장):
```powershell
# 단일 Role만 재생성
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "0X. <Role Name>" --write

# 모든 Active Role 일괄 재생성 (_MOC_.md 기준)
python "02. 3'rd Party/agent_master_prompt_generator.py" --write
```
매뉴얼: `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md`

---

## 04. Agent 적용하기

### 4.1 ChatGPT Custom Instructions

**권장 방식 (파일 첨부)**:
1. OS 첨부: `03. Operation System/99. Artifact/Master Prompt.md`
2. Role 첨부: `04. Agent/0X. <Role Name>/99. Artifact/<Role Name>.md`
3. 텍스트 입력: "위 첨부 파일의 모든 규칙을 최상위로 적용하라"

**대안 (텍스트만)**:
- `Master Prompt (Compact).md` 복사 → Custom Instructions 입력란에 붙여넣기

### 4.2 Gemini GEM

1. 새 GEM 생성
2. Knowledge에 <Role Name>.md 업로드
3. Instructions에 "본 문서는 전체 지침으로 적용" 입력

### 4.3 Cursor AI

1. `.cursor/rules/` 폴더 생성
2. `<role-name>.mdrule` 파일 생성
3. Role Rule.md + OS 핵심 규칙 작성
4. 프로젝트에서 자동 적용

### 4.4 Claude Projects

1. Project Knowledge에 <Role Name>.md 추가
2. Custom Instructions: "위 Knowledge의 모든 규칙 적용"

---

## 05. Agent 업데이트하기

### 05-A. Master Prompt 재생성 절차 (체크리스트)

Artifact는 **생성 산출물**이므로, 아래 변경 시 반드시 재생성한다.

| 변경 주체 | 실행 순서 | 참고 매뉴얼 |
|-----------|-----------|-------------|
| OS 규칙/Annex 수정 | ① `os_master_prompt_generator.py --write` → ② 각 Role별 `agent_master_prompt_generator.py --role "0X. ..." --write` | OS Master Prompt Generator 사용법 |
| 특정 Role 규칙 수정 | 해당 Role만 `agent_master_prompt_generator.py --role "0X. ..." --write` | Agent Master Prompt Generator 사용법 |
| 검증 | `validate_agent_structure.py` (필수 파일·OS 상속·References) | Agent Master Prompt Generator 사용법 §10.2 |

경로: `02. 3'rd Party/` (작업 디렉터리: `00.03. AI` 루트)

### OS 업데이트 시 (전체 동기화 필요)

```powershell
# 1. OS Master Prompt 재생성
cd "d:\03. Areas\Second-Brain-Area\00. Second-Brain-System\00.03. AI"
python "02. 3'rd Party/os_master_prompt_generator.py" --write --bump-version

# 2. 모든 Agent Artifact 재생성 (_MOC_.md Active Roles 기준)
python "02. 3'rd Party/agent_master_prompt_generator.py" --write --bump-version

# 3. Git 커밋
git add "03. Operation System/99. Artifact" "04. Agent/*/99. Artifact"
git commit -m "chore: Sync all Agents with OS v1.2"
```

### Role 규칙 업데이트 시

```powershell
# 1. Role Rule.md 수정
code "04. Agent/01. Computer-Science Expert/Role Rule.md"

# 2. 변경 확인
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --check --diff

# 3. Master Prompt 재생성
python "02. 3'rd Party/agent_master_prompt_generator.py" --role "01. Computer-Science Expert" --write --bump-version

# 4. Applied.md 업데이트
code "04. Agent/01. Computer-Science Expert/99. Artifact/Applied.md"

# 5. Git 커밋
git add "04. Agent/01. Computer-Science Expert"
git commit -m "feat(agent): Improve CS Expert comparison table generation"
```

---

## 06. 문제 해결 (Troubleshooting)

### Q1: Agent가 OS 규칙을 무시하는 것 같아요
**A**: OS 우선순위가 최상위임을 명시적으로 지시
```
"OS Layer 0 Governance Kernel 규칙을 절대 위반하지 마세요.
불확실한 경우 반드시 '알 수 없습니다'로 표기하세요."
```

### Q2: 여러 Role을 동시에 사용할 수 있나요?
**A**: 가능하지만 충돌 가능
- 권장: 한 세션에 하나의 Role
- 필요시: Multi-Role Master Prompt 생성 (OS + Role1 + Role2)
- 충돌 해결: 명시적으로 우선순위 지정

### Q3: Master Prompt 파일이 너무 커요
**A**: 
- ChatGPT/Gemini: 파일 첨부 제한 없음 (Full 버전 사용)
- 텍스트 입력란: Compact 버전 사용
- Cursor: Rule 파일은 핵심만 추출 (~2000줄)

### Q4: Compact vs Full 언제 쓰나요?
**A**:
- **Full**: 파일 첨부 가능한 모든 환경 (권장)
- **Compact**: 텍스트 입력만 가능 + 길이 제한 있을 때

### Q5: Role Rule을 수정했는데 적용이 안 돼요
**A**:
1. Master Prompt 재생성 확인
2. 세션 초기화 (새 대화 시작)
3. 명시적 적용 요청: "Computer-Science Expert Persona를 적용해주세요"

---

## 07. 모범 사례 (Best Practices)

### ✅ DO
- OS 상속 선언을 명시적으로 작성
- 검증 가능한 규칙만 추가 (yes/no 판단 가능)
- DoD(완료 조건)를 구체적으로 정의
- Master Prompt는 자동 생성 (수동 편집 최소화)
- Git으로 버전 관리

### ❌ DON'T
- OS 규칙을 약화/재정의 시도
- "더 좋은 느낌으로" 같은 검증 불가능한 규칙
- Role Rule.md 대신 Master Prompt 직접 수정
- 여러 Role을 하나의 Rule에 혼합
- 레거시 경로 참조 (독립적으로 완결되어야 함)

---

## 08. 참고 자료

- **목차·Quick Navigation**: `04. Agent/_MOC_.md`
- **설계 문서**: `01. Doc/01. Design/04. Agent - 설계서.md`
- **OS 설계**: `01. Doc/01. Design/03. Operation System - 설계서.md`
- **템플릿**: `04. Agent/00. Template/`
- **예시 Role**: `01. Computer-Science Expert/`, `02. LinguaBridge/`, `03. English Learning Helper/`

---

## 09. 도움말

문제가 발생하거나 추가 기능이 필요한 경우:
1. `04. Agent/_MOC_.md`의 Index·Version History 확인
2. 예시 Role 참고: `01. Computer-Science Expert/`, `02. LinguaBridge/`, `03. English Learning Helper/`
3. `01. Doc/02. Manual/Agent Master Prompt Generator - 사용법.md` 및 OS 설계 문서 재검토
