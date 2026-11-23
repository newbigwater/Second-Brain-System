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
# Footnote Auto Checklist (OS 정본)

> 본 체크리스트는 Footnote 표기 규칙을 자동/수동으로 검증하기 위한 기준이다.
> (정리/EDU 성격 출력물에 한해 적용)

## 01. 기본 원칙 검증

- [ ] Footnote는 “전문 용어·약어 정의 목적”과 “문장 의미 설명 목적”으로 명확히 구분되었는가
- [ ] 용어 정의 목적 Footnote가 문장 끝에 사용되지 않았는가
  - 잘못된 예: **수주생산(주문생산)**은 고객의 주문을 받은 이후에 제품을 생산하는 방식이다[^1].
  - 올바른 예: **수주생산(주문생산)[^1]** 은 고객의 주문을 받은 이후에 제품을 생산하는 방식이다.
- [ ] 동일 용어에 대해 Footnote가 최초 1회만 사용되었는가

## 02. 용어 정의 Footnote 검증 (필수)

- [ ] 전문 용어 또는 약어가 등장하는가
- [ ] 해당 용어에 Footnote 정의가 존재하는가
- [ ] Footnote 라벨 한 줄(`[^n]:`) 뒤에 **굵은 용어**가 기재되어 있는가 (빈칸 금지). 예: `[^1]: **통합된 데이터(Integrated data)**` (Obsidian 호환 형식)
- [ ] Footnote가 용어 토큰 바로 뒤에 위치하는가 (예: KPI[^1], MES[^2])
- [ ] 괄호가 있는 경우에도 약어 문자에 직접 부착되었는가
  - 허용: 성과지표 KPI[^1], 성과지표(KPI[^1])
  - 금지: 성과지표(KPI)[^1]
- [ ] (해당 시) Bold 강조된 용어 뒤에 조사/어미가 오는 경우 Bold 종료 후 공백 1칸이 존재하는가
  - 허용: **페이지랭크(PageRank) 알고리즘[^2]** 을 통해 …
  - 금지: **페이지랭크(PageRank) 알고리즘[^2]**을 통해 …

## 02-A. 3요소 구조 검증 (정리 요청 시 · Obsidian 호환 형식)

**적용 대상**: 정리 요청, 학습 정리(StudyNote), EDU 성격 출력물. 형식: OS-ART-015 To-Be.

- [ ] `[^n]:` 뒤에 **굵은 용어**(예: `**통합된 데이터(Integrated data)**`)가 같은 줄에 있는가 (빈칸 금지)
- [ ] Footnote에 **정의(Definition)** 가 포함되는가
  - 라벨 다음 줄부터 탭 들여쓰기된 **서술형 문단**으로 용어 정의(또는 약어 풀어쓰기)가 있는가
- [ ] Footnote에 **Scope (적용 범위)** 가 포함되는가
  - 들여쓰기된 `- **Scope**:` 불릿이 있거나, 정의 문단 내에 적용 범위·맥락이 있는가
- [ ] (해당 시) **Exclusion/Caution** 이 있으면 가산. 없어도 PASS 가능

**판정**:
- 정의 문단 + Scope 존재: PASS
- 정의 문단 누락 또는 라벨 빈칸: NG
- Scope 없음: 경고 (필수 권장)
- 정의와 Scope 모두 없음: NG

## 03. 혼합 표현 검증 (한글 + 약어)

- [ ] ‘한글 + 약어’ 구조가 최초 등장 시 사용되었는가
- [ ] Footnote가 약어(KPI) 토큰에 부착되었는가
- [ ] 한글 명칭 또는 괄호 전체에 Footnote가 달리지 않았는가

## 04. 문장 의미 설명 Footnote 검증 (제한적 허용)

- [ ] Footnote가 문장 전체 의미 보충 목적에 해당하는가
- [ ] 정책·배경·보충 설명 성격인가
- [ ] 용어 정의 목적이 아닌 것이 명확한가
- [ ] 이 경우에만 문장 끝 Footnote가 사용되었는가

## 05. 금지 패턴 자동 탐지 항목

다음 패턴이 존재할 경우 규칙 위반이다.

- [ ] ❌ `[^n]:` 라벨 한 줄이 빈칸(용어·풀 단어 없음)
- [ ] ❌ 용어 정의 Footnote가 문장 끝에 위치
- [ ] ❌ 괄호 전체에 Footnote 부착
- [ ] ❌ 하나의 용어 토큰에 복수 Footnote 연속 부착 (예: **구글 검색 서비스[^1][^2]**)
- [ ] ❌ 동일 용어에 Footnote 반복 사용
- [ ] ❌ 용어 정의 없이 문장 의미 Footnote만 존재

## 06. 최종 판정

- [ ] 모든 필수 항목을 충족함
- [ ] 위반 항목 없음
- [ ] Footnote 규칙 준수 판정(PASS)

## 07. 자동화 적용 권장 지점

- LLM 출력 후 Self-Check 단계
- Cursor/Agent Output Validator
- PRD/SRS/StudyNote 문서 리뷰 체크리스트

