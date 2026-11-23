---
type: Note
creation date: 2026-01-30 10:40
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 03__Operations
  - 01__Execution_Gate
  - 01__Core
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/00. Charter/01. Execution Gate/_MOC_|01. Execution Gate]]"
outgoinglinks:
Version: v1.1 - 01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md
References:
  - 01. Core/00. Charter/🖋️ StudyNote Markdown Rulebook.md
level: 0
---
---
> 본 체크리스트는 문서 작성 결과물이 **Footnote 표기 규칙을 정확히 준수하는지 자동 또는 수동으로 검증**하기 위한 기준이다.  
> 본 항목은 *[🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)으로 구체화**한 것이다.

---

## 01. 기본 원칙 검증

- [ ] Footnote는 **전문 용어·약어 정의 목적**과 **문장 의미 설명 목적**으로 명확히 구분되었는가
- [ ] 용어 정의 목적 Footnote가 **문장 끝에 사용되지 않았는가**
- [ ] 동일 용어에 대해 Footnote가 **최초 1회만 사용**되었는가

---

## 02. 용어 정의 Footnote 검증 (필수)

- [ ] 전문 용어 또는 약어가 등장하는가
- [ ] 해당 용어에 **Footnote 정의가 존재하는가**
- [ ] Footnote가 **용어 토큰 바로 뒤에 위치**하는가
	- 예: KPI[^1], MES[^2]
- [ ] 괄호가 있는 경우에도 **약어 문자에 직접 부착**되었는가
	- 허용: 성과지표 KPI[^1], 성과지표(KPI[^1])
	- 금지: 성과지표(KPI)[^1]
- [ ] (해당 시) Bold로 강조된 용어 뒤에 조사/어미가 오는 경우, **Bold 종료 후 공백 1칸**이 존재하는가
	- 허용: **페이지랭크(PageRank) 알고리즘[^2]** 을 통해 …
	- 금지: **페이지랭크(PageRank) 알고리즘[^2]**을 통해 …

---

## 03. 혼합 표현 검증 (한글 + 약어)

- [ ] ‘한글 + 약어’ 구조가 최초 등장 시 사용되었는가
- [ ] Footnote가 **약어(KPI) 토큰에 부착**되었는가
- [ ] 한글 명칭 또는 괄호 전체에 Footnote가 달리지 않았는가

---

## 04. 문장 의미 설명 Footnote 검증 (제한적 허용)

- [ ] Footnote가 문장 전체 의미 보충 목적에 해당하는가
- [ ] 정책·배경·보충 설명 성격인가
- [ ] 용어 정의 목적이 아닌 것이 명확한가
- [ ] 이 경우에만 **문장 끝 Footnote**가 사용되었는가

---

## 05. 금지 패턴 자동 탐지 항목

다음 패턴이 존재할 경우 **규칙 위반**으로 판단한다.

- [ ] ❌ 용어 정의 Footnote가 문장 끝에 위치
- [ ] ❌ 괄호 전체에 Footnote 부착
- [ ] ❌ 하나의 용어 토큰에 복수 Footnote 연속 부착
	- 예: **구글 검색 서비스[^1][^2]**
- [ ] ❌ 동일 용어에 Footnote 반복 사용
- [ ] ❌ 용어 정의 없이 문장 의미 Footnote만 존재

---

## 06. 최종 판정

- [ ] 모든 필수 항목을 충족함
- [ ] 위반 항목 없음
- [ ] Footnote 규칙 **준수 판정(PASS)**

---

## 07. 자동화 적용 권장 지점

- LLM 출력 후 **Self-Check 단계**
- Cursor / ChatGPT Agent의 **Output Validator**
- PRD / SRS / StudyNote 문서 리뷰 체크리스트
- CI 기반 Markdown Lint 규칙 확장 대상

---

본 체크리스트는  
**사람·AI·에이전트 모두가 동일한 기준으로 Footnote를 판단**하도록 설계되었다.
