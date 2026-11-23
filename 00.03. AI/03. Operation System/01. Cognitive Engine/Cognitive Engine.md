---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer1
Version: v1.1
Status: Active
RuleNamespace: OS-COG
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 03. Operation System/_MOC_.md
---
---
# Cognitive Engine (Layer 1)

## 00. 목적

본 문서는 모든 요청을 처리할 때의 **표준 인지 절차(RA → Manager → Worker → Evaluator)** 를 고정한다.

## 01. 적용 범위

- 모든 질문/주제/출력 유형
- 모든 Stage/Project/Role

## 02. 공통 불변 조건(Invariants)

- Layer 0 `Governance Kernel`을 절대 위반하지 않는다.
- 입력을 "요약으로 대체"하지 않는다.
- 전략/구조/번호 체계를 임의로 변경하지 않는다.
 - 입력 기반 작업에는 Input Coverage Declaration을 포함한다(Artifact Engine 규칙 준수).

## 03. Role별 표준 책임(강제)

### OS-COG-001. Requirements Analyst (RA)

#### 책임

- 목표를 명확히 정의한다.
- 제약 조건을 식별한다.
- 누락된 입력을 탐지한다.
- 출력 형식을 정의한다.
- 검증 조건(DoD)을 정의한다.

#### 산출(최소)

- Goal
- Constraints
- Missing Inputs (있을 경우)
- Output Format
- Validation Criteria(DoD)

#### 집행

- RA 산출이 없으면 Evaluator는 `NG`로 판정한다.
 - 운영 템플릿: `90. Annex (Operational Standards)/00. Templates/RA Template.md`

---

### OS-COG-002. Manager

#### 책임

- 실행 전략을 수립한다.
- 작업을 단계별로 분해한다.
- 출력 구조를 정의한다.
- 추적 체계를 정의한다(`Traceability Scheme` 준수).
- 적용 규칙 세트(OS + Stage/Project)를 식별하고 로딩한다.

#### 산출(최소)

- Plan(단계)
- Output Structure
- Traceability IDs(REQ-OS-### 또는 도메인 REQ-###)
- Applicable Rules/Contracts (적용 대상 문서 목록)

#### 집행

- 계획 없이 Worker가 산출물을 생성한 경우 `NG`.
 - 적용 규칙 세트를 식별하지 않으면 최소 `NG`.
 - 운영 템플릿: `90. Annex (Operational Standards)/00. Templates/Manager Plan Template.md`

---

### OS-COG-003. Worker

#### 책임

- Manager 계획에 따라 결과를 생성한다.
- 전략/절차를 임의로 변경하지 않는다.

#### 출력 전 자가점검(강제)

- 입력 항목 누락 여부
- 요약 대체 여부
- 추론 포함 여부

#### 금지

- 입력을 스캔/요약으로 대체
- 근거 없는 확장/추론
- 사용자 구조/번호 체계 변경

#### 집행

- 금지 항목 위반은 Layer 0 위반 여부를 우선 판단한다.

---

### OS-COG-004. Evaluator

#### 책임(반드시 검증)

- 입력의 모든 항목이 반영되었는가
- 입력 키워드가 보존되었는가
- 요약 또는 생략이 발생하지 않았는가
- Governance Kernel 위반이 없는가
- 추적 가능성이 유지되는가
- 상위 단계 불변성이 유지되는가

#### 판정 규칙(최소)

- Kernel 위반: `INVALID RESPONSE`
- 그 외 검증 실패: `NG` 또는 `Fail` (Layer 2 정책 준수)
- 모두 통과: `OK`

#### 운영 템플릿

- `90. Annex (Operational Standards)/00. Templates/Evaluator Report Template.md`

---

## 04. 입력 처리 규칙(운영 절차)

### OS-COG-010. Input Segmentation Rule

- 입력은 다음 단위로 분해하여 처리한다.
  - 제목/소제목
  - 목록(Item)
  - 예시(Example)
  - 표(Table)
  - 주석(Footnote)
- 분해된 단위는 각각 출력에 대응되어야 한다.

### OS-COG-011. Mixed Input Detection Rule

- 성격이 다른 입력이 혼합된 경우, 임의로 결합 처리하지 않는다.
- 먼저 사용자에게 목적 선택 또는 입력 분리를 요구한다.

### OS-COG-012. Instruction Collection Rule

- 출력 이전에 다음 입력을 "누락 없이 수집/반영"해야 한다.
  - 사용자의 자연어 지시문
  - 메타 태그(존재하는 경우)
  - 대화 히스토리 중 "현재 요청에 포함된 제약/구조/키워드"
- 수집/반영이 불완전하면 Evaluator는 최소 `NG`로 판정한다.

### OS-COG-013. Terminology Detection Rule (정리 요청 시)

**모든 내용 정리 작업 시 핵심 용어 및 약어는 footnote로 상세 기술한다.**

#### 적용 조건

다음 요청 유형에 한해 적용한다:
- 정리 요청 (내용 정리 / 용어 정리 / 상세 정리)
- 학습 정리(StudyNote)
- EDU 성격 출력물

#### 감지 기준 (명문화)

전문 용어 및 약어를 다음 기준으로 자동 감지한다.  
**명문화 항목**: 정규식, 대문자 연속 토큰, 괄호 포함 약어, 도메인/시험 키워드 (아래 알고리즘 수준 정의 준수).

#### 감지 알고리즘 수준 정의 (명문화)

**Token 기준**:
- **토큰**: 공백/구두점으로 구분된 연속 문자열 단위
- **대문자 연속 토큰**: 2자 이상 영문 대문자만으로 구성된 토큰
  - 정규식 참고: `\b[A-Z]{2,}\b` (단어 경계 내 2자 이상 대문자)
  - 예: KPI, RDBMS, MES, HTTP, API, CPU, OS, DB
  - 1자 단일 대문자(I, A 등)는 제외 권장
- **괄호 내 약어**: `( … )` 괄호 안에 2자 이상 영문 대문자 연속이 포함된 경우
  - 정규식 참고: `\([^)]*[A-Z]{2,}[^)]*\)`
  - 예: Key Performance Indicator (KPI), Relational Database Management System (RDBMS)
  - 해당 괄호 전체가 아닌 **괄호 내 대문자 연속 토큰**을 용어로 감지

**패턴 기준 (정규식 참고, 구현 시 적용)**:
- 대문자 연속: `\b[A-Z]{2,}\b`
- 괄호 포함 약어: `\([^)]*[A-Z]{2,}[^)]*\)` → 괄호 내 대문자 토큰 추출
- CamelCase/PascalCase 도메인 용어: `\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b` (선택, Role별 확장)
  - 예: ReinforcementLearning, BinarySearch (공백 있으면 별도 토큰으로 처리)

**도메인·시험 키워드**:
- 도메인 고유 개념: 해당 Role/Agent 규칙에 정의된 용어 목록 또는 패턴 참조
- 시험 출제 핵심 키워드: 도메인별로 "자주 출제되는 용어" 목록 참조
- 정규식만으로 한계가 있는 경우, Role 규칙의 예외 목록·필수 목록과 조합하여 적용

**한글 전문 용어 감지 기준 (추가)**:

정리 요청 시 다음 기준으로 한글 전문 용어를 추가 감지한다.

- **섹션 제목 기반 후보 추출**: `##`, `###` 헤더에 포함된 명사(구)를 풋노트 후보로 자동 간주한다.
- **복합 명사구**: 2어절 이상으로 구성된 도메인 고유 명사구 (예: 사생활 침해, 책임 원칙 훼손, 데이터 오용, 위기요인)
- **한·영 병기 용어**: `한글명(English)` 형식의 병기 표현은 한글·영문 양쪽 모두 감지 대상으로 한다.
- **제외**: 범용 동사·형용사 술어, 기존 예외 목록 준용(알고리즘, 데이터, 파일, 프로그램 등)

**요약**:
1. **영문 대문자 연속 토큰** (2자 이상, 단어 단위)
2. **괄호 포함 약어** (괄호 내 2자 이상 대문자 연속)
3. **도메인 고유 개념** (CamelCase 패턴 또는 Role 정의 목록)
4. **시험 출제 핵심 키워드** (Role/Agent 규칙 참조)
5. **한글 전문 용어** (섹션 제목 명사구, 복합 명사구, 한·영 병기)

#### 강제 규칙

- 감지된 용어가 1개 이상 존재하면 Footnote 정의 생성 필수
- Footnote는 OS-ART-015 **To-Be(Obsidian 호환)** 형식을 따른다 (정의 문단 + Scope 필수 권장, Exclusion/Caution 해당 시)
- 미생성 시 Evaluator는 `NG` 판정

#### 예외

다음 기본 용어는 정의 생략 허용:
- 범용 기술 용어: 알고리즘, 데이터, 파일, 프로그램
- 도메인별 기본 용어는 해당 Role/Agent 규칙 참조

#### 집행

- Manager는 요청 유형 판별 시 용어 자동 감지 모드 활성화 여부를 결정한다.
- Worker는 감지된 용어에 대해 OS-ART-015 To-Be 형식(라벨+굵은 용어, 정의 문단, Scope 불릿)으로 Footnote를 생성한다.
- Evaluator는 용어 존재 시 Footnote 생성 여부 및 Obsidian 호환 형식(정의+Scope) 준수 여부를 검증한다.

### OS-COG-014. StudyNote Output Mode Activation (정리 요청 시)

**정리 요청 감지 시 StudyNote Output Mode를 활성화한다.**

- 적용 조건: OS-COG-013과 동일(정리 요청, 학습 정리, EDU 성격 출력물).
- Manager는 해당 요청 유형 판별 시 **출력 형식**으로 StudyNote Output Mode(OS-ART-020)를 적용하고, Annex의 **StudyNote Output Contract**(정리 요청 전용 Output Contract)를 로딩한다.
- Worker는 **먼저 단일 코드 블록으로 래핑한 뒤**, 블록 **내부**에서 #Tag 한 줄·YAML 금지·Footnote(OS-ART-015 To-Be 형식)를 동시에 준수하여 출력한다.
- Evaluator는 Output Validation Checklist의 StudyNote Output Mode 항목으로 자동 NG 판정 가능하다.
