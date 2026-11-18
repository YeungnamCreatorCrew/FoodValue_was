# KREI 남은 월보36호 수집·추출·검증·로컬DB 적재 보고

작성 시각: 2026-11-18T03:37:01.603682+00:00 / 브랜치 feat/ridge-v2 / HEAD bb6de2489b8117db090ed56c6284afb3d018e0a7.

## 완료 결과

TODO의36호 모두 처리했다. 기존PDF20호 재사용, 신규PDF16호 수집, 수집실패0호. 공통JSON36개·수치2,000행을 생성하고 검증했다. PDF432쪽 전체를 이미지로 검토했다. 원문을 해석할 수 없는 전년 비교 후보1건은 제외하고 검토 목록에 보존했다. 스키마 통과와 원문 대조, 과거 공개 내용 검증을 구분한다. 추출 재현율100%나 독립된 사람의 감사 완료를 주장하지 않는다.

| 구분 | 건수 |
|---|---:|
| 대상/수집 성공/JSON 생성 | 36 / 36 / 36 |
| 재사용/신규 다운로드/실패 | 20 / 16 / 0 |
| 검증 통과 수치행/보류 비교 후보 | 2,000 / 1 |
| 기존JSON/기존수치/보존 | 83 / 5,989 / 변경0 |
| 호별JSON 전체/전체행 | 119 / 7,989 |
| 이번 로컬DB 원본INSERT/수치INSERT | 36 / 2,000 |
| 적재 전/후 수치행 | 0(테이블없음) → migration후0 / 2,000 |
| 기존DB 수치 UPDATE/DELETE | 0 / 0 |
| 적재실패/보류 호수 | 0 / 0 |
| 중복 고유키/원본SHA 불일치 | 0 / 0 |

품목별 수치행: 배추463, 무440, 양파455, 마늘410, 대파232. 지표별 건수는 공유 manifest에 있다. 공통10지표 중 소매가격은 해당 추출 범위에서 수치행이 없으며 없는 값을 만들지 않았다. 방향만 있는300행의 숫자는 null, 범위38행 중32행의 중앙값은 적재기 파생이다. 동일 문장·본문/표·요약 반복은 독립 사실로 중복 집계하지 않았다.

## 발행 시점과 버전

36호 모두 PDF 표기 발행일/API 등록·수정/현재 수집 시각을 별도로 보존했다. API 등록과 PDF 발행일은 실제 최초 공개를 확정하는 증거가 아니다. PR48의 published_at 계약을 그대로 사용했으며, 스키마에 없는 날짜 증거·버전 상태는 부속 manifest에 담았다.

기존 감사 등급별 대상 호수: {'VERIFIED_VINTAGE': 2, 'VERIFIED_PUBLICATION': 18, 'UNVERIFIED': 16}. 전체 과거PDF 동일성 증거가 있는2호(8517·8573), 수치126행은 `strict_current_content_known_by` 이후 기준일에서만 고려할 수 있다. 기존 Ridge Tune 시점에서 실제 선택되었다는 뜻은 아니다. 2026년16호는 과거 버전 확인을 새로 수행하지 않았다. 현재 수치2,000행 전체를 STRICT 학습 승인으로 표현하지 않는다.

날짜 예외: 8553의 인쇄일2025-04-02와5월호/API5월2일 충돌을 원문대로 보존했다. 8583은 인쇄2025-07-04/API7월2일인데 공통 정규식이 공백 있는 인쇄일을 놓쳐 DB published_at은7월2일이다. DB·기존 코드를 임의 교체하지 않고 명시적 주의와 보수적 +7일 연구 가정을 manifest에 보존했다. 따라서 DB published_at만 보고 과거 모델에 넣으면 안 된다. 8721은 인쇄7월2일/API등록7월7일을 구분한다. +7일 가정은 최초 공개 검증이 아니다.

## 원문 검증·보류·표준 계약

정확한 대상은 기존 TODO36행과 공식API PDF ID/URL/SHA로 확정했다. 기존20호를 월이나 이름만으로 연결하지 않았다. 전체36호 모두12쪽·SHA·크기 정상. 없는16호만 공식공개API와 PR48 parse_index로 수집했으며 요청간격1.2초, timeout60초·최대2회 시도를 적용했다. 현재다운로드 결과는 TODO SHA와 모두 같다.

공통JSON의 실제 parse_document를 사용했다. README는 품목·작형을 제한하지만 실제 형식 검증 함수는 이 목록을 전부 강제하지 않으므로 별도 검사로 허용5품목·표준작형을 확인했다. JSON에는 스키마 밖 페이지/버전 필드를 추가하지 않고 evidence의 p.N과 부속manifest에 보존했다. pdftotext 실행파일이 없는 환경이라 native PyMuPDF/기존WindowsOCR/신규WindowsOCR를 사용한 사실을 원본 payload에 명시했다. PR48 report_record 및 원본 collection_service의 등록 규칙은 유지했다.

보류1건: PDF8705 p.5 겨울무 재고의 본문 전년과 비슷과 그래프9,246/5,220의 비교가 정합적이지 않다. 현재 절대량9,246톤만 포함하고 전년 비교행은 생성·적재하지 않았다. source conflicts·입출고 계획·지역 촬영·생육/소비 자료 등은 각 JSON unmapped에도 있다. 8696 p.9 출하표 제목5월은 본문·호·가격전망 모두6월이므로 문맥으로 판정하고 근거에 기록했다.

## Flyway·DB·복구

Docker foodvalue-postgres(postgres:17)의 compose project/service·컨테이너ID·IP와 localhost:5432/foodvalue 접속DB를 대조했다. 운영·외부 공유DB 쓰기는 하지 않았다. 외부 원본0행, 기존 krei_report_value 없음 상태였다.

전체 DB백업 `C:\FoodValue_was\model_comparison\ridge\v2\krei_monthly\handoff\runs\handoff_20261118T010858354918Z\db_backup\foodvalue_before.dump`, 105,661bytes, SHA256 `b2e8986e39c92c622e0d6a86a77241cc039bd2535cabf06ba1ddc823c8103ac8`. pg_restore --list와 별도DB `foodvalue_krei_backupcheck_20261118_023124`의 실제 복원·기존 테이블별 행 수 일치를 확인했다. 기존13개Flyway 이력 검사 및 validate 성공, Pending이 PR48 migration1개임을 확인한 뒤 격리DB 먼저 적용하고 로컬 본DB에20261117.1722만 적용했다. 기존 이력은14개가 되었으며 기존 애플리케이션 데이터 행 해시는 그대로다.

공식 report_record와 collection_service.run_dataset으로 필요한 원본36호만 등록했다. 공통 CLI python -m app.krei_values에 신규36개 경로만 명시해1,999행 INSERT, removed0. 최종대조 중 누락된8553의 평년 대비 가격 하락1행을 발견해 원문확인·JSON 수정 후, 기존행을 재적재하지 않는 INSERT ONLY 보완을 실행했다. 이1행도 공통 parse_document/report_version/테이블 계약으로 검증했으며 기존1,999행과 원본36행의 모든 필드·ID·시각이 동일함을 확인했다. 전체파일 재적재에 의한 UPDATE/DELETE는 수행하지 않았다.

격리DB에서 같은36JSON 재적재 시 순증0·정규행 동일성을 확인하고 NUMERIC 범위초과 오류를 강제로 발생시켜 트랜잭션 롤백을 확인했다. 이후1행 보완도 격리DB 먼저 적용했다. 실제 본DB INSERT2,000과 현재 총2,000을 각각 확인했다. 원본 observation_id/PDF SHA/JSON fact key/근거 페이지까지 추적 가능하다. 로컬 복구DB와 백업은 보존했다.

복구는 백업을 새 빈 로컬DB에 pg_restore --exit-on-error --no-owner로 복원하는 방식이다. 기존DB 위에 복구하거나 기존 데이터를 삭제하지 않았다. 백업에는 로컬 앱 데이터가 포함되므로 PR에 넣지 않는다.

## 테스트·보호 검사

- `.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider tests/test_krei.py tests/test_krei_values.py`:19 passed.
- `.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider`:465 passed,13 skipped,1 failed,158 warnings,872.12초.
- 실패: model_comparison/ridge/v2/tests/test_integration.py:72의 test_failed_weekly_refit_never_reuses_previous_model_and_retains_partial. FIT_FAILED 처리/부분보존은 통과하지만 로그에 `Target prices` 문자열이 없다는 assertion 실패.
- 새KREI JSON이 없는 기존코드 복사본에서 같은 실패를 재현했다. 보호시점 SHA와 원본 코드 일치를 확인했으므로 이번 KREI 신규데이터로 생긴 회귀와 구분한다. 문구 검사/환경 이슈를 고치기 위해 Ridge 코드를 수정하지 않았다. Windows cp949 관련 subprocess 경고도 별도로 관찰됐다.
- 전체검사 중 합성·임시fixture 기반 모델 단위/통합테스트는 실행됐다. 기존 가격스냅샷을 이용한 Ridge Tune/Validation/Test 실험은 실행하지 않았다.
- 기존보호파일8,530개, PDF120개, 기존83JSON, 모든 기존 감사/merge_safety: 변경0·누락0. SHA목록 sha256_before.csv/sha256_final.csv 및 preservation_final.json.
- 브랜치/HEAD 유지, tracked diff 없음. commit/push/merge/rebase/PR 생성 없음. 기존TODO도 수정하지 않고 별도 완료대조표를 생성했다.

## 공유·PR 준비

공유설명서: `data/krei_values/handoff_20261118/README.ko.md`. 근거manifest·SHA·행수·날짜·보류목록과 신규36JSON 경로목록을 함께 전달한다. PR추천 파일은 이번36JSON + 해당 공유설명 폴더다. 정확한 목록: `model_comparison/ridge/v2/krei_monthly/handoff/runs/handoff_20261118T010858354918Z/PR_FILES.txt`. 기존83JSON·원본PDF·OCR·DB덤프·로컬감사·merge_safety·기존 untracked Ridge 기록은 포함하지 않는다.

형식·원문 수치 전달용 PR을 준비할 수 있다. 날짜 예외8583과 원문 비교보류8705를 공개한 상태로 데이터 검토 PR로 전달하며, 전체가 과거학습 승인됐다고 쓰지 않는다. 추후 공통 수집기 날짜 공백 인식 개선과 역사시점/버전 안전 결합은 별도 검토 대상이다. 기존 적재기 재실행은 기존값 삭제 위험이 있으므로 팀원도 DB신원·백업·대상 기존값을 먼저 확인해야 한다.

## PDF별 결과

| 발행호 | 묶음 | PDF ID | 수치행 | JSON |
|---|---|---:|---:|---|
| 2025-03 | 엽근채소 | 8517 | 62 | `data/krei_values/OVR0000000008/8517.json` |
| 2025-04 | 엽근채소 | 8535 | 75 | `data/krei_values/OVR0000000008/8535.json` |
| 2025-05 | 엽근채소 | 8553 | 72 | `data/krei_values/OVR0000000008/8553.json` |
| 2025-06 | 엽근채소 | 8573 | 64 | `data/krei_values/OVR0000000008/8573.json` |
| 2025-07 | 엽근채소 | 8583 | 41 | `data/krei_values/OVR0000000008/8583.json` |
| 2025-08 | 엽근채소 | 8593 | 30 | `data/krei_values/OVR0000000008/8593.json` |
| 2025-09 | 엽근채소 | 8601 | 30 | `data/krei_values/OVR0000000008/8601.json` |
| 2025-10 | 엽근채소 | 8623 | 38 | `data/krei_values/OVR0000000008/8623.json` |
| 2025-11 | 엽근채소 | 8632 | 34 | `data/krei_values/OVR0000000008/8632.json` |
| 2025-12 | 엽근채소 | 8644 | 36 | `data/krei_values/OVR0000000008/8644.json` |
| 2026-03 | 엽근채소 | 8665 | 39 | `data/krei_values/OVR0000000008/8665.json` |
| 2026-04 | 엽근채소 | 8681 | 60 | `data/krei_values/OVR0000000008/8681.json` |
| 2026-05 | 엽근채소 | 8687 | 65 | `data/krei_values/OVR0000000008/8687.json` |
| 2026-06 | 엽근채소 | 8705 | 60 | `data/krei_values/OVR0000000008/8705.json` |
| 2026-07 | 엽근채소 | 8721 | 51 | `data/krei_values/OVR0000000008/8721.json` |
| 2026-08 | 엽근채소 | 8731 | 39 | `data/krei_values/OVR0000000008/8731.json` |
| 2026-09 | 엽근채소 | 8748 | 49 | `data/krei_values/OVR0000000008/8748.json` |
| 2026-10 | 엽근채소 | 8769 | 58 | `data/krei_values/OVR0000000008/8769.json` |
| 2025-03 | 양념채소 | 8518 | 55 | `data/krei_values/OVR0000000036/8518.json` |
| 2025-04 | 양념채소 | 8539 | 68 | `data/krei_values/OVR0000000036/8539.json` |
| 2025-05 | 양념채소 | 8548 | 64 | `data/krei_values/OVR0000000036/8548.json` |
| 2025-06 | 양념채소 | 8562 | 62 | `data/krei_values/OVR0000000036/8562.json` |
| 2025-07 | 양념채소 | 8581 | 86 | `data/krei_values/OVR0000000036/8581.json` |
| 2025-08 | 양념채소 | 8591 | 49 | `data/krei_values/OVR0000000036/8591.json` |
| 2025-09 | 양념채소 | 8600 | 51 | `data/krei_values/OVR0000000036/8600.json` |
| 2025-10 | 양념채소 | 8622 | 54 | `data/krei_values/OVR0000000036/8622.json` |
| 2025-11 | 양념채소 | 8630 | 56 | `data/krei_values/OVR0000000036/8630.json` |
| 2025-12 | 양념채소 | 8640 | 57 | `data/krei_values/OVR0000000036/8640.json` |
| 2026-03 | 양념채소 | 8663 | 61 | `data/krei_values/OVR0000000036/8663.json` |
| 2026-04 | 양념채소 | 8682 | 66 | `data/krei_values/OVR0000000036/8682.json` |
| 2026-05 | 양념채소 | 8691 | 62 | `data/krei_values/OVR0000000036/8691.json` |
| 2026-06 | 양념채소 | 8696 | 55 | `data/krei_values/OVR0000000036/8696.json` |
| 2026-07 | 양념채소 | 8717 | 89 | `data/krei_values/OVR0000000036/8717.json` |
| 2026-08 | 양념채소 | 8727 | 51 | `data/krei_values/OVR0000000036/8727.json` |
| 2026-09 | 양념채소 | 8745 | 54 | `data/krei_values/OVR0000000036/8745.json` |
| 2026-10 | 양념채소 | 8763 | 57 | `data/krei_values/OVR0000000036/8763.json` |

## 요청한 최종 질문

1. 남은36호 모두 처리했는가? **예.** 수집·전체쪽 검토·JSON·DB 적재36/36. 비교 후보1건은 명시적 보류.
2. 기존20호·신규16호 안전 처리했는가? **예.** 정확한ID/URL/SHA/크기/12쪽 대조, 기존원본 무변경.
3. 모든신규JSON 공통스키마 통과? **예.**36/36,2,000행. 기존83개도 읽기전용 검증.
4. PDF원문과 수치검증 완료? **저장2,000행은 완료.**432쪽을 검토했고 비교후보1건은 제외. 과거공개내용·버전까지 모두 확인했다는 뜻은 아님.
5. 로컬개발DB 적재 완료? **예.**36원본·2,000수치 INSERT, 기존UPDATE/DELETE0. 날짜주의1호는 부속manifest 필수.
6. 기존83JSON과Ridge데이터 보존? **예.**8,530개 보호파일 변경·누락0, PDF120개 유지.
7. 이제팀원에게PR을 올려도되는가? **데이터검토PR 준비 가능.**36JSON과근거설명서를 함께 포함하고 날짜/보류/기존테스트실패를 명시한다. 과거모델학습 자동승인PR로 표현하지 않는다. 실제commit/push/PR은 하지 않았다.
