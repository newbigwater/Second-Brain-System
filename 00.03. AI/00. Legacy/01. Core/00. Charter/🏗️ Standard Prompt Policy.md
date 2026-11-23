---
Version: v1.1
outgoinglinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/00. Charter/🧠 Common Rule|🧠 Common Rule]]"
References:
  - 01. Core/00. Charter/🧠 Common Rule.md
level: 00.00
---
---
>AI Prompt Design & Usage Guideline 

기본 중요 참고 지침 :[🧠 Common Rule](🧠%20Common%20Rule.md)se)

본 문서는 사내에서 AI(ChatGPT, GPT-계열, 추론 모델 포함)를 활용할 때  
일관된 품질의 결과물을 확보하고,  
환각(Hallucination), 오해, 불필요한 반복 작업을 최소화하기 위해  
표준 프롬프트 작성 규칙을 정의한다.

---

## 02. 적용 범위 (Scope)

- 기획 문서 작성 (PRD, SRS, 보고서)
- 개발 설계 및 코드 생성
- 데이터 분석 및 요약
- 기술 문서 작성
- 사내 자동화 및 AI 업무 보조

---

## 03. 기본 원칙 (Core Principles)

### 03.01. 명확성 (Clarity)
- 모호한 요청 금지
- 추상적 표현 대신 구체적 지시 사용

### 03.02. 재현성 (Reproducibility)
- 동일 프롬프트 → 유사 결과
- 형식·분량·구성 수치화

### 03.03. 검증 가능성 (Verifiability)
- 불확실성 명시
- 확신도 또는 추측 여부 포함

---

## 04. 표준 프롬프트 구조

1. Role  
2. Task  
3. Context  
4. Example  
5. Output  
6. Constraints  
7. Advanced Instructions  

---

## 05. 통합 프롬프트 템플릿

```text
[Role]
너는 [경력/연차]의 [전문 분야]를 담당해온 [직무]이다.

[Task]
다음 작업을 수행하라:
1)
2)
3)

[Context]
- 도메인:
- 대상:
- 문제:
- 참고 정보:

[Output]
- 형식:
- 분량:
- 구성 요소:

[Constraints]
- 분량 제한:
- 금지 사항:
- 스타일 규칙:

[Advanced]
- 최종 결과만 제시
- 불확실성 명시
- 확신도(%) 포함
```

---

## 06. 품질 점검 체크리스트

- Role 구체성
- Task 행동 동사 여부
- Context 적절성
- Output 명세 수치화
- 제약 조건 명시
- 불확실성 처리 포함

---

## 07. 결론

본 정책은 사내 AI 활용의 표준 규범으로 사용한다.

## 08. 연관 Policy 안내

본 표준은 **Common Rule**을 상위 준거로 삼고, 각 Stage 고유 템플릿이나 Traceability 규칙은 해당 Stage 문서에서 별도로 정의한다. Core Charter 문서는 하위 Stage 문서를 직접 참조하지 않으며, 필요한 경우 Stage MOC에서 거슬러 올라와 본 정책을 상속하도록 한다.