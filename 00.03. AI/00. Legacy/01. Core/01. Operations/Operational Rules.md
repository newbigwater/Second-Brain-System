---
type: Note
creation date: 2026-01-30 10:26
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 03__Operations
  - 01__Core
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/01. Operations/_MOC_|01. Operations]]"
outgoinglinks:
Version: v1.1
References:
level: 0.01
parent_level: 0
---
---
# 📘 Operational Rules

> 본 문서는 기존 지침(Common Rule, StudyNote Rulebook, Traceability Rules)에 포함되어 있었으나  
> Unified Format 과정에서 의도적으로 제거된 **실무 운영 규칙(Operational Details)** 을 재배치한 문서이다.  
> 본 문서는 Root Contract를 확장하지 않으며, **실행 방법과 판단 기준을 보완**한다.

---

## 00. Governance Index (운영 허브)

- **Tag/메타데이터 운영 표준**
  - `01. Core/01. Operations/🏷️ Tag & Metadata Governance.md`
- **Custom Instructions 등록/첨부 최소 세트(Registration Pack)**
  - `01. Core/01. Operations/📎 Custom Instructions Registration Pack Standard.md`
- **Obsidian wikilink 표시명(display) 스타일**
  - `01. Core/01. Operations/🧷 Link Display Name Style Guide.md`
- **자동 점검(스크립트)**
  - 링크 무결성: `workspace/tools/link_check.py`
  - Master Prompt 생성: `workspace/tools/artifact_master_prompt.py`
  - Master Prompt 검증: `workspace/tools/master_prompt_audit.py`
  - (아카이브) MOC 품질: `workspace/tools/archive/moc_audit.py`
  - (아카이브) 태그 정규화: `workspace/tools/archive/tag_normalize.py`
- **Windows/PowerShell UTF-8 출력 표준(모지바케 방지)**
  - Unicode 경로(한글/Emoji)에서 `git diff`/스크립트 출력이 깨지면 아래를 먼저 실행한다.
    ```
    chcp 65001
    powershell -NoProfile -Command "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8"
    ```

---

## 01. Purpose

- 실무 단계에서 발생하는 판단 공백을 제거한다.
    
- ‘어떻게 해야 하는가(How-to)’를 제공하되,  
    Root Rule(Common Rule)을 수정하거나 약화시키지 않는다.
    

---

## 02. Scope

- 학습 정리(StudyNote)
    
- 문서 정리 / 요약
    
- SRS / SDS / SCS 작성 및 검토
    
- 번역 및 재작성 작업
    

---

## 03. Input Handling Rules

### 03.01. Input Segmentation Rule

- 입력은 다음 단위로 분해하여 처리한다.
    
    - 제목 / 소제목
        
    - 목록(Item)
        
    - 예시(Example)
        
    - 표(Table)
        
    - 주석(Footnote)
        
- 분해된 단위는 **각각 출력에 대응**되어야 한다.
    

---

### 03.02. Mixed Input Detection Rule

- 성격이 다른 입력이 혼합된 경우 즉시 중단한다.
    
- Manager는 아래 중 하나를 사용자에게 요구해야 한다.
    
    1. 작업 목적 선택
        
    2. 입력 분리 요청
        

---

## 04. StudyNote Operational Rules

### 04.01. Practice Handling Rule

- Practice 영역은 입력 단어를 **100% 포함**해야 한다.
    
- 단어 1개당 문장 수·테이블 구조는 지침에서 지정한 형식을 따른다.
    
- 조건 불충족 시 결과는 NG다.
    

---

### 04.02. Footnote Expansion Rule

- 약어·전문용어·교육 개념은 Footnote로 정의한다.
    
- Footnote에는 다음을 포함해야 한다.
    
    - 정의(Definition)
        
    - 적용 범위(Scope)
        
    - 비적용/주의 조건(Exclusion)
        

---

## 05. SRS / SDS / SCS Operational Rules

### 05.01. SRS Handling Rule

- 요구사항은 반드시 단일 의미 단위로 분리한다.
    
- 복합 요구사항은 허용되지 않는다.
    

---

### 05.02. SDS Derivation Rule

- SDS는 SRS 문장을 **재해석하지 않는다**.
    
- 구조 변환만 허용된다.
    

---

### 05.03. SCS Implementation Rule

- 구현 단계에서 신규 판단은 금지된다.
    
- 설계에서 정의된 요소만 코드로 변환한다.
    

---

## 06. Output Validation Rules

### 06.01. Mandatory Self-Check

- Worker는 출력 전에 다음을 자체 확인해야 한다.
    
    - 입력 항목 누락 여부
        
    - 요약 대체 여부
        
    - 추론 포함 여부
        

---

### 06.02. NG / Fail Classification

- NG: 규칙 위반이 있으나 수정 가능
    
- Fail: Root Rule 위반 또는 재출력 불가
    

---

## 07. Relation to Other Rules

- 본 문서는 🧠 Common Rule을 대체하지 않는다.
    
- 충돌 시 🧠 Common Rule이 항상 우선한다.
    
- 본 문서는 🧪 Validation & Examples 문서의 기준이 된다.
    

---

## 08. Execution Gate

- 본 문서 규칙 미준수 시 Evaluator는 즉시 NG 또는 Fail로 판정한다.