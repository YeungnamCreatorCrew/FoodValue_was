# 시세·예측 백엔드 기준

이 문서는 README의 일부이며 초기 참고 명세서보다 우선합니다.
시세 조회 API는 저장된 결과만 읽고 학습은 별도 배치에서 실행합니다.
여러 공공 Open API(KAMIS·기상청·한국천문연구원)를 수집해 하나의 예측 파이프라인으로 통합합니다.

## 첫 구현 범위

- 시세 제공 품목 목록·이름/별칭 검색·카테고리 필터·등락률 정렬
- 전국 가격의 과거 14/30/90일 조회, 향후 달력 7일 예측
- 구매 가이드·예측 평가 지표·구간 포함률·업데이트 지연 표시
- 비로그인 조회 허용. 토큰을 보내면 검증하고, 로그인 사용자의 냉장고 잔량만 연결
- 예측 대상은 KAMIS 가격 계열(소매·도매, 처음 적재한 품목은 대파). 참가격 가공품은 가격 계열이 없어 시세·예측 API에서 빠짐
- Open API 수집기와 통합 파이프라인(`python -m app.price_pipeline`). 아래 [외부 원천 통합](#외부-원천-통합) 참고
- 관심 품목·알림·지역별 확장·레시피 연결은 후속 작업

가격은 가격 계열(`price_series`) 단위로 저장·예측합니다. 계열 = 품목 × 시장(RETAIL 소매·WHOLESALE 도매)이며
KAMIS 품목·품종·등급 코드(예: `246`-`00`-`04`)와 가격 단위(`unit_quantity`·`unit`, 예: 1 kg)를 가집니다.
소매·도매 계열 모두 예측 대상이고, 각 계열은 같은 품목의 상대 시장 가격을 예측 변수(MARKET 묶음)로 씁니다.
지역은 전국(KAMIS '평균')만 씁니다. API는 `market` 쿼리 파라미터(기본 RETAIL)로 계열을 고릅니다.

## 예측 알고리즘

Prophet과 XGBoost를 고정 결합하지 않습니다. 후보는 직전 가격 유지(LAST_PRICE),
최근 7일 평균(MEAN_7), D+1~D+7 각각 학습하는 XGBoost 세 가지입니다.

- XGBOOST: 현재가·1/7/14/28일 시차·7/28일 평균·변동률·변동성·목표일 요일·연중 계절·원본 가격의 경과일
- XGBOOST_EXT: XGBOOST 입력 + 수집된 외부 원천 특징 전부를 한 모델에 넣습니다. 외부 자료가 하나도 없으면 후보에서 빠집니다.
- XGBOOST_WEIGHTED: XGBOOST 예측 b에 외부변수 묶음(시장·기상·달력·계절·거시)별 전문가 모델 e_k의 수정분을
  가중 결합합니다. `b + Σ w_k (e_k − b)`, `0 ≤ w_k ≤ 1`. 가중치는 예측 시작일까지 정답이 확인된 과거 예측 오차로만
  7일마다 다시 학습하고, 시간순 교차검증에서 일관되게 오차를 줄이지 못한 묶음은 0입니다.
  결정 방식과 실험 기록은 [가중치 결정 기록](README_WEIGHTING.md)을 참고합니다.

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

VALIDATED 결과에만 다음 규칙을 적용합니다. 가격 기준 단위는 계열의 `unit_quantity`·`unit`입니다.

- 7일 내 최저 예상가가 현재가보다 3% 이상 낮으면 BUY_LATER, 최초 최저가 날짜와 예상 절약액 반환
- 위 조건이 아니고 D+7 가격이 현재가보다 3% 이상 높으면 BUY_NOW
- 그 외 STABLE

추천은 예측에 따른 참고 정보이며 실제 절약을 보장하지 않습니다.
factors는 현재 가격과 최근 관측 평균 등 확인 가능한 통계입니다.
외부 원천은 상대 시장 가격·주산지 기상·예측 기간의 공휴일 관측값과 선택된 모델이 그 자료를 사용했는지(usedByModel)만 표시합니다.
XGBOOST_WEIGHTED가 선택되면 원천별 `modelWeight`와 '외부변수 가중치'(kind=MODEL) 항목을 함께 표시합니다.
이 값은 과거 예측 오차로 학습한 결합 비중이며 인과적 영향이 아닙니다.
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
macOS는 XGBoost가 쓰는 OpenMP 런타임이 따로 필요합니다(`brew install libomp`). 없으면 배치·백테스트가 `ModelDependencyError`와 안내 메시지를 출력합니다.

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

`python -m app.price_pipeline`은 수집 → 적재 → 정형 테이블 정제 → 가격 계열(소매·도매)별 7일 예측을 한 번에 실행합니다.

| 기관 | API | dataset | 적재 위치 | 예측 사용 |
| --- | --- | --- | --- | --- |
| KAMIS | 최근 1년: 기간별 품목 가격 `periodProductList`, 그 이전: 일별 부류별 가격 `dailyPriceByCategoryList` 소매(01) | RETAIL_DAILY | `external_observation` → `price_daily`(소매 계열) | 예측 대상. 도매 계열 예측에는 상대 시장 가격 |
| KAMIS | 같은 API 도매(02) | WHOLESALE_DAILY | `external_observation` → `price_daily`(도매 계열) | 예측 대상. 소매 계열 예측에는 상대 시장 가격(전일 값·대상/상대 비율·7/28일 변화율) |
| 기상청 | 지상(종관, ASOS) 일자료 `AsosDalyInfoService` | ASOS_DAILY | `external_observation` → `weather_daily` | 검증된 주산지 관측소의 7일 기온·최고/최저·습도·일조, 7/28일 강수. 전국 평균 7일 기온·28일 강수·폭염/호우/한파 지수 |
| 한국천문연구원 | 특일 정보 `SpcdeInfoService/getRestDeInfo` | HOLIDAY | `external_observation` → `calendar_event` | 목표일 공휴일 여부, 설날·추석까지/이후 일수(최대 45), 목표일의 명절 영향기간 여부·명절 가격 압력 |
| (파생) | `price_daily` | — | `price_change_history` | 과거 최대 5년 같은 시기(±3일)·같은 시점 변동률 평균 |
| KOSIS | 농작물생산조사 통계표 `statisticsParameterData` | CROP_PRODUCTION | `external_observation` → `item_production` | 최신 공개 연도 생산량의 전년 대비 증감(Y년 값은 Y+1년 6월 30일부터) |
| 한국은행 | ECOS 통계검색 `StatisticSearch` 731Y001 | EXCHANGE_RATE_DAILY | `external_observation` → `exchange_rate_daily` | 원/미국달러 7·28일 변화율(1일 지연) |
| 기상청 | 단기예보 `VilageFcstInfoService_2.0/getVilageFcst` | VILAGE_FCST_DAILY | `external_observation` | 사용 안 함(과거 발표본이 없어 백테스트 불가). `weather_daily` FORECAST용 |

- 수집·예측 대상은 `price_series`에 소매 계열이 있는 품목입니다. 계열 코드는 `품목-품종-등급`(예: `246-00-04`)이고 부류코드는 품목코드 첫 자리로 정합니다.
- KAMIS 응답은 `countyname='평균'` 행만 전국 값으로 보존합니다. `price_daily`는 원본의 최신 버전에서 계열별로 다시 만들고
  (`warehouse_service.refresh_price_daily`, 수집 직후와 정제 단계에서 같은 함수), 만든 원본 행을 `observation_id`로 남깁니다.
- `periodProductList`는 로컬 실측에서 최근 1년치만 돌려주고 그 이전 기간은 시간 초과가 났습니다. 그래서 최근 364일만 이 API로 받고,
  더 오래된 날짜는 `dailyPriceByCategoryList`를 평일마다 1회(4개 병렬) 호출해 품목·품종·등급이 일치하는 행의 당일 가격(`dpr1`)을 씁니다.
  당일 열(`day1`)의 (월/일)이 요청일과 다르면 저장하지 않고, 코드 열(`item_code`·`kind_code`·`rank_code`)이 없는 응답은
  `KAMIS_UNEXPECTED_DAILY_RESPONSE`로 실패 처리합니다(추측해서 저장하지 않음). 이 응답 형식은 공개 규격 기준이며 실제 응답으로 한 번 확인이 필요합니다.
- 기상은 `item_weather_station.mapping_status='VERIFIED'`인 관측소만 사용합니다. `share`가 없으면 같은 비중, `months`·유효기간 밖의 관측소는 제외합니다.
- 수집 실행마다 `external_collection_run`에 상태(SUCCESS/NO_DATA/PARTIAL/AUTH_ERROR/NETWORK_ERROR/FAILED/SKIPPED)와 요청·수신·삽입 건수를 남깁니다.
- 같은 원천 키·같은 내용은 다시 저장하지 않습니다. 원천이 값을 수정하면 새 버전으로 보존하고 예측은 최신 수집본을 사용합니다.
- 증분 수집은 저장된 최신 관측일 14일 전부터 다시 받습니다. 처음이면 1,830일(모델 최대 5년)을 백필합니다. 공휴일은 임시공휴일 반영을 위해 올해·내년을 매번 다시 받습니다.
- 인증키가 없으면 해당 원천은 SKIPPED로 기록하고 나머지 수집과 예측은 계속합니다. 인증키는 이력·출력에 남기지 않습니다.

### 시점 규칙 (미래 정보 누수 방지)

예측 시작일 d의 입력은 d − 공개지연일 이하에 관측된 값만 사용합니다. 백테스트·최종 예측 모두 같은 규칙입니다.

| 원천 | 공개지연 | 근거 |
| --- | --- | --- |
| KAMIS 상대 시장 가격 | 1일 | 배치 시각에 당일 가격이 공표되지 않았을 수 있어 보수적으로 둠 |
| ASOS 일자료 | 1일 | 기상청은 전일까지의 일자료를 제공 |
| 공휴일·명절 영향기간 | 목표일 값 사용 | 법정공휴일은 미리 확정. 임시공휴일은 과거 백테스트에서 실제보다 일찍 알려진 것으로 취급됨 |
| 전국 기상(`weather_daily`)·환율 | 1일 지연 | ASOS·상대 시장 가격과 같은 보수적 가정 |
| 과거 변동률(`price_change_history`) | 기준일 b·시점 h 값은 b+h ≤ 예측 시작일 | 그 변동률을 만든 가격이 확인된 뒤에만 사용 |
| 명절 가격 압력 | 영향기간의 7일 뒤 가격이 확인된 명절만 | 2개 연도 미만이면 결측 |
| 연간 생산량 | Y년 값은 Y+1년 6월 30일부터 | KOSIS가 최초 공표일을 주지 않아 둔 가정 |

- 외부 값이 7일 넘게 비면 결측(NaN)으로 두고 XGBoost 결측 분기에 맡깁니다. 0이나 평균으로 채우지 않습니다. 단, ASOS의 빈 강수량은 무강수(0mm)로 해석합니다.
- 공휴일 자료를 수집하지 않은 연도는 '공휴일 없음'으로 보지 않고 결측으로 둡니다.
- 원천 수정 이력이 있으면 백테스트도 최신 수정본을 사용합니다. 수정 전 값으로 재현하는 시점 복원은 하지 않습니다.
- 공개지연 값은 기관 공지 기준의 가정입니다. 원천에서 공표 시각을 받지 못해 `publication_status`는 UNKNOWN으로 저장됩니다.

`metrics`에는 `candidates`, `featureSets`, `externalGroups`, `externalCoverage`(최종 평가 시점에서 그룹별 값이 채워진 비율),
`weighting`(묶음 구성·공개 가중치·κ·평가 구간 평균 가중치)이 함께 저장됩니다. 모델 버전은 `direct-xgb-v5-huber`입니다(버전별 변경은 [모델 변경 기록](model_comparison/xgboost/README_MODEL.md)).
합성 자료 테스트(도매가가 소매가를 5일 앞서는 자료)에서 외부 원천 모델(XGBOOST_EXT 또는 XGBOOST_WEIGHTED)이 선택·검증되고, 무관한 환율 묶음의 가중치는 0이 되는 것을 확인했습니다. 실제 시장에서의 효과는 실데이터 백테스트로만 판단합니다.

### 실행

`.env`에 `KAMIS_CERT_KEY`, `KAMIS_CERT_ID`, `DATA_GO_KR_SERVICE_KEY`, `KOSIS_API_KEY`, `ECOS_API_KEY`를 추가합니다. 공공데이터포털 키는 인코딩·디코딩 키 모두 사용할 수 있습니다.
공공데이터포털에서 기상청 ASOS 일자료·단기예보와 한국천문연구원 특일 정보 활용신청이 각각 필요합니다.

```bash
uv sync --extra prices   # macOS는 XGBoost용 OpenMP가 필요: brew install libomp
docker compose run --rm flyway
uv run --extra prices python -m app.price_pipeline --start 2016-01-01 --collect-only   # 최초 백필(1시간 안팎. 학습은 최근 5년, 그 이전은 과거 동기 변동률에 사용. model_comparison/xgboost/README_MODEL.md 참고)
uv run --extra prices python -m app.price_pipeline                                     # 매일: 증분 수집 + 예측
uv run --extra prices python -m app.price_pipeline --item-id 1 --predict-only
```

`--item-id`는 반복 지정할 수 있고 생략하면 가격 계열이 있는 모든 품목이 대상입니다. 품목마다 소매·도매 계열을 각각 예측합니다.
종료 코드: 0 성공, 1 예측 실패, 2 자료 부족 또는 일부 원천 수집 실패, 3 동일 계열 실행 중. 결과는 JSON 한 줄로 출력합니다.

### 과거 기준일 재현 백테스트

과거 기준일마다 그날까지의 자료로만 7일 예측을 만들고, 이후 실제 가격과 비교합니다. 기본은 DB를 읽기만 합니다.
`--save`를 주면 결과를 `backtest_run`(조건·요약·커밋)·`backtest_origin`(기준일별 선택 모델)·`backtest_point`(시점별 비교)에 남깁니다.
운영 예측 테이블(`price_model_run`·`price_forecast`)에는 어떤 경우에도 쓰지 않습니다.
운영 배치와 같은 입력 로딩(`price_batch_service.load_inputs`)·모델·공개지연 규칙을 씁니다.

```bash
uv run --extra prices python -m app.price_backtest --item-id 1 --start 2026-05-01 --end 2026-10-27 --every 7 --workers 4 --csv backtest.csv
uv run --extra prices python -m app.price_backtest --item-id 1 --market WHOLESALE --start 2026-05-01 --end 2026-10-27 --save --note '도매 기준선'
```

출력 JSON의 `summary`에 전체·시점별·선택 모델별 MAPE/MAE, 직전 가격 유지(naive) 대비 개선율, 방향 적중률(실제로 움직인 날만), 예측구간 포함률이 있고,
`runs`에 기준일별 선택 모델·검증 여부·외부변수 가중치가 있습니다. 기준일당 수십 초가 걸리므로 `--workers`로 병렬 실행합니다.
원천 수정 이력은 최신 수정본으로 재현합니다.

주산지 관측소는 근거를 확인한 뒤 직접 등록합니다. 검증 전에는 `CANDIDATE`로 두면 예측에 쓰이지 않습니다.

```sql
INSERT INTO item_weather_station(item_id, station_code, station_name, producing_region,
    mapping_status, months, share, rationale)
VALUES (<대파 item_id>, '<ASOS 지점번호>', '<지점명>', '<주산지>', 'VERIFIED', NULL, NULL, '<근거 자료>');
```

### 정형 테이블 정제

수집 직후(`--predict-only` 제외) 원천을 정형 테이블로 정제합니다. 같은 키는 갱신하므로 다시 실행해도 결과가 같습니다.
원본은 계속 `external_observation`에 보존합니다. 주산지 기상·공휴일은 원본(관측소 단위)을, 계열 가격·전국 기상·명절 기간·과거 변동률·생산량·환율은 정형 테이블을 예측에 사용합니다.

| 테이블 | 정제 규칙 |
| --- | --- |
| `price_daily` | 계열 코드로 저장된 KAMIS 원본(키 `{코드}:{날짜}`)의 최신 버전. 가격이 없거나 0 이하면 만들지 않음 |
| `weather_daily` (ACTUAL) | 전국 ASOS 관측소(`data_go_kr.NATIONAL_STATIONS`, 97곳) 단순 평균. 폭염(최고 33℃↑)·호우(80mm↑)·한파(최저 −12℃↓) 관측소 비율(%), 자료가 있는 관측소 수 |
| `weather_daily` (FORECAST) | 단기예보 17개 시·도 대표 격자의 최신 발표본 평균. 오늘 이후 날짜를 덮어쓰고 지난 날짜는 마지막 예보로 남김. 일조시간은 예보 항목이 없어 NULL |
| `calendar_day` | 공휴일을 수집한 연도의 모든 날짜. 요일(1=월), 공휴일명(대체·임시 포함), 음력(천문연 자료 기반 `korean-lunar-calendar`), 휴장일 |
| `calendar_event` | 공휴일명이 설날·추석인 연속 기간. 영향 기간은 시작 D−14 ~ 종료 D+3 |
| `item_production` | KOSIS 농작물생산조사 연간 전국 생산량(PRODUCTION·YEAR·톤·확정치) |
| `exchange_rate_daily` | ECOS 일별 원/미국달러 매매기준율(영업일만). `V20261105_1500` migration으로 추가 |
| `price_change_history` | 계열별 `price_daily`의 기준일 대비 1~7일 뒤 변동률(%) |
| `event_item_weight` (LEARNED) | 품목별(소매 계열 기준) 설날·추석 가격 압력(−1~1). 예측의 EVENT 특징과 같은 함수(`exogenous.event_weight`)로 오늘 기준 계산. MANUAL 행은 덮어쓰지 않음 |

- 전국 관측소 97곳은 2026-11-03 자료로 지점번호 1~339를 전수 조회해 응답이 있는 지점만 남긴 목록입니다. 신설 지점은 설치 이전 기간이 무자료라 그 날짜 집계에서 빠집니다(`station_count`로 확인).
- ASOS는 지점마다 기간 전체를 한 번에 요청하고 999행 단위로 페이지를 넘깁니다. 실측: 5년 백필 194회 요청·177,073행·약 6분, 매일 증분 97회·약 40초(4개 병렬).
- 단기예보는 매 실행마다 최신 발표본(발표 15분 후부터) 17회 요청합니다. 24시간 값이 모두 있는 날만 평균기온·강수합·습도를 만들고, 강수량 범주는 범위 중간값, '1mm 미만'은 0.5mm, 'Nmm 이상'은 N mm로 환산합니다.
- 음력은 2021~2027년 2,556일을 천문연 음양력 API(`LrsrCldInfoService`)와 대조해 모두 일치함을 확인했습니다(2023 윤2월, 2025 윤6월 포함).
- `is_market_closed`는 KAMIS 가격 미조사일(시세 결측이 정상인 날)입니다: 토·일과 모든 공휴일(대체공휴일 포함).
  2025-12~2026-10 KAMIS 대파 도매·소매 실데이터의 결측일과 정확히 일치함을 확인했습니다. 가락시장 부류별 실제 휴장 일정(예: 채소 전날 저녁 경매 후 휴장)과는 다를 수 있습니다.
- 변동률의 휴장일 기준가는 직전 거래일 가격(최대 7일)을 쓰고, 목표일까지 새 거래가 없으면 0%를 만들지 않고 제외합니다. 윤년 2월 29일은 02-28로 합치며 같은 해 02-28 행이 우선합니다.
- 공휴일을 수집하지 않은 연도는 `calendar_day`에 넣지 않습니다(공휴일 없음으로 단정하지 않음).
- 매일 실행은 이번에 수집한 기간만 다시 계산합니다. 달력은 수집된 전 연도를 갱신합니다.
- KOSIS 생산량은 `item.name`이 `kosis.PRODUCTION_SERIES`의 키(대파·양파·마늘·배추·무·감자·사과 등 21개)와 같은 품목만 연결합니다. 통계표·항목 코드는 KOSIS 메타 API로 확인한 값입니다.
  다른 이름을 쓰는 품목은 이 사전에 추가합니다. 수정 공표 반영을 위해 매 실행 최근 6년(품목당 1회 요청)을 다시 받고, `LST_CHN_DE`(최종 수정일)를 공표 시점으로 저장합니다.
- ECOS는 경로형 URL이라 끝에 `?`가 붙으면 무자료(INFO-200)를 돌려줍니다. 파라미터가 없으면 `?`를 붙이지 않습니다(로컬 실측으로 확인된 문제).
- KAMIS·ECOS는 해외 서버(클라우드 개발 환경)에서는 연결이 끊깁니다. 국내 IP에서 실행합니다. 서버에서 아래로 확인합니다.
  `uv run --extra prices python -c "from app.collectors import ecos; from app.collectors.http import fetch_json; import os, datetime as d; print(ecos.collect(fetch_json, key=os.environ['ECOS_API_KEY'], start=d.date(2026,10,1), end=d.date.today()).records[:3])"`
- `item_production`의 가락시장 반입량(ARRIVAL·DAY)·KREI 전망치는 아직 채우지 않습니다.

```bash
uv run --group dev --extra prices pytest tests/test_collectors.py tests/test_exogenous.py tests/test_weighting.py tests/test_warehouse.py tests/test_price_prediction.py -p no:cacheprovider
FOODVALUE_TEST_POSTGRES=1 uv run --group dev --extra prices pytest tests/test_pipeline_postgres.py -p no:cacheprovider
```

통합 테스트는 가짜 Open API 응답으로 수집·중복 방지·수정 버전·인증키 누락·예측 공개까지 확인하며 실제 API를 호출하지 않습니다.
