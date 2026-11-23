---
type: Template
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - Template
Version: v1.0
Status: Active
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/01. Cognitive Engine/Cognitive Engine.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/02. Validation Engine/Validation Engine.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/03. Self-Reflection Loop/Reflection Loop.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/04. Artifact Engine/Artifact Engine.md
---
---
# Role Rule Template (Agent 확장 템플릿)

## 00. Role

- **Role Name**: (예: Document Designer, Translation Specialist)
- **Audience/Domain**: (예: 문서 설계자, 번역 작업)
- **Applies To**: (예: 설계 문서 작성, 번역 작업, 특정 Stage)

---

## 01. OS 상속 선언 (강제)

- 본 Role은 `03. Operation System`(Layer 0~4)을 **전체 상속**한다.
- 본 Role은 OS 규칙을 **약화/무력화/재정의** 할 수 없다.
- 충돌 시 우선순위: **OS Layer 0 > L1 > L2 > L3 > L4 > 본 Role 확장 규칙**

---

## 02. Extension Points (확장 지점)

> 아래는 "추가"만 허용한다. 삭제/완화는 금지.

### 02.01. 추가 제약 (Constraints)

**예시**:
- 용어 금지 목록 (예: 특정 도메인에서 사용 금지 단어)
- 형식 고정 (예: 문서 구조, 헤더 레벨)
- 도메인 정책/컴플라이언스 준수

**작성 가이드**:
- 검증 가능한 제약만 추가
- "더 좋게", "느낌 있게" 같은 감성 기준 금지

---

### 02.02. 추가 검증 (Validation Hooks)

**예시**:
- ROLE-VAL-001: 도메인 체크리스트 항목 존재 검증
- ROLE-VAL-002: 규정 준수 여부 검증
- ROLE-VAL-003: 산출물 품질 게이트 통과 검증

**작성 가이드**:
- 반드시 검증 가능해야 한다 (yes/no 판단 가능)
- 자연어 감성 기준 금지
- 각 검증에 Rule ID 부여

**검증 구조**:
```
ROLE-VAL-###. [검증명]
- Rule: [검증 규칙]
- Enforcement: [위반 시 조치] (예: NG, 경고)
```

---

### 02.03. 추가 산출물 템플릿 (Output Templates)

**예시**:
- 도메인 전용 섹션/표/매핑 포맷
- 의사결정 메모 템플릿
- 주간 회고 템플릿

**작성 가이드**:
- 사용자 제공 구조가 있을 경우 구조 보존이 우선
- 템플릿은 "권장"이지 "강제"가 아님 (명시 요청 시만 강제)

---

### 02.04. 문서 설계/정합성 강화 훅 (선택)

> Role이 "규칙/문서/템플릿 설계" 성격이라면 아래 추가 가능

**추가 제약 예시**:
- 문서 구조/번호 체계/폴더 명명 규칙 변경 시 "변경 전/후 + 영향 범위 + 롤백 가능성" 함께 제시
- 템플릿/체크리스트는 "검증 가능 문장(yes/no)"로만 작성

**추가 검증 예시**:
- 문서 간 정합성:
  - 동일 개념(판정/모드/불변 조건)이 서로 다른 표현으로 중복 정의되지 않았는가
  - 인덱스(`_MOC_.md`)가 최신인가
- 금지 참조:
  - 참조 전용(레거시) 영역의 경로를 OS/Agent 문서에서 참조하지 않는가

---

## 03. Conflict Resolution (충돌 해결)

충돌 시 우선순위:
```
OS Layer 0 > OS Layer 1 > OS Layer 2 > OS Layer 3 > OS Layer 4 > 본 Role 확장 규칙
```

- 본 Role 규칙은 OS를 **약화할 수 없다**
- 다른 Role과 충돌: 명시적 우선순위 정의 필요

---

## 04. DoD (Role 전용 완료 조건)

**예시**:
- [ ] 필수 섹션 존재
- [ ] 키워드/요구사항 매핑 완료
- [ ] 도메인 리스크/예외 조건 명시
- [ ] OS 약화/무력화 시도 0건

**작성 가이드**:
- 검증 가능한 조건만 추가
- 체크리스트 형태로 작성

---

## 05. 사용 예시

### 새 Role 생성 시

**Step 1**: 본 템플릿을 복사
```bash
Copy-Item "00. Template/Role Rule Template.md" `
  "0X. <Role Name>/Role Rule.md"
```

**Step 2**: 필수 항목 채우기
- Role Name, Domain, Applies To
- OS 상속 선언 확인
- Extension Points 정의
- DoD 작성

**Step 3**: 추가 파일 생성 (선택)
- Validation Checklist.md
- Templates.md
- Domain Knowledge.md

**Step 4**: Artifact 생성
- 99. Artifact/ 폴더 생성
- Master Prompt 생성 (자동화 스크립트 사용)

---

## 06. 참고 자료

- **설계 문서**: `01. Doc/01. Design/04. Agent - 설계서.md`
- **OS 설계**: `01. Doc/01. Design/03. Operation System - 설계서.md`
- **Persona Template**: `00. Template/Persona Template.md` (전문가 역할 중심)
- **예시**: `01. Computer-Science Expert/Role Rule.md`
