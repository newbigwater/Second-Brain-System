---
type: Note
creation date: 2026-01-30 11:31
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 03__Operations
  - 01__Execution_Gate
  - 01__Core
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/00. Charter/01. Execution Gate/_MOC_|01. Execution Gate]]"
outgoinglinks:
Version: v1.1
References:
level: 0
---
---
# Output Validation Checklist

## 01. Purpose

본 문서는 AI 출력 결과가 규칙을 충족했는지 **객관적으로 검증**하기 위한 체크리스트다.  
Evaluator는 본 체크리스트를 기준으로만 판정한다.

---

## 02. Pre-Validation Check

-  요청 유형이 명확히 식별되었는가
    
-  혼합 입력 여부를 사전에 차단했는가
    

---

## 03. Input Coverage Check

-  입력 항목 총 개수가 명시되었는가
    
-  처리 완료 항목 개수가 일치하는가
    
-  미처리 항목이 있는 경우 명시되었는가
    

---

## 04. Content Integrity Check

-  입력의 모든 제목/소제목이 출력에 반영되었는가
    
-  목록/예시/표가 누락되지 않았는가
    
-  요약이나 추정으로 대체된 내용은 없는가
    

---

## 05. Traceability Check (해당 시)

-  입력–출력 매핑 표가 존재하는가
    
-  모든 출력 요소가 입력과 매핑되는가
    
-  추적 불가 항목이 명시되었는가
    

---

## 06. Format & Rule Check

-  Markdown 규칙을 준수했는가
    
-  금지된 형식(Canvas, HTML 등)을 사용하지 않았는가
    
-  StudyNote 규칙(해당 시)을 준수했는가
    
-  (정리/EDU 문서 해당 시) 문서 첫 줄에 Tag 라인이 존재하는가 (예: `#Tag: ...` 또는 `#TagName ...`)
-  (해당 시) Stage/Project Organizer Contract(정리 요청 전용 Output Contract)의 템플릿/형식을 준수했는가
    

---

## 07. Final Decision

-  모든 항목 통과 → **OK**
    
-  일부 항목 미통과 → **NG**
    
-  Root Rule 위반 → **Fail**
    

---

## 08. Execution Gate

- 본 체크리스트는 03.Operations 영역의 공식 검증 도구다.
    
- 판정 결과는 NG / Fail Classification 문서를 따른다.