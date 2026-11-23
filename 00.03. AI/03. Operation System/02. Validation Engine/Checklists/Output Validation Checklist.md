---
type: Checklist
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer2
Version: v1.0
Status: Active
RuleNamespace: OS-VAL
References:
  - 03. Operation System/02. Validation Engine/Validation Engine.md
---
---
# Output Validation Checklist (OS 정본)

## 01. Purpose

본 체크리스트는 AI 출력 결과가 규칙을 충족했는지 **객관적으로 검증**하기 위한 기준이다.  
Evaluator/Validation Engine은 본 체크리스트를 기준으로 판정한다.

## 02. Pre-Validation Check

- [ ] 요청 유형이 명확히 식별되었는가
- [ ] 혼합 입력 여부를 사전에 차단했는가

## 03. Input Coverage Check

- [ ] 입력 항목 총 개수가 명시되었는가
- [ ] 처리 완료 항목 개수가 일치하는가
- [ ] 미처리 항목이 있는 경우 명시되었는가
- [ ] (입력 기반 작업) Input Coverage Declaration이 출력에 포함되었는가

## 04. Content Integrity Check

- [ ] 입력의 모든 제목/소제목이 출력에 반영되었는가
- [ ] 목록/예시/표가 누락되지 않았는가
- [ ] 요약이나 추정으로 대체된 내용은 없는가

## 05. Traceability Check (해당 시)

- [ ] 입력–출력 매핑 표가 존재하는가
- [ ] 모든 출력 요소가 입력과 매핑되는가
- [ ] 추적 불가 항목이 명시되었는가

## 06. Format & Rule Check

- [ ] Markdown 규칙을 준수했는가
- [ ] 금지된 형식(Canvas, HTML 등)을 사용하지 않았는가
- [ ] (Explanation Mode 제외: 산출물 출력/파일 생성/정리 요청 해당 시) 출력이 **단일** 코드 블록으로 감싸져 있는가. 코드 블록 밖에 본문·산출물 내용이 없는가 (OS-ART-012, Output Modes 01-A)
- [ ] (동일 적용 시) 코드 블록 **내부** 본문에 닫는 백틱(```) 한 줄이 없어 블록 조기 종료가 발생하지 않았는가
- [ ] StudyNote 규칙(해당 시)을 준수했는가
- [ ] (정리/EDU 문서 해당 시) 문서 첫 줄에 Tag 라인이 존재하는가. **형식**: 각 용어마다 `#TagName` 또는 `$TagName`(구동사 등)로 접두사 부착. `#Tag: word1 word2` 형태 금지. 예: `#Podo #Start2 #ModalVerb $GO-BACK #TURN-OFF`
- [ ] (정리/EDU 문서 해당 시, 풋노트 존재 시) 풋노트에 등록된 용어·약어가 문서 최상단에 각각 `#TagName` 또는 `$TagName` 형식으로 일괄 등록되었는가 (띄어쓰기 한 줄, 개행 금지). YAML frontmatter 없이 문서 첫 줄이 #Tag 한 줄로 시작하는가 (정리·EDU 산출물 기본 규칙 06절)
- [ ] (정리 요청 해당 시) **출력 래핑**: 단일 코드 블록으로 감싸져 있는가. 정리 전용 구조(#Tag 등)는 코드 블록 **내부**에서만 검증 대상이다.
- [ ] (정리 요청 해당 시, StudyNote Output Mode) 출력이 **단일** 코드 블록(```markdown 또는 ```text)으로 감싸져 있는가 (OS-ART-020, StudyNote Output Contract)
- [ ] (정리 요청 해당 시, StudyNote Output Mode) 코드 블록 **밖**에 설명·요약·부가 텍스트가 없는가
- [ ] (정리 요청 해당 시, StudyNote Output Mode) 코드 블록 **내부** 첫 줄이 #Tag 한 줄(띄어쓰기)로 시작하는가
- [ ] (해당 시) Stage/Project Organizer Contract 또는 StudyNote Output Contract의 템플릿/형식을 준수했는가

## 07. Final Decision

- [ ] 모든 항목 통과 → **OK**
- [ ] 일부 항목 미통과 → **NG**
- [ ] Governance Kernel(Layer 0) 위반 → **INVALID RESPONSE**
- [ ] 치명적 오류(재출력 불가) → **Fail**

## 08. Execution Gate

- 본 체크리스트는 `03. Operation System/02. Validation Engine`의 공식 검증 도구다.
- 판정 정책은 `00. Governance Kernel/Violation Policy.md` 및 `02. Validation Engine/NG-Fail Policy.md`를 따른다.

