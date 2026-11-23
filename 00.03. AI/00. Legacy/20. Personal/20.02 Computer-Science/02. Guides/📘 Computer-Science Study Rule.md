---
type: Note
creation date: 2026-02-03 09:26
tags:
  - 00__System
  - 00_03__AI
  - 07__Application
  - 02__Computer_Science
  - 04__Application
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/20. Personal/20.02 Computer-Science/_MOC_|02. Computer-Science]]"
outgoinglinks:
Version: v1.1 - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
References:
  - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
level: 20.02
---
---
# 📘 Computer-Science Study Rule

Version: v1.0  
Scope: Computer-Science 학습 정리 전용 (시험·개념·비교 중심)  
Applies To: 빅데이터분석기사, 정보처리기사, 컴퓨터과학 전반 학습 정리

---

## 0. 선언 (Declaration)

본 문서는 **Computer-Science 프로젝트 내 학습 정리 전용 규칙(Study Rule)** 이다.  
본 규칙은 AI의 사고 방식이나 운영 규칙을 정의하지 않으며,  
**학습 내용을 “어떻게 정리하고 기록할 것인가”만을 규정**한다.

- 본 문서는 🧠 Common Rule, Computer-Science Custom Instructions를 **대체하지 않는다**
- 충돌 시 항상 🧠 Common Rule이 최상위 기준이다

### ※상위 표준(필수 참조)

Computer-Science 학습 정리는 기본적으로 **EDU/Study 산출물**이며,  
Markdown/Footnote/Tag 표준은 `@01. Core/00. Charter`의 아래 문서를 **상위 표준**으로 따른다.

- [🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)Rulebook.md)
  - 문서 첫 줄 `#Tag` 규칙
  - Footnote **용어 토큰 바로 뒤 직접 매핑** 규칙
  - Bold 용어 뒤 **공백 1칸** 규칙 (예: `**용어[^1]** 을`)

---

## 1. 학습 정리의 기본 목표

Computer-Science 학습 정리는 다음 목적을 가진다.

- 시험 대비에 유효한 **개념 중심 정리**
- 단순 설명이 아닌 **구분·비교·판별이 가능한 구조**
- “아는 것”이 아니라 **문제에서 고를 수 있는 상태** 달성
- Obsidian 기반 **장기 누적·재사용 가능 문서** 생성

---

## 2. 학습 정리의 기본 단위 (Atomic Unit)

모든 학습 정리는 아래 **4요소 단위**를 기본으로 구성한다.

- 개념(Concept)
- 목적(Purpose)
- 특징(Characteristics)
- 구분 기준(Discriminator)

> 하나의 항목이 위 요소 중 2개 이상을 포함하지 못하면  
> 학습 정리로 간주하지 않는다.

---

## 3. 분류 우선 원칙 (Classification-First Rule)

### 3.1. 설명보다 분류가 우선이다

- “무엇인가?” 설명 전에 반드시 다음을 먼저 정리한다.
	- 어디에 속하는가
	- 무엇과 구분되는가
	- 어떤 범주에서 선택되는가

### 3.2. 단독 설명 금지

다음 형태는 **학습 정리로 불충분**하다.

- 단일 개념 설명만 존재
- 맥락 없는 정의 나열
- 비교 대상 없는 특징 서술

---

## 4. 비교·대조 강제 규칙 (Comparison Rule)

### 4.1. 비교 트리거

아래 표현이 등장하면 **비교 정리 필수**다.

- ~와 / ~과
- vs
- ~형 / ~기반
- 중앙집중 / 분산
- Online / Offline
- Transaction / Analysis

### 4.2. 비교 최소 단위

비교 시 반드시 다음 항목을 포함한다.

- 목적 차이
- 처리 대상 차이
- 사용 맥락 차이
- 시험에서의 선택 기준

---

## 5. 시험 트리거 연결 규칙 (Exam-Oriented Rule)

모든 학습 항목은 다음 중 **하나 이상**과 연결되어야 한다.

- 자주 출제되는 키워드
- 오답 유도 포인트
- 선택지에서 헷갈리는 지점
- “이 개념이 나오면 무엇을 고르는가”

> 시험과 연결되지 않는 정리는  
> “지식 설명”이지 “학습 정리”가 아니다.

---

## 6. 범위 고정 원칙 (Scope Fixing Rule)

- 학습 정리는 **교재·기출·입력 자료 범위 내**에서만 수행한다
- 입력에 없는 개념 확장, 배경 이론 추가를 금지한다
- “도움이 될 것 같아서” 추가하는 설명은 허용되지 않는다

---

## 7. 요약·압축 규칙 (Compression Rule)

### 7.1. 문장 길이 제한

- 한 Bullet은 **1~2문장**을 초과하지 않는다
- 장문 설명은 분해하여 Bullet로 재구성한다

### 7.2. 서술 금지 패턴

다음 표현은 학습 정리에서 제한한다.

- 일반적인 설명체 문단
- 교과서 문장 그대로 복사
- 문맥 의존적 서술(“앞에서 설명한 것처럼…”)

---

## 8. 용어·약어 정의 책임 (Terminology Rule)

- 전문 용어, 약어, 시험 개념은 **정의 책임이 발생**한다
- 정의는 Footnote 또는 명시적 정의 블록으로 고정한다
- “많이 쓰이는 말”이라는 이유로 정의를 생략할 수 없다

---

## 9. 출력 형식 원칙 (Output Form)

### 9.1. 기본 형식

- 출력은 **Markdown 기반 학습 노트**를 전제로 한다
- 헤더 구조는 사용자가 설계하고,  
  AI는 **본문만 정확히 채운다**

### 9.2. 구조 안정성

- 헤더 임의 생성 금지
- 순서 재배치 금지
- 요약으로 입력 내용을 대체 금지

---

## 10. 학습 정리 판정 기준 (Self-Check)

학습 정리 완료 전, 다음 질문에 모두 Yes여야 한다.

- 이 개념을 시험 보기 직전에 읽어도 선택이 가능한가?
- 비슷한 개념과 헷갈리지 않게 구분 기준이 있는가?
- 설명 없이 Bullet만 봐도 의미가 고정되는가?
- 입력 자료의 모든 핵심 항목이 반영되었는가?

하나라도 No라면 **학습 정리 미완성**이다.

---

## 11. 적용 범위 명시

본 Study Rule은 다음 작업에 적용된다.

- 내용 정리 요청
- 기출 기반 개념 정리
- 이미지·슬라이드 기반 학습 정리
- 빅데이터분석기사 / 정보처리기사 이론 정리

본 규칙은 설계 문서(SRS/SDS/SCS),  
코드 생성, 아이디어 발산에는 적용되지 않는다.

---

## 12. 종료 선언

Computer-Science 학습 정리는  
“많이 아는 것”이 아니라  
**“구분해서 고를 수 있는 상태”를 만드는 작업**이다.

본 Study Rule은  
그 상태를 **일관되게 재현하기 위한 최소 규칙 집합**이다.
