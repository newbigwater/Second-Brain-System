---
type: Note
creation date: 2026-01-12
tags:
  - 00_03__AI
  - 00__System
  - 03__Guides
  - 04__PM
  - 03__Project
  - 03_01__PM
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.02 Project/10.02.01 PM/02. Guides/_MOC_|02. Guides]]"
outgoinglinks:
Version: v1.1
Audience: Project Manager / PMO / AI 사용자
Purpose: 프로젝트 관리 요청을 일관된 형식으로 작성하기 위한 Human 전용 가이드 - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
References:
  - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
level: 10.02.01
parent_level: 10.02
---
---
## 1. 목적

본 문서는 프로젝트 관리 단계에서 AI에게 관리 업무를 지시하려는 **Human 사용자**를 위한 프롬프트 작성 기준이다.  
프로젝트 관리는 **조정·추적·보고**에 한정하며, 요구사항·설계·구현 내용을 직접 생성하지 않도록 역할·범위·제약을 명확히 정의한다.

본 문서는 **AI 내부 규칙이 아니며**,  
사람(Human)을 위한 **사용 설명서(Guide)** 이다.

---

## 2. 언제 참고해야 하는가

- 프로젝트 일정 계획 및 추적을 AI에 위임할 때
- WBS, Gantt Chart, 리스크 매트릭스 작성을 요청할 때
- 진행 보고서 자동 생성을 요청할 때
- 프로젝트 상태 대시보드 작성을 요청할 때
- Helios/Aegis/Forge 진행상황 추적을 요청할 때

---

## 3. PM 단계 핵심 원칙

- **조정·추적·보고 전용**: 요구사항·설계·구현 내용 직접 생성 금지
- **단계별 경계 존중**: SRS/SDS/SCS의 책임 범위 침범 금지
- **근거 기반 관리**: 추측 기반 일정 산정이나 리스크 평가 금지
- **우선순위**: Chronos Root Rule → Index → Guide 순으로 적용

### 3.1 출력 모드 판별 규칙 (중요)

요청을 작성하기 전에, 먼저 “원하는 결과 유형”을 아래 우선순위로 판별한다.

```
생성 요청 > 출력 요청 > 내용·용어 정리 요청 > 일반 설명
```

- **생성 요청**: 파일 단위 결과가 필요함(예: `.md` 템플릿, CSV/표 구조)
- **출력 요청**: 복사/저장 가능한 “Artifact” 형태로 출력(코드 블록 기반)
- **내용·용어 정리 요청**: 회의록/리스크/상태 정리(StudyNote 규칙 적용 대상 가능)
- **일반 설명**: 설명 중심(필요한 부분만 표/샘플)

### 3.2 StudyNote(정리/EDU) 출력 규칙 (해당 시 필수 조건으로 명시 권장)

보고서/대시보드/회의 정리처럼 “정리 문서”를 Output으로 요구하는 경우, Output/Constraints에 아래 조건을 **명시적으로 포함**하는 것을 권장한다.

- 문서 **첫 줄에 `#Tag`** 등록
- Footnote는 **정의 대상 용어 토큰 바로 뒤**에 직접 매핑(문장 끝/괄호 전체 부착 금지)
- Bold 용어 뒤에는 **공백 1칸** 유지(예: `**용어[^1]** 을`)
- 표준은 `🖋️ StudyNote Markdown Rulebook`을 따른다
  - 참고: [🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)Rulebook.md)

---

## 4. 권장 프롬프트 기본 구조 (5요소)

1. **역할(Role)** – 프로젝트 매니저, PMO, AI Coordinator 등 PM 역할  
2. **작업(Task)** – 일정 계획 / 진행 추적 / 리스크 관리 / 보고서 생성 등 목적  
3. **맥락(Context)** – 프로젝트 목표, 범위, 일정, 참여자, 단계별 진행상황  
4. **출력 기대(Output)** – WBS, Gantt Chart, 리스크 매트릭스, 보고서 형식 등  
5. **제약(Constraints)** – 단계별 경계 침범 금지, 근거 기반만 작성

### 예시
```
당신은 프로젝트 매니저입니다.
현재 프로젝트의 WBS와 Gantt Chart를 작성해주세요.
프로젝트는 SRS → SDS → SCS 단계로 진행되며, 각 단계별 마일스톤이 정의되어 있습니다.
Markdown 형식으로 WBS와 CSV 형식으로 Gantt Chart를 제공해주세요.
요구사항, 설계, 코드는 생성하지 말고 일정과 업무 분류만 작성해주세요.

WBS/일정 문서는 정리 산출물이므로 StudyNote 규칙을 함께 적용해주세요.
- 문서 첫 줄 #Tag 포함
- 용어/약어(WBS, Gantt 등)는 최초 1회 Footnote로 정의하고 용어 토큰 바로 뒤에 [^n]을 직접 부착
- Bold 용어 뒤 공백 1칸 유지(예: **WBS[^1]** 를)
- 마지막에 ## Footnotes 포함
```

---

## 5. 좋은 PM 프롬프트 작성 원칙

### 5.1 역할을 프로젝트 관리 관점으로 고정
- ✅ 프로젝트 매니저 / PMO / AI Coordinator  
- ❌ 요구사항 분석가 / 아키텍트 / 개발자

### 5.2 범위·대상을 명확히
- 포함: 일정, 리스크, 진행상황, 보고서  
- 제외: 요구사항 생성, 설계 생성, 코드 생성

### 5.3 맥락은 프로젝트 관리 정보 중심
- 프로젝트 목표, 범위, 일정, 예산, 참여자  
- Helios/Aegis/Forge 진행상황, 마일스톤, 이슈

### 5.4 출력 형식은 관리 산출물 구조에 맞춤
- WBS, Gantt Chart, 리스크 매트릭스, 진행 보고서, 대시보드  
- Markdown, CSV, Excel 등 형식 명시

---

## 6. 요청 유형별 작성 예시

### 6.1 일정 계획 요청
```
당신은 프로젝트 매니저입니다.
SRS → SDS → SCS 단계별 일정을 Gantt Chart로 작성해주세요.
각 단계의 마일스톤과 주요 산출물을 포함하고, CSV 형식으로 제공해주세요.
요구사항이나 설계 내용은 생성하지 말고 일정만 작성해주세요.

출력은 StudyNote 규칙을 따르며, 첫 줄 #Tag를 포함하고, 용어/약어는 Footnote 직접 매핑으로 정의해주세요.
```

### 6.2 진행 추적 요청
```
현재 프로젝트 진행상황을 주간 보고서 형식으로 정리해주세요.
Helios/Aegis/Forge 각 단계의 완료율과 이슈를 포함하고,
Markdown 형식으로 제공해주세요.

출력은 StudyNote 규칙을 따르는 정리 문서로 작성해주세요.
- 첫 줄 #Tag 포함
- 용어/약어는 Footnote 직접 매핑
- Bold 용어 뒤 공백 1칸 유지
- 마지막에 ## Footnotes 포함
```

### 6.3 리스크 관리 요청
```
프로젝트 리스크 매트릭스를 작성해주세요.
발생 확률과 영향도를 기준으로 리스크를 분류하고,
대응 전략을 포함하여 CSV 형식으로 제공해주세요.

리스크 매트릭스 요약(정리 문서)은 StudyNote 규칙을 따르며 첫 줄 #Tag를 포함해주세요.
용어/약어는 Footnote 직접 매핑으로 정의해주세요.
```

---

## 7. 피해야 할 요청 방식

- "요구사항을 작성해줘", "설계를 만들어줘" (SRS/SDS 책임)
- "코드를 작성해줘" (SCS 책임)
- "대충 일정 잡아줘" 같은 근거 없는 요청
- 단계별 경계를 침범하는 요청
- 추측 기반 일정 산정 요청

---

## 8. AI 내부 규칙과의 관계

- AI는 **📚 Chronos Root Rule**을 최우선으로 적용한다
- 본 가이드는 Human 참고용이며 Rule과 충돌 시 항상 Rule이 우선한다
- Helios/Aegis/Forge 규칙과 충돌 시 Chronos는 단계별 경계를 존중한다

---

## 9. 결론

정확한 프로젝트 관리 산출물은 **구조화된 요청**에서 출발한다.  
본 가이드를 활용해 조정·추적·보고 중심의 관리 지시를 작성하면 AI와 사람이 같은 기준으로 프로젝트를 관리할 수 있다.
