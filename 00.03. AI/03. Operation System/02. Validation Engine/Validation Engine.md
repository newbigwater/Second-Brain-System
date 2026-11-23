---
type: Standard
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
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Violation Policy.md
  - 03. Operation System/02. Validation Engine/Checklists/Output Validation Checklist.md
  - 03. Operation System/02. Validation Engine/Checklists/Footnote Auto Checklist.md
  - 03. Operation System/02. Validation Engine/NG-Fail Policy.md
---
---
# Validation Engine (Layer 2) — 독립 검증

## 00. 목적

본 문서는 Evaluator 이후에 수행되는 **독립 검증 절차**를 표준화한다.

## 01. 검증 원칙

- Layer 0 위반 여부를 최우선으로 판정한다.
- 검증은 “체크리스트 기반”으로 수행하며, 임의 판단을 금지한다.
- 추적 불가능한 항목은 숨기지 않고 `"추적 불가"`로 명시한다.

## 02. 최소 검증 묶음(강제)

### OS-VAL-001. Input Coverage Check

- 입력 항목 총 개수가 명시되었는가
- 처리 완료 항목 개수가 일치하는가
- 미처리 항목이 있는 경우 명시되었는가

### OS-VAL-001-A. Input Coverage Declaration Check

- 입력 기반 작업의 출력에 Input Coverage Declaration이 포함되었는가
- 누락 시 결과는 무효 처리 대상이며 최소 `NG`다.

### OS-VAL-002. Keyword Mapping Check

- 입력의 핵심 키워드가 출력에 존재하는가
- 키워드가 의미가 바뀌지 않도록 보존되었는가

### OS-VAL-003. Traceability Check

- 입력–출력 매핑 표가 존재하는가(해당 시)
- 모든 출력 요소가 입력과 매핑되는가
- 추적 불가 항목이 명시되었는가

### OS-VAL-004. Governance Compliance Check

- `Governance Kernel` 위반이 없는가
- 불확실성 표기 누락/숨은 가정/근거 없는 결론이 없는가

### OS-VAL-FOOT-001. 용어 감지 검증 (정리 요청 시)

**적용 대상**: 정리 요청, 학습 정리(StudyNote), EDU 성격 출력물

- 전문 용어/약어 존재 여부 탐지
  - 영문 대문자 연속 토큰 (예: KPI, RDBMS, HTTP)
  - 괄호 포함 약어 (예: Key Performance Indicator (KPI))
  - 도메인 고유 개념 (예: B-Tree, Reinforcement Learning)
- 전문 용어 존재 시 Footnote 생성 여부 검증
- Footnote 미생성 항목 0건 확인

**판정**:
- 전문 용어 존재하나 Footnote 없음: `NG`

### OS-VAL-FOOT-002. 3요소 구성 검증 (정리 요청 시 · Obsidian 호환 형식)

**적용 대상**: 정리 요청, 학습 정리(StudyNote), EDU 성격 출력물

Footnote가 존재하는 경우 **Obsidian 호환 형식**(OS-ART-015 To-Be) 검증:

- **라벨 + 용어**: `[^n]:` 뒤에 **굵은 용어**(예: `**통합된 데이터(Integrated data)**`)가 같은 줄에 있는가. 빈칸 금지.
- **Definition (정의)**: 라벨 다음 줄부터 탭 들여쓰기된 **서술형 정의 문단**이 있는가. 용어의 명확한 정의(또는 약어 풀어쓰기)를 포함하는가.
- **Scope (적용 범위)**: 들여쓰기된 `- **Scope**:` 불릿이 있거나, 정의 문단 내에 적용 범위·맥락이 포함되어 있는가.
- **Exclusion/Caution (비적용·주의 조건)**: 해당 시 `- **Exclusion/Caution**:` 불릿 또는 문단 내 주의 내용이 있으면 가산. 없어도 PASS 가능.

**판정**:
- 정의 문단 누락 또는 라벨 한 줄 빈칸: `NG`
- Scope 없음: 경고 (필수 권장)
- 정의 + Scope 모두 없음: `NG`
- 1개만 누락(정의 또는 Scope): 경고

### OS-VAL-FOOT-003. 위치 검증

**적용 대상**: 정리 요청, 학습 정리(StudyNote), EDU 성격 출력물

Footnote 위치 규칙 검증:

- Footnote가 용어 토큰 직후 부착 (예: KPI[^1], RDBMS[^2])
- 괄호 전체 부착 금지 확인
  - 허용: 성과지표 KPI[^1], 성과지표(KPI[^1])
  - 금지: 성과지표(KPI)[^1]
- 동일 용어 반복 사용 시 Footnote 중복 금지 (최초 1회만)

**판정**:
- 위치 규칙 위반: `NG`
- 중복 Footnote 사용: `NG`

## 03. 체크리스트(정본)

- Output Validation Checklist: `02. Validation Engine/Checklists/Output Validation Checklist.md`
- Footnote Auto Checklist(해당 시): `02. Validation Engine/Checklists/Footnote Auto Checklist.md`

## 04. 판정 규칙(강제)

- Kernel 위반: `INVALID RESPONSE`
- 그 외 검증 실패:
  - 치명적(재출력 불가) 기준 충족 시 `Fail`
  - 그 외 `NG`
- 전 항목 통과: `OK`

판정의 정의/우선순위는 `00. Governance Kernel/Violation Policy.md`를 따른다.

