---
type: Template
creation date: 2026-02-21
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - OS__Annex
Version: v1.0
Status: Active
References:
  - 03. Operation System/04. Artifact Engine/Artifact Engine.md
  - 03. Operation System/90. Annex (Operational Standards)/00. Templates/OS Output Template.md
---
---
# Persona Output Template — Computer-Science Expert

> 본 문서는 **Computer-Science Expert** 전용 산출물 출력 형식 템플릿이다. OS Output Template을 확장하며, **아래 본문 구조(섹션·테이블·항목)는 사용자가 수정**할 수 있다. Persona Agent는 정리 요청·산출물 출력 시 OS 래핑(단일 코드 블록, #Tag, Footnote·OS-ART-015)을 유지한 채, 본 템플릿의 내부 형식을 기준으로 출력한다.

---

## 01. 적용 범위

- **정리 요청**(내용/용어/상세 정리, 학습 정리, StudyNote, EDU)
- **산출물 출력 요청**(Artifact Output Mode)
- **파일 생성 요청** 시 응답에 제시하는 내용

Explanation Mode(설명 요청)는 본 템플릿을 적용하지 않는다.

---

## 02. OS가 강제하는 형식 요소

| 요소 | 규칙 |
|------|------|
| 래핑 | 전체 산출물을 **단일** ` ```markdown ` 또는 ` ```text ` 코드 블록으로 감싼다. |
| 코드 블록 밖 | 본문·설명·요약을 두지 않는다. |
| (정리 요청 시) 블록 내 첫 줄 | 풋노트에서 추출한 용어를 **#Tag** 형태로 띄어쓰기 한 줄로 나열(개행 금지). |
| (정리 요청 시) YAML | `---` frontmatter 사용하지 않는다. |
| (정리 요청 시) Footnotes | OS-ART-015(Obsidian 호환): `[^n]: **용어(English)**` 한 줄 → **탭 들여쓰기** 정의 문단 → `- **Scope**:` (필수 권장) → 해당 시 `- **Exclusion/Caution**:`. 본문 하단에 `## Footnotes` 섹션으로 배치. 정의한 용어는 본문에서 **용어 직후 [^n] 부착**(미부착 시 미준수). 라벨 빈칸 금지. |
| 구조 | 사용자 제공 헤더/구조/번호 체계를 변경하지 않는다. |
| Input Coverage Declaration | **미처리 항목이 있을 때만** 해당 단락을 출력한다. 없으면 출력하지 않는다. |

---

## 03. 템플릿 (정리 요청 / StudyNote 출력)

아래는 **정리 요청** 시 OS 기본 형식에 맞춘 최소 구조이다.  
본문(`## 1. ...` 이하)의 **섹션 구성·표·항목**은 사용자가 지정한 구조 또는 Role Rule 03.03 학습 정리/비교표 템플릿에서 정의한다.

```markdown
#Tag1 #Tag2 #Tag3

## 1. <섹션 제목>
(본문: 사용자 제공 구조 또는 Role/Organizer Contract에서 정의)

## 2. <섹션 제목>
...

---
## Footnotes
[^1]: **수주생산 (Make-to-Order)**
	(탭 들여쓰기) 정의 서술 문단.
	- **Scope**: 적용 범위 요약
	- **Exclusion/Caution**: (해당 시) 비적용·주의 조건

[^2]: **용어(English term)**
	(탭 들여쓰기) 정의 서술 문단.
	- **Scope**: 적용 범위 요약
	- **Exclusion/Caution**: (해당 시) 비적용·주의 조건
```

**Input Coverage Declaration**: 입력 기반 작업에서 **미처리 항목이 있을 때만** 해당 단락을 출력한다. 전부 처리되었으면 출력하지 않는다.

---

## 04. 산출물 출력 모드(일반) 시

사용자가 **헤더/구조를 제공한 경우** 그대로 따른다. 미제공 시 기본 헤더는 `##`로 시작한다.  
단일 코드 블록 래핑 + 코드 블록 밖 본문 금지는 동일 적용.

```markdown
## <제목>
(사용자 정의 구조 또는 요청에 따른 본문)
```

---

## 05. 참고

- OS 기본 형식: `03. Operation System/90. Annex/00. Templates/OS Output Template.md`
- 본 Role 확장: `04. Agent/01. Computer-Science Expert/Role Rule.md` 03.03
