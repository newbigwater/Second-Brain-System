---
type: Note
creation date: 2026-01-12 11:27
tags:
  - 00_03__AI
  - 00__System
  - 03__Guides
  - 03__SCS
  - 02__Business
  - 02_03__SCS
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.01 Architect/10.01.03 SCS/03. Guides/_MOC_|03. Guides]]"
outgoinglinks:
Version: v1.1
Audience: 사내 구성원 (AI 사용자
Purpose: AI에게 정확하고 효과적으로 요청하기 위한 가이드 - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
References:
  - 01. Core/02. Standards/🖋️ StudyNote Markdown Rulebook.md
level: 10.01.03
parent_level: 10.01
---
---
## 1. 목적

본 문서는 사내 구성원이 AI에게 요청을 작성할 때  
**오해·재작업·품질 저하를 방지**하기 위한 **프롬프트 작성 가이드**이다.

본 문서는 **AI 내부 규칙이 아니며**,  
사람(Human)을 위한 **사용 설명서(Guide)** 이다.

---

## 2. 이 문서를 언제 참고해야 하는가

- AI에게 처음 요청을 작성할 때
- 원하는 결과가 잘 나오지 않을 때
- "어떻게 요청해야 할지" 막막할 때
- 코드 / 설계 / 문서 요청을 명확히 하고 싶을 때

---

## 3. SCS 단계 핵심 원칙

- **SDS 준수**: 설계 범위를 벗어나지 않고 구현만 수행
- **완전성**: TODO, 미구현 코드 금지, 실행 가능한 완전한 코드 제공
- **Traceability**: 모든 구현이 SDS 설계 ID와 연결되어야 함
- **우선순위**: Forge Root Rule → Behavior Rule → Playbook 순으로 적용

### 3.1 출력 모드 판별 규칙 (중요)

요청을 작성하기 전에, 먼저 “원하는 결과 유형”을 아래 우선순위로 판별한다.

```
생성 요청 > 출력 요청 > 내용·용어 정리 요청 > 일반 설명
```

- **생성 요청**: 파일 단위 결과가 필요함(예: `.md`/소스 파일 구조)
- **출력 요청**: 복사/저장 가능한 “Artifact” 형태로 출력(코드 블록 기반)
- **내용·용어 정리 요청**: 기술 문서/EDU 정리(StudyNote 규칙 강제 적용)
- **일반 설명**: 설명 중심(필요한 부분만 코드/표)

### 3.2 StudyNote(정리/EDU) 출력 규칙 (필수 조건으로 명시 권장)

기술 정리/EDU 문서를 Output으로 요구하는 경우, Output/Constraints에 아래 조건을 **명시적으로 포함**하는 것을 권장한다.

- 문서 **첫 줄에 `#Tag`** 등록
- Footnote는 **정의 대상 용어 토큰 바로 뒤**에 직접 매핑(문장 끝/괄호 전체 부착 금지)
- Bold 용어 뒤에는 **공백 1칸** 유지(예: `**용어[^1]** 을`)
- 표준은 `🖋️ StudyNote Markdown Rulebook`을 따른다
  - 참고: [🖋️ StudyNote Markdown Rulebook](🖋️%20StudyNote%20Markdown%20Rulebook.md)Rulebook.md)

---

## 4. 프롬프트 기본 구조 (권장)

아래 5요소를 포함하면 대부분의 요청 품질이 안정된다.

1. **역할(Role)**  
2. **작업(Task)**  
3. **맥락(Context)**  
4. **출력 기대(Output)**  
5. **제약(Constraints)**

### 예시
```
당신은 .NET 백엔드 개발자입니다.
Kafka Consumer 코드를 작성해주세요.
환경은 .NET 7, Confluent.Kafka 라이브러리 사용입니다.
전체 실행 가능한 코드로 제공해주세요.
SDS 범위를 넘어서는 기능 추가는 금지입니다.

코드 외에, 구현 요약을 StudyNote 규칙으로 간단히 함께 제공해주세요.
- 요약 문서 첫 줄에 #Tag를 등록해주세요.
- 전문 용어/약어는 최초 1회 Footnote로 정의하고 용어 토큰 바로 뒤에 [^n]을 직접 부착해주세요.
- Bold 용어 뒤에는 공백 1칸을 유지해주세요. (예: **용어[^1]** 을)
```

---

## 5. 좋은 프롬프트 작성 원칙

### 4.1 역할을 명확히 하라
- “전문가입니다 / 개발자입니다 / 아키텍트입니다” 등

### 4.2 범위를 분명히 하라
- 포함 / 제외 사항을 명시
- “설계는 제외”, “구현만”

### 4.3 환경을 구체화하라
- 언어, 프레임워크, 버전
- 운영 환경, 제약 조건

### 4.4 출력 형태를 지정하라
- 코드 블록
- Markdown 문서
- 파일 단위 산출물

### 4.5 제약 조건을 명시하라
- SDS 범위 준수
- 설계 확장 금지
- 금지 사항 명시

---

## 6. 요청 유형별 작성 예시

### 5.1 코드 작성 요청
```
C# Kafka Producer 코드를 작성해주세요.
.NET 7 기준이며, 전체 실행 가능한 코드로 제공해주세요.

코드 외에 간단한 구현 요약(StudyNote 규칙)을 함께 제공해주세요:
- 첫 줄 #Tag 포함
- 전문 용어/약어 Footnote 직접 매핑
- Bold 용어 뒤 공백 1칸 유지
```

### 5.2 기술 문서 요청
```
Kafka 아키텍처를 기술 검토 문서 형식으로 정리해주세요.
MES 연계 관점에서 설명해주세요.

출력은 StudyNote 규칙을 따르는 정리 문서로 작성해주세요.
- 문서 첫 줄 #Tag 포함
- 전문 용어/약어 Footnote 직접 매핑(용어 토큰 바로 뒤)
- Bold 용어 뒤 공백 1칸 유지
- 마지막에 ## Footnotes 포함
```

### 5.3 설계 요청
```
SDS 기반으로 시스템 구성도를 텍스트로 설명해주세요.
설계 확장은 하지 말아주세요.

출력은 StudyNote 규칙을 따르며, 첫 줄 #Tag를 포함하고, 전문 용어/약어는 Footnote 직접 매핑으로 정의해주세요.
```

---

## 7. 피해야 할 요청 방식

- “대충 만들어줘”
- “알아서 잘 해줘”
- 맥락 없는 단문 요청
- 여러 요청을 한 문장에 혼합

---

## 8. AI 내부 규칙과의 관계

- AI는 **Forge / Behavior / Playbook** 규칙을 따른다
- 본 가이드는 **사람을 위한 문서**이다
- 충돌 시 AI 내부 규칙이 우선된다

---

## 9. 결론

좋은 결과는  
**좋은 요청에서 시작된다.**

본 가이드는  
사내 구성원이 AI를 **도구로 안정적으로 활용**하기 위한  
최소한의 프롬프트 작성 기준이다.
