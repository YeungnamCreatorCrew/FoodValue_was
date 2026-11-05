# 시세·예측 백엔드 기준

이 문서는 README의 일부이며 초기 참고 명세서보다 우선합니다.
시세 조회 API는 저장된 결과만 읽고 학습은 별도 배치에서 실행합니다.
여러 공공 Open API(KAMIS·기상청·한국천문연구원)를 수집해 하나의 예측 파이프라인으로 통합합니다.

## 첫 구현 범위

- 시세 제공 품목 목록·이름/별칭 검색·카테고리 필터·등락률 정렬
- 전국 가격의 과거 14/30/90일 조회, 향후 달력 7일 예측
- 구매 가이드·예측 평가 지표·구간 포함률·업데이트 지연 표시
- 비로그인 조회 허용. 토큰을 보내면 검증하고, 로그인 사용자의 냉장고 잔량만 연결
- 예측 MVP는 KAMIS 원물(처음 적재할 품목은 대파). 참가격 가공품은 현재 시세 조회 가능
- Open API 수집기와 통합 파이프라인(`python -m app.price_pipeline`). 아래 [외부 원천 통합](#외부-원천-통합) 참고
- 관심 품목·알림·지역별 확장·레시피 연결은 후속 작업

DB의 NATIONAL 값은 수집기가 제공하는 전국 소매가입니다.
도매가·소매가를 같은 item/region/date 키에 섞어 적재하지 않습니다.
품목의 price_source/price_code/price_unit_label로 출처와 상품·단위를 식별합니다.
KAMIS 실제 코드 조합과 지역 대응표는 실데이터 적재 전에 확정합니다.

## 예측 알고리즘

Prophet과 XGBoost를 고정 결합하지 않습니다. 후보는 직전 가격 유지(LAST_PRICE),
최근 7일 평균(MEAN_7), D+1~D+7 각각 학습하는 XGBoost 두 가지입니다.

- XGBOOST: 현재가·1/7/14/28일 시차·7/28일 평균·변동률·변동성·목표일 요일·연중 계절·원본 가격의 경과일
- XGBOOST_EXT: XGBOOST 입력 + 수집된 외부 원천 특징(도매가·주산지 기상·공휴일). 외부 자료가 하나도 없으면 후보에서 빠집니다.

XGBoost는 가격 수준이 아니라 시작일 가격 대비 변화율을 학습합니다. 학습 기간에 없던 가격대에서도 예측이 한쪽으로 묶이지 않게 하기 위해서입니다.
외부 원천은 가격만 쓴 모델과 같은 백테스트·같은 기준으로 비교해 이길 때만 선택됩니다. 자료가 있다고 강제로 쓰지 않습니다.

1. 최대 5년을 사용하고, 최근 최대 240개의 예측 시작일을 시간순으로 평가합니다.
2. 앞 절반은 모델 선택, 다음 구간은 예측 오차 보정, 마지막 구간은 최종 평가입니다.
3. 각 경계에 7일 간격을 두어 평가 정답이 다음 구간 시작 이후로 넘어가지 않게 합니다.
4. XGBoost는 각 평가 시점까지 알려진 정답으로만 학습하며 평가 중 7일마다 재학습합니다.
5. 선택 구간에서 기준 모델보다 MAPE가 1% 이상 낮고 MAE가 나쁘지 않은 XGBoost 후보 중 MAPE가 가장 낮은 것을 선택합니다.
6. 최종 평가에서도 같은 조건을 통과해야 VALIDATED입니다. 탈락 시 선택 구간에서 정한 기준 모델로 돌아갑니다.
7. 공개용 모델은 기준일까지 확보한 정답으로 다시 학습해 7개 가격을 저장합니다.

기준 모델은 BASELINE이며 구매 권고는 HOLD, 구매일·절약액은 null입니다.
이력 부족은 INSUFFICIENT_DATA로 기록하고 가짜 정확도·예측을 만들지 않습니다.
최소 학습 표본은 시점별 120개, 평가 시작일은 200개 이상 필요합니다.
실제 최소 적재 기간은 휴일·결측에 따라 달라집니다. 운영은 3년 이상 확보를 목표로 합니다.

평가 방법 참고: [시간순 검증](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html),
[XGBoost Python API](https://xgboost.readthedocs.io/en/stable/python/python_api.html).
임시 데이터 테스트 통과는 실제 농산물 가격 예측 정확도가 입증됐다는 뜻이 아닙니다.

## 결측·예측구간

- 원본 price_daily의 결측은 채워 저장하지 않습니다. 과거 조회에서 해당 날짜 price=null입니다.
- 모델 입력만 직전 가격으로 최대 7일까지 보정하며 경과일을 입력에 포함합니다.
- 실제 가격이 없는 날은 정답 표본에서 제외합니다. 미래 가격으로 역방향 보정하지 않습니다.
- 최신 원본이 7일 넘게 지연되면 새 예측은 생성하지 않습니다.
- 시점별 오차 보정 30개, 최종 평가 10개 이상이면 절대오차의 명목 95% 분위수로 구간을 만듭니다.
- 실제 포함률(coverage)과 평균 폭(meanWidth)을 시점별 저장합니다. 표본 부족은 상하한 null입니다.
- 겹치는 시계열 오차가 독립이라고 가정하지 않으며 실제 95% 포함을 보장하지 않습니다.
- UI는 '예측구간'으로 표시하고 측정된 포함률을 함께 사용합니다. 확정적인 '95% 신뢰도' 문구는 사용하지 않습니다.

## 구매 가이드·근거

VALIDATED 결과에만 다음 규칙을 적용합니다. 가격 기준 단위는 price_unit_label입니다.

- 7일 내 최저 예상가가 현재가보다 3% 이상 낮으면 BUY_LATER, 최초 최저가 날짜와 예상 절약액 반환
- 위 조건이 아니고 D+7 가격이 현재가보다 3% 이상 높으면 BUY_NOW
- 그 외 STABLE

추천은 예측에 따른 참고 정보이며 실제 절약을 보장하지 않습니다.
factors는 현재 가격과 최근 관측 평균 등 확인 가능한 통계입니다.
외부 원천은 도매가격·주산지 기상·예측 기간의 공휴일 관측값과 선택된 모델이 그 자료를 사용했는지(usedByModel)만 표시합니다.
모델의 인과적 기여도·SHAP·날씨 영향 방향을 만들어 표시하지 않습니다.

## API

기본 경로 /api/v1/prices. JSON은 camelCase, 쿼리는 snake_case입니다.
인증이 없어도 조회 가능합니다. 잘못된 토큰을 보내면 401입니다.

| 메서드 | 경로 | 기능 |
| --- | --- | --- |
| GET | /items | 품목 목록: category, keyword, sort, page, size |
| GET | /items/{itemId} | 요약·예측·구매 가이드·내 냉장고 잔량 |
| GET | /items/{itemId}/history?days=14 | 과거 14/30/90일 가격 |
| GET | /items/{itemId}/forecast | 최신 완성된 7일 예측·평가 지표 |
| GET | /items/{itemId}/factors | 같은 실행의 관측 통계 |

category: VEGETABLE/GRAIN/FRUIT/MEAT/SEAFOOD/ETC.
sort: name(기본), change(전주 등락률 오름차순), forecast(예측 등락률 오름차순).
page=1, size=20(최대 50). 정렬값이 없는 품목은 마지막입니다.
시세 출처가 없는 품목·미존재 ID는 404, 입력 오류는 400입니다.

현재 가격은 서울 기준 오늘 이하의 최신 관측일입니다. 오늘 가격이 없으면 priceDate를 반드시 표시합니다.
전주 비교는 최신 관측일-7일 이하의 가격을 최대 7일 더 거슬러 조회합니다.
forecastBaseDate와 targetDate를 그대로 표시합니다. 지연된 예측을 '오늘 기준 +7일'로 바꾸어 표시하지 않습니다.
내 냉장고 잔량은 단위별로 합산합니다. 단/팩/g를 임의로 더하지 않습니다.

주요 상태: NO_DATA, NO_FORECAST, INSUFFICIENT_DATA, BASELINE, READY, STALE.
예측 기준일이 1일 넘게 지연되거나 원본 관측이 7일 넘게 지연되면 STALE입니다.
latestAttemptStatus로 최신 배치 실패·학습 자료 부족·실행 중 여부도 확인할 수 있습니다.

## 실행·협업

API 서버에는 무거운 예측 의존성이 필요하지 않습니다. 배치 실행 환경은 추가 패키지를 설치합니다.

```bash
uv sync --group dev --extra prices
docker compose run --rm flyway
uv run --extra prices python -m app.price_batch --item-id 1
```

item-id는 실제 대파 마스터 ID로 지정합니다. 배치는 DATABASE_URL만 요구하며 JWT/S3 키는 사용하지 않습니다.
운영은 이 명령을 서울 기준 하루 1회 OS 스케줄러에서 실행합니다. 현재 기기에 예약 작업을 자동 등록하지 않습니다.
이 명령은 이미 적재된 가격만 사용합니다. 수집부터 예측까지 한 번에 실행하려면 아래 통합 파이프라인을 사용합니다.

종료 코드: 0 성공, 1 실패, 2 자료 부족, 3 동일 품목 실행 중.
품목별 PostgreSQL advisory lock으로 중복 실행을 막습니다.
실행 이력을 먼저 저장하고, 7개 예측·가이드·성공 상태는 한 트랜잭션으로 공개합니다.
재실행은 같은 품목·기준일의 결과만 교체하고 중복을 만들지 않습니다.
실패하면 기존 완성 결과를 유지합니다. 원시 예외에 포함될 수 있는 DB 주소·비밀값은 기록하지 않습니다.
실행 중 프로세스가 종료되면 RUNNING 이력이 남을 수 있고 재실행으로 복구합니다.

V20261008_1331과 V20261008_1346을 추가했고 기존 migration은 변경하지 않습니다.
앱 테이블은 price_model_run 포함 총 22개입니다.

```powershell
uv run --group dev --extra prices pytest tests/test_price_prediction.py tests/test_prices.py -p no:cacheprovider
$env:FOODVALUE_TEST_POSTGRES='1'
uv run --group dev --extra prices pytest tests/test_prices_postgres.py tests/test_fridge_postgres.py -p no:cacheprovider
```

실제 PostgreSQL 테스트는 로컬 주소만 허용하고 생성한 테스트 데이터만 정리합니다.
전체 migration의 빈 스키마 재현성·동시 실행·실패 복구까지 확인합니다.

## 외부 원천 통합

`python -m app.price_pipeline`은 수집 → 적재 → 정형 테이블 정제 → 품목별 7일 예측을 한 번에 실행합니다.

| 기관 | API | dataset | 적재 위치 | 예측 사용 |
| --- | --- | --- | --- | --- |
| KAMIS | 기간별 품목 가격 `periodProductList` 소매(01) | RETAIL_DAILY | `price_daily`(NATIONAL) + 원본 버전 | 예측 대상 |
| KAMIS | 같은 API 도매(02) | WHOLESALE_DAILY | `external_observation` | 전일 도매가·소매/도매 비율·7/28일 변화율 |
| 기상청 | 지상(종관, ASOS) 일자료 `AsosDalyInfoService` | ASOS_DAILY | `external_observation` | 검증된 주산지 관측소의 7일 기온·최고/최저·습도·일조, 7/28일 강수 |
| 한국천문연구원 | 특일 정보 `SpcdeInfoService/getRestDeInfo` | HOLIDAY | `external_observation` | 목표일 공휴일 여부, 설날·추석까지/이후 일수(최대 45) |

- 품목은 `price_source='KAMIS'`, `food_type='RAW'`이고 `price_code`가 `품목-품종-등급`(예: `246-00-04`)이어야 합니다. 부류코드는 품목코드 첫 자리로 정합니다.
- KAMIS 응답은 `countyname='평균'` 행만 전국 값으로 적재합니다. 도매가는 `price_daily`에 섞지 않습니다.
- 기상은 `item_weather_station.mapping_status='VERIFIED'`인 관측소만 사용합니다. `share`가 없으면 같은 비중, `months`·유효기간 밖의 관측소는 제외합니다.
- 수집 실행마다 `external_collection_run`에 상태(SUCCESS/NO_DATA/PARTIAL/AUTH_ERROR/NETWORK_ERROR/FAILED/SKIPPED)와 요청·수신·삽입 건수를 남깁니다.
- 같은 원천 키·같은 내용은 다시 저장하지 않습니다. 원천이 값을 수정하면 새 버전으로 보존하고 예측은 최신 수집본을 사용합니다.
- 증분 수집은 저장된 최신 관측일 14일 전부터 다시 받습니다. 처음이면 1,830일(모델 최대 5년)을 백필합니다. 공휴일은 임시공휴일 반영을 위해 올해·내년을 매번 다시 받습니다.
- 인증키가 없으면 해당 원천은 SKIPPED로 기록하고 나머지 수집과 예측은 계속합니다. 인증키는 이력·출력에 남기지 않습니다.

### 시점 규칙 (미래 정보 누수 방지)

예측 시작일 d의 입력은 d − 공개지연일 이하에 관측된 값만 사용합니다. 백테스트·최종 예측 모두 같은 규칙입니다.

| 원천 | 공개지연 | 근거 |
| --- | --- | --- |
| KAMIS 도매가 | 1일 | 배치 시각에 당일 도매가가 공표되지 않았을 수 있어 보수적으로 둠 |
| ASOS 일자료 | 1일 | 기상청은 전일까지의 일자료를 제공 |
| 공휴일 | 목표일 값 사용 | 법정공휴일은 미리 확정. 임시공휴일은 과거 백테스트에서 실제보다 일찍 알려진 것으로 취급됨 |

- 외부 값이 7일 넘게 비면 결측(NaN)으로 두고 XGBoost 결측 분기에 맡깁니다. 0이나 평균으로 채우지 않습니다. 단, ASOS의 빈 강수량은 무강수(0mm)로 해석합니다.
- 공휴일 자료를 수집하지 않은 연도는 '공휴일 없음'으로 보지 않고 결측으로 둡니다.
- 원천 수정 이력이 있으면 백테스트도 최신 수정본을 사용합니다. 수정 전 값으로 재현하는 시점 복원은 하지 않습니다.
- 공개지연 값은 기관 공지 기준의 가정입니다. 원천에서 공표 시각을 받지 못해 `publication_status`는 UNKNOWN으로 저장됩니다.

`metrics`에는 `candidates`, `featureSets`, `externalGroups`, `externalCoverage`(최종 평가 시점에서 그룹별 값이 채워진 비율)가 함께 저장됩니다.
합성 자료 테스트(도매가가 소매가를 5일 앞서는 자료)에서 XGBOOST_EXT가 선택·검증되는 것을 확인했습니다. 실제 시장에서의 효과는 실데이터 백테스트로만 판단합니다.

### 실행

`.env`에 `KAMIS_CERT_KEY`, `KAMIS_CERT_ID`, `DATA_GO_KR_SERVICE_KEY`를 추가합니다. 공공데이터포털 키는 인코딩·디코딩 키 모두 사용할 수 있습니다.
공공데이터포털에서 기상청 ASOS 일자료와 한국천문연구원 특일 정보 활용신청이 각각 필요합니다.

```bash
uv sync --extra prices
docker compose run --rm flyway
uv run --extra prices python -m app.price_pipeline --start 2021-11-01 --collect-only   # 최초 백필
uv run --extra prices python -m app.price_pipeline                                     # 매일: 증분 수집 + 예측
uv run --extra prices python -m app.price_pipeline --item-id 1 --predict-only
```

`--item-id`는 반복 지정할 수 있고 생략하면 모든 KAMIS 원물 품목이 대상입니다.
종료 코드: 0 성공, 1 예측 실패, 2 자료 부족 또는 일부 원천 수집 실패, 3 동일 품목 실행 중. 결과는 JSON 한 줄로 출력합니다.

주산지 관측소는 근거를 확인한 뒤 직접 등록합니다. 검증 전에는 `CANDIDATE`로 두면 예측에 쓰이지 않습니다.

```sql
INSERT INTO item_weather_station(item_id, station_code, station_name, producing_region,
    mapping_status, months, share, rationale)
VALUES (<대파 item_id>, '<ASOS 지점번호>', '<지점명>', '<주산지>', 'VERIFIED', NULL, NULL, '<근거 자료>');
```

### 정형 테이블 정제

수집 직후(`--predict-only` 제외) 원천을 V2 정형 테이블로 정제합니다. 같은 키는 갱신하므로 다시 실행해도 결과가 같습니다.
원본은 계속 `external_observation`에 보존하고, 예측 모델은 여전히 원본(관측소 단위)을 사용합니다.

| 테이블 | 정제 규칙 |
| --- | --- |
| `weather_daily` (ACTUAL) | 전국 ASOS 관측소(`data_go_kr.NATIONAL_STATIONS`, 95곳) 단순 평균. 폭염(최고 33℃↑)·호우(80mm↑)·한파(최저 −12℃↓) 관측소 비율(%), 자료가 있는 관측소 수 |
| `calendar_day` | 공휴일을 수집한 연도의 모든 날짜. 요일(1=월), 공휴일명(대체·임시 포함), 음력(천문연 자료 기반 `korean-lunar-calendar`), 휴장일 |
| `calendar_event` | 공휴일명이 설날·추석인 연속 기간. 영향 기간은 시작 D−14 ~ 종료 D+3 |
| `price_change_history` | `price_daily`(NATIONAL)의 기준일 대비 1~7일 뒤 변동률(%) |

- 전국 집계 관측소는 수집 대상에 항상 포함됩니다(첫 백필 약 95곳 × 6년 요청, 이후 매일 관측소당 1회). 폐지 지점은 무자료로 집계에서 빠집니다. 목록은 기상자료개방포털 지점 목록과 대조해 갱신합니다.
- `is_market_closed`는 원천이 없어 규칙으로 정합니다: 일요일과 설날·추석 연휴. 대체공휴일은 휴장으로 보지 않습니다.
- 변동률의 휴장일 기준가는 직전 거래일 가격(최대 7일)을 쓰고, 목표일까지 새 거래가 없으면 0%를 만들지 않고 제외합니다. 윤년 2월 29일은 02-28로 합치며 같은 해 02-28 행이 우선합니다.
- 공휴일을 수집하지 않은 연도는 `calendar_day`에 넣지 않습니다(공휴일 없음으로 단정하지 않음).
- 매일 실행은 이번에 수집한 기간만 다시 계산합니다. 달력은 수집된 전 연도를 갱신합니다.
- `weather_daily`의 FORECAST, `item_production`, `event_item_weight`는 원천 수집기가 없어 채우지 않습니다.

```bash
uv run --group dev --extra prices pytest tests/test_collectors.py tests/test_exogenous.py tests/test_warehouse.py tests/test_price_prediction.py -p no:cacheprovider
FOODVALUE_TEST_POSTGRES=1 uv run --group dev --extra prices pytest tests/test_pipeline_postgres.py -p no:cacheprovider
```

통합 테스트는 가짜 Open API 응답으로 수집·중복 방지·수정 버전·인증키 누락·예측 공개까지 확인하며 실제 API를 호출하지 않습니다.
