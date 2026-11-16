# AutoARIMA 2차 비교(p2, EVENT) 검증 제출

공식 실행 ID: `arima-p2-20261112-01`; config ID: `fba906ce`; 실행 커밋 `c6abef3`(설정 `model_comparison/autoarima/config_p2_event.json`).
1차 결과: `experiments/arima-p1-20261112-01`(config ID `fe2fa17f`).

**EVENT 효과는 오차 범위 안이고, 검증 관문은 여전히 통과하지 못했다(1X 2O 3X 4O 5X).**

## 설정

1차 선택 설정(비계절, 로그, 요일 외생변수, 탐색 범위 동일)을 그대로 두고 EVENT 묶음만 더했다. 2차 추가 튜닝은 하지 않았다(`tuning_log.csv` 0회).

- `extra_features: ["EVENT"]`, `feature_set: "base_v1+EVENT"`, `params.event_exog: true`
- EVENT 4개 열(`days_to_major_holiday`, `days_from_major_holiday`, `target_in_event_window`, `target_prev_day_holiday`)을 요일 더미와 함께 ARIMA 회귀 외생변수(X)로 넣는다. 미래 7일 값은 `inputs.features`의 목표일 값을 그대로 쓴다.
- 학습 구간의 주말·휴장일 값은 공통 입력에서 되살린다(재구성 규칙과 정확도 점검은 `model_comparison/autoarima/README_MODEL.md`).
- AutoARIMA 2차는 EVENT만 해당한다. MARKET·NATIONAL_WEATHER·MACRO·PRODUCTION은 기준일 이후 값이 필요해 N/A(§5.2).

## 결과(metrics.json)

| 항목 | p1 | p2 (EVENT) | 차이 |
|---|---:|---:|---:|
| policy macro MAPE | 4.854893% | 4.850527% | −0.004366%p (상대 −0.09%) |
| naive 대비 상대 개선율 | +1.173605% | +1.262480% | |
| macro rMAE | 0.999302 | 0.997655 | |
| naive보다 나은 계열 | 4/10 | 5/10 | 양파 소매가 우위로 바뀜 |
| 평가 대상 성공률 | 99.2018% | 99.2018% | |
| 부트스트랩 Δ 95% | [-0.014363, 0.149254] | [-0.012299, 0.148238] | |
| model_only macro MAPE | 4.863111% | 4.858635% | |
| 전체 실행 시간 | 1,933.8초 | 2,608.5초 | +35% |

naive macro MAPE 4.912547%. 상태: `OK=16793`, `NO_INPUT=287`(1차와 같음, 깐마늘 도매 원천 결측 기간).

| 관문 | 기준 | 판정 |
|---:|---|---|
| 1 | naive 대비 상대 개선율 ≥ 5% | 미통과 |
| 2 | macro rMAE < 1 | 통과 |
| 3 | 10개 중 6개 이상 계열 우위 | 미통과(5/10) |
| 4 | 평가 대상 성공률 ≥ 99% | 통과 |
| 5 | 부트스트랩 Δ 95% 하한 > 0 | 미통과 |

계열별 policy MAPE p1 → p2(naive): 대파 소매 5.210 → 5.215(5.198), 대파 도매 5.844 → 5.843(5.941), 양파 도매 2.934 → 2.938(3.184), 양파 소매 4.877 → 4.819(4.873), 깐마늘 도매 0.925 → 0.914(0.800), 깐마늘 소매 3.760 → 3.752(3.830), 배추 소매 4.632 → 4.683(5.241), 배추 도매 7.424 → 7.432(7.193), 무 소매 4.300 → 4.263(4.249), 무 도매 8.643 → 8.645(8.616).

## 해석

EVENT를 넣으면 macro MAPE가 0.0044%p 낮아지지만, 팀 동률 기준(상대 2%)보다 훨씬 작고 계열별로도 좋아진 곳(양파 소매·무 소매)과 나빠진 곳(배추 소매)이 섞여 있다. 실행 시간은 35% 늘었다. p2 결과로 p1 순위를 바꾸지 않는다.
