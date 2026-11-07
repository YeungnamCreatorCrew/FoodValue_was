# 가격 예측 모델 변경 기록

모델을 바꿀 때마다 버전과 변경 내용, 실데이터 백테스트 결과를 여기에 남깁니다. 발표 자료도 이 기록을 바탕으로 만듭니다.
버전 문자열은 `app/services/price_prediction.py`의 `MODEL_VERSION`과 같고, 예측 결과(`price_model_run`)와 백테스트(`backtest_run`)에도 함께 저장됩니다.

## 기록 규칙

- 예측값이 달라지는 변경(특징·후보 모델·하이퍼파라미터·선택 규칙)을 하면 `MODEL_VERSION`을 올리고 아래 표와 상세 기록에 한 항목을 추가합니다.
- 성능은 **실데이터 백테스트**(`python -m app.price_backtest` 또는 `python -m app.price_tuning`)의 MAPE와, 직전 가격 유지(naive) 대비 개선율로 적습니다.
  합성 자료로만 확인한 결과는 "합성 자료"라고 표시합니다.
- 비교할 때는 같은 품목·시장·기간·기준일 간격을 씁니다. 기간과 실행 명령도 함께 적습니다.
- 외부변수 가중치 설계와 실험은 [가중치 결정 기록](README_WEIGHTING.md)에 자세히 있습니다.

## 버전 요약

| 버전 | 날짜 | 커밋 | 핵심 변경 | 검증 |
| --- | --- | --- | --- | --- |
| `direct-xgb-v1` | 2026-10-08 | af66b76 | 시점별(D+1~D+7) 직접 예측 XGBoost, 직전가·7일 평균 기준 모델과 백테스트로 비교 | 합성 자료 |
| `direct-xgb-v2-change-exog` | 2026-11-05 | 265b50e | 가격 수준 대신 변화율 학습, Open API 외부 원천(도매가·기상·공휴일 등) 특징 추가(XGBOOST_EXT) | 합성 자료 |
| `direct-xgb-v3-weighted-exog` | 2026-11-05 ~ 06 | 326f77a, d8af3d9 | 외부변수 묶음별 전문가 모델의 가중 결합(XGBOOST_WEIGHTED), 소매·도매 계열별 예측, 백테스트 결과 저장 | 합성 자료 |
| (진행 중) | 2026-11-07 | feat/model-tuning | XGBoost 하이퍼파라미터 튜닝: 실데이터 백테스트로 후보 비교 | 실데이터 백테스트 예정 |

## 상세 기록

### direct-xgb-v1 (2026-10-08)

- 후보: LAST_PRICE(직전 가격 유지), MEAN_7(최근 7일 평균), XGBOOST(가격 특징만).
- XGBoost 설정: `n_estimators=80, max_depth=3, learning_rate=0.05`.
- 시간순 백테스트로 선택 구간에서 기준 모델보다 MAPE가 1% 이상 낮을 때만 XGBoost를 선택.

### direct-xgb-v2-change-exog (2026-11-05)

- XGBoost가 가격 수준 대신 기준일 대비 변화율을 학습하도록 변경.
- 외부 원천 특징을 모두 넣은 XGBOOST_EXT 후보 추가. 가격만 쓴 모델과 같은 백테스트에서 이길 때만 선택.
- 하이퍼파라미터는 v1과 같음.

### direct-xgb-v3-weighted-exog (2026-11-05 ~ 06)

- XGBOOST_WEIGHTED 추가: 가격 모델 예측에 외부변수 묶음(시장·기상·달력·계절·거시)별 전문가 모델의 수정분을 0~1 가중치로 결합.
- 가격 계열(소매·도매)별로 따로 예측. 과거 기준일 재현 백테스트(`app/price_backtest.py`)와 결과 저장 테이블 추가.
- 하이퍼파라미터는 v1과 같음. 상세 실험은 [가중치 결정 기록](README_WEIGHTING.md).

### 하이퍼파라미터 튜닝 (2026-11-07, 진행 중)

- 하이퍼파라미터를 `XGB_PARAMS`로 분리하고 `FOODVALUE_XGB_PARAMS` 환경변수로 실험값을 넣을 수 있게 함. 기본값은 v3와 같아 예측 결과는 바뀌지 않음.
- `app/price_tuning.py`: 후보 파라미터를 튜닝 구간 백테스트로 비교하고, 겹치지 않는 확인 구간에서 현재 기본값과 다시 비교.
- 실데이터 결과와 채택 여부는 백테스트 후 이 항목에 기록하고, 기본값을 바꾸면 `MODEL_VERSION`을 올립니다.
