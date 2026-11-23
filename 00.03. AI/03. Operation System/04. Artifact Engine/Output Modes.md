---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer4
Version: v1.1
Status: Active
RuleNamespace: OS-ART
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 03. Operation System/04. Artifact Engine/Artifact Engine.md
---
---
# Output Modes (Layer 4)

## 00. 목적

본 문서는 요청 유형에 따라 "설명/출력/생성" 모드를 구분하고, 혼합을 금지하여 산출물의 재현성을 보장한다.

## 00-A. 용어(표준)

- Markdown Plain Text: 설명·해설·분석을 문서처럼 읽을 수 있도록 제공하는 일반 Markdown 출력
- Markdown Code Block: 삼중 백틱 코드 블록(복사/붙여넣기 목적)
- Markdown Artifact Output: Markdown Code Block 형식으로 `*.md` 파일 단위로 즉시 저장 가능한 문서 산출 방식(헤더 시작: 기본 `##`)
- Markdown Artifact File Generation: 코드 블록이 아니라 실제 `*.md` 파일을 생성하는 방식(헤더 시작: 기본 `#`)

## 01. 모드 정의

### 01-A. 코드 블록 강제(공통)

**Explanation Mode(OS-ART-001)를 제외한 모든 출력 모드**에서는 다음을 강제한다.
- 전체 산출물은 **단일** ` ```markdown ` 또는 ` ```text ` 코드 블록으로 감싼다.
- 코드 블록 밖에 본문·설명·요약을 두지 않는다(필요 시 최소한의 안내 문장만 허용).
- 코드 블록 **내부** 본문에는 닫는 백틱(```) 한 줄을 포함하지 않는다. 포함 시 마크다운이 첫 번째 ``` 를 블록 종료로 인식하여 블록이 조기 종료되고 그 뒤 내용이 블록 밖으로 빠진다.
- 적용 대상: Artifact Output(002), File Generation(003), 정리 요청/StudyNote(004·020).

### OS-ART-001. 설명 요청(Explanation Mode)

- 트리거(예):
  - "설명", "해설", "분석", "의견", "알려줘"
- 규칙:
  - 구조화된 형식으로 작성한다.
  - 불필요한 문장을 사용하지 않는다.
  - 감성적 표현을 사용하지 않는다.

### OS-ART-002. 산출물 출력 요청(Artifact Output Mode)

- 트리거(예):
  - "출력", "문서로 출력", "md로 내보내", "결과물 출력", "파일 형태로 보여줘"
- 규칙(강제):
  - 단일 코드 블록만 사용한다.
  - 코드 블록 외 텍스트를 작성하지 않는다.
  - 사용자 정의 구조/번호 체계를 유지한다.

### OS-ART-003. 파일 생성 요청(File Generation Mode)

- 트리거(예):
  - "생성", "파일 생성", "md 파일 만들어", "실제 파일로"
- 규칙(강제):
  - 실제 `*.md` 파일을 생성한다(레포 내 경로).
  - 파일 메타데이터(frontmatter)를 포함한다.
  - **응답에서 생성된 파일 내용을 제시할 때**: 단일 코드 블록으로 감싼다. 코드 블록 외 텍스트는 최소한으로 한다(01-A 적용).

## 02. 혼합 금지(기본)

- 명시적 요청이 없는 한 산출물과 설명을 혼합하지 않는다.
- 사용자가 "설명 + 출력"을 동시에 명시하면:
  - 설명 모드로 개요 제공 후,
  - 산출물 출력 모드로 전체 문서를 별도 제공한다.

## 03. 모드 우선순위(강제)

- 복합 요청에서 우선순위는 아래를 따른다.
  - 파일 생성 요청 > 산출물 출력 요청 > 정리 요청(내용/용어/상세) > 설명 요청

## 04. 정리 요청(내용/용어/상세) 모드(확장)

### OS-ART-004. 정리 요청(Organizer Mode)

- **트리거 문장 (필수)**  
  **"정리 요청 시 자동 Footnote 확장"** — 정리 요청이 발생하면 전문 용어·약어가 1개 이상 있을 때 반드시 Footnote 자동 확장을 적용한다.
  
- 트리거(예):
  - "내용 정리 요청", "용어 정리 요청", "용어 정리 자세히 요청"
  - 위 유형 요청 시 → "정리 요청 시 자동 Footnote 확장" 트리거 활성화
  
- **강제 연결 문장 (필수 적용)**:
  - **"내용 정리 요청"이 발생한 경우, 전문 용어·약어가 1개 이상 존재하면 반드시 Footnote 자동 확장 모드를 적용한다.**
  - 이때 출력은 Organizer Mode로 처리하며, OS-COG-013(용어 감지) 및 OS-ART-015(Footnote 3요소 구조)를 준수한다.
  - 위 조건 충족 시 Validation(OS-VAL-FOOT-001/002/003) 미통과 시 NG 판정이다.
  
- 기본 규칙:
  - 정리 출력은 Stage/Project의 Organizer Contract가 존재하면 해당 템플릿을 적용할 수 있다.
  - Organizer Contract가 없으면 본 Annex의 **정리·EDU 산출물 기본 규칙**(`90. Annex (Operational Standards)/정리·EDU 산출물 기본 규칙.md`)을 기본으로 한다.
  
- 불변 조건:
  - 입력 누락/요약 대체 금지
  - 사용자 제공 헤더/구조 변경 금지
  - 순수 Markdown 및 금지 형식(HTML/Canvas 등) 준수

- **용어 자동 감지 및 Footnote 확장**:
  - 전문 용어·약어 존재 여부 자동 탐지 (OS-COG-013 감지 알고리즘 수준 정의 준수)
  - 전문 용어 존재 시 **Footnote 3요소 정의 자동 확장 모드로 전환** (선택이 아님, 강제)
  - Footnote는 OS-ART-015 To-Be(Obsidian 호환) 형식 필수 (정의 문단 + Scope 필수 권장)
  - Footnote 미생성 시 Validation 단계에서 NG 판정

### OS-ART-020. StudyNote Output Mode (정리 요청 전용 출력 형식)

정리 요청(내용/용어/상세 정리, 학습 정리, EDU 성격)이 감지되면 **StudyNote Output Mode**를 활성화한다. 이때 출력 형식은 **정리 요청 전용 Output Contract**(StudyNote Output Contract)를 따른다.

#### 강제 규칙

1. **단일 코드 블록**: 전체 문서는 **단일** ` ```markdown ` 코드 블록(또는 ` ```text `)으로 감싼다.
2. **코드 블록 외 텍스트 금지**: 코드 블록 밖에 설명·요약·부가 문단을 두지 않는다.
3. **코드 블록 내부 첫 줄**: 풋노트에서 추출한 용어를 **#Tag** 한 줄(띄어쓰기로 나열, 개행 금지)로 둔다. 그 다음 빈 줄, 이후 본문 첫 헤더.
4. **YAML frontmatter 금지**: 내용 정리 산출물에는 `---` 블록( title, date, tags 등)을 사용하지 않는다.
5. **Footnote 3요소 구조 필수**: 핵심 용어·약어는 OS-ART-015 **To-Be(Obsidian 호환)** 형식(라벨+굵은 용어, 정의 문단, Scope 불릿, 해당 시 Exclusion/Caution)을 따른다.
6. **헤더 계층 구조 필수** (§07): 문서 제목(`NN. 제목` 형식)이 제공된 경우, H1=상위 토픽(이미지 또는 제목에서 자동 유도), H2=`NN. 제목`(사용자 제공 값 그대로, 변경 금지), H3=`NN.MM. 소절`(두 자리 번호). 임의 번호 체계(1., 3.1 등) 사용 금지.

#### 적용 순서(해석 원칙)

- (1) **출력 래핑**: 정리 산출물은 반드시 **단일** ` ```markdown `(또는 ` ```text `) 코드 블록으로 감싼다.
- (2) **코드 블록 내부**: #Tag 한 줄, YAML 금지, Footnote 3요소 등은 모두 **코드 블록 내부**에서만 적용된다.
- 정리 전용 문서 구조 규칙은 **래핑을 대체하지 않는다.**

#### 금지 해석(오해 방지)

- "#Tag 한 줄, YAML 금지" 등을 "코드 블록 없이 일반 Markdown으로만 출력해야 한다"로 해석하지 않는다. 해당 구조는 **항상 코드 블록 내부**에서만 적용된다.

#### 적용 조건

- 트리거: "내용 정리 요청", "용어 정리", "학습 정리", "정리해 줘", EDU/StudyNote 성격 요청
- Organizer Contract가 있는 Stage/Project는 해당 Contract를 우선하되, 출력 형식(단일 코드 블록·#Tag·YAML 금지)은 본 규칙을 따른다.
- 상세 계약: `90. Annex (Operational Standards)/📜 StudyNote Output Contract.md`
