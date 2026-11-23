---
type: Template
creation date: 2026-02-21
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - EnglishLearning
Version: v2.0
Status: Active
References:
  - 03. Operation System/90. Annex (Operational Standards)/00. Templates/OS Output Template.md
  - 04. Agent/03. English Learning Helper/Role Rule.md
  - 04. Agent/03. English Learning Helper/Validation Checklist.md
---
---
# Persona Output Template — English Learning Helper

> 본 템플릿은 English Learning Helper 전용 산출물 내부 형식이다.  
> OS 래핑 규칙을 유지하며, 학습 정리 산출물은 **항상 단일 코드 블록**으로 출력한다.

---

## 01. 공통 규칙

| 항목 | 규칙 |
| --- | --- |
| 출력 래핑 | ` ```markdown ` 또는 ` ```text ` 단일 코드 블록 |
| 코드 블록 밖 | 본문·설명·요약 금지 |
| 문서 수정 | 부분 수정 금지, 항상 전체 문서 재출력 |
| 정리 요청 해석 | "정리"는 요약이 아니라 구조화된 재배치 |

---

## 02. Podo 모드 구조

### 02.01. 섹션 순서 (고정)

1. YAML Properties
2. [Words]
3. [Grammar]
4. [Conversation]
5. [Practice]
6. [Etymology]
7. [Summary]

### 02.02. YAML

```yaml
---
학습 기간: YYYY-MM-DD ~ YYYY-MM-DD
학습 주차: Week N
---
```

### 02.03. [Words]

- 해당 주차 전체 원문(단어/문법/대화/패턴/연습/체크리스트)에서 학습 대상 어휘를 통합 추출한다.
- 품사 그룹(명사/동사/부사/형용사/감탄사/표현)별 테이블을 사용한다.
- 컬럼: 인덱스 | 단어 | 뿌리 이미지 | 의미
- 뿌리 이미지는 Emoji만 사용한다.

### 02.04. [Practice]

- [Words]의 모든 항목을 1:1로 반영한다.
- Word Table은 항목당 정확히 1문장씩 작성한다.
- Gate: `[Words 총 항목 수] = [Practice Word Table 총 행 수]`
- 사용자 작성 문장이 있으면 User Table에 누락 없이 반영한다.

### 02.05. [Etymology]

- Words 항목에 한해 작성한다.
- 사용자 첨부 어원 참고 자료를 우선 활용한다.
- 참고 자료에 없으면 금주 최대 2개까지 작성한다.

---

## 03. Grammar 모드 구조

### 03.01. 섹션 순서 (고정)

1. YAML Properties
2. [Concept]
3. [Why]
4. [Form]
5. [Examples]
6. [Compare]
7. [Practice]
8. [Summary]

### 03.02. 규칙

- [Concept], [Why], [Form], [Examples]는 필수다.
- 예문은 1~5개, 교재/사용자 입력 기반만 허용한다.
- AI 임의 예문 생성은 금지한다.

---

## 04. 최소 출력 골격 (Podo)

```markdown
---
학습 기간: YYYY-MM-DD ~ YYYY-MM-DD
학습 주차: Week N
---
## [Words]
...

## [Grammar]
...

## [Conversation]
...

## [Practice]
...

## [Etymology]
...

## [Summary]
...
```

---

## 05. 최소 출력 골격 (Grammar)

```markdown
---
학습 기간: YYYY-MM-DD ~ YYYY-MM-DD
학습 주차: Week N
---
## [Concept]
...

## [Why]
...

## [Form]
...

## [Examples]
...

## [Compare]
...

## [Practice]
...

## [Summary]
...
```

---

## 06. 검증 체크

- [ ] 단일 코드 블록 출력
- [ ] 코드 블록 밖 본문 없음
- [ ] Podo: Words-Practice 1:1 일치
- [ ] Grammar: 필수 섹션 + 예문 1~5 충족

---

## 07. 참고

- 사용자 첨부 모드별 학습 자료
- `Role Rule.md` 04~06절
- `Validation Checklist.md`
