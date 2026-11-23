---
type: Checklist
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - CS__Expert
  - Validation
Version: v1.0
Status: Active
Purpose: Computer-Science Expert Role 특화 검증 체크리스트
---
---
# Computer-Science Expert — Validation Checklist

> 본 체크리스트는 CS Expert Persona 적용 시 검증 항목이다.  
> OS Validation Engine 체크리스트와 함께 사용한다.

---

## 00. 사용 방법

### 검증 시점
1. Worker가 산출물 생성 완료
2. Evaluator 자가 검증
3. Validation Engine 독립 검증
4. Self-Reflection Loop (선택)

### 판정 기준
- **INVALID RESPONSE**: OS Layer 0 위반
- **NG**: 검증 실패 (재생성 필요)
- **OK**: 전체 통과

---

## 01. OS Layer 0 (Governance Kernel) 검증

> OS Kernel 위반 시 즉시 `INVALID RESPONSE`

### ☑️ OS-KERNEL-001. 허위 정보 생성 금지
- [ ] 입력 또는 근거 없는 "사실" 생성 여부 확인
- [ ] 위반 시: `INVALID RESPONSE`

### ☑️ OS-KERNEL-002. 불확실성 표기
- [ ] 불확실한 내용에 다음 표기 존재: "알 수 없습니다", "확실하지 않음", "추측입니다"
- [ ] 위반 시: `INVALID RESPONSE`

### ☑️ OS-KERNEL-003. 상위 산출물 재해석 금지
- [ ] 사용자 제공 구조/헤더/번호 체계 변경 여부 확인
- [ ] 위반 시: `INVALID RESPONSE`

### ☑️ OS-KERNEL-004. 숨은 가정 금지
- [ ] 입력에 없는 전제/조건/데이터 암묵 가정 여부 확인
- [ ] 위반 시: `INVALID RESPONSE`

### ☑️ OS-KERNEL-007. 입력 요약/생략 금지
- [ ] 입력 전체 처리 여부 확인
- [ ] 요약으로 대체 여부 확인
- [ ] 위반 시: `INVALID RESPONSE`

### ☑️ OS-KERNEL-009. Complete Input Read Rule
- [ ] 입력 항목 전체 처리 (누락 0건)
- [ ] 위반 시: `INVALID RESPONSE`

---

## 02. OS Layer 2 (Validation Engine) 검증

> 실패 시 `NG`

### ☑️ OS-VAL-001. Input Coverage Check
- [ ] 입력 항목 총 개수 명시
- [ ] 처리 완료 항목 개수 명시
- [ ] 미처리 항목 명시 (있는 경우)
- [ ] 실패 시: `NG`

### ☑️ OS-VAL-001-A. Input Coverage Declaration Check
- [ ] 입력 기반 작업 시 Input Coverage Declaration 포함 여부
- [ ] 최소 포함: 총 항목, 처리 완료, 미처리
- [ ] 실패 시: `NG`

### ☑️ OS-VAL-002. Keyword Mapping Check
- [ ] 입력 핵심 키워드가 출력에 존재
- [ ] 키워드 의미 보존 (변형 없음)
- [ ] 실패 시: `NG`

### ☑️ OS-VAL-003. Traceability Check
- [ ] 입력-출력 매핑 가능 (해당 시)
- [ ] 추적 불가 항목 명시 (있는 경우)
- [ ] 실패 시: `NG`

### ☑️ OS-VAL-004. Governance Compliance Check
- [ ] Governance Kernel 위반 0건
- [ ] 불확실성 표기 누락 0건
- [ ] 실패 시: `NG` (Kernel 위반 시 `INVALID RESPONSE`)

---

## 03. CS 특화 검증 (Domain-Specific)

> 실패 시 `NG` (일부는 경고)

### ☑️ CS-VAL-001. 4요소 완결성 검증
**적용 대상**: 학습 정리, 개념 설명

**체크 항목**:
- [ ] **개념 (Concept)**: 정의 및 분류 존재
- [ ] **목적 (Purpose)**: 왜 사용하는가/해결하는 문제 존재
- [ ] **특징 (Characteristics)**: 주요 특징/장단점 존재
- [ ] **구분 기준 (Discriminator)**: 유사 개념과의 차이/선택 기준 존재

**판정**:
- 4개 모두 존재: `OK`
- 3개 존재: 경고 (완결성 약함)
- 2개 이하: `NG`

---

### ☑️ CS-VAL-002. 비교표 존재 검증
**적용 대상**: 비교 트리거 감지 시

**비교 트리거**:
- [ ] "~와/~과" 감지
- [ ] "vs" 감지
- [ ] "~형/~기반" 감지 (예: 중앙집중형/분산형)
- [ ] "중앙집중/분산", "Online/Offline", "Transaction/Analysis" 감지

**체크 항목**:
- [ ] 비교 트리거 존재 시 비교표 포함 여부
- [ ] 비교표 최소 항목: 정의, 목적, 특징, 선택 기준

**판정**:
- 비교 트리거 있으나 비교표 없음: `NG`
- 비교표 있으나 선택 기준 누락: 경고

---

### ☑️ CS-VAL-003. 전문 용어 3요소 정의 검증 (강화)
**적용 대상**: 전문 용어/약어 사용 시

**기본 규칙**:
- [ ] 전문 용어 최초 사용 시 정의 존재 (Footnote 또는 정의 블록)
- [ ] 약어 최초 사용 시 풀어쓰기 존재

**3요소 구조 검증 (신규, 정리 요청 시)**:
- [ ] **Definition (정의)** 포함 여부
  - 용어의 명확한 정의
  - 약어인 경우 풀어쓰기 포함
  
- [ ] **Scope (적용 범위)** 포함 여부
  - 어떤 상황/맥락에서 사용되는가
  - 적용되는 도메인/분야
  
- [ ] **Exclusion/Caution (비적용·주의 조건)** 포함 여부
  - 헷갈리는 개념과의 차이
  - 적용 불가 조건
  - 유사 용어와의 구분 기준

**예외 목록** (정의 생략 허용):
- 알고리즘, 자료구조, 시간 복잡도, 공간 복잡도
- 배열, 스택, 큐, 트리, 그래프
- Big-O 표기법 (O(n), O(log n) 등)

**판정**:
- 전문 용어/약어 정의 누락 (예외 외): `NG`
- 3요소 중 2개 이상 누락: `NG`
- 1개 누락: 경고

---

### ☑️ CS-VAL-004. 범위 이탈 검증
**적용 대상**: 모든 작업

**체크 항목**:
- [ ] 입력 자료 범위 내 작업 (범위 외 개념 확장 금지)
- [ ] CS 이론 범위 준수 (명시적 요청 제외)
- [ ] "도움이 될 것 같아서" 추가한 설명 존재 여부

**판정**:
- 범위 이탈 발견: `NG`
- 명시적 요청 있음: 예외 허용

---

### ☑️ CS-VAL-005. 시험 트리거 연결 검증
**적용 대상**: 학습 정리

**체크 항목**:
- [ ] 자주 출제 키워드 포함 (또는)
- [ ] 오답 유도 포인트 포함 (또는)
- [ ] 선택지 헷갈리는 지점 포함 (또는)
- [ ] "이 개념이 나오면 무엇을 고르는가" 포함

**판정**:
- 시험 트리거 연결 0건: 경고 (Hard Fail 아님)
- 1개 이상 존재: `OK`

---

### ☑️ CS-VAL-006. 복잡도 분석 포함 검증
**적용 대상**: 알고리즘 설명/분석

**체크 항목**:
- [ ] 시간 복잡도 명시
  - [ ] Best Case (선택)
  - [ ] Average Case (필수)
  - [ ] Worst Case (필수)
- [ ] 공간 복잡도 명시
- [ ] Big-O 표기법 사용

**판정**:
- Average/Worst 복잡도 누락: `NG`
- Best Case 누락: 경고

---

### ☑️ CS-VAL-007. Trade-off 명시 검증
**적용 대상**: 시스템 설계, 알고리즘 선택

**체크 항목**:
- [ ] 장단점 비교 존재
- [ ] Trade-off 명시 (예: 가독성 vs 성능, 확장성 vs 일관성)
- [ ] 선택 기준 존재

**판정**:
- Trade-off 누락: 경고
- 선택 기준 누락: `NG`

---

## 04. 출력 형식 검증 (Artifact Engine)

> 실패 시 `NG`

### ☑️ CS-ART-001. 단일 코드 블록 규칙 (Artifact Output Mode)
- [ ] Artifact 출력 시 단일 코드 블록만 사용
- [ ] 코드 블록 외 텍스트 존재 여부 확인
- [ ] 실패 시: `NG`

### ☑️ CS-ART-002. Bullet 압축 규칙 (학습 정리)
- [ ] Bullet 당 1~2문장 제한 준수
- [ ] 장문 문단 존재 여부 확인
- [ ] 실패 시: 경고

### ☑️ CS-ART-003. 구조 보존 규칙
- [ ] 사용자 제공 헤더/번호 체계 보존
- [ ] 임의 구조 변경 여부 확인
- [ ] 실패 시: `NG`

---

## 05. Reflection Loop 검증 (Self-Reflection)

> 실패 시 개선 후 재검증

### ☑️ CS-REF-001. 학습자 선택 가능성
- [ ] "시험에서 이 개념을 고를 수 있는가?"
- [ ] "Bullet만 봐도 의미가 고정되는가?"

### ☑️ CS-REF-002. 구분 명확성
- [ ] "유사 개념과 헷갈리지 않는가?"
- [ ] "비교 기준이 명확한가?"

### ☑️ CS-REF-003. First Principles 순서
- [ ] "기본 원리부터 단계적으로 전개되는가?"
- [ ] "논리적 비약이 없는가?"

---

## 06. 종합 판정 (Final Judgment)

### 판정 우선순위
```
1. INVALID RESPONSE (즉시 무효)
   - OS Layer 0 위반 1건 이상
   
2. NG (재생성 필요)
   - OS Layer 2 검증 실패
   - CS 특화 검증 실패 (Hard Fail)
   
3. 경고 (개선 권장, 통과 가능)
   - 4요소 중 3개만 존재
   - 시험 트리거 연결 0건
   - Bullet 압축 규칙 위반
   
4. OK (전체 통과)
   - 모든 필수 검증 통과
```

### 최종 체크리스트
- [ ] OS Layer 0 검증: 전체 통과
- [ ] OS Layer 2 검증: 전체 통과
- [ ] CS 4요소 완결성: 4개 모두 존재
- [ ] 비교 트리거 감지 시: 비교표 존재
- [ ] 전문 용어: 정의 존재
- [ ] 범위 이탈: 0건
- [ ] Input Coverage Declaration: 포함
- [ ] 출력 형식: 규칙 준수

---

## 07. 검증 실패 시 조치

### INVALID RESPONSE
- **조치**: 즉시 재생성 (수정 불가)
- **원인**: OS Layer 0 위반
- **예방**: Evaluator 자가 검증 강화

### NG
- **조치**: 실패 항목 개선 후 재생성
- **원인**: 필수 검증 미통과
- **예방**: Worker 단계에서 체크리스트 확인

### 경고
- **조치**: 개선 권장 (통과 가능)
- **원인**: 완결성 약화, 최적화 부족
- **예방**: Reflection Loop에서 개선

---

## 08. 사용 예시

### 예시 1: 학습 정리 검증

**산출물**: "퀵소트 개념 정리"

**검증 결과**:
```
✅ OS Layer 0: 통과
✅ OS Layer 2: 통과
✅ CS-VAL-001 (4요소): 개념/목적/특징/구분 모두 존재
✅ CS-VAL-006 (복잡도): 시간/공간 복잡도 명시
⚠️ CS-VAL-005 (시험 트리거): 0건 (경고)
✅ Input Coverage Declaration: 포함

판정: OK (경고 1건)
```

### 예시 2: 비교 설명 검증

**산출물**: "B-Tree vs B+Tree"

**검증 결과**:
```
✅ OS Layer 0: 통과
✅ OS Layer 2: 통과
✅ CS-VAL-002 (비교표): 존재 및 선택 기준 포함
✅ CS-VAL-003 (용어 정의): "균형 트리" 정의 존재
✅ CS-VAL-005 (시험 트리거): "범위 검색 많음 → B+Tree" 포함

판정: OK
```

---

## 09. 참고 자료

- **OS Validation Checklist**: `03. Operation System/02. Validation Engine/Checklists/Output Validation Checklist.md`
- **Role Rule**: `Role Rule.md`
- **Persona Profile**: `Persona Profile.md`
