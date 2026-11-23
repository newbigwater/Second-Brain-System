---
type: Checklist
creation date: 2026-02-26
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - EnglishLearning
  - Validation
Version: v1.0
Status: Active
Purpose: English Learning Helper(Podo/Grammar) 특화 검증 체크리스트
References:
  - 04. Agent/03. English Learning Helper/Role Rule.md
  - 03. Operation System/02. Validation Engine/Checklists/Output Validation Checklist.md
---
---
# English Learning Helper — Validation Checklist

> 본 체크리스트는 English Learning Helper Persona 적용 시, **Podo 모드** 산출물 검증용이다.  
> OS Output Validation Checklist와 함께 사용한다.  
> Work Order 260223(Practice 단어 누락 검출 및 지침 업데이트, Words 추출 범위 확장 v1.3) 반영.

---

## 00. 사용 방법

### 검증 시점
1. [Practice] Word Table 작성 완료 직후 (출력 전 자가 검증)
2. Evaluator/사용자 검증 시
3. Output Validation Checklist 수행 시

### 판정 기준
- **Fail/NG**: 아래 Podo Practice 커버리지 항목 중 하나라도 불일치 → 출력 금지, 재작성 필수
- **OK**: 전체 통과

---

## 01. Podo — [Words] ↔ [Practice] 커버리지 (필수 · REQ-004)

**적용**: Podo 모드 산출물. ## [Practice] Word Table이 ## [Words]의 모든 단어·표현을 1:1(항목당 1문장)로 커버하는지 검증한다.

### 01.0 [Words] 추출 범위 검증 (WO 260223 v1.3 · 재발 방지)

- [ ] **전체 주차 원문 기반** WordsSet 생성 여부 확인 (단어 학습 리스트만이 아닌 문법/대화/패턴/연습/체크리스트 통합)
- [ ] **Grammar/Conversation** 영역 어휘 누락 여부 확인
- [ ] **Source Vocabulary vs WordsSet** 비교 완료 (주간 통합 기준 충족)

### 01.1 Words 집합 정의 (WO 260223)
- [ ] **WordsSet**: ## [Words]에 등재된 **모든 항목**(명사·동사·형용사·부사·감탄사·**구동사**·표현)을 집합으로 정의했는가
- [ ] **구동사**(turn off, go back 등), **숙어·패턴 표현**(I can ~, do ~ a favor 등)도 WordsSet에 포함하는가 (1:1 Gate 적용 대상)

### 01.2 Practice 집합 및 누락 검출
- [ ] **PracticeSet**: Word Table에 등장하는 단어·표현 집합을 추출했는가
- [ ] **Missing** = WordsSet − PracticeSet 을 계산했는가
- [ ] **Missing = ∅** (누락 단어 0개)인가
- [ ] **구동사·표현 항목** 누락 0건인가 (WO 260223)

### 01.3 단어당 문장 수 및 인덱스
- [ ] ## [Words] 총 항목 수 = N 인가
- [ ] ## [Practice] Word Table 총 행 수 = **N** 인가 (1:1 대응)
- [ ] 각 단어·표현별로 정확히 **1문장(1행)**이 있는가 ("이하 동일" 등 생략·대체 없음)
- [ ] **인덱스 중복** 없음 (WO 260223)

### 01.4 완료 선언 문구 조건 (REQ-003)
- [ ] "모든 단어 반영 완료" 등 **완료 선언 문구**는 **Missing=0이 확인된 경우에만** 사용했는가
- [ ] 검증 없이 완료 문구만 기재하지 않았는가

**판정**:
- Missing ≠ ∅ → **NG** (출력 금지, 누락 목록 명시 후 재작성)
- N ≠ Word Table 행 수 → **NG**
- 완료 문구만 있고 Missing 검증 없음 → **NG**

---

## 02. Podo — 기타 출력 검증

- [ ] 단일 코드 블록으로 감싸져 있는가
- [ ] [Words] 뿌리 이미지(아이콘) 누락 0건인가
- [ ] [Conversation]이 사용자 제공 대화 **원문 그대로**인가 (오타·문법 수정 금지)
- [ ] 입력에 사용자 오류 문장이 있으면 [Practice] User Table에 반드시 포함했는가
- [ ] 사용자 오류 문장이 Word Table 예문으로 **통합 처리되지 않았는가** (User Table에만 반영, "통합 처리" 선언으로 제외 금지)

---

## 03. Grammar 모드 (해당 시)

- [ ] [Concept], [Why], [Form], [Examples] 섹션 존재
- [ ] 예문 1~5개, 교재/사용자 입력 기반만
- [ ] 단일 코드 블록, 코드 블록 외 텍스트 없음

---

## 04. DoD 요약 (Work Order 260223 기준)

- **DoD-001**: ## [Words]에 등재된 N개 항목이 ## [Practice] Word Table에 **모두** 등장한다.
- **DoD-002**: 각 항목별 문장 수가 정확히 **1개**다 (1:1 대응).
- **DoD-003**: 누락 단어가 **0개**일 때만 완료 선언 문구 사용.
- **DoD-004**: 입력 원문 단어 목록이 [Words]에 누락 없이 반영되도록(또는 누락 허용 규칙이 명문화된 경우 그에 따름) 일관되게 동작한다.
