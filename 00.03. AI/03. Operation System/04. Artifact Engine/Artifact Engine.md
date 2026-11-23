---
type: Standard
creation date: 2026-02-11
tags:
  - 00__System
  - 00_03__AI
  - 03__OperationSystem
  - OS__Layer4
Version: v1.1
Status: Active
RuleNamespace: OS-ART
References:
  - 00. Second-Brain-System/00.03. AI/03. Operation System/00. Governance Kernel/Kernel.md
  - 00. Second-Brain-System/00.03. AI/03. Operation System/04. Artifact Engine/Output Modes.md
  - 03. Operation System/_MOC_.md
---
---
# Artifact Engine (Layer 4)

## 00. 목적

본 문서는 최종 출력의 형식/구조/모드 규칙을 강제하여, 결과물의 저장/배포/재사용을 안정화한다.

## 01. 기본 규칙(강제)

### OS-ART-010. 구조 보존

- 사용자가 제공한 헤더/구조/번호 체계를 변경하지 않는다.
- 구조를 새로 생성하거나 계층을 바꾸지 않는다.

### OS-ART-011. 출력 모드 판별

- 출력 모드는 `Output Modes.md`를 따른다.
- 모드 판별이 모호하면, 먼저 명확화 질문을 수행한다(=Kernel/Engine 준수).

### OS-ART-012. 단일 코드 블록 규칙(Explanation Mode 제외 전 모드)

- **Explanation Mode(OS-ART-001)를 제외한 모든 출력 모드**에서:
  - 단일 코드 블록만 사용한다.
  - 코드 블록 외에 본문·산출물 내용을 두지 않는다.
  - 코드 블록 **내부** 본문에는 닫는 백틱(```) 한 줄을 포함하지 않는다. 포함 시 마크다운이 첫 번째 ``` 를 블록 종료로 인식하여 블록이 조기 종료되고 그 뒤 내용이 블록 밖으로 빠진다.
- 적용: Artifact Output(002), File Generation(003), 정리 요청/StudyNote(004·020). 상세는 `Output Modes.md` 01-A 및 각 모드 정의를 따른다.
- 정리 요청(StudyNote)의 경우에도 동일하다. 단일 코드 블록 **래핑**이 정리 전용 문서 구조(#Tag, YAML 금지 등)보다 우선 적용되며, 해당 구조는 **코드 블록 내부**에서만 적용된다.

### OS-ART-013. Artifact 헤더 기본 규칙(기본값)

- 사용자가 산출물의 헤더 구조를 제공하지 않은 경우:
  - Markdown Artifact Output은 기본 헤더를 `##`로 시작한다.
  - Markdown Artifact File Generation은 기본 헤더를 `#`로 시작한다.
- 사용자가 구조/헤더를 제공한 경우:
  - 제공된 구조를 그대로 따른다(구조 보존).

### OS-ART-014. Input Coverage Declaration 포함(강제)

- 입력 데이터를 기반으로 하는 모든 작업(요약/정리/재작성/검토/번역/분석 등) 산출에는
  - 입력 전체 처리 여부를 반드시 포함해야 한다.
- 최소 포함 항목:
  - 입력 항목 총 개수
  - 처리 완료 항목 개수
  - 미처리 항목 목록(없으면 "없음")

### OS-ART-015. Footnote 3요소 구조 강제 (정리 요청 시 · Obsidian 호환 형식)

**모든 내용 정리 작업 시 핵심 용어 및 약어는 footnote로 상세 기술한다.**

#### 적용 대상

다음 요청 유형에 한해 적용한다:
- 정리 요청 (내용 정리 / 용어 정리 / 상세 정리)
- 학습 정리(StudyNote)
- EDU 성격 출력물

#### 출력 형식 (To-Be · Obsidian 호환)

Footnote는 **아래 형식**으로 작성한다. Obsidian에서 호버 시 제목·정의·Scope가 가독성 있게 표시된다.

1. **첫 줄**: `[^n]: **용어(English term)**` — 라벨과 굵은 용어를 같은 줄에 쓴다. 빈칸으로 두지 않는다.
2. **둘째 줄**: 탭 들여쓰기 후 **정의(Definition)** 를 한 문단으로 서술한다. 용어의 명확한 정의·약어 풀어쓰기를 포함한다.
3. **이어서(선택)**: 탭 들여쓰기 후 `- **Scope**: 적용 범위 요약` 을 쓴다. 적용되는 맥락·도메인을 포함한다.
4. **이어서(해당 시)**: 탭 들여쓰기 후 `- **Exclusion/Caution**: 비적용·주의 조건` 을 쓴다. 헷갈리는 개념과의 차이·적용 불가 조건이 있으면 포함한다.

최소 포함: **정의 문단** + **Scope** 불릿. Exclusion/Caution은 해당 시에만 추가.

#### 예시 (올바른 Footnote 구조)

```markdown
[^1]: **통합된 데이터(Integrated data)**  
	데이터베이스에서 동일한 의미의 데이터가 중복 없이 통합되어 관리되는 상태로, 데이터 일관성과 무결성을 유지하기 위한 기본 특성이다.
	- **Scope**: 데이터 중복 최소화, 무결성 유지

[^2]: **Key Performance Indicator (핵심 성과 지표)**  
	조직·프로젝트의 목표 달성도를 정량적으로 측정하는 지표로, 단순 통계 데이터와 달리 전략적 목표와 직접 연결된다.
	- **Scope**: 성과 평가, KPI 대시보드, OKR 연계
	- **Exclusion/Caution**: 일회성 수치만으로는 KPI라 부르지 않음
```

#### 검증

- 정의 문단 누락 또는 라벨 한 줄 빈칸: `NG`
- Scope 누락: 경고 (필수 권장)
- 3요소 중 2개 이상 누락(정의·Scope·Exclusion 해당 시): Validation Engine에서 `NG` 판정

#### 예외

도메인별 기본 용어는 예외 허용 (해당 Role/Agent 규칙 참조)

### OS-ART-016. 기본 출력 형식 및 Persona 확장

- **기본 산출물 출력 형식**은 Annex의 `90. Annex (Operational Standards)/00. Templates/OS Output Template.md`를 따른다.
- Role/Persona는 Organizer Contract·Role Rule 등으로 **산출물 내부 형식**(섹션·테이블·템플릿)을 확장할 수 있다.
- 확장 시에도 OS 기본 형식(단일 코드 블록, 정리 요청 시 #Tag 한 줄·YAML 금지·Footnote 3요소 등)을 완화하거나 대체하지 않는다.

---

## 02. 등록팩(Registration Pack) 연계

- Custom Instructions/세션 시작 시 적용할 "최소 첨부 세트"는 Annex의
  - `📎 Custom Instructions Registration Pack Standard.md`
  를 따른다.

## 03. 위반 시 처리

- Layer 0 위반: `INVALID RESPONSE`
- 출력 모드 위반(예: 산출물 요청인데 코드블록이 2개 이상/외부 텍스트 존재): 최소 `NG`
