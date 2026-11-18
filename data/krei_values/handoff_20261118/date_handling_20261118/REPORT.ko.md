# KREI 날짜 처리 및 보류 검증 최종 재점검

2026-11-18, PR #47 head `data/krei-monthly-36-reports`, HEAD `f2fdc56a67a63498942814eb80f29791e9ace895`. 작업 위치는 기존 PR worktree다. `dev`와 `feat/ridge-v2`는 수정하지 않았다. 이전 검토용 문서 버전은 개인 감사 영역에 별도로 보존했다.

**결론: 미보유 PDF 2호와 판권 자동 추출 실패 사례의 날짜 검증을 모두 해결했다. JSON 119개·7,989행은 그대로이며, 관련 테스트 210개 통과 후 커밋 전 검토 상태다. 이번 추가 점검에서 실제 개발 DB의 변경은 0건이다. 실제 최초 공개 시각·역사적 원본 버전의 미확인 사항은 여전히 별도다.**

## 해결 1: 8780·8786 공식 원본

| PDF ID | 묶음 | 원본 크기 | 기존 SHA와 일치 | 표지 인쇄일 |
|---|---|---:|---|---|
| 8780 | 양념채소 | 4,048,447 bytes | 정확히 일치 | 2026-11-03 |
| 8786 | 엽근채소 | 4,597,918 bytes | 정확히 일치 | 2026-11-03 |

공식 URL과 SHA-256:

- 8780: https://aglook.krei.re.kr/main/uObserveMonth/OVR0000000036/download/8780/ORGTEXT_FILE / `4dc5138b938edb63006986e46b23dbf72f2081806227656b3ce7bd5b8889866a`
- 8786: https://aglook.krei.re.kr/main/uObserveMonth/OVR0000000008/download/8786/ORGTEXT_FILE / `ffb99cdef11ee88342a7d8ef081bdc13133a8ebbcf429aeea323f4d0f6d26b46`

HTTP 200의 PDF 응답과 파일명 VS202611.pdf / VC202611.pdf를 확인하고 PDF를 정상 열었다. 기존 JSON·manifest의 식별자·URL·SHA와 같은 파일이다. 신규 자료는 개인 감사 폴더에만 저장해 기존 원본을 덮어쓰지 않았다. SHA가 다른 별도 버전은 발견하지 않았다. PDF 바이트와 확인 이미지는 PR에 포함하지 않는다. 두 인쇄일은 표지 이미지와 판권 OCR을 함께 확인한 값이며 최초 공개 시각의 증거는 아니다.

## 해결 2: 자동 추출 실패 34호 및 신규 2호

119호 원본 SHA와 첫 페이지 판권을 재대조했다. 입력 근거별 공통 파서 성공은 **native 83호 + 기존 OCR 28호 + 새 판권 부분 OCR 8호 = 119호**다. 이전 실패 34호는 텍스트가 없는 이미지 PDF 또는 중첩 레이어가 원인이었다. 원래 없던 날짜를 정규식이나 호 월로 채우지 않았다.

새 판권 부분 OCR은 7654·8687·8705·8721·8748·8769·8780·8786에만 수행했다. 전체 PDF OCR을 다시 실행하거나 기존 OCR 캐시를 변경하지 않았다. 7654의 native 텍스트에는 2020-11-23과 2021-03-31의 두 판권이 겹쳐 있었지만 렌더링한 표지에는 2021-03-31이 보인다. 공통 파서가 모호한 native 텍스트를 계속 거부하도록 유지하고, 이미지 검토를 마친 판권 부분 OCR만 명시적으로 채택했다.

공통 수집기에 `imprint_with_evidence`와 선택적 `cover_evidence` 입력을 추가했다. 호 식별자·실제 PDF SHA·표지 1쪽·텍스트 해시·검토 상태·파서 결과와 기대 인쇄일을 모두 확인한다. 유효한 native 날짜와 다른 OCR은 거부하며, 중첩 native를 대신하려면 이미지 검토된 FOCUSED_COVER_OCR만 허용한다. PDF ID 하드코딩이나 임의 날짜 보정은 없다. native 경로는 그대로 유지된다.

입력 근거는 [imprint_evidence119.json](imprint_evidence119.json)에 있다. 숫자 추출 JSON 또는 DB 적재 입력이 아니다. 프로그램에서 사용한다면 다음처럼 명시적으로 전달한다.

```python
proofs = {p['source_record_key']: p for p in manifest['reports']}
batch = krei.collect(fetch, groups=groups, years=years, cache_dir=cache_dir,
                     cover_evidence=proofs)
```

기본 `python -m app.krei_monthly` CLI는 이 manifest를 자동 읽거나 OCR을 자동 수행하지 않는다. 이번 검증은 각 실제 PDF 바이트를 공통 report_record에 전달하는 오프라인 검사이며 수집기·적재기를 실제 DB에 재실행한 것이 아니다. 메타데이터가 달라지는 일반 재수집은 새 observation 버전을 만들 수 있으므로 날짜 정정 목적의 무조건 재수집/전체 재적재를 피한다.

## 119호 날짜 정합성

- API 등록 원문·등록시각, PDF 인쇄일·원문, 이용 가능 후보를 전부 구분했다.
- `available_from = max(API 등록시각, PDF 인쇄일의 서울 자정 표현)`을 119호 전부 실제 계산·대조했다.
- API 원문 `reg_date`는 보존한다. 인쇄일의 자정과 API 14자리 값의 Asia/Seoul 해석은 기존 프로젝트 표현 규칙이며 실제 공개 시각을 확정하는 규칙이 아니다.
- 인쇄일 미확인 **0호**, 근거 모호성을 숫자로 메운 사례 **0건**, PDF SHA 차이 **0건**이다.
- 119호 날짜 대조표는 [date_audit119.json](date_audit119.json)에 있다. `db_published_at_before`는 최초 날짜 정정 전 값, `db_published_at_after`는 당시 정정 결과, `db_published_at_checked_now`는 이번 읽기 전용 확인 값이다. NULL은 현재 로컬 DB 미등록이며 날짜 결측을 보충한 것이 아니다.

등록일과 인쇄일이 다른 5호는 계속 구분해 보존한다:

| PDF | API 등록시각 (KST) | 인쇄 발행일 | 이용 가능 후보 (KST) |
|---|---|---|---|
| 7987 | 2021-10-05T07:38:28+09:00 | 2021-10-01 | 2021-10-05T07:38:28+09:00 |
| 8214 | 2022-12-02T13:25:00+09:00 | 2022-12-01 | 2022-12-02T13:25:00+09:00 |
| 8553 | 2025-05-02T17:12:17+09:00 | 2025-04-02 | 2025-05-02T17:12:17+09:00 |
| 8583 | 2025-07-02T16:05:59+09:00 | 2025-07-04 | 2025-07-04T00:00:00+09:00 |
| 8721 | 2026-07-07T09:18:58+09:00 | 2026-07-02 | 2026-07-07T09:18:58+09:00 |

8553의 5월호에 적힌 4월 2일은 원문 그대로다. 발행호를 근거로 임의로 5월로 수정하지 않았다. 8780·8786은 API와 인쇄일이 같은 날이며, 시간값은 API 등록시각과 프로젝트 인쇄일 표현 중 늦은 쪽을 유지한다.

## PDF 8583 및 로컬 DB

기존 승인된 날짜 정정에서 API 등록 2025-07-02T16:05:59+09:00, 인쇄일 2025-07-04를 구분하고 보수적 후보를 2025-07-04T00:00:00+09:00으로 계산했다. 수집기는 `통권발행·편집인/원장제1319호 2025년한두봉7월발행처4일 발행`처럼 두 열이 혼입된 판권을 처리한다.

당시 전체 DB 백업(396,583 bytes, SHA-256 `aa2d7f17581efafded76857fc738a548cbb0557d3bffda67d15d75c08defcbbf`)과 격리 복원을 검증한 후 로컬 원본 36행의 날짜 구분 메타데이터를 갱신했다. 그중 published_at이 바뀐 것은 **8583 원본 1행·연결 수치 41행**뿐이었다. 수치 JSON과 수치 내용은 유지했다. 이 이력은 팀원 DB에 적용됐다는 뜻이 아니다.

이번에는 Docker 신원과 loopback 연결을 다시 확인하고 DB를 읽기 전용으로 검사했다. 원본 36행·수치 2,000행, 전체 public 32개 테이블의 데이터 해시/건수와 컬럼·제약이 이전 정정 완료 상태와 동일하다. 원본 published_at·payload.available_from과 연결 수치 날짜가 새 119호 감사 후보와 모두 일치했다. 기존 DB의 수치·단위·비교 기준·기간·관계가 그대로다.

**이번 추가 DB INSERT/UPDATE/DELETE는 0건이다. 스키마 변경·Flyway·추가 백업/복원도 실행하지 않았다.** 추가 날짜 수정이 필요하지 않았기 때문이다. 미등록 83호를 재적재하지 않았다. 회귀 테스트의 DB 쓰기는 이전에 백업 복원한 격리 DB에서만 수행했으며 실제 개발 DB와 분리했다.

## 검증·회귀 테스트

최종 범위는 기존 KREI/수치 파서, 날짜 정책, SHA-bound 근거, 공통 수집기, 격리 DB 롤백·멱등성이다. **210 passed**이며 기존 76개에 119호 판권과 15개 근거 안전성 검사를 추가했다. 실행 명령:

```text
python -B -X utf8 -m pytest -q -p no:cacheprovider tests/test_krei.py tests/test_krei_values.py tests/test_krei_dates.py tests/test_krei_date_db.py tests/test_collectors.py tests/test_krei_imprint_evidence.py
```

형식/해시/다른 PDF/다른 페이지/미검토 OCR/기대일 불일치/유효 native 충돌/숨은 레이어/빈 PDF를 거부하는 검사, 원본 API 보존 및 늦은 기준일 선택, 기존 숫자 적재기의 날짜 복사·중복/삭제 없음과 롤백 검사가 포함된다. 격리 DB URL을 명시하지 않은 일반 실행에서는 DB 검사 4개가 skip된다. 실제 PDF와 SHA를 확인한 오프라인 원본 검증과, PDF가 없는 CI에서 실행하는 텍스트 fixture 회귀 검사는 구분한다.

## 계속 보류하는 사항

- **실제 최초 공개 시각**: API·인쇄일의 최댓값이 해당 시각의 공개 접근을 증명하지 않는다.
- **역사적 PDF 버전과 당시 이용 가능성**: 현재 같은 SHA의 파일 확보와 날짜 계산으로 과거 원본 동일성이 자동 검증되는 것은 아니다. 기존 archive 등급·known-by 한계는 유지한다. 일괄 STRICT 학습 승인하지 않는다.
- **8705 비교 후보 1건**: 본문과 그래프의 겨울무 재고 전년 비교 불일치는 그대로 보류한다. `HELD_OUT_NOT_LOADED`, `use_for_training=false`와 JSON/DB 제외를 유지한다. 별도 작기 저장량 40,200톤·전년비 15.5%는 다른 대상이다.

현재 인쇄일/원본 미보유라는 이유로 보류된 월보는 없다. 위 사항들은 근거의 종류가 달라 날짜 파서만으로 해결할 수 없다. Ridge 특성 연결·학습은 구현하거나 실행하지 않았다.

## 파일 보존 및 커밋 준비

JSON **119개·7,989행(기존 83개·5,989행 + 신규 36개·2,000행)**의 원문 바이트/수치와 Ridge 코드·실험 기록·기존 PDF·기존 감사/merge_safety를 보존한다. 기존 개인 감사 보고서는 덮어쓰지 않았고 현재 공유 문서의 이전 버전도 따로 보관했다. 원본 두 PDF와 OCR 캐시·확인 이미지·DB 로그는 PR 밖에 둔다.

현재 검토할 변경 파일은 **11개**, stage는 0개다:

- `app/collectors/krei.py`
- `app/services/krei_date_service.py`
- `data/krei_values/handoff_20261118/README.ko.md`
- `data/krei_values/handoff_20261118/date_handling_20261118/PR_BODY_DATE_UPDATE.ko.md`
- `data/krei_values/handoff_20261118/date_handling_20261118/REPORT.ko.md`
- `data/krei_values/handoff_20261118/date_handling_20261118/date_audit119.json`
- `data/krei_values/handoff_20261118/date_handling_20261118/imprint_evidence119.json`
- `tests/test_krei.py`
- `tests/test_krei_date_db.py`
- `tests/test_krei_dates.py`
- `tests/test_krei_imprint_evidence.py`

추천 commit message: `fix(krei): correct monthly report publication date handling`

Git add/commit/push, PR 생성/수정/merge, reset/clean/stash/rebase는 실행하지 않았다. 기존 사용자 index와 HEAD를 유지한다. 코드·테스트·문서 diff를 검토한 뒤에만 추가 커밋/푸시와 PR 본문 갱신을 진행할 수 있다. PR 본문 수정안은 [PR_BODY_DATE_UPDATE.ko.md](PR_BODY_DATE_UPDATE.ko.md)다.

## 최종 완료 확인

최종 재실행은 **210 passed in 4.75s**다. 실제 로컬 DB의 전체 행·스키마 해시와 원본/수치 행은 이번 검사 전후 동일했다. 원래 프로젝트 보호 파일 **10,291개**(주 실행 계정 7,934개 + 별도 제한 경로 2,357개)의 SHA-256에서 변경·누락 0개를 확인했다. JSON 119개·7,989행은 원문 바이트와 공통 파서 검사를 통과했고 Ridge 코드·실험·스냅샷 및 기존 원본 PDF 120개를 보존했다. 작업 worktree의 변경은 의도한 11개 파일뿐이며 stage 0건, 기존 HEAD·브랜치·index는 동일하다. 추가 DB 수정·Git 전송·PR 갱신 없이 커밋 검토 상태에서 종료한다.
