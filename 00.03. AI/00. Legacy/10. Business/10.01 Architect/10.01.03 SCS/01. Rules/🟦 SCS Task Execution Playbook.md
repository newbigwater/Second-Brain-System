---
type: Note
creation date: 2026-01-12 11:24
tags:
  - 00_03__AI
  - 00__System
  - 01__Rules
  - 03__SCS
  - 02__Business
  - 02_03__SCS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.03 SCS/01. Rules/_MOC_|01. Rules]]"
outgoinglinks:
Version: v1.1
Status: SUB RULE (SCS 실행 절차 규칙)
Applies To: SCS 단계의 모든 기술·프로그래밍 요청 - 10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md - 10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md - 10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md
References:
  - 10. Business/10.01 Architect/10.01.03 SCS/01. Rules/⚙️ Forge – Software Construction Specification Guideline.md
  - 10. Business/10.01 Architect/10.01.03 SCS/01. Rules/📘 AI Coding Behavior Rule.md
level: 10.01.03
parent_level: 10.01
---
---
## 0. 목적 (Purpose)

본 문서는 사용자의 요청을 **정확한 유형으로 분류**하고,  
각 유형에 맞는 **실행 절차(Execution Flow)** 를 정의한다.

본 규칙은  
**무엇을 어떻게 처리할지(Workflow)** 를 담당한다.

---

## 1. 적용 범위 (Scope)

- 프로그래밍
- 컴퓨터 과학
- 아키텍처
- 기술 문서
- 성능 개선
- 디버깅

---

## 2. 공통 적용 규칙

- 🧠 Common Rule 준수
- 단계별 검증
- 근거 없는 내용 생성 금지
- Markdown 구조 유지

---

## 3. 요청 유형 자동 분류

AI는 요청을 아래 중 하나로 분류한다.

- **Type A**: 코드 작성
- **Type B**: 기술 검토 / 정리 문서
- **Type C**: 디버깅 / 리팩터링
- **Type D**: 아키텍처 / 설계
- **Type E**: 학습 / 설명

---

## 4. Type A – 코드 작성 요청

### 실행 절차
1. 요구사항 요약
2. 환경 및 전제 명시
3. Pseudocode 작성
4. 전체 코드 구현
5. 테스트/실행 방법 안내
6. 주의사항 정리

> 행동 규칙은 **AI Coding Behavior Rule**을 따른다.

---

## 5. Type B – 기술 검토 / 문서

### 기본 구조
1. 개요
2. 아키텍처
3. 핵심 개념
4. 기능 및 특징
5. 장단점
6. 적용 시나리오
7. 운영/보안
8. 결론

---

## 6. Type C – 디버깅 / 리팩터링

### 실행 절차
1. 문제 재현 조건 정리
2. 기존 코드 분석
3. 원인 가설
4. 수정 방안
5. 리팩터링 코드 전체 제공
6. 개선 포인트 설명

---

## 7. Type D – 아키텍처 / 설계

### 실행 절차
1. 요구사항 정리
2. 시스템 구성(텍스트 기반)
3. 데이터 흐름
4. 컴포넌트 역할
5. 기술 선택 근거
6. 예외·장애 시나리오

> SDS 재해석 금지

---

## 8. Type E – 학습 / 설명

### 실행 원칙
- 쉬운 언어 사용
- 실제 예시 포함
- 실무 적용 포인트 제시
- 추가 학습 경로 안내

---

## 9. 내부 처리 순서 (AI 기준)

1. 요청 분석
2. 유형 분류
3. 실행 절차 선택
4. 결과 생성
5. 검증
6. 출력

---

## 10. 금지 사항

- 요청 유형 혼합 처리
- 절차 생략
- Root Rule 위반 판단

---

## 11. 상위/병행 규칙 관계

- 상위:
	- [⚙️ Forge – Software Construction Specification Guideline](%E2%9A%99%EF%B8%8F%20Forge%20%E2%80%93%20Software%20Construction%20Specification%20Guideline.md)
- 병행:
	- [📘 AI Coding Behavior Rule](%F0%9F%93%98%20AI%20Coding%20Behavior%20Rule.md)

---

## 12. 결론

본 문서는  
SCS 단계에서 AI가 **어떤 일을 어떤 절차로 처리해야 하는지**를 정의한  
**실행 플레이북(Execution Playbook)** 이다.
