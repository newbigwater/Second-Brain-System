---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Annex
Version: v1.0
Status: Active
RuleNamespace: OS-OPS
References: []
---
---
# 🏷️ Tag & Metadata Governance (OS 정본)

## Purpose

- Obsidian/Markdown 기반 지식관리에서 태그(`tags:`)와 메타데이터(frontmatter)를 운영 표준으로 고정한다.
- 목표:
  - 드리프트 방지
  - 호환성 유지(legacy 유지)
  - 운영 자동화

## Scope

- 대상: 레포 내 모든 Markdown 문서의 YAML frontmatter
- 제외: `99. Backup`

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

규칙: 문서는 최소 1개 이상의 Layer Tag를 가져야 한다.

### 2) Legacy Tags (병행 유지, 삭제 금지)

- 과거 트리/명명 기반 태그(예: `01__SRS`, `04__PM`, `05__Translation`)는 삭제하지 않는다.
- 정책: 추가(Additive) 방식만 허용한다.

## Frontmatter 운영 규칙

- `tags:`는 YAML list 형태를 사용한다.

```text
tags:
  - 02__Business
  - 02_01__SRS
  - 01__SRS   # legacy (존치)
```

- 태그는 “문서의 소속(레이어/스테이지)” 같은 안정적인 분류만 담는다.
- 세부 내용/주제 키워드는 본문 `#Tag:` 또는 제목/섹션으로 관리한다.

## 풋노트 기반 Tag 출력 형식 (정리·EDU)

- **내용 정리 산출물은 YAML frontmatter를 사용하지 않는다.** 문서는 #Tag 한 줄로만 시작한다.
- 문서 **첫 줄**에 풋노트에서 추출한 용어를 **각각** `#TagName` 또는 `$TagName`(구동사 등) 형태로, **띄어쓰기로 한 줄**에 나열한다. (개행하지 않는다.) **금지**: `#Tag: word1 word2` 형태.
- 둘째 줄은 빈 줄, 셋째 줄부터 본문 헤더(`# 1. ...`)로 이어진다.
- 상세: 정리·EDU 산출물 기본 규칙 06. 풋노트 기반 Tag 자동 생성 규칙.

## Query/Filter 권장 방식 (Obsidian)

- 신규 쿼리는 Layer Tags 기반으로 작성한다.
  - 예: `tag:#02__Business AND tag:#02_01__SRS`
- 기존 쿼리(legacy)는 유지하되 점진적으로 교체한다.

## Deprecation (제거) 정책

- 즉시 제거 금지(최소 1개 운영 주기 병행).
- 제거 조건:
  - 레포 전역에서 legacy 태그 기반 사용처가 없음을 확인
  - README/가이드 문서가 신규 체계만 참조하도록 정리 완료
- 제거 실행 시:
  - 제거 대상 태그 목록을 변경 로그에 기록
  - 자동화로 일괄 제거 후 link/format 검증

## Maintenance Workflow (운영 절차)

- 폴더 구조 이동/리네이밍 후:
  - 태그 정규화: `workspace/tools/archive/tag_normalize.py`
  - 링크 검증: `workspace/tools/link_check.py`
