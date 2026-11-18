# Ridge v2 결과

아직 실제 모델 실험을 실행하지 않았다. 측정되지 않은 성능은 N/A이며 숫자를 채워 넣지 않는다.

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N/A | Ridge v2 CONTROL (미실행) | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

실행 후 이 문서에 요약과 모든 계열/모든 주요 지표 표를 누적한다. 실행 폴더의 RESULTS.md와 comparison.json이 감사 원본이다.
과거 결과는 historical_baselines.json에서 원본 경로·해시를 연결한다. 과거 지표가 없는 항목은 N/A이며 재계산해 원본인 것처럼 채우지 않는다.

## 과거 원본 확인 (참고 자료, v2 학습 결과 아님)

기존 metrics.json의 값을 코드로 직접 읽었다. 원본 재평가·수정 없음. RMSE 등 미저장 지표는 N/A. 전체 증거: historical_baselines.json.

| 원본 실행 ID | 원본 policy macro MAPE (%) | 원본 Naive macro MAPE (%) | 조건 |
| --- | ---: | ---: | --- |
| ridge-p1-20261111-07 | 5.060471 | 4.912547 | Validation / reference |
| ridge-p2-20261112-01 | 5.060471 | 4.912547 | Validation / reference |
| ridge-p2-20261112-02 | 4.940629 | 4.912547 | Validation / reference |
| ridge-p2-20261112-03 | 5.143822 | 4.912547 | Validation / reference |
| ridge-p2-20261112-04 | 5.200425 | 4.912547 | Validation / reference |
| ridge-p2-20261112-05 | 5.085541 | 4.912547 | Validation / reference |
| ridge-p2-20261112-06 | 5.043419 | 4.912547 | Validation / reference |
| ridge-p2-20261112-07 | 4.942954 | 4.912547 | Validation / reference |

과거 p2 최소 policy MAPE 실행: `ridge-p2-20261112-02`. 후보 전체와 선택 기준은 catalog에 남겼다. Validation 결과로 선택한 기록이므로 선택 편향에 유의한다.

## ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7 | control | 4.4689544 | 540.2 | 808.30059 | 1.5241743 | N/A | 11.221361 (direct) | N/A |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 5.0338172 | 4.4689544 | -0.56486279 | %p | 11.221361 | improved |
| mae | 482.872 | 540.2 | 57.328 | price | -11.872297 | worsened |
| rmse | 749.19896 | 808.30059 | 59.101631 | price | -7.888643 | worsened |
| rmae | 1 | 1.5241743 | 0.52417429 | ratio | -52.417429 | worsened |
| success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| valid_predictions | 250 | 250 | 0 | count | 0 | count_change |
| failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 6.106342 | 6.5641646 | 0.45782263 | %p | -7.4974941 | worsened |
| 1 | 대파/RETAIL | mae | 196.72 | 213.36 | 16.64 | price | -8.4587231 | worsened |
| 1 | 대파/RETAIL | rmse | 283.12386 | 289.32528 | 6.2014242 | price | -2.1903573 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0845872 | 0.084587231 | ratio | -8.4587231 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5210907 | 5.0420888 | -0.47900194 | %p | 8.675857 | improved |
| 2 | 대파/WHOLESALE | mae | 150.08 | 136.32 | -13.76 | price | 9.1684435 | improved |
| 2 | 대파/WHOLESALE | rmse | 189.01259 | 169.29832 | -19.714276 | price | 10.430139 | improved |
| 2 | 대파/WHOLESALE | rmae | 1 | 0.90831557 | -0.091684435 | ratio | 9.1684435 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 0.56964827 | 0.68135753 | 0.11170926 | %p | -19.610216 | worsened |
| 7 | 양파/WHOLESALE | mae | 114.4 | 136.84 | 22.44 | price | -19.615385 | worsened |
| 7 | 양파/WHOLESALE | rmse | 147.34992 | 179.70765 | 32.357728 | price | -21.959786 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1961538 | 0.19615385 | ratio | -19.615385 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.1840015 | 4.1329238 | -0.051077748 | %p | 1.220787 | improved |
| 8 | 양파/RETAIL | mae | 77.88 | 76.88 | -1 | price | 1.2840267 | improved |
| 8 | 양파/RETAIL | rmse | 131.22332 | 133.47599 | 2.2526693 | price | -1.7166684 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 0.98715973 | -0.012840267 | ratio | 1.2840267 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.10934516 | 0.75002305 | 0.6406779 | %p | -585.92252 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 152 | 1040 | 888 | price | -584.21053 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 317.49016 | 1229.5211 | 912.03092 | price | -287.26274 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 6.8421053 | 5.8421053 | ratio | -584.21053 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.3761182 | 4.5765013 | 0.20038315 | %p | -4.579016 | worsened |
| 10 | 깐마늘/RETAIL | mae | 377.76 | 395.96 | 18.2 | price | -4.8178738 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 666.29849 | 672.90329 | 6.6048 | price | -0.99126745 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0481787 | 0.048178738 | ratio | -4.8178738 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 9.9534525 | 5.8179989 | -4.1354536 | %p | 41.547931 | improved |
| 9001 | 배추/RETAIL | mae | 371.48 | 212.4 | -159.08 | price | 42.823301 | improved |
| 9001 | 배추/RETAIL | rmse | 473.53754 | 275.16599 | -198.37155 | price | 41.89141 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.57176699 | -0.42823301 | ratio | 42.823301 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 6.2502244 | 4.5333827 | -1.7168417 | %p | 27.46848 | improved |
| 9002 | 배추/WHOLESALE | mae | 703.36 | 520.96 | -182.4 | price | 25.932666 | improved |
| 9002 | 배추/WHOLESALE | rmse | 940.17769 | 816.08671 | -124.09097 | price | 13.198673 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.74067334 | -0.25932666 | ratio | 25.932666 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 4.5469793 | 3.864617 | -0.68236232 | %p | 15.006937 | improved |
| 9011 | 무/RETAIL | mae | 122.92 | 106 | -16.92 | price | 13.76505 | improved |
| 9011 | 무/RETAIL | rmse | 189.77176 | 151.12008 | -38.651673 | price | 20.367453 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.8623495 | -0.1376505 | ratio | 13.76505 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 8.7209703 | 8.7264866 | 0.0055163464 | %p | -0.063253815 | worsened |
| 9012 | 무/WHOLESALE | mae | 2562.12 | 2563.28 | 1.16 | price | -0.045275007 | worsened |
| 9012 | 무/WHOLESALE | rmse | 4154.0043 | 4166.4015 | 12.397246 | price | -0.29844087 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0004528 | 0.00045275007 | ratio | -0.045275007 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d | control | 4.6062595 | 565.55167 | 926.40586 | 1.0199316 | N/A | 0.018012668 (direct) | N/A |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6062595 | -0.00082985971 | %p | 0.018012668 | improved |
| mae | 532.31701 | 565.55167 | 33.234666 | price | -6.2433974 | worsened |
| rmse | 943.1701 | 926.40586 | -16.764241 | price | 1.7774356 | improved |
| rmae | 1 | 1.0199316 | 0.019931568 | ratio | -1.9931568 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.729811 | -0.038685529 | %p | 0.81127308 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.83004 | -0.43873518 | price | 0.31730604 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.17894 | -1.6071074 | price | 0.76243538 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99682694 | -0.0031730604 | ratio | 0.31730604 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7321563 | 0.23009455 | %p | -4.1819697 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.66403 | 3.9130435 | price | -3.3805703 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.73898 | 7.6028944 | price | -4.4426014 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0338057 | 0.033805703 | ratio | -3.3805703 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6804386 | -0.21296481 | %p | 7.3603567 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 490.60474 | -27.490119 | price | 5.306001 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 779.08186 | -49.381623 | price | 5.9606276 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94693999 | -0.05306001 | ratio | 5.306001 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5910002 | 0.084358332 | %p | -1.8718668 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.95618 | 2.3187251 | price | -2.304038 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 165.03507 | 6.1719759 | price | -3.8850911 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0230404 | 0.02304038 | ratio | -2.304038 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0666711 | 0.26932547 | %p | -33.777756 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1711.4688 | 379.77232 | price | -28.517935 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2838.9402 | -34.250235 | price | 1.1920628 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2851793 | 0.28517935 | ratio | -28.517935 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5386936 | 0.089009517 | %p | -2.5802223 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 378.0751 | 9.9051383 | price | -2.6903711 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 565.37403 | 13.019602 | price | -2.35711 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0269037 | 0.026903711 | ratio | -2.6903711 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7784957 | -0.55330551 | %p | 10.377459 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 225.22222 | -24.329365 | price | 9.7492328 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 373.33966 | -36.716828 | price | 8.9540903 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90250767 | -0.097492328 | ratio | 9.7492328 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.078732 | -0.50786177 | %p | 5.9145894 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 964.14229 | -85.094862 | price | 8.1101647 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1703.9703 | -126.88835 | price | 6.9305379 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91889835 | -0.081101647 | ratio | 8.1101647 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6490033 | 0.021445338 | %p | -0.59117838 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.142292 | 1.1146245 | price | -1.1607327 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.16118 | 0.27829781 | price | -0.17968274 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0116073 | 0.011607327 | ratio | -1.1607327 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2175931 | 0.6102858 | %p | -9.2365282 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1428.4111 | 72.675889 | price | -5.3606258 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2295.2384 | 54.128966 | price | -2.4152755 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0536063 | 0.053606258 | ratio | -5.3606258 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

