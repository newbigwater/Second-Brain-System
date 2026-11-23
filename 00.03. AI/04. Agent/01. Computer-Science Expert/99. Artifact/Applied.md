---
type: Record
creation date: 2026-02-18
tags:
  - 00__System
  - 00_03__AI
  - 04__Agent
  - CS__Expert
  - Applied
Version: v1.0
---
---
# Applied — Computer-Science Expert

## 00. 적용 이력

### 2026-02-18 (v1.0) — 최초 생성

**생성 정보**:
- OS Version: v1.1
- Role Version: v1.0
- 생성 방법: 수동 생성 (자동화 스크립트 예정)

**포함 내용**:
- OS Layer 0~4 핵심 규칙
- CS Expert Persona 전체
- 확장 규칙 (제약/검증/템플릿)
- 사용 예시

**적용 환경**: (적용 후 기록)

---

## 01. 적용 방법

### ChatGPT Custom Instructions

**방법 1 (권장)**: 
```
1. OS Master Prompt 첨부
   - 파일: 03. Operation System/99. Artifact/Master Prompt.md
2. CS Expert Master Prompt 첨부
   - 파일: 04. Agent/01. Computer-Science Expert/99. Artifact/Computer-Science Expert.md
3. 텍스트 입력: "위 첨부 파일의 모든 규칙을 최상위로 적용"
```

**방법 2 (단일)**:
```
- CS Expert Master Prompt만 첨부 (OS 핵심 포함)
```

---

### Gemini GEM

```
1. 새 GEM 생성: "CS Expert"
2. Knowledge 등록:
   - OS Master Prompt
   - CS Expert Master Prompt
3. Instructions:
   "본 Knowledge의 모든 규칙 적용.
   우선순위: OS Layer 0 > L1 > L2 > L3 > L4 > CS Expert"
```

---

### Cursor AI

```
1. .cursor/rules/ 폴더 생성
2. computer-science-expert.mdrule 파일 생성
3. 내용: OS 핵심 + Role Rule 전체
4. 프로젝트 자동 적용
```

---

## 02. 적용 환경별 기록

### 환경 1: ChatGPT (예시)

**적용 일시**: YYYY-MM-DD  
**적용 방법**: Master Prompt 첨부 (OS + CS Expert)  
**버전**: OS v1.1 + CS v1.0  
**테스트 결과**:
- [ ] 4요소 단위 확인
- [ ] 비교표 자동 생성 확인
- [ ] 시험 포인트 연결 확인
- [ ] Input Coverage Declaration 확인

**노트**: (피드백 기록)

---

### 환경 2: Gemini GEM (예시)

**적용 일시**: YYYY-MM-DD  
**적용 방법**: Knowledge 등록  
**버전**: OS v1.1 + CS v1.0  
**테스트 결과**: (기록)

---

### 환경 3: Cursor (예시)

**적용 일시**: YYYY-MM-DD  
**적용 방법**: .cursor/rules/  
**버전**: CS v1.0 (OS 핵심 포함)  
**테스트 결과**: (기록)

---

## 03. 변경 이력

### v1.0 (2026-02-18)
- 최초 릴리스
- OS Layer 0~4 상속
- CS 특화 규칙 정의
- 4요소 단위, 비교 우선, 시험 지향 적용

---

## 04. 알려진 이슈

### 이슈 1: (예시)
**문제**: 비교표 자동 생성이 가끔 누락됨  
**원인**: 비교 트리거 감지 실패  
**해결**: 명시적으로 "비교표 작성" 요청  
**상태**: 모니터링 중

---

## 05. 피드백 및 개선 사항

### 피드백 1: (예시)
**날짜**: YYYY-MM-DD  
**내용**: 시험 포인트가 더 구체적이면 좋겠음  
**조치**: CS-VAL-005 강화 검토  
**상태**: 예정

---

## 06. 성공 사례

### 사례 1: (예시)
**시나리오**: B-Tree vs B+Tree 비교 요청  
**결과**: 4요소 + 비교표 + 선택 기준 완벽 제공  
**평가**: Excellent

---

## 07. 다음 단계

### 단기 (1주)
- [ ] ChatGPT 환경 테스트
- [ ] 피드백 수집
- [ ] 이슈 목록 업데이트

### 중기 (1개월)
- [ ] Master Prompt 자동 생성 스크립트 적용
- [ ] Compact 버전 생성
- [ ] 다중 환경 테스트

### 장기 (3개월)
- [ ] 버전 2.0 계획
- [ ] 추가 템플릿 개발
- [ ] 다른 도메인 Role 확장

---

## 08. 참고 자료

- **Role Rule**: `../Role Rule.md`
- **Persona Profile**: `../Persona Profile.md`
- **Validation Checklist**: `../Validation Checklist.md`
- **Master Prompt**: `./Computer-Science Expert.md`
