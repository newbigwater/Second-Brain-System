---
type: Domain Knowledge
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - EnglishLearning
Version: v1.0
Status: Active
References: []
---
---
# English Learning Helper — Domain Knowledge

## 00. 목적

본 문서는 English Learning Helper Agent의 **도메인 참고**용이다.  
Podo/Grammar 상세 템플릿·실행 규칙·Gate는 사용자가 **별도 첨부**한 문서를 따라 준수한다.

---

## 01. 모드 요약

| 구분 | Podo | Grammar |
|------|------|---------|
| 용도 | 주간(Week) 학습 정리 | 책 기반 문법 한 주차 정리 |
| 구조 | YAML → Words → Grammar → Conversation → Practice → Etymology → Summary | YAML → Concept → Why → Form → Examples → Compare → Practice → Summary |
| 핵심 Gate | Words×3 = Practice 문장 수, 뿌리 이미지 필수 | 예문 1~5개, 교재/사용자 입력만 |
| 출력 | 단일 코드 블록 | 단일 코드 블록 |

---

## 02. ChatGPT 사용 시 모드별 참고 문서

| 모드 | 참고 PDF | 비고 |
|------|----------|------|
| **Grammar** | 사용자 첨부 문법 교재/PDF | [Concept]/[Why]/[Form]/[Examples] 참고 |
| **Podo** | 사용자 첨부 어원/구동사 학습 자료 | **Etymology 작성 시 어원 자료 필수** |

- **Podo 출력 형식 표준**: `language/Podo/01.Standard/Start2/04. 조동사를 활용한 정보 요청 표현.md` — Podo 출력은 이 문서와 동일한 구조·형식으로 작성.
- **Podo 규칙 정본 (필수)**: Podo 상세 규칙 문서를 사용자가 별도 첨부하여 준수한다.

---

## 03. 공통 원칙

- **정리 요청** = 요약이 아님. 구조 유지·전체 재배치.
- **출력** = 항상 단일 코드 블록. 코드 블록 밖 설명 금지.
- **수정 요청** = 부분 수정 금지. 전체 문서 재출력만.
- **난이도** = 비기너. 현재형·일상 표현·이해 중심. 시험 문법·학술 용어·예외 나열 지양.

(Podo/Grammar 규칙·템플릿·Gate는 사용자가 별도 첨부한 문서로 준수한다.)
