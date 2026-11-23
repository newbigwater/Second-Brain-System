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
Version: v1.2
Status: ROOT RULE (최상위 실행 규칙)
Applies To: SCS (Software Construction Specification) 단계 전반
References:
level: 10.01.03
parent_level: 10.01
---
---
## 0. 선언 (Declaration)

본 문서는 **SCS 단계에서 적용되는 최상위 실행 규칙(Root Rule)** 이다.  
SCS 단계에서 수행되는 모든 **코드 구현, 테스트, 빌드, 배포, AI 기반 코드 생성 행위**는  
본 문서를 **절대 우선 규칙**으로 적용한다.

본 문서는 하위 규칙을 **지시·제어**하며,  
하위 규칙은 본 문서를 **재해석·확장·수정할 수 없다**.

---

## 1. 프로젝트 개요 (Project Overview)

**Forge**는  
SRS → SDS를 거쳐 확정된 설계를 기반으로  
실제 **소프트웨어 구현 및 빌드(SCS)** 를 수행하는 실행 프로젝트이다.

Forge의 목적은 다음과 같다.

- 설계(SDS)와 구현(SCS) 간 **일관성 보장**
- AI 기반 코드 생성 시 **품질·안정성·재현성 확보**
- 테스트·빌드·배포까지 포함한 **완결된 구현 체계 수립**

---

## 2. 최상위 적용 원칙 (Root Principles)

### 2.1 Common Rule 우선 적용
- 모든 응답·산출물은 **🧠 Common Rule**을 최상위로 적용한다.
- 근거 없는 내용은 생성하지 않는다.
- 불확실한 경우 반드시 아래 중 하나를 명시한다.
	- 알 수 없습니다
	- 잘 모르겠습니다
	- 확실하지 않음
	- 추측입니다

### 2.2 설계 불가침 원칙 (Design Non-Infringement)
- SCS 단계에서는 **SDS를 재해석·확장·보완·추론하지 않는다**
- 구현은 **SDS에 명시된 범위만 수행**한다
- 설계에 없는 판단은 **금지**한다

---

## 3. 역할 및 책임 (Roles & Responsibilities)

| 역할 | 책임 |
|----|----|
| Developer | 설계 기반 코드 구현, 테스트 수행 |
| Code Reviewer | 코드 품질, 규칙 준수 검증 |
| DevOps Engineer | CI/CD, 빌드·배포 자동화 |
| Architect (Aegis) | SDS–SCS 일치성 검증 |
| **AI Agent (Forge)** | 코드 생성, 테스트 보조, 빌드 검증 |

> AI Agent는 **Developer를 대체하지 않으며**,  
> 본 문서와 하위 규칙을 따르는 **보조 실행 주체**이다.

---

## 4. SCS 산출물 범위 (Deliverables)

Forge 단계에서 생성되는 산출물은 다음과 같다.

- **SCS (Software Construction Specification)**
- Source Code (Complete, Buildable)
- Unit / Integration / System Test Report
- CI/CD Pipeline Configuration
- Deployment / Release Manual

---

## 5. 코드 작성 및 구현 원칙 (Implementation Rules)

### 5.1 구현 절차 (강제 순서)

1. 요구사항 및 SDS 범위 확인  
2. **Pseudocode(의사코드) 작성**  
3. 사용자 또는 승인 주체와 합의  
4. **완전한 코드 구현**
5. 테스트 수행 및 검증

### 5.2 코드 품질 기준

- TODO, 미구현, 빈 코드 **절대 금지**
- 모든 import / dependency 명시
- 가독성·안정성·보안성 균형 유지
- 예외는 예측 가능하고 단순하게 처리
- 실행 불가 코드 제공 금지

---

## 6. 테스트 및 배포 원칙 (Test & Deployment)

- 테스트 순서:
	- Unit → Integration → System
- 테스트 자동화 우선 적용
- 배포 전:
	- 코드 리뷰 필수
	- 빌드 성공 여부 검증 필수
- CI/CD는 **SCS 산출물의 일부**로 간주한다

---

## 7. AI Agent 행동 규칙 (AI Behavior Control)

AI Agent는 다음을 반드시 준수한다.

- 📘 **AI Coding Behavior Rule**을 하위 규칙으로 따른다
- 의사코드 없이 바로 코드 생성 금지
- 추측 기반 구현 금지
- 오류·실행 실패 시 **수정 후 재제공**

AI Agent는 판단 주체가 아니라  
**규칙 기반 실행 도구**이다.

---

## 8. 하위 규칙 체계 (Sub Rules)

본 Root Rule 하위에는 다음 규칙들이 존재한다.

- 📘 AI Coding Behavior Rule
- 🟦 SCS Task Execution Playbook

하위 규칙은:
- 본 문서를 **보완**할 수 있으나
- **우선하거나 충돌할 수 없다**

하위 규칙 간 해석 또는 적용 충돌이 발생할 경우, **AI Agent는 판단을 중단하고 Root Rule 기준 위반으로 즉시 재질문하거나 실행을 중단한다.**

---

## 9. 검증 체크리스트 (Verification Checklist)

| 항목 | 기준 |
|----|----|
| 설계 일치성 | SDS 범위 내 구현 여부 |
| 코드 완성도 | TODO / 누락 없음 |
| 예외 처리 | 모든 경로 정의 |
| 테스트 | Unit / Integration / System |
| 빌드 | 재현 가능 |
| 문서 | Markdown 규칙 준수 |

---

## 10. 절대 금지 사항 (Absolute Prohibitions)

- SDS 재해석 또는 기능 추가
- 추측 기반 코드 생성
- 규칙 충돌 시 임의 판단
- Root Rule 위반(상위 규칙 위반)

---

## 11. 결론

본 문서는  
**SCS 단계에서 단 하나의 기준점(Single Source of Truth)** 이다.

Forge는  
AI와 사람이 함께 작업하더라도  
**설계 무결성·코드 품질·운영 안정성**을 보장하기 위한  
실행 중심 SCS Root Rule이다.
