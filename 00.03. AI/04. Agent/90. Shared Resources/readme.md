---
type: Guide
creation date: 2026-02-21
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
Version: v1.0
Status: Active
---
---
# 90. Shared Resources — 공유 리소스

## 00. 목적

본 폴더는 **여러 Role/Persona가 공통으로 참조하는 리소스**를 둔다.

- Role 간 공통 용어집·도메인 용어 정의
- 공통 템플릿(정리 출력, 메일 등) 초안
- Agent 시스템 전역에서 쓰는 체크리스트·스니펫

**단**, OS 규칙·계약은 `03. Operation System`이 정본(SSOT)이며, 본 폴더는 **확장·참고용**만 담는다.

---

## 01. 사용 원칙

- **추가만 허용**: Role은 Shared Resources를 참고할 수 있으나, OS를 약화하는 내용을 여기에 두지 않는다.
- **선택 참조**: 각 Role의 `Role Rule.md` 또는 `Domain Knowledge.md`에서 필요 시 본 폴더 문서를 References에 넣을 수 있다.
- **비어 있어도 무방**: 현재 리소스가 없어도 된다. 필요할 때만 파일을 추가한다.

---

## 02. 권장 하위 구조 (필요 시)

- `00. Index/` — 목차·MOC (필요 시)
- `01. Glossary/` — 공통 용어 정의 (필요 시)
- `02. Templates/` — Role 간 공통 템플릿 초안 (필요 시)

파일을 추가할 때는 `04. Agent/_MOC_.md`에 링크를 반영한다.
