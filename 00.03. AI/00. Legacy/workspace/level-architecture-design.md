---
title: Level Architecture Design
author: AI Engineer
date: 2026-02-10
---
---

# 1. Overview
- **Purpose**: Formalize the 00~99 Layer hierarchy so every guideline or artifact lives in an explicit level, preventing top-level (00) documents from referencing downstream outputs.
- **Drivers**
  - 상위 규약을 Charter(00 Root)에 집중
  - Business / Project / Application Stage를 2 Level에서 운용
  - 3~9 Level은 확장용으로 예약
- **Out of Scope**: 물리적 폴더 리네임(예: `02. Business → 10. Business`)은 향후 결정 시 별도 스크립트로 처리.

# 2. Objectives & Success Criteria
| No | Objective | Success Metric |
| -- | --------- | -------------- |
| O1 | Level 메타데이터 일괄 부여 | 100% `.md` 문서 front matter에 `level` 필드 존재 |
| O2 | 상향 참조 강제 | `check_level_links` 실행 시 위반 0건 |
| O3 | README 및 MOC에서 레벨 구조 안내 | Core README + Stage `_MOC_`에 레벨 코드 노출 |

# 3. Level Mapping
| Level Code | Layer | 대표 폴더/문서 |
| --- | --- | --- |
| `00.00` | Root Charter (최상위 규약) | `01. Core/00. Charter/🧠 Common Rule.md`, Execution Gate, Standard Prompt Policy |
| `00.01` | Core Stage | `01. Core/01. Operations`, `01. Core/02. Standards`, `01. Core/03. Frameworks` |
| `10.00` | Business Root | `10. Business/_MOC_.md` |
| `10.01.01` | Business – SRS | `10. Business/10.01 Architect/10.01.01 SRS/…` |
| `10.01.02` | Business – SDS | `10. Business/10.01 Architect/10.01.02 SDS/…` |
| `10.01.03` | Business – SCS | `10. Business/10.01 Architect/10.01.03 SCS/…` |
| `10.02.01` | Project – PM | `10. Business/10.02 Project/10.02.01 PM/…` |
| `10.02.02` | Project – Translation | `10. Business/10.02 Project/10.02.02 Translation/…` |
| `20.00` | Application Root (Personal/Domain) | `20. Personal/_MOC_.md` |
| `20.01.xx` | Application – English | `20. Personal/20.01 English/01. Rules/20.01.01 Podo English`, `20. Personal/20.01 English/01. Rules/20.01.02 Grammar` |
| `20.02.xx` | Application – Computer-Science | `20. Personal/20.02 Computer-Science/…` |
| `30~89` | Reserved | (미사용, 향후 확장) |
| `90~99` | Artifact/Backup | `01. Core/99. Artifact`, `99. Backup` |

## 3.1 Tree View
```
00 Root
└── 00.00 Charter
    └── 00.01 Core Stage
        ├── 10.00 Business
        │   ├── 10.01 Architect
        │   │   ├── 10.01.01 SRS (Helios)
        │   │   ├── 10.01.02 SDS (Aegis)
        │   │   └── 10.01.03 SCS (Forge)
        │   └── 10.02 Project Ops
        │       ├── 10.02.01 PM (Chronos)
        │       └── 10.02.02 Translation (LinguaBridge)
        └── 20.00 Application
            ├── 20.01 English
            │   └── 01. Rules
            │       ├── 20.01.01 Podo English
            │       └── 20.01.02 Grammar
            └── 20.02 Computer-Science
                └── 20.02.xx Domain Guides

30~89 Reserved for future domains
90~99 Artifact / Backup (outputs only)
```

# 4. Metadata & Link Policy
1. **Front Matter**
   ```yaml
   level: 10.01.02
   parent_level: 10.01
   ```
   - `parent_level`는 자동화 시 추적 용도.
2. **Link Direction**
   - 문서 A가 문서 B를 참조하려면 `level(B) ≤ level(A)`.
   - 00 Layer 문서는 절대 하위 레벨을 링크하지 않음.
3. **MOC 규칙**
- `_MOC_.md`는 동일 레벨 또는 상위 레벨 문서만 wikilink로 연결한다.
   - 하위 문서는 서술/리스트로만 안내하고, 실제 링크는 그 하위 폴더의 MOC에서 처리.
4. **Artifacts**
   - Level 90~99 폴더에서만 저장.
   - 상위 문서는 “산출물 존재”만 언급.

# 5. Automation Plan
| Script | 역할 | 구현 포인트 |
| --- | --- | --- |
| `workspace/tools/apply_level_metadata.py` | 폴더 경로 → 레벨 코드 매핑 기반으로 front matter 갱신 | (현행) `workspace/tools` 자동화 파이프라인 사용 |
| `workspace/tools/check_level_links.py` | Markdown 링크 방향 검증 | `.md` 파싱 → 상대 경로 → target level 조회 → 위반 리포트 |
| `workspace/tools/archive/moc_audit.py` 확장 | `_MOC_.md` 링크 규칙 검사 | (현행) archive 스크립트로 관리 |
| (선택) `rename_levels.py` | 물리 폴더 리네임 (미사용) | 추후 필요 시 작성 |

# 6. Implementation Phases
1. **Phase A – Metadata**
   - Build `LEVEL_MAP` (폴더 prefix → 코드)
   - 메타데이터 스크립트 실행
2. **Phase B – Documentation**
   - README/Stage `_MOC_`에 레벨 표기 (README 이미 갱신됨)
   - Charter/Common Rule 등 00 Layer 문서에서 하위 링크 제거 (완료)
3. **Phase C – Automation**
   - `check_level_links.py` 작성 및 CI/Hooks 적용
   - `moc_audit.py` 업데이트
4. **Phase D – Validation**
   - 스크립트 실행 → 위반 사항 수정
   - 최종 리포트: 전체 문서 수, level 메타 필드 채움 여부, 링크 위반 0건 확인

# 7. Work Breakdown
| ID | Task | Owner | Status |
| --- | ---- | ----- | ------ |
| T1 | LEVEL_MAP 정의 및 스크립트 초안 작성 | AI Engineer | TODO |
| T2 | front matter `level` 일괄 주입 | AI Engineer | TODO |
| T3 | README/Stage MOC 레벨 명시 점검 | AI Engineer | TODO (Core README 완료, Stage 미점검) |
| T4 | `check_level_links.py` 구현 & CI 통합 | AI Engineer | TODO |
| T5 | `moc_audit.py` 레벨 규칙 확장 | AI Engineer | TODO |
| T6 | 실행 결과 보고서/README 업데이트 | AI Engineer | TODO |

# 8. Risks & Mitigations
| Risk | Impact | Mitigation |
| --- | --- | --- |
| 레벨 코드 중복/누락 | 자동화 실패 | LEVEL_MAP 검토, dry-run 로그 |
| 스크립트가 링크 파서와 충돌 | 검증 누락 | 기존 `link_check.py` 로직 활용, 테스트 케이스 작성 |
| Commit 이전에 메타데이터 누락 파일 발생 | CI fail | pre-commit hook에 검사 추가 |

# 9. Next Steps
1. LEVEL_MAP 정의 → 스크립트 초안
2. 메타데이터 주입 및 README/MOC 검토
3. 링크 검증/자동화 스크립트 배포
4. 최종 결과 보고
