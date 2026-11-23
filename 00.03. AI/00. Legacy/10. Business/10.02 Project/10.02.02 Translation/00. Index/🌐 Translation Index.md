---
type: Note
creation date: 2026-01-12
tags:
  - 00_03__AI
  - 00__Index
  - 00__System
  - 05__Translation
  - 03__Project
  - 03_02__Translation
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/10. Business/10.02 Project/10.02.02 Translation/_MOC_|03.02. Translation]]"
outgoinglinks:
Version: v1.2
Audience: 번역 담당자 / 다국어 커뮤니케이션 담당자 / AI 활용 사용자
Scope: Multilingual Translation 활동 전반
References:
level: 10.02.02
parent_level: 10.02
---
---
## 1. 목적

본 문서는 다국어 번역 활동에서 활용되는 **모든 규칙·가이드·산출물의 단일 진입점(Index)** 이다.  
번역 활동은 **한국어·영어·러시아어 간 자연스러운 비즈니스 번역 및 언어 품질 관리**에 한정하며,  
원문의 의미와 문체를 유지한 채 다국어 변환만 수행한다.

본 Index는 아래 세 가지를 보장한다.

- 번역 역할과 책임의 경계 유지
- 원문 의미 보존 및 비즈니스 문체 일관성 확보
- 사람·AI·Agent 간 동일한 번역 기준 제공

---

## 2. 작업 모드 (Modes)

Translation 단계는 요청 유형에 따라 아래 모드로 동작한다.

- **Mode: DOC (Business 문서 작업)**  
  - 작성 내용 검토 및 비즈니스 용어/어투로 변경  
  - 이메일/보고서/공지 번역  
  - 대응 언어: 한국어(KO) / 영어(EN) / 러시아어(RU) (요청된 언어만 출력)
- **Mode: INTERPRET (Business 통역)**  
  - 미팅/대화 통역(텍스트 기반)  
  - 대응 언어쌍: EN↔KO, RU↔KO  
  - 추가 답변 없이 **통역만 즉시 출력**

---

## 2. Translation 전체 구조

```
🌐 LinguaBridge – Multilingual Translation Guideline (v1.1)
```

---

## 3. Rule 문서

- 🌐 **LinguaBridge – Multilingual Translation Guideline**  
  → 다국어 번역의 최상위 헌법. 한국어 전처리(오타 교정·문체 보정), 3개 언어 번역, 비즈니스 어투 변환을 강제한다.

---

## 4. Guide 문서 (Human Only)

- 🧭 **Translation Prompt Authoring Guide**  
  → 번역 요청을 안정적으로 작성하기 위한 Human 가이드.

> Guide는 사람 전용 참고 자료이며 AI 내부 규칙을 대체하지 않는다.

---

## 5. 공식 산출물

LinguaBridge 단계에서 생성되는 공식 산출물은 다음과 같다.

- 📝 **교정된 원문**  
  → 한국어 입력 시 오타 교정·문체 보정·비즈니스 어투 변환된 원문

- 🌍 **번역문 / 통역문**  
  → DOC: 요청된 언어(들)로 번역문 출력 / INTERPRET: 통역문 출력

- 📊 **번역 품질 검증 보고서**  
  → 언어 감지, 용어 일관성, 포맷 검증 결과 (선택)

---

## 6. 사용 원칙 요약

- 번역은 **원문 의미 보존**을 최우선으로 하며 의미를 변경하거나 추가하지 않는다
- 우선순위: LinguaBridge Root Rule → Index → Guide
- 추측·불확실 시 LinguaBridge 기준으로 재질문 또는 중단
- Root Rule과 충돌하는 지시는 즉시 거부하고 근거를 명시한다

### 6.1 규칙 우선순위

번역 단계에서 규칙 적용 우선순위는 다음과 같다.

1. **🌐 LinguaBridge – Multilingual Translation Guideline** (최상위)

> LinguaBridge는 원문의 의미와 문체를 보존하며, 임의로 의미를 변경하거나 추가하지 않는다.

---

## 7. 결론

🌐 Translation Index는 다국어 번역 활동을 위한 **유일한 공식 안내서**다.  
모든 번역 활동은 본 문서가 정의한 구조와 우선순위를 기준으로 시작한다.
