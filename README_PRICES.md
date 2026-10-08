# 시세·예측 백엔드 기준

이 문서는 README의 일부이며 초기 참고 명세서보다 우선합니다.
시세 조회 API는 저장된 결과만 읽고 학습은 별도 배치에서 실행합니다.
실데이터 수집·적재는 스키마와 임시 데이터 검증 이후 진행합니다.

## 첫 구현 범위

- 시세 제공 품목 목록·이름/별칭 검색·카테고리 필터·등락률 정렬
- 전국 가격의 과거 14/30/90일 조회, 향후 달력 7일 예측
- 구매 가이드·예측 평가 지표·구간 포함률·업데이트 지연 표시
- 비로그인 조회 허용. 토큰을 보내면 검증하고, 로그인 사용자의 냉장고 잔량만 연결
- 예측 MVP는 KAMIS 원물(처음 적재할 품목은 대파). 참가격 가공품은 현재 시세 조회 가능
- 관심 품목·알림·지역별 확장·레시피 연결·외부 수집기는 후속 작업

DB의 NATIONAL 값은 수집기가 제공하는 전국 소매가입니다.
도매가·소매가를 같은 item/region/date 키에 섞어 적재하지 않습니다.
품목의 price_source/price_code/price_unit_label로 출처와 상품·단위를 식별합니다.
KAMIS 실제 코드 조합과 지역 대응표는 실데이터 적재 전에 확정합니다.

## 예측 알고리즘

Prophet과 XGBoost를 고정 결합하지 않습니다. 후보는 직전 가격 유지(LAST_PRICE),
최근 7일 평균(MEAN_7), D+1~D+7 각각 학습하는 XGBoost(XGBOOST)입니다.

입력은 현재가·1/7/14/28일 시차·7/28일 평균·변동률·변동성·목표일 요일·연중 계절·원본 가격의 경과일입니다.
날씨·생산량·명절 데이터는 실제로 확보한 뒤 성능 비교를 거쳐 추가합니다.

1. 최대 5년을 사용하고, 최근 최대 240개의 예측 시작일을 시간순으로 평가합니다.
2. 앞 절반은 모델 선택, 다음 구간은 예측 오차 보정, 마지막 구간은 최종 평가입니다.
3. 각 경계에 7일 간격을 두어 평가 정답이 다음 구간 시작 이후로 넘어가지 않게 합니다.
4. XGBoost는 각 평가 시점까지 알려진 정답으로만 학습하며 평가 중 7일마다 재학습합니다.
5. 선택 구간에서 기준 모델보다 MAPE가 1% 이상 낮고 MAE가 나쁘지 않아야 XGBoost를 선택합니다.
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
모델의 인과적 기여도·SHAP·날씨 영향을 만들어 표시하지 않습니다.

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
가격 수집기는 아직 포함하지 않으므로 실행 전에 전국 소매 가격 이력이 필요합니다.

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
