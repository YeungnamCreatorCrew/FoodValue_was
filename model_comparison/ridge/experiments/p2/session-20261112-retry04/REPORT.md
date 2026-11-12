# Ridge p2 Validation 실행 보고서

## 1. 개요 및 실제 실행 상태

전체 자동화 상태: **COMPLETED**. COMPLETED는 실행·감사 완료이며 채택 관문 통과와 구분한다. 공식 Test, 추가 튜닝, 새로운 데이터 추가, Git Commit/Push/PR/Merge는 수행하지 않았다.

## 2. 스냅샷·버전·고정 설정

`fv-snap-20261031-v1`, manifest SHA-256 `3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0`. 10계열, Validation 244기준일, Tune 53, Test 234. Tune/Test 목록 수 검사는 학습·평가 실행이 아니다. 깐마늘 도매의 기존 공백은 REVIEW로 유지했다.

브랜치 `feat/ridge-p2`, HEAD `1adbac5f2f666056e5f91f8468eeba4c4971dc47`. Python 3.12.16, NumPy 2.5.3, SciPy 1.18.1, scikit-learn 1.9.1. alpha=10, solver=lsqr, StandardScaler, raw_price, direct_pooled, seed=42, 7일 예측, 최근 최대 1,825일 학습 창, 주별 첫 기준일 재학습, 공통 기준 v1을 고정했다. 변경은 p2 모델 클래스와 해당 외부변수 묶음뿐이며 상호작용·추가 선택·튜닝은 없다.

소스·설정·Loader·평가기·lock 해시는 `preflight.json`, 실행별 `start.json`에, 정확한 소스 바이트는 실행별 `sources/`에 있다. 모든 특징명은 `start.json`과 매 FIT 진단에 보존했다.

기본 15개 특징: `current, lag1, lag7, lag14, lag28, mean7, mean28, change7, volatility7, price_age, target_weekday, target_season_sin, target_season_cos, horizon, days_since_kind_switch`. 실행별 열 순서는 `feature-names.csv`, 버전·소스·설정·Loader·평가기 해시는 `run-provenance.csv`로도 제공한다.

| 묶음 | 기본+추가=전체 특징 수 | 외부 특징 |
| --- | --- | --- |
| CONTROL | 15+0=15 | 없음 |
| MARKET | 15+4=19 | counter_price, target_counter_ratio, counter_change7, counter_change28 |
| NATIONAL_WEATHER | 15+6=21 | nat_temp_mean7, nat_rain_sum28, nat_heat_index7, nat_heat_index28, nat_heavy_rain_index28, nat_cold_index28 |
| EVENT | 15+4=19 | days_to_major_holiday, days_from_major_holiday, target_in_event_window, target_prev_day_holiday |
| MACRO | 15+2=17 | usd_krw_change7, usd_krw_change28 |
| PRODUCTION | 15+1=16 | production_yoy |
| MARKET+PRODUCTION | 15+5=20 | counter_price, target_counter_ratio, counter_change7, counter_change28, production_yoy |

## 3. p1과 CONTROL

CONTROL 검증 **PASSED**. p1 5.060471%, CONTROL 5.060471%. 17,080행, 평가 대상 11,275점. 원시 예측 최대 절대차 0.0, 비식별 지표 일치=True, 평가 대상·정답·Naive·후처리 입력 일치=True. CSV의 실험 ID/config_id 및 지표의 의도된 phase=p1/p2 메타데이터만 비교에서 제외했다. 원시 예측은 공통 CSV의 소수 6자리 저장값 기준이다. 세부 증거는 `control-parity.json`.

## 4. 단독 5개 실험 결과

| 묶음 | 실행 ID | MAPE % | p1 변화 %p | p1 개선 % | Naive 개선 % | rMAE | 개선/악화 | 성공률 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONTROL | ridge-p2-20261112-01 | 5.060471 | 0.0 | 0.0 | -3.011147 | 1.026703 | 0/0 | 99.2018% |
| MARKET | ridge-p2-20261112-02 | 4.940629 | -0.119842 | 2.368199 | -0.571646 | 1.001712 | 5/5 | 99.2018% |
| NATIONAL_WEATHER | ridge-p2-20261112-03 | 5.143822 | 0.083351 | -1.6471 | -4.707839 | 1.040708 | 3/7 | 99.2018% |
| EVENT | ridge-p2-20261112-04 | 5.200425 | 0.139954 | -2.765632 | -5.860064 | 1.051477 | 1/9 | 99.2018% |
| MACRO | ridge-p2-20261112-05 | 5.085541 | 0.02507 | -0.495408 | -3.521481 | 1.031832 | 2/8 | 99.2018% |
| PRODUCTION | ridge-p2-20261112-06 | 5.043419 | -0.017052 | 0.336965 | -2.66404 | 1.024007 | 6/4 | 99.2018% |
| MARKET+PRODUCTION | ridge-p2-20261112-07 | 4.942954 | -0.117517 | 2.322254 | -0.618974 | 1.002837 | 5/5 | 99.2018% |

p1 변화=실험−p1, p1 상대 개선=(p1−실험)/p1×100. 음의 변화 또는 양의 상대 개선이 유리하다. 성공률은 전체 행의 OK 비율이 아닌 공식 평가 대상 기준이다. `summary.csv` 참조.

## 5. 조건부 조합

완료 단독 5/5, p1보다 낮은 묶음: MARKET, PRODUCTION.

조합 MARKET+PRODUCTION: MAPE 4.942954%, p1 개선 2.322254%, Naive 개선 -0.618974%.

| 비교 단독 | 조합−단독 %p |
| --- | --- |
| MARKET | 0.002325 |
| PRODUCTION | -0.100465 |

## 6. 10계열 및 품목·시장별 성능

| 계열 | 품목 | 시장 | p1 | CONTROL | MARKET | NATIONAL_WEATHER | EVENT | MACRO | PRODUCTION | MARKET+PRODUCTION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 대파 | RETAIL | 5.215571 | 5.215571 | 4.822789 | 5.239902 | 5.297684 | 5.228793 | 5.223973 | 4.801082 |
| 10 | 깐마늘 | RETAIL | 3.766812 | 3.766812 | 3.822711 | 3.781459 | 3.732744 | 3.760954 | 3.757596 | 3.829458 |
| 2 | 대파 | WHOLESALE | 6.119194 | 6.119194 | 6.189897 | 6.119782 | 6.491865 | 6.231175 | 6.040548 | 6.101153 |
| 7 | 양파 | WHOLESALE | 2.90284 | 2.90284 | 2.973095 | 2.834122 | 2.905113 | 2.918997 | 2.892533 | 3.003249 |
| 8 | 양파 | RETAIL | 5.006221 | 5.006221 | 5.005916 | 4.951549 | 5.04722 | 5.018444 | 5.015708 | 5.027921 |
| 9 | 깐마늘 | WHOLESALE | 0.841483 | 0.841483 | 0.872217 | 0.869936 | 0.853615 | 0.851736 | 0.842209 | 0.881806 |
| 9001 | 배추 | RETAIL | 5.355494 | 5.355494 | 4.948731 | 5.185967 | 5.561569 | 5.330852 | 5.347846 | 4.917417 |
| 9002 | 배추 | WHOLESALE | 7.944784 | 7.944784 | 7.844082 | 7.98107 | 8.508926 | 8.007331 | 7.945764 | 7.833409 |
| 9011 | 무 | RETAIL | 4.500893 | 4.500893 | 3.895722 | 4.852471 | 4.533646 | 4.529034 | 4.461328 | 3.939253 |
| 9012 | 무 | WHOLESALE | 8.951417 | 8.951417 | 9.031133 | 9.621959 | 9.071871 | 8.978097 | 8.906686 | 9.094795 |

계열별 전체 수치·변화는 `series-comparison.csv`, 품목 평균 및 소매/도매 결과는 실행별 result.json과 analysis.json에 있다.

### CONTROL

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.304148 | 0.0 |
| 대파 | 5.667383 | 0.0 |
| 무 | 6.726155 | 0.0 |
| 배추 | 6.650139 | 0.0 |
| 양파 | 3.95453 | 0.0 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.768998 | 0.0 |
| WHOLESALE | 5.351944 | 0.0 |

최대 개선/최소 악화 계열: ('1', {'delta_vs_p1_pp': 0.0, 'item': '대파', 'mae': 150.367133, 'mape': 5.215571, 'market': 'RETAIL', 'naive_mae': 149.085664, 'naive_mape': 5.198433, 'points': 1144, 'relative_improvement_pct': -0.329663, 'rmae': 1.008596, 'win': False}). 최대 악화/최소 개선 계열: ('9012', {'delta_vs_p1_pp': 0.0, 'item': '무', 'mae': 1715.925699, 'mape': 8.951417, 'market': 'WHOLESALE', 'naive_mae': 1640.436189, 'naive_mape': 8.615672, 'points': 1144, 'relative_improvement_pct': -3.896912, 'rmae': 1.046018, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### MARKET

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.347464 | 0.043316 |
| 대파 | 5.506343 | -0.16104 |
| 무 | 6.463427 | -0.262727 |
| 배추 | 6.396407 | -0.253732 |
| 양파 | 3.989505 | 0.034975 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.499174 | -0.269824 |
| WHOLESALE | 5.382085 | 0.030141 |

최대 개선/최소 악화 계열: ('9011', {'delta_vs_p1_pp': -0.605171, 'item': '무', 'mae': 101.786713, 'mape': 3.895722, 'market': 'RETAIL', 'naive_mae': 111.173077, 'naive_mape': 4.2493, 'points': 1144, 'relative_improvement_pct': 8.320849, 'rmae': 0.91557, 'win': True}). 최대 악화/최소 개선 계열: ('9012', {'delta_vs_p1_pp': 0.079716, 'item': '무', 'mae': 1732.141608, 'mape': 9.031133, 'market': 'WHOLESALE', 'naive_mae': 1640.436189, 'naive_mape': 8.615672, 'points': 1144, 'relative_improvement_pct': -4.822159, 'rmae': 1.055903, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### NATIONAL_WEATHER

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.325697 | 0.02155 |
| 대파 | 5.679842 | 0.012459 |
| 무 | 7.237215 | 0.51106 |
| 배추 | 6.583519 | -0.06662 |
| 양파 | 3.892835 | -0.061695 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.80227 | 0.033272 |
| WHOLESALE | 5.485374 | 0.13343 |

최대 개선/최소 악화 계열: ('9001', {'delta_vs_p1_pp': -0.169527, 'item': '배추', 'mae': 242.685689, 'mape': 5.185967, 'market': 'RETAIL', 'naive_mae': 240.765584, 'naive_mape': 5.240542, 'points': 1139, 'relative_improvement_pct': 1.041397, 'rmae': 1.007975, 'win': True}). 최대 악화/최소 개선 계열: ('9012', {'delta_vs_p1_pp': 0.670542, 'item': '무', 'mae': 1828.422203, 'mape': 9.621959, 'market': 'WHOLESALE', 'naive_mae': 1640.436189, 'naive_mape': 8.615672, 'points': 1144, 'relative_improvement_pct': -11.679739, 'rmae': 1.114595, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### EVENT

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.293179 | -0.010968 |
| 대파 | 5.894775 | 0.227392 |
| 무 | 6.802758 | 0.076604 |
| 배추 | 7.035248 | 0.385109 |
| 양파 | 3.976167 | 0.021636 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.834573 | 0.065575 |
| WHOLESALE | 5.566278 | 0.214334 |

최대 개선/최소 악화 계열: ('10', {'delta_vs_p1_pp': -0.034068, 'item': '깐마늘', 'mae': 398.803322, 'mape': 3.732744, 'market': 'RETAIL', 'naive_mae': 408.164336, 'naive_mape': 3.830226, 'points': 1144, 'relative_improvement_pct': 2.545068, 'rmae': 0.977066, 'win': True}). 최대 악화/최소 개선 계열: ('9002', {'delta_vs_p1_pp': 0.564142, 'item': '배추', 'mae': 1175.130245, 'mape': 8.508926, 'market': 'WHOLESALE', 'naive_mae': 1004.042832, 'naive_mape': 7.193477, 'points': 1144, 'relative_improvement_pct': -18.286701, 'rmae': 1.170399, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### MACRO

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.306345 | 0.002197 |
| 대파 | 5.729984 | 0.062601 |
| 무 | 6.753566 | 0.027411 |
| 배추 | 6.669092 | 0.018953 |
| 양파 | 3.96872 | 0.01419 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.773615 | 0.004617 |
| WHOLESALE | 5.397467 | 0.045523 |

최대 개선/최소 악화 계열: ('9001', {'delta_vs_p1_pp': -0.024642, 'item': '배추', 'mae': 249.18086, 'mape': 5.330852, 'market': 'RETAIL', 'naive_mae': 240.765584, 'naive_mape': 5.240542, 'points': 1139, 'relative_improvement_pct': -1.72329, 'rmae': 1.034952, 'win': False}). 최대 악화/최소 개선 계열: ('2', {'delta_vs_p1_pp': 0.111981, 'item': '대파', 'mae': 129.427448, 'mape': 6.231175, 'market': 'WHOLESALE', 'naive_mae': 124.70979, 'naive_mape': 5.940815, 'points': 1144, 'relative_improvement_pct': -4.887554, 'rmae': 1.037829, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### PRODUCTION

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.299902 | -0.004245 |
| 대파 | 5.632261 | -0.035122 |
| 무 | 6.684007 | -0.042148 |
| 배추 | 6.646805 | -0.003334 |
| 양파 | 3.954121 | -0.00041 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.76129 | -0.007708 |
| WHOLESALE | 5.325548 | -0.026396 |

최대 개선/최소 악화 계열: ('2', {'delta_vs_p1_pp': -0.078646, 'item': '대파', 'mae': 125.997378, 'mape': 6.040548, 'market': 'WHOLESALE', 'naive_mae': 124.70979, 'naive_mape': 5.940815, 'points': 1144, 'relative_improvement_pct': -1.678776, 'rmae': 1.010325, 'win': False}). 최대 악화/최소 개선 계열: ('8', {'delta_vs_p1_pp': 0.009487, 'item': '양파', 'mae': 111.585538, 'mape': 5.015708, 'market': 'RETAIL', 'naive_mae': 108.325397, 'naive_mape': 4.87323, 'points': 1134, 'relative_improvement_pct': -2.923707, 'rmae': 1.030096, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

### MARKET+PRODUCTION

| 품목 | 품목 Macro MAPE | p1 변화 %p |
| --- | --- | --- |
| 깐마늘 | 2.355632 | 0.051484 |
| 대파 | 5.451118 | -0.216265 |
| 무 | 6.517024 | -0.209131 |
| 배추 | 6.375413 | -0.274726 |
| 양파 | 4.015585 | 0.061055 |

| 시장 | MAPE | p1 변화 %p |
| --- | --- | --- |
| RETAIL | 4.503026 | -0.265972 |
| WHOLESALE | 5.382882 | 0.030938 |

최대 개선/최소 악화 계열: ('9011', {'delta_vs_p1_pp': -0.56164, 'item': '무', 'mae': 102.601399, 'mape': 3.939253, 'market': 'RETAIL', 'naive_mae': 111.173077, 'naive_mape': 4.2493, 'points': 1144, 'relative_improvement_pct': 7.296427, 'rmae': 0.922898, 'win': True}). 최대 악화/최소 개선 계열: ('9012', {'delta_vs_p1_pp': 0.143378, 'item': '무', 'mae': 1740.888112, 'mape': 9.094795, 'market': 'WHOLESALE', 'naive_mae': 1640.436189, 'naive_mape': 8.615672, 'points': 1144, 'relative_improvement_pct': -5.56107, 'rmae': 1.061235, 'win': False}).

공식 검증 관문: `{"checks": {"1_relative_improvement_ge_5pct": false, "2_macro_rmae_lt_1": false, "3_series_wins_majority": false, "4_success_rate_ge_99pct": true, "5_bootstrap_ci_low_gt_0": false}, "majority_required": 6, "note": "6(자원)은 최종 시험 Docker 실행 값으로 판단", "validation_gate_passed": false}`.

전체 행 상태: `{"NO_INPUT": 287, "OK": 16793}`; 실패 유형: `{"NO_INPUT:STALE_OR_GAP": 287}`.

## 7. 개선·악화 해석과 측정 범위

같은 평가 대상과 고정 설정에서 달라진 예측의 성능 차이는 위 표로 측정했다. 외부변수 추가는 새 열의 계수뿐 아니라 기존 가격 특징의 계수도 다시 배분하므로, 특정 열의 계수 하나만으로 점수 변화 원인을 확정할 수 없다. 품목별 큰 차이는 해당 계열 오차 변화이며 공급·수요·시차의 인과 효과를 입증하지 않는다.

### MARKET의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 9011 | 무 RETAIL | -0.605171 | -0.0605171 |
| 9001 | 배추 RETAIL | -0.406763 | -0.0406763 |
| 1 | 대파 RETAIL | -0.392782 | -0.0392782 |

### NATIONAL_WEATHER의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 9012 | 무 WHOLESALE | 0.670542 | 0.0670542 |
| 9011 | 무 RETAIL | 0.351578 | 0.0351578 |
| 9001 | 배추 RETAIL | -0.169527 | -0.0169527 |

이 묶음의 외부 특징은 실제 FIT/PREDICT에서 결측이 0이었다. 따라서 관측된 성능 변화는 외부 특징 중앙값 대체가 작동해서 생긴 변화가 아니다. 추가 열의 선형 적합·기존 계수 재배분과 일반화 오차가 함께 반영된 결과다.

### EVENT의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 9002 | 배추 WHOLESALE | 0.564142 | 0.0564142 |
| 2 | 대파 WHOLESALE | 0.372671 | 0.0372671 |
| 9001 | 배추 RETAIL | 0.206075 | 0.0206075 |

이 묶음의 외부 특징은 실제 FIT/PREDICT에서 결측이 0이었다. 따라서 관측된 성능 변화는 외부 특징 중앙값 대체가 작동해서 생긴 변화가 아니다. 추가 열의 선형 적합·기존 계수 재배분과 일반화 오차가 함께 반영된 결과다.

### MACRO의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 2 | 대파 WHOLESALE | 0.111981 | 0.0111981 |
| 9002 | 배추 WHOLESALE | 0.062547 | 0.0062547 |
| 9011 | 무 RETAIL | 0.028141 | 0.0028141 |

이 묶음의 외부 특징은 실제 FIT/PREDICT에서 결측이 0이었다. 따라서 관측된 성능 변화는 외부 특징 중앙값 대체가 작동해서 생긴 변화가 아니다. 추가 열의 선형 적합·기존 계수 재배분과 일반화 오차가 함께 반영된 결과다.

### PRODUCTION의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 2 | 대파 WHOLESALE | -0.078646 | -0.0078646 |
| 9012 | 무 WHOLESALE | -0.044731 | -0.0044731 |
| 9011 | 무 RETAIL | -0.039565 | -0.0039565 |

이 묶음의 외부 특징은 실제 FIT/PREDICT에서 결측이 0이었다. 따라서 관측된 성능 변화는 외부 특징 중앙값 대체가 작동해서 생긴 변화가 아니다. 추가 열의 선형 적합·기존 계수 재배분과 일반화 오차가 함께 반영된 결과다.

### MARKET+PRODUCTION의 평균 변화를 구성한 계열

| 계열 | 품목·시장 | 계열 변화 %p | 10계열 Macro 변화 기여 %p |
| --- | --- | --- | --- |
| 9011 | 무 RETAIL | -0.56164 | -0.056164 |
| 9001 | 배추 RETAIL | -0.438077 | -0.0438077 |
| 1 | 대파 RETAIL | -0.414489 | -0.0414489 |

## 8. 결측값·데이터 품질

현재 FIT의 학습 표본에서만 열별 중앙값을 구하고 저장하며 예측에서는 이를 재사용한다. 전체 결측 열은 학습·예측 모두 0으로 고정하고 다음 FIT에서 다시 판단한다. 무한대·비정상 타깃은 거부한다. 기본 특징의 유한 입력 동일성은 CONTROL로 확인한다. `feature-diagnostics.csv`의 학습 가중 결측률은 겹치는 주별 학습 표본의 노출 수 기준이며 고유 원천 관측률이 아니다. 예측 결측률은 성공 PREDICT 이벤트의 7개 특징 셀 기준이다. NO_INPUT은 별도로 집계했다.

CONTROL: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 11185, "series": 10, "mape": 5.067858, "delta_vs_p1_pp": 0.0}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

MARKET: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| counter_price | 0.1264% | 0.9170% | 0 |
| target_counter_ratio | 4.3032% | 2.5844% | 0 |
| counter_change7 | 0.1784% | 1.1255% | 0 |
| counter_change28 | 0.2347% | 1.7090% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 10788, "series": 10, "mape": 4.921445, "delta_vs_p1_pp": -0.121038}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}, "external_missing": {"points": 397, "series": 5, "mape": 7.408814, "delta_vs_p1_pp": -0.432734}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

NATIONAL_WEATHER: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| nat_temp_mean7 | 0.0000% | 0.0000% | 0 |
| nat_rain_sum28 | 0.0000% | 0.0000% | 0 |
| nat_heat_index7 | 0.0000% | 0.0000% | 0 |
| nat_heat_index28 | 0.0000% | 0.0000% | 0 |
| nat_heavy_rain_index28 | 0.0000% | 0.0000% | 0 |
| nat_cold_index28 | 0.0000% | 0.0000% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 11185, "series": 10, "mape": 5.151493, "delta_vs_p1_pp": 0.083635}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

EVENT: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| days_to_major_holiday | 0.0000% | 0.0000% | 0 |
| days_from_major_holiday | 0.0000% | 0.0000% | 0 |
| target_in_event_window | 0.0000% | 0.0000% | 0 |
| target_prev_day_holiday | 0.0000% | 0.0000% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 11185, "series": 10, "mape": 5.207934, "delta_vs_p1_pp": 0.140076}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

MACRO: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| usd_krw_change7 | 0.0000% | 0.0000% | 0 |
| usd_krw_change28 | 0.0000% | 0.0000% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 11185, "series": 10, "mape": 5.093031, "delta_vs_p1_pp": 0.025173}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

PRODUCTION: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| production_yoy | 0.0000% | 0.0000% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 11185, "series": 10, "mape": 5.050814, "delta_vs_p1_pp": -0.017044}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

MARKET+PRODUCTION: FIT 530, PREDICT 2399, 전체 결측인 계열·특징·FIT 수 0.

| 외부 특징 | 학습 노출 가중 결측률 | 예측 결측률 | 전체 결측 FIT |
| --- | --- | --- | --- |
| counter_price | 0.1264% | 0.9170% | 0 |
| target_counter_ratio | 4.3032% | 2.5844% | 0 |
| counter_change7 | 0.1784% | 1.1255% | 0 |
| counter_change28 | 0.2347% | 1.7090% | 0 |
| production_yoy | 0.0000% | 0.0000% | 0 |

동일 평가점의 결측 그룹 비교: `{"external_complete": {"points": 10788, "series": 10, "mape": 4.924708, "delta_vs_p1_pp": -0.117775}, "NO_INPUT": {"points": 90, "series": 1, "mape": 0.099438, "delta_vs_p1_pp": 0.0}, "external_missing": {"points": 397, "series": 5, "mape": 7.412526, "delta_vs_p1_pp": -0.429022}}`. 구간별 품목·계절 구성이 달라 그룹끼리의 차이를 대체 방식의 인과 효과로 해석하지 않는다.

## 9. Ridge 선형 모델 해석

StandardScaler는 현재 학습 표본의 평균·표준편차로 z=(x−mean)/scale을 만든다. 표준화 계수는 다른 열을 조건으로 한 원 가격 단위 변화이며 원 단위 계수는 beta_z/scale이다. 서로 다른 계열의 가격 단위가 달라 계수 크기를 그대로 품목 간 중요도로 비교하지 않는다. Ridge L2는 중복 열에 계수를 나눌 수 있으며 공선성 아래 부호 변동은 인과 방향 반전을 뜻하지 않는다.

CONTROL: 활성 표준화 행렬 조건수 통계 `{'min': 34.77022616860294, 'max': 227.85149208637276, 'mean': 72.91913920154772, 'std_population': 41.385582774192265}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[]`.

MARKET: 활성 표준화 행렬 조건수 통계 `{'min': 38.39435803145483, 'max': 246.650289829312, 'mean': 79.16707693515426, 'std_population': 44.41543391346412}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[{'left': 'lag7', 'right': 'counter_price', 'fit_count': 155}, {'left': 'mean7', 'right': 'counter_price', 'fit_count': 153}, {'left': 'mean28', 'right': 'counter_price', 'fit_count': 153}, {'left': 'current', 'right': 'counter_price', 'fit_count': 70}, {'left': 'lag1', 'right': 'counter_price', 'fit_count': 38}, {'left': 'lag14', 'right': 'counter_price', 'fit_count': 33}]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 9012 | counter_price | mean28 | 0.920306 | 0.849995 |
| 9002 | counter_price | lag7 | 0.912541 | 0.806656 |
| 2 | counter_price | mean28 | 0.911402 | 0.846159 |
| 9011 | counter_price | current | 0.90533 | 0.913925 |
| 1 | counter_price | current | 0.892589 | 0.905704 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 7 | counter_change7 | 6 | -39.640019 | 10.036628 | 14.415782 |
| 9012 | counter_price | 4 | -36.347948 | 1500.81427 | 422.984622 |
| 9012 | target_counter_ratio | 4 | -4.564387 | 670.7976 | 189.417856 |
| 9012 | counter_change28 | 4 | -150.336073 | 82.175695 | 57.577396 |
| 9 | counter_change7 | 4 | -11.31366 | 66.39074 | 17.302291 |

NATIONAL_WEATHER: 활성 표준화 행렬 조건수 통계 `{'min': 37.56043705257309, 'max': 236.84316171539598, 'mean': 76.48606861950566, 'std_population': 42.487731084490925}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[{'left': 'nat_rain_sum28', 'right': 'nat_heavy_rain_index28', 'fit_count': 530}]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 7 | nat_temp_mean7 | target_season_cos | -0.855622 | -0.255492 |
| 8 | nat_temp_mean7 | target_season_cos | -0.852992 | -0.411865 |
| 1 | nat_temp_mean7 | target_season_cos | -0.852427 | -0.350376 |
| 2 | nat_temp_mean7 | target_season_cos | -0.852427 | -0.332153 |
| 10 | nat_temp_mean7 | target_season_cos | -0.852427 | 0.074573 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 9002 | nat_temp_mean7 | 7 | -135.719011 | 76.840812 | 52.672242 |
| 9002 | nat_heavy_rain_index28 | 6 | -139.666468 | 57.918979 | 42.324978 |
| 9011 | nat_heavy_rain_index28 | 5 | -4.205515 | 16.608136 | 5.549102 |
| 9012 | nat_heat_index28 | 4 | -156.494797 | 95.572697 | 73.607559 |
| 2 | nat_rain_sum28 | 4 | -16.951979 | 29.411986 | 13.132536 |

EVENT: 활성 표준화 행렬 조건수 통계 `{'min': 35.027277164784074, 'max': 229.0358772380602, 'mean': 73.27473223580148, 'std_population': 41.47480878818984}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 9002 | days_from_major_holiday | lag7 | -0.30624 | -0.19347 |
| 9011 | days_to_major_holiday | days_since_kind_switch | 0.293254 | -0.093875 |
| 9012 | days_from_major_holiday | days_since_kind_switch | -0.281092 | -0.084891 |
| 9001 | days_from_major_holiday | current | -0.273212 | -0.275226 |
| 1 | days_from_major_holiday | target_season_cos | -0.269714 | -0.218296 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 9012 | target_in_event_window | 4 | -51.745911 | 74.290507 | 32.759508 |
| 9002 | days_from_major_holiday | 2 | -3.420335 | 111.812556 | 26.022272 |
| 10 | days_to_major_holiday | 2 | -14.037522 | 8.594182 | 5.855359 |
| 1 | days_from_major_holiday | 2 | -11.771527 | 1.459023 | 3.731857 |
| 2 | target_in_event_window | 2 | -0.82811 | 6.915251 | 1.502504 |

MACRO: 활성 표준화 행렬 조건수 통계 `{'min': 34.87297237247106, 'max': 228.16537559631024, 'mean': 73.05945466083227, 'std_population': 41.4382115432959}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 9001 | usd_krw_change28 | mean7 | 0.304611 | 0.292996 |
| 9002 | usd_krw_change28 | lag7 | 0.266794 | 0.224166 |
| 9012 | usd_krw_change28 | days_since_kind_switch | 0.251075 | 0.192515 |
| 9011 | usd_krw_change28 | days_since_kind_switch | 0.206829 | 0.164775 |
| 8 | usd_krw_change28 | lag28 | -0.187037 | -0.054415 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 9011 | usd_krw_change7 | 6 | -5.712019 | 0.160765 | 2.098988 |
| 7 | usd_krw_change28 | 4 | -2.306343 | 47.804973 | 13.50763 |
| 1 | usd_krw_change7 | 4 | -10.163611 | 0.49596 | 3.585722 |
| 7 | usd_krw_change7 | 3 | -51.262494 | 11.541205 | 23.225438 |
| 9 | usd_krw_change28 | 2 | -157.264087 | 0.920293 | 44.435421 |

PRODUCTION: 활성 표준화 행렬 조건수 통계 `{'min': 34.771050195825026, 'max': 228.49956281353494, 'mean': 73.47884530246675, 'std_population': 41.81830207148697}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 8 | production_yoy | mean28 | 0.497137 | 0.452173 |
| 7 | production_yoy | mean28 | 0.454802 | 0.422863 |
| 10 | production_yoy | lag28 | -0.358129 | -0.239016 |
| 9012 | production_yoy | mean28 | 0.209893 | 0.19951 |
| 9 | production_yoy | lag28 | -0.207903 | -0.056499 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 9002 | production_yoy | 2 | -43.950428 | 27.899658 | 19.076096 |
| 9011 | production_yoy | 2 | -1.469382 | 10.965408 | 3.149722 |
| 9 | production_yoy | 0 | 57.760397 | 238.283977 | 49.983059 |
| 9012 | production_yoy | 0 | 8.387675 | 134.210493 | 30.484577 |
| 7 | production_yoy | 0 | 7.976538 | 63.062165 | 19.491441 |

MARKET+PRODUCTION: 활성 표준화 행렬 조건수 통계 `{'min': 38.39502119119078, 'max': 247.25146127986878, 'mean': 79.73251651121252, 'std_population': 44.81252535197449}`, 특이/빈 행렬 FIT 0. 외부변수 관련 |r|≥0.9 상위 쌍: `[{'left': 'lag7', 'right': 'counter_price', 'fit_count': 155}, {'left': 'mean7', 'right': 'counter_price', 'fit_count': 153}, {'left': 'mean28', 'right': 'counter_price', 'fit_count': 153}, {'left': 'current', 'right': 'counter_price', 'fit_count': 70}, {'left': 'lag1', 'right': 'counter_price', 'fit_count': 38}, {'left': 'lag14', 'right': 'counter_price', 'fit_count': 33}]`.

| 계열 | 외부 특징 | 최대 중복 기본 특징 | Pearson r | 타깃 r |
| --- | --- | --- | --- | --- |
| 9012 | counter_price | mean28 | 0.920306 | 0.849995 |
| 9002 | counter_price | lag7 | 0.912541 | 0.806656 |
| 2 | counter_price | mean28 | 0.911402 | 0.846159 |
| 9011 | counter_price | current | 0.90533 | 0.913925 |
| 1 | counter_price | current | 0.892589 | 0.905704 |

| 계열 | 특징 | 주별 부호변경 | 표준화 계수 최소 | 최대 | 표준편차 |
| --- | --- | --- | --- | --- | --- |
| 9012 | target_counter_ratio | 6 | -19.588364 | 638.427311 | 182.573894 |
| 9012 | counter_change28 | 6 | -151.065832 | 75.438123 | 60.051234 |
| 7 | counter_change7 | 5 | -38.517318 | 16.329195 | 15.276759 |
| 9 | counter_change7 | 4 | -13.077951 | 57.120211 | 17.535912 |
| 10 | counter_change28 | 3 | -25.957042 | 34.29127 | 21.861105 |

해석 가설(미검증): 시장 가격은 기존 자기 가격 lag·이동평균과 중복될 수 있다. 전국 평균 기상은 주산지 차이와 임계·누적·지연 반응을 희석할 수 있다. 명절 수요는 전후 비대칭·품목별 차이가 있을 수 있다. 환율 전달은 수입 비중·지연에 따라 다르고, 연간 생산량은 발표 지연과 낮은 갱신 빈도로 단기 7일 가격 변동과 다른 시계를 가진다. 이번 선형·고정 특징 실험만으로 이러한 관계의 존재 여부를 확정하지 않는다. 개선 묶음 조합도 중복·계수 재배분 때문에 단독 효과가 가산된다고 가정하지 않는다.

## 10. 유지·제외 판단

변수별 추가 선택 실험은 하지 않았다. 아래는 고정 묶음 단위의 향후 연구 판단이며 공식 Test 채택 선언이 아니다.

| 묶음 | 포함 변수 | 판단 | 근거 |
| --- | --- | --- | --- |
| MARKET | counter_price, target_counter_ratio, counter_change7, counter_change28 | 후속 비교 후보 유지 | p1 변화 -0.119842%p, Naive 개선 -0.571646% |
| NATIONAL_WEATHER | nat_temp_mean7, nat_rain_sum28, nat_heat_index7, nat_heat_index28, nat_heavy_rain_index28, nat_cold_index28 | 현재 p1 대체 후보에서 제외 | p1 변화 +0.083351%p, Naive 개선 -4.707839% |
| EVENT | days_to_major_holiday, days_from_major_holiday, target_in_event_window, target_prev_day_holiday | 현재 p1 대체 후보에서 제외 | p1 변화 +0.139954%p, Naive 개선 -5.860064% |
| MACRO | usd_krw_change7, usd_krw_change28 | 현재 p1 대체 후보에서 제외 | p1 변화 +0.025070%p, Naive 개선 -3.521481% |
| PRODUCTION | production_yoy | 후속 비교 후보 유지 | p1 변화 -0.017052%p, Naive 개선 -2.664040% |

## 11. 오류·경고·재시도 및 원본 보존

첫 세션 `session-20261112`는 uv 사용자 캐시 잠금 파일 접근 거부로 학습 전 종료했다. 재시도 01은 스냅샷을 통과한 뒤 감사 스크립트가 기존 p2 공통 도구 확장까지 p1 바이트 동일성을 요구해 중단됐다. 이는 실험 모델·데이터 결함이 아닌 추가 감사 스크립트의 과도한 검사였다. 재시도 02는 리뷰한 변경 경로와 diff를 p1-source-review.json에 기록했으나 Windows의 프로젝트 임시 폴더 및 pytest 캐시 ACL 문제로 fixture 생성과 종료 단계가 실패했다. 재시도 03은 OS 임시 경로와 캐시 비활성화를 사용했으며 평가기 동일성 및 CONTROL 전체 재현을 요구했다. 재시도 03의 CONTROL은 모든 예측과 평가점이 일치했지만 감사 스크립트가 의도된 phase 메타데이터 차이를 지표 불일치로 오판했다. diff는 phase와 config_id 두 필드뿐이었다. 재시도 04는 이 메타데이터만 분리하고 기존 완료 CONTROL과 80개 테스트를 소스·설정·데이터·환경·결과 해시 및 공식 재계산으로 검증해 재사용했다. 원본 실패 판정과 수정 후 통과 판정은 별도 파일로 보존했다. 모델·공통 도구·평가 기준은 이번 작업에서 수정하지 않았다. 실패 세션 및 수정 전후 실행 스크립트는 모두 보존했다.

기존 PREPARATION_REPORT.md의 ? 손상은 실행 전부터 존재했다. 원본을 덮어쓰지 않았다. 초기 해시와 최종 무결성·UTF-8 검사는 `final-integrity.json`, `artifact-manifest.csv` 참조. 공식 실행별 경고·공통 검증 결과는 result.json.validation, stderr 포함 CLI 로그와 run.log에 있다.

로컬 공통 실행기의 RESOURCES.peak_memory_mb는 0.0으로 기록되어 실제 메모리 사용량의 증거로 사용할 수 없다. 시간·refit 횟수·timeout은 기록했으나 메모리 및 관문 6의 채택 판정은 미확정으로 유지한다. 이 계측 한계는 예측·평가 점수 계산과 분리되며 공통 계측 코드는 수정하지 않았다.

## 12. 실제 실행 명령 및 재현

프로젝트 루트에서 실행했다. 아래 감사 드라이버는 새 시도마다 별도 폴더로 복사하여 실행한다. 이미 initial.json이 있으면 덮어쓰기 방지를 위해 거부한다.

```powershell
.venv/Scripts/python.exe -X utf8 model_comparison/ridge/experiments/p2/session-20261112-retry04/run_session.py
```

이 드라이버는 재시도 03의 검증된 테스트 기록을 요구한다. 독립 재현에서는 같은 4개 테스트 파일을 `uv run --extra prices python -X utf8 -m pytest`로 실행하며 `-q -W error -p no:cacheprovider --basetemp <새 OS 임시 경로>`를 사용한다. 단독 공식 CLI는 아래 표의 명령 그대로 실행할 수 있다.

실제 CLI 명령·시작/종료·exit code·소요시간은 아래와 같으며 command.json과 session-events.jsonl이 원본이다.

| 단계 | 명령 | 시작 UTC | 종료 UTC | 초 | exit |
| --- | --- | --- | --- | --- | --- |
| 01-snapshot-check | `uv run --extra prices python -X utf8 -m tools.check_snapshot C:\FoodValue_was\data\snapshots\fv-snap-20261031-v1` | 2026-11-12T06:45:30.644177+00:00 | 2026-11-12T06:45:30.699399+00:00 | 0.063 | 2 |
| 01-snapshot-check | `uv run --extra prices python -X utf8 -m tools.check_snapshot C:\FoodValue_was\data\snapshots\fv-snap-20261031-v1` | 2026-11-12T06:47:46.293306+00:00 | 2026-11-12T06:47:47.095571+00:00 | 0.809 | 0 |
| 01-snapshot-check | `uv run --extra prices python -X utf8 -m tools.check_snapshot C:\FoodValue_was\data\snapshots\fv-snap-20261031-v1` | 2026-11-12T06:48:57.946622+00:00 | 2026-11-12T06:48:58.563887+00:00 | 0.619 | 0 |
| 02-tests | `uv run --extra prices python -X utf8 -m pytest tests/test_ridge_p2.py tests/test_backtest_tools.py tests/test_standard_tools.py tests/test_snapshot_tools.py -q -W error --basetemp C:\FoodValue_was\.tmp\ridge-p2-session-20261112T064900304591` | 2026-11-12T06:49:00.304591+00:00 | 2026-11-12T06:49:42.349284+00:00 | 42.044 | 1 |
| 01-snapshot-check | `uv run --extra prices python -X utf8 -m tools.check_snapshot C:\FoodValue_was\data\snapshots\fv-snap-20261031-v1` | 2026-11-12T06:53:22.862198+00:00 | 2026-11-12T06:53:23.478321+00:00 | 0.62 | 0 |
| 02-tests | `uv run --extra prices python -X utf8 -m pytest tests/test_ridge_p2.py tests/test_backtest_tools.py tests/test_standard_tools.py tests/test_snapshot_tools.py -q -W error -p no:cacheprovider --basetemp C:\Users\22212\AppData\Local\Temp\ridge-p2-session-20261112T065325586908` | 2026-11-12T06:53:25.586908+00:00 | 2026-11-12T06:54:16.331856+00:00 | 50.745 | 0 |
| 03-control | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --control` | 2026-11-12T06:54:16.334887+00:00 | 2026-11-12T06:55:22.395203+00:00 | 66.068 | 0 |
| 01-snapshot-check | `uv run --extra prices python -X utf8 -m tools.check_snapshot C:\FoodValue_was\data\snapshots\fv-snap-20261031-v1` | 2026-11-12T06:56:44.815156+00:00 | 2026-11-12T06:56:45.725802+00:00 | 0.916 | 0 |
| 03-control | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --control` | 2026-11-12T06:56:48.214947+00:00 | 2026-11-12T06:56:51.078614+00:00 | 2.864 | 0 |
| 04-market | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle MARKET` | 2026-11-12T06:56:54.508108+00:00 | 2026-11-12T06:58:04.408094+00:00 | 69.9 | 0 |
| 05-national_weather | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle NATIONAL_WEATHER` | 2026-11-12T06:58:05.651955+00:00 | 2026-11-12T06:59:19.277451+00:00 | 73.627 | 0 |
| 06-event | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle EVENT` | 2026-11-12T06:59:20.410058+00:00 | 2026-11-12T07:00:31.726824+00:00 | 71.315 | 0 |
| 07-macro | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle MACRO` | 2026-11-12T07:00:32.988763+00:00 | 2026-11-12T07:01:42.985014+00:00 | 69.997 | 0 |
| 08-production | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --bundle PRODUCTION` | 2026-11-12T07:01:44.017275+00:00 | 2026-11-12T07:02:52.291572+00:00 | 68.275 | 0 |
| 09-combine | `uv run --extra prices python -m model_comparison.ridge.p2 --execute --combine` | 2026-11-12T07:02:53.369714+00:00 | 2026-11-12T07:04:09.330195+00:00 | 75.961 | 0 |

p2 CLI 재실행은 같은 소스·스냅샷·범위·설정·환경·공식 결과 해시 및 공통 재계산을 통과한 완료 결과만 재사용한다. 새 학습이 필요하면 별도 --records 경로와 신규 실행 ID를 사용한다. 테스트의 합성 결과는 공식 결과와 분리되어 있다.

## 13. 새 스냅샷 후속 작업 및 한계

가락시장·주산지 날씨는 이번 실험에 제공되지 않아 사용하지 않았다. 새 스냅샷은 새 ID와 manifest로 수령 검사하고, 품목·시장·단위·지역 매핑, 실제 공개시점/수정 이력, 기상 관측/예보 구분, 가락시장 거래량·가격 집계와 d−1 가용성, 지역 가중치와 결측 정책을 명세해야 한다. 공통 기준 변경은 버전으로 분리하고 새 데이터에서 base CONTROL과 p1 기준선을 다시 만든 뒤 현재 특징 묶음을 고정하여 비교한다. 데이터 효과와 특징 효과를 분리하려면 동일 기간·계열·평가점을 유지해야 한다. 이번 결과와 새 스냅샷 결과를 섞어 순위를 만들지 않는다.

현재 스냅샷은 과거 시점별 원천 수정본을 모두 복원한 vintage 데이터가 아니며 생산량 공개일 규칙은 명시된 가정이다. Validation에서 묶음을 골랐으므로 선택 편향이 있고, 로컬 실행은 Docker Test 자원 관문 확정 근거가 아니다. 공식 Test 성능은 아직 측정하지 않았다.
