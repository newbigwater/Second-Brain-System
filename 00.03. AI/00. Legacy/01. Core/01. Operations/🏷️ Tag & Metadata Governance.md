---
type: Note
creation date: 2026-02-09
tags:
  - 00__System
  - 00_03__AI
  - 00__Core
  - 01__Core
  - 03__Operations
backlinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/01. Operations/_MOC_|01. Operations]]"
outgoinglinks:
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/_MOC_|01. Core]]"
  - "[[00. Second-Brain-System/00.03. AI/00. Legacy/01. Core/01. Operations/Operational Rules|Operational Rules]]"
Version: v1.1
References:
level: 0.01
---
---

## Purpose

- 본 문서는 Obsidian/Markdown 기반 지식관리에서 **태그(`tags:`)와 메타데이터(frontmatter)** 를 운영 표준으로 고정한다.
- 목표는 다음 3가지다.
  - **드리프트 방지**: 폴더 이동/리네이밍 이후에도 검색·쿼리가 깨지지 않게 한다.
  - **호환성 유지**: 기존(legacy) 태그·쿼리와의 호환을 끊지 않는다.
  - **운영 자동화**: 태그/링크 정리 작업을 스크립트로 반복 가능하게 만든다.

---

## Scope

- 대상: 레포 내 모든 Markdown 문서의 YAML frontmatter
- 제외: `99. Backup` (보관/스냅샷 영역)

---

## Tag Taxonomy (정규 체계)

### 1) Layer Tags (필수 권장)

- `01__Core`
- `02__Business`
  - `02_00__Common`
  - `02_01__SRS`
  - `02_02__SDS`
  - `02_03__SCS`
- `03__Project`
  - `03_01__PM`
  - `03_02__Translation`
- `04__Application`

> 규칙: 문서는 최소 1개 이상의 Layer Tag를 가져야 한다.  
> (예: `10. Business/10.01 Architect/10.01.01 SRS/...` 문서라면 `02__Business` + `02_01__SRS`)

### 2) Legacy Tags (병행 유지, 삭제 금지)

- 과거 트리/명명 기반 태그(예: `01__SRS`, `04__PM`, `05__Translation`)는 **삭제하지 않는다**.
- 이유: 기존 Obsidian 쿼리/필터/자동화(템플릿, Dataview 등)를 즉시 깨지지 않게 하기 위함.

> 정책: **추가(Additive) 방식**만 허용.  
> “정리”는 제거가 아니라 “신규 체계 병행 추가”로 수행한다.

---

## Frontmatter 운영 규칙

- `tags:`는 YAML list 형태를 사용한다.

```text
tags:
  - 02__Business
  - 02_01__SRS
  - 01__SRS   # legacy (존치)
```

- 태그는 **의미를 과도하게 담지 않는다**.
  - “문서의 소속(레이어/스테이지)” 같은 안정적인 분류만 태그로 둔다.
  - 세부 내용/주제 키워드(변하기 쉬움)는 본문 `#Tag:`(StudyNote 규칙) 또는 제목/섹션으로 관리한다.

---

## Query/Filter 권장 방식 (Obsidian)

- 신규 쿼리는 Layer Tags 기반으로 작성한다.
  - 예: `tag:#02__Business AND tag:#02_01__SRS`
- 기존 쿼리(legacy)는 유지하되, 점진적으로 신규 쿼리로 교체한다.

---

## Deprecation (제거) 정책

- **즉시 제거 금지**. 최소 1개 릴리즈/분기(운영 주기) 동안 병행한다.
- 제거 조건(둘 다 만족 시에만):
  - (1) 레포 전역에서 legacy 태그 기반 쿼리/자동화 사용처가 없음을 확인
  - (2) README/가이드 문서들이 신규 체계만을 참조하도록 정리 완료
- 제거 실행 시:
  - 제거 대상 태그 목록을 “변경 로그(Operations)”에 기록
  - 자동화 스크립트로 일괄 제거 후 link/format 검증 수행

---

## Maintenance Workflow (운영 절차)

- 폴더 구조 이동/리네이밍 후에는 다음을 실행한다.
  - (아카이브) 태그 정규화: `workspace/tools/archive/tag_normalize.py`
  - 링크 검증: `workspace/tools/link_check.py`

