# KREI 신규36호 DB 스키마 정합성 최종 점검

작성: 2026-11-18T04:04:46.205140+00:00 / feat/ridge-v2 / HEAD bb6de2489b8117db090ed56c6284afb3d018e0a7.

**판정: 신규 JSON36개·2,000행은 현재 PR48 공통 스키마/적재기와 호환되며 데이터 검토용 PR 전달 준비가 되었다. 이번 점검에서 수정한 JSON은0개다.** DB 저장값과 적재기 변환 후 수치의 차이는0건이다. 8583의 원본 발행 메타데이터 문제와8705 보류사항을 함께 전달해야 하며, 이 판정은 전체 자료에 대한 과거 학습 승인을 뜻하지 않는다.

## 1. 실제 계약과 검사 범위

직접 확인한 파일: db/migration/V20261117_1722__krei_report_value.sql, app/krei_values.py, app/services/krei_value_service.py, app/collectors/krei.py, data/krei_values/README.md, EXTRACTION_GUIDE.md, 기존83JSON·신규36JSON 및 KREI_HANDOFF_REPORT.ko.md. 공통 코드는 수정하지 않았다.

| JSON 또는 생성값 | DB 대응과 처리 | 확인 결과 |
|---|---|---|
| source_record_key + pdf_sha256 | external_observation의 KREI/MONTHLY_REPORT 원본 키와 SHA로 버전을 선택, observation_id FK | 36/36 정확히 연결 |
| extractor, extractor_version | VARCHAR(40), NOT NULL | 전행 적합 |
| item_name, crop_type | VARCHAR(30), 작형NULL 허용; 품목/작형별 DB CHECK는 없으므로 README 표준 별도 검사 | 신규5품목·표준작형 적합 |
| metric | 허용10지표 CHECK | 적합; 신규자료에 RETAIL_PRICE 행 없음 |
| kind | ACTUAL / OUTLOOK NOT NULL | 적합; 가격 실적은 발행월 전, 전망은 해당 발행월 |
| target_start, target_end | DATE, 시작≤종료 | 적합; 월초~말일/명시 구간/연산 표준 확인 |
| basis | LEVEL / PREV_YEAR / NORMAL / PREV_MONTH | 적합 |
| value, value_low, value_high | NUMERIC(14,3), NULL 허용 | 유한숫자·정밀도·범위 적합 |
| unit | VARCHAR(20), 값 있으면 단위 필요 | 단위·비교기준 적합, 품목간 강제환산 없음 |
| direction | UP / DOWN / FLAT 또는NULL; 비교행은 적재기에서 필수 | 부호 및 원문 비슷 표현 예외 구분 |
| evidence | TEXT NOT NULL | 원문 근거와 PDF p.N, 2,000행 추적 가능 |
| published_at | JSON 필드 아님; 원본 observation의 TIMESTAMPTZ 복사, NOT NULL | JSON으로 덮어쓸 수 없음 |
| id, created_at | DB 생성 | JSON에 추가하지 않음 |
| unmapped | 형식만 검사하고 적재하지 않음 | 제외/보류 이유 보존 |

허용 지표10종: ARRIVAL, IMPORT, PLANTED_AREA, PRODUCTION, RETAIL_PRICE, SHIPMENT, SHIPMENT_AREA, STOCK, WHOLESALE_PRICE, YIELD. 실제 PostgreSQL의 컬럼 타입·NULL·길이·NUMERIC(14,3)·FK·CHECK·UNIQUE NULLS NOT DISTINCT 정의를 migration과 대조했다. 품목·작형 표준 및 비교행 단위/방향은 DB보다 공통 파서/문서가 엄격하므로 두 규칙을 모두 검사했다.

공통파서의 고유키는 item_name/crop_type/metric/kind/basis/target_start/target_end이며 DB에서는 observation_id가 추가된다. 신규2,000행의 같은 원본 내 고유키 중복·충돌0건. 다른 호가 같은 대상을 전망한 사실은 원본 observation으로 구분한다.

## 2. 수정 여부·수치 행 수

**수정 JSON 목록: 없음. 수정 전후36개·2,000행 그대로다.** 기존83개·5,989행은 읽기 전용 검사했고 전부 공통파서를 통과했다. 호별119개·총7,989행의 SHA가 점검 전후 동일하다. 기존팀원 자료에서 문서상 알려진 작형 표기 차이는 수정 범위 밖이며 과거 자료를 새 표준으로 무단 정규화하지 않았다.

범위38행 중32행은 raw value가NULL이고 공통파서가 (low+high)/2를 계산한다. 나머지6행은 PDF 표에 인쇄된 점 값과 범위를 함께 보존한다. 이 변환 후 값과 DB값을 Decimal로 비교해 모두 일치했다. 방향만 있는300행은 DB value도NULL이다. FLAT이면서 소수 증감률이0이 아닌 행은 문서의 비슷/평년수준을 따르는 허용 사례이며 임의로0을 넣지 않았다.

일반 마늘 공급 수치를 깐마늘 가격으로 취급하지 않았고, 마늘 가격의 깐마늘/난지형 구분과 품목별 원/kg·원/10kg·원/20kg을 유지했다. 생산량/재고/수입은톤, 면적ha, 단수kg/10a, 일평균 반입량톤/일과 월전체톤을 구분했다. 연산 YYYY-01-01~12-31은 계약 표현이지 실제 수확일 구간이 아니다.

## 3. PDF 원문·원본 연결

신규36개 모두 공식PDF ID/URL/묶음·파일크기·SHA256와12쪽을 확인했다. 기존2,000행 페이지별 검토 근거와 현재 JSON 행을 전부 대조해 원문페이지/원본SHA/근거 인덱스가 일치함을 확인했다. 이번에는8583 표지,8705 p.5,8682 p.3 범위표,8553 p.5 가격 전망을 PDF 이미지로 다시 확인했다. 기존 월보 전체432쪽 검토 기록을 보존했으며 이번에 전체 OCR이나 독립된 전수 재추출을 다시 수행한 것으로 표현하지 않는다. 원문이 모호한 후보는 확정하지 않았다.

## 4. 실제 로컬DB 읽기 전용 비교

localhost:5432/foodvalue, PostgreSQL17.11, 서버IP172.18.0.3을 기존 로컬Docker 신원 기록과 대조했다. 연결의 default_transaction_read_only=on, transaction_read_only=on, REPEATABLE READ로 검사했고 마지막에 rollback했다. INSERT/UPDATE/DELETE/Flyway/테이블변경0건이다.

현재36개 external_observation과2,000개 krei_report_value를 조회했다. PDF ID/SHA/URL/크기·observation_id, 원본의 published_at 복사, 수치·단위·방향·비교기준·시작/종료일·NULL·범위·적재기 파생값·extractor/version·근거 문장을 JSON 변환값과 비교했다. **차이0건.** 신규JSON에 불필요한 재적재를 하지 않았다. 현재DB에 기존83호 수치는 없으므로 그83개를 몰래 재적재하지 않았다.

행 데이터의 해시/건수와 전체 public 스키마 컬럼·제약을 같은 읽기전용 스냅샷 전후 비교해 동일함을 확인했다. 이는 해당 검사 트랜잭션에서의 보존 확인이며 다른 세션의 동시 외부 쓰기까지 차단했다는 뜻은 아니다.

## 5. PDF8583 — JSON 수정 불가, 팀원 수정 요청

PDF 인쇄 발행일2025-07-04, 공식API 등록2025-07-02, 현재DB published_at2025-07-02T16:05:59+09:00을 확인했다. 원본 observation_id는5, 연결수치는41행이다. JSON에는 published_at을 지정하는 필드가 없으며 임의 필드 추가 시 실제 parse_document가 거부함을 확인했다. **8583 JSON과DB는 유지했다.**

기존 보고서의 원인을 보완한다. 실제 저장된 표지 텍스트는 다음과 같이 두 열이 혼입되어 있다.

```text
www.krei.re.kr   통권발행·편집인/원장제1319호 2025년한두봉7월발행처4일 발행(월간·비매품)한국농촌경제연구원등록번호디자인·인쇄나주 라 세일포커스(주)00017호(2024.9.10)
```

`2025년한두봉7월발행처4일 발행`이므로 단순한 공백 제거로는 해결되지 않는다. 정상 PDF 이미지의 인쇄일은7월4일이지만 텍스트 추출 단계에서 편집인 이름/발행처가 끼어 기존 날짜 정규식이 잡지 못한다. 이번에는 공통 수집기·적재기·정규식을 변경하지 않았다.

팀원에게 요청할 안전한 처리:

1. 표지 판권의 텍스트 읽기 순서/좌표 또는 pdftotext layout을 먼저 확인한다. 일반 본문에 임의 문자를 허용하는 광범위한 날짜 정규식은 피한다. 판권 통권·발행 표식이 있는 제한된 구역에서 날짜와 원문 증거를 추출하는 방안을 검토한다.
2. 실제 혼입 텍스트8583, 정상 판권, 여러 본문 날짜가 먼저 있는 사례, 줄바꿈/띄어쓰기, 잘못된 날짜/불완전날짜·통권 없는 오탐 방지, 기존 조기/일괄 재등록 필터를 포함하는 회귀 테스트를 공통코드 담당자가 추가한다. 기존119호로 dry-run 메타데이터 차이를 조사한 뒤 적용한다.
3. 검증된 표기일을 기존 availability 계약에 넣으면 후보는2025-07-04T00:00:00+09:00이다. 이것은 날짜만 있는 판권을 서울 자정으로 표현한 **계약 후보**이며 실제 최초 공개시각이7월4일 자정이었다는 증거가 아니다.
4. 현재 로컬36호의 검증된 판권으로 가용시점만 오프라인 재계산한 결과 published_at이 달라지는 호는8583 하나(원본1행+연결수치41행)다. 저장 payload의 imprint_date가 추가/변경될 수 있는 호는12개다. 전체 기존119호나 외부DB의 영향 건수로 확대해 해석하면 안 된다.
5. 변경 전 해당 원본·연결값·Flyway이력을 백업하고 DB신원/원본SHA를 고정한 뒤 격리 복원DB에서 메타데이터 수정과 기준일별 누수방지 회귀를 검증한다. 원본 published_at만 바꾸면 수치41행의 복사값은 자동 갱신되지 않으므로 양쪽을 단일트랜잭션으로 일관되게 다룰 계획이 필요하다. 기존시간/증거/적용이력을 별도로 보존하고 건수41·다른수치불변을 검산한 뒤 승인된 담당자가 수행한다. 이 작업에서는 실행하지 않았다.
6. 일반 수집기를 재실행하면 payload SHA가 달라져 새 observation 버전이 생길 수 있다. 공통 적재기를 전체 재실행하면 upsert와 stale 삭제가 발생하므로 날짜 수정만을 위해 무조건 재수집·재적재하지 않는다. 기존값 교체를 피하려면 새 메타데이터 버전과 기존버전 처리 정책을 먼저 정하고, 기존41행을 이중 집계하지 않도록 조회정책까지 검토한다.

## 6. PDF8705 — 비교후보 보류 유지

2026-05 겨울무 **재고량** 절대량9,246톤 LEVEL만 JSON/DB에 있으며 동일 기간의 PREV_YEAR 비교행은없다. 원문 본문은 전년과 비슷인데 그래프는2025년산9,246·2024년산5,220이므로 이 비교를 확정하지 않았다. `unmapped`와 공유 review_queue.json에 HELD_OUT_NOT_LOADED / use_for_training=false가 남아 있다.

같은 PDF의 **작기 저장량**40,200톤·전년비15.5%는 별도 대상기간(2025년산 연산)과 지표 근거를 가진 유효한 행이므로 혼동해 제거하지 않았다. 보류한 것은5월말 재고의 전년 비교1건이다. 임의 증감률은 계산하지 않았다.

## 7. 테스트와 기존 Ridge 실패

이번 실행: `.venv/Scripts/python.exe -B -X utf8 -m pytest -q -p no:cacheprovider tests/test_krei.py tests/test_krei_values.py` → **19 passed**. 공통파서로 신규36/2,000 및 기존83/5,989 전부검사, 실제DB 컬럼/제약·변환후2,000행 비교통과. 별도 DB 쓰기 테스트는 하지 않았다. JSON 변경이 없으므로 변경후 재적재 테스트도 불필요했다.

기존 전체검사465 passed·13 skipped·1 failed·158 warnings 결과와, 신규KREI JSON이 없는 원래코드 복사본에서 동일실패를 재현한 tests_verified.json/baseline_failure.log를 확인했다. 실패는 model_comparison/ridge/v2/tests/test_integration.py:72의 test_failed_weekly_refit_never_reuses_previous_model_and_retains_partial에서 로그에 Target prices 문자열이 없다는 assertion이다. 기존 Ridge 소스의 SHA가 당시 복사본과 같음을 확인했다. 이번 데이터 작업과 무관한 기존 재현 사례로 분리했고 Ridge 코드 수정·재학습·전체검사 재실행을 하지 않았다.

## 8. 보존·변경사항

JSON119개 전부 SHA 동일, 변경파일0개. 기존보호8,530개 변경0·누락0으로 Ridge코드/실험/스냅샷·KREI PDF120개·기존감사·merge_safety를 보존했다. 공통 수집기/적재기/SQL migration/기존테스트/README/추출가이드 SHA 동일. Git tracked diff 없음, HEAD 유지. Git reset/clean/commit/push/merge/PR 생성은 하지 않았다.

새로 생성한 것은 이 보고서와 별도 로컬 점검 결과뿐이다. 기존 감사·인수인계 보고서는 덮어쓰지 않았다. 기계판독 근거 위치: `model_comparison/ridge/v2/krei_monthly/handoff/runs/schema_compatibility_20261118`의 static_verified.json, db_verified.json, date_impact.json, json_db_diff.json, preservation_verified.json, tests.json 및 pdf_row_counts.csv. 개인DB 감사정보는 검토ZIP 기본포함 대상이 아니다.

## 9. 팀원 전달·PR 판정

**신규36 JSON은 현재 공통DB 스키마에 맞춰 팀원에게 전달할 준비가 되었다. 수정 JSON은없고2,000행을 그대로 전달한다.** 검토용 데이터 PR을 진행할 수 있다. 8583의 원본시점/연결41행 문제는 공통 수집기 담당자에게 별도 수정 요청으로 전달하고,8705 보류1건 및 기존Ridge 테스트실패를 PR설명에 명시한다. 날짜 문제가 해결된 과거학습 승인 자료로 표현하거나 DB를 지금 재적재하면 안 된다. 실제PR은 생성하지 않았다.
