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


## ridge-v2-20261118T135229658420Z-aeb0e9a5b6fb4aa2a1a3c2bf5e85a20e

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135229658420Z-aeb0e9a5b6fb4aa2a1a3c2bf5e85a20e | v1feat | 4.5391348 | 553.57874 | 910.2849 | 1.0021178 | 1.4572497 (direct) | 1.4749999 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5391348 | -0.067954562 | %p | 1.4749999 | improved |
| mae | 532.31701 | 553.57874 | 21.261737 | price | -3.9941872 | worsened |
| rmse | 943.1701 | 910.2849 | -32.885197 | price | 3.4866666 | improved |
| rmae | 1 | 1.0021178 | 0.0021178169 | ratio | -0.21178169 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.439733 | -0.32876352 | %p | 6.89449 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.36759 | -8.9011858 | price | 6.4375965 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.41889 | -18.367164 | price | 8.7136526 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93562404 | -0.064375965 | ratio | 6.4375965 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8491429 | 0.34708115 | %p | -6.3082016 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 122.22134 | 6.4703557 | price | -5.5898924 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 182.97472 | 11.838627 | price | -6.9176683 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0558989 | 0.055898924 | ratio | -5.5898924 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.728634 | -0.16476938 | %p | 5.6946563 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 497.18972 | -20.905138 | price | 4.0350021 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 782.2103 | -46.253176 | price | 5.5830073 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95964998 | -0.040350021 | ratio | 4.0350021 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5769182 | 0.070276253 | %p | -1.5593929 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.04382 | 1.4063745 | price | -1.3974663 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 160.99468 | 2.1315874 | price | -1.3417763 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0139747 | 0.013974663 | ratio | -1.3974663 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.010062 | 0.21271634 | %p | -26.678058 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1620.5357 | 288.83929 | price | -21.689574 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2724.0606 | -149.12983 | price | 5.1903914 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2168957 | 0.21689574 | ratio | -21.689574 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5739886 | 0.12430456 | %p | -3.6033608 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 381.96443 | 13.794466 | price | -3.7467659 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 572.99301 | 20.638573 | price | -3.7364728 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0374677 | 0.037467659 | ratio | -3.7467659 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7408145 | -0.59098672 | %p | 11.084185 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.59524 | -26.956349 | price | 10.801915 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 355.715 | -54.341489 | price | 13.252196 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89198085 | -0.10801915 | ratio | 10.801915 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9415835 | -0.64501019 | %p | 7.5118284 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 954.7747 | -94.462451 | price | 9.0029647 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1695.6307 | -135.22789 | price | 7.3860367 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.90997035 | -0.090029647 | ratio | 9.0029647 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4647414 | -0.16281656 | %p | 4.4883242 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.932806 | -4.0948617 | price | 4.2642519 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 142.69508 | -12.187805 | price | 7.8690457 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.95735748 | -0.042642519 | ratio | 4.2642519 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0657298 | 0.45842245 | %p | -6.938113 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1413.1621 | 57.426877 | price | -4.2358477 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2293.156 | 52.046592 | price | -2.3223584 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0423585 | 0.042358477 | ratio | -4.2358477 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5391348 | -0.067124702 | %p | 1.4572497 | improved |
| mae | 565.55167 | 553.57874 | -11.972929 | price | 2.1170353 | improved |
| rmse | 926.40586 | 910.2849 | -16.120956 | price | 1.7401613 | improved |
| rmae | 1.0199316 | 1.0021178 | -0.017813751 | ratio | 1.7465634 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.439733 | -0.29007799 | %p | 6.1329721 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.36759 | -8.4624506 | price | 6.1397723 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.41889 | -16.760057 | price | 8.0123059 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93562404 | -0.061202904 | ratio | 6.1397723 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8491429 | 0.1169866 | %p | -2.0408829 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 122.22134 | 2.5573123 | price | -2.1370768 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 182.97472 | 4.2357326 | price | -2.3697867 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0558989 | 0.022093222 | ratio | -2.1370768 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.728634 | 0.048195432 | %p | -1.7980428 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 497.18972 | 6.5849802 | price | -1.342217 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 782.2103 | 3.1284465 | price | -0.40155556 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95964998 | 0.012709989 | ratio | -1.342217 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5769182 | -0.014082079 | %p | 0.30673227 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.04382 | -0.9123506 | price | 0.88615432 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 160.99468 | -4.0403885 | price | 2.4482 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0139747 | -0.0090657165 | ratio | 0.88615432 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.010062 | -0.056609137 | %p | 5.3070843 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1620.5357 | -90.933036 | price | 5.3131578 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2724.0606 | -114.87959 | price | 4.0465661 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2168957 | -0.068283607 | ratio | 5.3131578 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5739886 | 0.035295045 | %p | -0.99740327 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 381.96443 | 3.8893281 | price | -1.0287184 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 572.99301 | 7.6189713 | price | -1.3475984 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0374677 | 0.010563947 | ratio | -1.0287184 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7408145 | -0.037681211 | %p | 0.78855801 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.59524 | -2.6269841 | price | 1.1663965 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 355.715 | -17.624661 | price | 4.7208114 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89198085 | -0.010526818 | ratio | 1.1663965 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9415835 | -0.13714842 | %p | 1.6976479 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 954.7747 | -9.3675889 | price | 0.97159818 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1695.6307 | -8.3395372 | price | 0.489418 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.90997035 | -0.0089279996 | ratio | 0.97159818 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4647414 | -0.1842619 | %p | 5.0496502 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.932806 | -5.2094862 | price | 5.3627375 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 142.69508 | -12.466103 | price | 8.0342922 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.95735748 | -0.054249846 | ratio | 5.3627375 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0657298 | -0.15186335 | %p | 2.104072 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1413.1621 | -15.249012 | price | 1.0675507 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2293.156 | -2.0823735 | price | 0.090725806 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0423585 | -0.011247781 | ratio | 1.0675507 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5391348 | 0.037993473 | %p | -0.84408532 | worsened |
| mae | 557.9753 | 553.57874 | -4.3965605 | price | 0.78794895 | improved |
| rmse | 915.84853 | 910.2849 | -5.5636336 | price | 0.60748403 | improved |
| rmae | 0.99470404 | 1.0021178 | 0.0074137721 | ratio | -0.74532441 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.439733 | 0.013305276 | %p | -0.30058722 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.36759 | 0.62055336 | price | -0.48199429 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 192.41889 | 0.83865682 | price | -0.4377575 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93562404 | 0.0044880224 | ratio | -0.48199429 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.8491429 | 0.11622841 | %p | -2.0273877 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 122.22134 | 2.7035573 | price | -2.2620544 | worsened |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 182.97472 | 2.102631 | price | -1.1624961 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0558989 | 0.023356667 | ratio | -2.2620544 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.728634 | -0.0056811921 | %p | 0.20777386 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 497.18972 | 3.4150198 | price | -0.69161497 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 782.2103 | -6.047586 | price | 0.76720907 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.95964998 | 0.0065914951 | ratio | -0.69161497 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.5769182 | 0.15172965 | %p | -3.4287726 | worsened |
| 8 | 양파/RETAIL | mae | 98.860558 | 102.04382 | 3.1832669 | price | -3.2199565 | worsened |
| 8 | 양파/RETAIL | rmse | 158.71298 | 160.99468 | 2.2817035 | price | -1.4376289 | worsened |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 1.0139747 | 0.031631037 | ratio | -3.2199565 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.010062 | -0.030837379 | %p | 2.9625706 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1620.5357 | -61.160714 | price | 3.6368463 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2724.0606 | -70.347694 | price | 2.5174451 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2168957 | -0.045926919 | ratio | 3.6368463 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.5739886 | 0.11629725 | %p | -3.3634365 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 381.96443 | 12.110672 | price | -3.2744488 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 572.99301 | 21.405641 | price | -3.8807345 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0374677 | 0.032894242 | ratio | -3.2744488 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7408145 | -0.013457667 | %p | 0.28306471 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 222.59524 | -0.003968254 | price | 0.0017826901 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 355.715 | -1.5493281 | price | 0.43366437 | improved |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89198085 | -1.5901538e-05 | ratio | 0.0017826901 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9415835 | 0.0017904802 | %p | -0.022550716 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 954.7747 | -5.0711462 | price | 0.52832924 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1695.6307 | -14.253179 | price | 0.83357586 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.90997035 | -0.0048331745 | ratio | 0.52832924 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4647414 | 0.1076589 | %p | -3.2069187 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 91.932806 | 2.6640316 | price | -2.9842816 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 142.69508 | 1.5641997 | price | -1.1083327 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.95735748 | 0.027742334 | ratio | -2.9842816 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.0657298 | -0.077099 | %p | 1.0793903 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1413.1621 | -2.4268775 | price | 0.17143942 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2293.156 | 8.3686197 | price | -0.36627564 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0423585 | -0.0017900822 | ratio | 0.17143942 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T135507144504Z-37e1097038364262ac1f76e19b8aac02

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135507144504Z-37e1097038364262ac1f76e19b8aac02 | v1feat_garak | 4.54983 | 555.1525 | 885.59494 | 1.0052831 | 1.2250618 (direct) | 1.2428538 (direct) | 6 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.54983 | -0.057259385 | %p | 1.2428538 | improved |
| mae | 532.31701 | 555.1525 | 22.835495 | price | -4.2898301 | worsened |
| rmse | 943.1701 | 885.59494 | -57.57516 | price | 6.1044302 | improved |
| rmae | 1 | 1.0052831 | 0.0052830556 | ratio | -0.52830556 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4253069 | -0.34318965 | %p | 7.19702 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 128.86166 | -9.4071146 | price | 6.8034989 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.22089 | -18.565163 | price | 8.807586 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93196501 | -0.068034989 | ratio | 6.8034989 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8086218 | 0.30655997 | %p | -5.571729 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.25692 | 5.5059289 | price | -4.7567014 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 181.54615 | 10.410058 | price | -6.0829124 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.047567 | 0.047567014 | ratio | -4.7567014 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8174596 | -0.075943772 | %p | 2.6247212 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 516.35968 | -1.7351779 | price | 0.33491509 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 794.4573 | -34.006182 | price | 4.1047292 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.99665085 | -0.0033491509 | ratio | 0.33491509 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5117569 | 0.0051149934 | %p | -0.113499 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 100.44622 | -0.19123506 | price | 0.19002375 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.85283 | -0.010257478 | price | 0.0064568037 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.99809976 | -0.0019002375 | ratio | 0.19002375 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0135551 | 0.21620939 | %p | -27.116142 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1609.8438 | 278.14732 | price | -20.886691 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2420.8858 | -452.30464 | price | 15.742244 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2088669 | 0.20886691 | ratio | -20.886691 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.6180703 | 0.16838628 | %p | -4.8812087 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 385.8498 | 17.679842 | price | -4.802087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 582.52646 | 30.172026 | price | -5.4624394 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0480209 | 0.04802087 | ratio | -4.802087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8017184 | -0.53008286 | %p | 9.9419096 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 226.46429 | -23.087302 | price | 9.2515146 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 367.27408 | -42.782405 | price | 10.433296 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90748485 | -0.092515146 | ratio | 9.2515146 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0250786 | -0.56151513 | %p | 6.5394398 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 967.50988 | -81.727273 | price | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1741.1694 | -89.689234 | price | 4.8987526 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92210791 | -0.077892088 | ratio | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4539222 | -0.17363572 | %p | 4.7865732 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.916996 | -4.1106719 | price | 4.2807162 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 142.35358 | -12.529304 | price | 8.0895343 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.95719284 | -0.042807162 | ratio | 4.2807162 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.02281 | 0.41550265 | %p | -6.2885322 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1403.0158 | 47.280632 | price | -3.4874534 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2274.6629 | 33.553506 | price | -1.4971828 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0348745 | 0.034874534 | ratio | -3.4874534 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.54983 | -0.056429525 | %p | 1.2250618 | improved |
| mae | 565.55167 | 555.1525 | -10.399171 | price | 1.8387659 | improved |
| rmse | 926.40586 | 885.59494 | -40.810919 | price | 4.4052959 | improved |
| rmae | 1.0199316 | 1.0052831 | -0.014648513 | ratio | 1.436225 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4253069 | -0.30450412 | %p | 6.4379764 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 128.86166 | -8.9683794 | price | 6.5068395 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.22089 | -16.958055 | price | 8.106961 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93196501 | -0.064861929 | ratio | 6.5068395 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8086218 | 0.07646542 | %p | -1.333973 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.25692 | 1.5928854 | price | -1.3311313 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 181.54615 | 2.807164 | price | -1.5705382 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.047567 | 0.013761311 | ratio | -1.3311313 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8174596 | 0.13702104 | %p | -5.1118887 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 516.35968 | 25.754941 | price | -5.2496314 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 794.4573 | 15.375441 | price | -1.9735334 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.99665085 | 0.049710859 | ratio | -5.2496314 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5117569 | -0.079243339 | %p | 1.7260583 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 100.44622 | -2.5099602 | price | 2.4378918 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.85283 | -6.1822334 | price | 3.7460119 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.99809976 | -0.024940618 | ratio | 2.4378918 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0135551 | -0.053116089 | %p | 4.9796125 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1609.8438 | -101.625 | price | 5.9378823 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2420.8858 | -418.05441 | price | 14.725721 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2088669 | -0.076312437 | ratio | 5.9378823 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.6180703 | 0.07937676 | %p | -2.2431092 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 385.8498 | 7.7747036 | price | -2.0563913 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 582.52646 | 17.152425 | price | -3.033819 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0480209 | 0.021117159 | ratio | -2.0563913 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8017184 | 0.023222649 | %p | -0.48598241 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 226.46429 | 1.2420635 | price | -0.55148354 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 367.27408 | -6.0655775 | price | 1.6246807 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90748485 | 0.0049771813 | ratio | -0.55148354 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0250786 | -0.053653365 | %p | 0.66413102 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 967.50988 | 3.3675889 | price | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1741.1694 | 37.199116 | price | -2.1830848 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92210791 | 0.0032095594 | ratio | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4539222 | -0.19508105 | %p | 5.3461463 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.916996 | -5.2252964 | price | 5.3790129 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 142.35358 | -12.807602 | price | 8.2543854 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.95719284 | -0.054414489 | ratio | 5.3790129 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.02281 | -0.19478315 | %p | 2.6987272 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1403.0158 | -25.395257 | price | 1.7778676 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2274.6629 | -20.57546 | price | 0.8964411 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0348745 | -0.018731724 | ratio | 1.7778676 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### V1FEAT: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5391348 | 4.54983 | 0.010695177 | %p | -0.23562149 | worsened |
| mae | 553.57874 | 555.1525 | 1.5737577 | price | -0.28428795 | worsened |
| rmse | 910.2849 | 885.59494 | -24.689963 | price | 2.7123336 | improved |
| rmae | 1.0021178 | 1.0052831 | 0.0031652387 | ratio | -0.31585495 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.439733 | 4.4253069 | -0.014426129 | %p | 0.32493235 | improved |
| 1 | 대파/RETAIL | mae | 129.36759 | 128.86166 | -0.50592885 | price | 0.39107852 | improved |
| 1 | 대파/RETAIL | rmse | 192.41889 | 192.22089 | -0.19799851 | price | 0.10289973 | improved |
| 1 | 대파/RETAIL | rmae | 0.93562404 | 0.93196501 | -0.0036590246 | ratio | 0.39107852 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.8491429 | 5.8086218 | -0.040521176 | %p | 0.69277117 | improved |
| 2 | 대파/WHOLESALE | mae | 122.22134 | 121.25692 | -0.96442688 | price | 0.78908221 | improved |
| 2 | 대파/WHOLESALE | rmse | 182.97472 | 181.54615 | -1.4285687 | price | 0.78074648 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0558989 | 1.047567 | -0.0083319105 | ratio | 0.78908221 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.728634 | 2.8174596 | 0.088825604 | %p | -3.255314 | worsened |
| 7 | 양파/WHOLESALE | mae | 497.18972 | 516.35968 | 19.16996 | price | -3.8556631 | worsened |
| 7 | 양파/WHOLESALE | rmse | 782.2103 | 794.4573 | 12.246994 | price | -1.5656907 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95964998 | 0.99665085 | 0.03700087 | ratio | -3.8556631 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5769182 | 4.5117569 | -0.06516126 | %p | 1.4236929 | improved |
| 8 | 양파/RETAIL | mae | 102.04382 | 100.44622 | -1.5976096 | price | 1.5656112 | improved |
| 8 | 양파/RETAIL | rmse | 160.99468 | 158.85283 | -2.1418448 | price | 1.3303824 | improved |
| 8 | 양파/RETAIL | rmae | 1.0139747 | 0.99809976 | -0.015874901 | ratio | 1.5656112 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.010062 | 1.0135551 | 0.0034930472 | %p | -0.34582503 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1620.5357 | 1609.8438 | -10.691964 | price | 0.65977961 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2724.0606 | 2420.8858 | -303.17481 | price | 11.129518 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2168957 | 1.2088669 | -0.00802883 | ratio | 0.65977961 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5739886 | 3.6180703 | 0.044081714 | %p | -1.2334039 | worsened |
| 10 | 깐마늘/RETAIL | mae | 381.96443 | 385.8498 | 3.8853755 | price | -1.0172087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 572.99301 | 582.52646 | 9.5334534 | price | -1.6637993 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0374677 | 1.0480209 | 0.010553212 | ratio | -1.0172087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7408145 | 4.8017184 | 0.06090386 | %p | -1.2846708 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59524 | 226.46429 | 3.8690476 | price | -1.7381538 | worsened |
| 9001 | 배추/RETAIL | rmse | 355.715 | 367.27408 | 11.559084 | price | -3.2495351 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89198085 | 0.90748485 | 0.015503999 | ratio | -1.7381538 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9415835 | 8.0250786 | 0.08349506 | %p | -1.0513654 | worsened |
| 9002 | 배추/WHOLESALE | mae | 954.7747 | 967.50988 | 12.735178 | price | -1.3338411 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1695.6307 | 1741.1694 | 45.538654 | price | -2.6856469 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.90997035 | 0.92210791 | 0.012137559 | ratio | -1.3338411 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.4647414 | 3.4539222 | -0.010819155 | %p | 0.31226444 | improved |
| 9011 | 무/RETAIL | mae | 91.932806 | 91.916996 | -0.015810277 | price | 0.017197644 | improved |
| 9011 | 무/RETAIL | rmse | 142.69508 | 142.35358 | -0.34149915 | price | 0.2393209 | improved |
| 9011 | 무/RETAIL | rmae | 0.95735748 | 0.95719284 | -0.00016464293 | ratio | 0.017197644 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0657298 | 7.02281 | -0.042919795 | %p | 0.60743612 | improved |
| 9012 | 무/WHOLESALE | mae | 1413.1621 | 1403.0158 | -10.146245 | price | 0.71798171 | improved |
| 9012 | 무/WHOLESALE | rmse | 2293.156 | 2274.6629 | -18.493087 | price | 0.80644695 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0423585 | 1.0348745 | -0.0074839432 | ratio | 0.71798171 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T135554430186Z-d55b1f362df24e9ea30f704ef39793c2

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135554430186Z-d55b1f362df24e9ea30f704ef39793c2 | v1feat_cross | 4.5686864 | 561.06115 | 923.10566 | 1.015589 | 0.81569688 (direct) | 0.83356262 (direct) | 6 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5686864 | -0.038402975 | %p | 0.83356262 | improved |
| mae | 532.31701 | 561.06115 | 28.744148 | price | -5.3998177 | worsened |
| rmse | 943.1701 | 923.10566 | -20.064436 | price | 2.1273401 | improved |
| rmae | 1 | 1.015589 | 0.015588998 | ratio | -1.5588998 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5485647 | -0.21993183 | %p | 4.6121839 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 132.79447 | -5.4743083 | price | 3.959179 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 198.25985 | -12.526199 | price | 5.9426131 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.96040821 | -0.03959179 | ratio | 3.959179 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8303609 | 0.32829912 | %p | -5.9668381 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.3083 | 5.5573123 | price | -4.8010927 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 181.99011 | 10.854018 | price | -6.3423312 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0480109 | 0.048010927 | ratio | -4.8010927 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8337759 | -0.059627473 | %p | 2.0608075 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 508.80237 | -9.2924901 | price | 1.7935886 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 835.12668 | 6.6631953 | price | -0.80428352 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.98206411 | -0.017935886 | ratio | 1.7935886 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6185251 | 0.11188322 | %p | -2.4826294 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.77689 | 2.1394422 | price | -2.1258907 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 163.61714 | 4.7540515 | price | -2.9925462 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0212589 | 0.021258907 | ratio | -2.1258907 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0652587 | 0.26791303 | %p | -33.600612 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1707.75 | 376.05357 | price | -28.238686 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2807.0542 | -66.136243 | price | 2.3018399 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2823869 | 0.28238686 | ratio | -28.238686 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5657216 | 0.11603754 | %p | -3.363715 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 381.35968 | 13.189723 | price | -3.5825094 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 573.98502 | 21.630583 | price | -3.9160695 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0358251 | 0.035825094 | ratio | -3.5825094 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7257219 | -0.60607933 | %p | 11.367253 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 223.4127 | -26.138889 | price | 10.474343 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 362.53961 | -47.516876 | price | 11.587886 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89525657 | -0.10474343 | ratio | 10.474343 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9574773 | -0.62911647 | %p | 7.3267292 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 956.29249 | -92.944664 | price | 8.8583085 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1684.8676 | -145.99104 | price | 7.9739114 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91141691 | -0.088583085 | ratio | 8.8583085 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6201683 | -0.0073896053 | %p | 0.20370744 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 96.162055 | 0.13438735 | price | -0.13994649 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 148.72224 | -6.1606443 | price | 3.9776147 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0013995 | 0.0013994649 | ratio | -0.13994649 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9212894 | 0.31398206 | %p | -4.7520426 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1379.9526 | 24.217391 | price | -1.7862922 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2274.8942 | 33.7848 | price | -1.5075034 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0178629 | 0.017862922 | ratio | -1.7862922 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5686864 | -0.037573115 | %p | 0.81569688 | improved |
| mae | 565.55167 | 561.06115 | -4.4905185 | price | 0.79400676 | improved |
| rmse | 926.40586 | 923.10566 | -3.300195 | price | 0.35623641 | improved |
| rmae | 1.0199316 | 1.015589 | -0.0043425698 | ratio | 0.4257707 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5485647 | -0.1812463 | %p | 3.8319988 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 132.79447 | -5.0355731 | price | 3.6534656 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 198.25985 | -10.919092 | price | 5.2199767 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.96040821 | -0.03641873 | ratio | 3.6534656 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8303609 | 0.098204567 | %p | -1.7132221 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.3083 | 1.6442688 | price | -1.374071 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 181.99011 | 3.2511232 | price | -1.8189223 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0480109 | 0.014205225 | ratio | -1.374071 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8337759 | 0.15333734 | %p | -5.7206062 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 508.80237 | 18.197628 | price | -3.7092239 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 835.12668 | 56.044818 | price | -7.1937008 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.98206411 | 0.035124125 | ratio | -3.7092239 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6185251 | 0.027524884 | %p | -0.59954003 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.77689 | -0.17928287 | price | 0.17413513 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 163.61714 | -1.4179244 | price | 0.85916551 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0212589 | -0.0017814727 | ratio | 0.17413513 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0652587 | -0.0014124485 | %p | 0.13241649 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1707.75 | -3.71875 | price | 0.21728413 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2807.0542 | -31.886007 | price | 1.1231659 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2823869 | -0.0027924908 | ratio | 0.21728413 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5657216 | 0.027028023 | %p | -0.76378535 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 381.35968 | 3.284585 | price | -0.86876522 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 573.98502 | 8.6109818 | price | -1.5230593 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0358251 | 0.0089213823 | ratio | -0.86876522 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7257219 | -0.052773823 | %p | 1.1044024 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 223.4127 | -1.8095238 | price | 0.80343928 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 362.53961 | -10.800048 | price | 2.8928211 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89525657 | -0.0072511012 | ratio | 0.80343928 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9574773 | -0.1212547 | %p | 1.5009125 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 956.29249 | -7.8498024 | price | 0.81417467 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1684.8676 | -19.102693 | price | 1.1210696 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91141691 | -0.0074814377 | ratio | 0.81417467 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6201683 | -0.028834943 | %p | 0.79021424 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 96.162055 | -0.98023715 | price | 1.0090735 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 148.72224 | -6.4389421 | price | 4.1498409 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0013995 | -0.010207862 | ratio | 1.0090735 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9212894 | -0.29630374 | %p | 4.1052985 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1379.9526 | -48.458498 | price | 3.3924757 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2274.8942 | -20.344165 | price | 0.88636394 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0178629 | -0.035743336 | ratio | 3.3924757 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### V1FEAT: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5391348 | 4.5686864 | 0.029551587 | %p | -0.65104009 | worsened |
| mae | 553.57874 | 561.06115 | 7.4824102 | price | -1.3516433 | worsened |
| rmse | 910.2849 | 923.10566 | 12.820761 | price | -1.4084339 | worsened |
| rmae | 1.0021178 | 1.015589 | 0.013471182 | ratio | -1.3442712 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.439733 | 4.5485647 | 0.10883169 | %p | -2.4513116 | worsened |
| 1 | 대파/RETAIL | mae | 129.36759 | 132.79447 | 3.4268775 | price | -2.6489459 | worsened |
| 1 | 대파/RETAIL | rmse | 192.41889 | 198.25985 | 5.8409647 | price | -3.0355465 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93562404 | 0.96040821 | 0.024784175 | ratio | -2.6489459 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.8491429 | 5.8303609 | -0.018782029 | %p | 0.32110738 | improved |
| 2 | 대파/WHOLESALE | mae | 122.22134 | 121.3083 | -0.91304348 | price | 0.74704094 | improved |
| 2 | 대파/WHOLESALE | rmse | 182.97472 | 181.99011 | -0.98460948 | price | 0.53811231 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0558989 | 1.0480109 | -0.0078879973 | ratio | 0.74704094 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.728634 | 2.8337759 | 0.1051419 | %p | -3.8532798 | worsened |
| 7 | 양파/WHOLESALE | mae | 497.18972 | 508.80237 | 11.612648 | price | -2.3356573 | worsened |
| 7 | 양파/WHOLESALE | rmse | 782.2103 | 835.12668 | 52.916372 | price | -6.7649801 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95964998 | 0.98206411 | 0.022414135 | ratio | -2.3356573 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5769182 | 4.6185251 | 0.041606963 | %p | -0.90906068 | worsened |
| 8 | 양파/RETAIL | mae | 102.04382 | 102.77689 | 0.73306773 | price | -0.7183852 | worsened |
| 8 | 양파/RETAIL | rmse | 160.99468 | 163.61714 | 2.6224641 | price | -1.6289135 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0139747 | 1.0212589 | 0.0072842439 | ratio | -0.7183852 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.010062 | 1.0652587 | 0.055196688 | %p | -5.4646831 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1620.5357 | 1707.75 | 87.214286 | price | -5.3818182 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2724.0606 | 2807.0542 | 82.993585 | price | -3.0466864 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2168957 | 1.2823869 | 0.065491116 | ratio | -5.3818182 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5739886 | 3.5657216 | -0.0082670225 | %p | 0.23131082 | improved |
| 10 | 깐마늘/RETAIL | mae | 381.96443 | 381.35968 | -0.60474308 | price | 0.15832445 | improved |
| 10 | 깐마늘/RETAIL | rmse | 572.99301 | 573.98502 | 0.99201049 | price | -0.17312785 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0374677 | 1.0358251 | -0.001642565 | ratio | 0.15832445 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7408145 | 4.7257219 | -0.015092612 | %p | 0.31835483 | improved |
| 9001 | 배추/RETAIL | mae | 222.59524 | 223.4127 | 0.81746032 | price | -0.3672407 | worsened |
| 9001 | 배추/RETAIL | rmse | 355.715 | 362.53961 | 6.8246127 | price | -1.918562 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89198085 | 0.89525657 | 0.0032757168 | ratio | -0.3672407 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9415835 | 7.9574773 | 0.015893724 | %p | -0.20013293 | worsened |
| 9002 | 배추/WHOLESALE | mae | 954.7747 | 956.29249 | 1.5177866 | price | -0.15896803 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1695.6307 | 1684.8676 | -10.763156 | price | 0.63475825 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.90997035 | 0.91141691 | 0.001446562 | ratio | -0.15896803 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.4647414 | 3.6201683 | 0.15542696 | %p | -4.4859613 | worsened |
| 9011 | 무/RETAIL | mae | 91.932806 | 96.162055 | 4.229249 | price | -4.6003697 | worsened |
| 9011 | 무/RETAIL | rmse | 142.69508 | 148.72224 | 6.0271606 | price | -4.2238041 | worsened |
| 9011 | 무/RETAIL | rmae | 0.95735748 | 1.0013995 | 0.044041984 | ratio | -4.6003697 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0657298 | 6.9212894 | -0.14444039 | %p | 2.0442388 | improved |
| 9012 | 무/WHOLESALE | mae | 1413.1621 | 1379.9526 | -33.209486 | price | 2.3500126 | improved |
| 9012 | 무/WHOLESALE | rmse | 2293.156 | 2274.8942 | -18.261792 | price | 0.79636064 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0423585 | 1.0178629 | -0.024495555 | ratio | 2.3500126 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T135635195036Z-6855b1a40faa47878ebaeeecf790cb52

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135635195036Z-6855b1a40faa47878ebaeeecf790cb52 | v1feat_anom | 4.7390609 | 632.248 | 988.39672 | 1.0904329 | -2.8830639 (direct) | -2.8645319 (direct) | 3 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.7390609 | 0.13197154 | %p | -2.8645319 | worsened |
| mae | 532.31701 | 632.248 | 99.930991 | price | -18.772835 | worsened |
| rmse | 943.1701 | 988.39672 | 45.226628 | price | -4.795172 | worsened |
| rmae | 1 | 1.0904329 | 0.090432886 | ratio | -9.0432886 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5821161 | -0.18638044 | %p | 3.9085787 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 133.60474 | -4.6640316 | price | 3.3731633 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 197.60705 | -13.179002 | price | 6.2523122 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.96626837 | -0.033731633 | ratio | 3.3731633 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.0687032 | 0.56664145 | %p | -10.298711 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 126.75889 | 11.007905 | price | -9.509988 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 186.68449 | 15.5484 | price | -9.0854011 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0950999 | 0.09509988 | ratio | -9.509988 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.305139 | 0.41173561 | %p | -14.230149 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 606.4585 | 88.363636 | price | -17.055494 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 931.42353 | 102.96005 | price | -12.427832 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1705549 | 0.17055494 | ratio | -17.055494 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6243721 | 0.1177302 | %p | -2.6123709 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 103.05578 | 2.4183267 | price | -2.4030087 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 161.34281 | 2.4797167 | price | -1.5609143 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0240301 | 0.024030087 | ratio | -2.4030087 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.4359685 | 0.63862287 | %p | -80.093602 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2237.9241 | 906.22768 | price | -68.05062 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3218.7465 | 345.55606 | price | -12.026911 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.6805062 | 0.6805062 | ratio | -68.05062 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5994958 | 0.14981175 | %p | -4.3427673 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 384.90514 | 16.735178 | price | -4.5455033 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 568.72483 | 16.370398 | price | -2.9637488 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.045455 | 0.045455033 | ratio | -4.5455033 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9067067 | -0.42509456 | %p | 7.9728132 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 233.51984 | -16.031746 | price | 6.4242212 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 384.34712 | -25.709363 | price | 6.2697127 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.93575779 | -0.064242212 | ratio | 6.4242212 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.1610011 | -0.42559264 | %p | 4.9564782 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 983.50198 | -65.735178 | price | 6.2650448 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1761.1001 | -69.758506 | price | 3.8101525 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.93734955 | -0.062650448 | ratio | 6.2650448 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6466819 | 0.019123931 | %p | -0.52718471 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 96.474308 | 0.44664032 | price | -0.46511628 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 145.90134 | -8.9815413 | price | 5.7989244 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0046512 | 0.0046511628 | ratio | -0.46511628 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0604246 | 0.45311726 | %p | -6.8578203 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1416.2767 | 60.541502 | price | -4.4655846 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2328.0895 | 86.980069 | price | -3.8811166 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0446558 | 0.044655846 | ratio | -4.4655846 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 3, 'worsened': 7, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.7390609 | 0.1328014 | %p | -2.8830639 | worsened |
| mae | 565.55167 | 632.248 | 66.696325 | price | -11.793144 | worsened |
| rmse | 926.40586 | 988.39672 | 61.990869 | price | -6.6915455 | worsened |
| rmae | 1.0199316 | 1.0904329 | 0.070501317 | ratio | -6.9123576 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5821161 | -0.14769491 | %p | 3.1226387 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 133.60474 | -4.2252964 | price | 3.0655846 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 197.60705 | -11.571895 | price | 5.5320552 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.96626837 | -0.030558573 | ratio | 3.0655846 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.0687032 | 0.3365469 | %p | -5.8712093 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 126.75889 | 7.0948617 | price | -5.9289843 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 186.68449 | 7.9455057 | price | -4.4453121 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0950999 | 0.061294178 | ratio | -5.9289843 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.305139 | 0.62470042 | %p | -23.305903 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 606.4585 | 115.85375 | price | -23.614479 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 931.42353 | 152.34167 | price | -19.554001 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.1705549 | 0.22361495 | ratio | -23.614479 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6243721 | 0.033371869 | %p | -0.72689757 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 103.05578 | 0.099601594 | price | -0.096741738 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 161.34281 | -3.6922592 | price | 2.2372573 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0240301 | 0.00098970705 | ratio | -0.096741738 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.4359685 | 0.36929739 | %p | -34.621485 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2237.9241 | 526.45536 | price | -30.760442 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3218.7465 | 379.80629 | price | -13.378454 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.6805062 | 0.39532685 | ratio | -30.760442 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5994958 | 0.060802232 | %p | -1.7182113 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 384.90514 | 6.8300395 | price | -1.8065299 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 568.72483 | 3.3507964 | price | -0.59266896 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.045455 | 0.018551322 | ratio | -1.8065299 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9067067 | 0.12821096 | %p | -2.6830819 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 233.51984 | 8.297619 | price | -3.684192 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 384.34712 | 11.007464 | price | -2.948378 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.93575779 | 0.033250115 | ratio | -3.684192 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.1610011 | 0.082269122 | %p | -1.018342 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 983.50198 | 19.359684 | price | -2.0079696 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1761.1001 | 57.129845 | price | -3.352749 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.93734955 | 0.018451199 | ratio | -2.0079696 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6466819 | -0.0023214073 | %p | 0.063617573 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 96.474308 | -0.66798419 | price | 0.68763478 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 145.90134 | -9.2598391 | price | 5.9678839 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0046512 | -0.0069561638 | ratio | 0.68763478 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0604246 | -0.15716854 | %p | 2.1775755 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1416.2767 | -12.134387 | price | 0.84950247 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2328.0895 | 32.851104 | price | -1.431272 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0446558 | -0.0089504112 | ratio | 0.84950247 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 3, 'worsened': 7, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### V1FEAT: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5391348 | 4.7390609 | 0.19992611 | %p | -4.4044981 | worsened |
| mae | 553.57874 | 632.248 | 78.669254 | price | -14.211032 | worsened |
| rmse | 910.2849 | 988.39672 | 78.111825 | price | -8.5810305 | worsened |
| rmae | 1.0021178 | 1.0904329 | 0.088315069 | ratio | -8.8128429 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.439733 | 4.5821161 | 0.14238308 | %p | -3.207019 | worsened |
| 1 | 대파/RETAIL | mae | 129.36759 | 133.60474 | 4.2371542 | price | -3.2752826 | worsened |
| 1 | 대파/RETAIL | rmse | 192.41889 | 197.60705 | 5.1881621 | price | -2.6962853 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93562404 | 0.96626837 | 0.030644331 | ratio | -3.2752826 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.8491429 | 6.0687032 | 0.2195603 | %p | -3.7537175 | worsened |
| 2 | 대파/WHOLESALE | mae | 122.22134 | 126.75889 | 4.5375494 | price | -3.7125671 | worsened |
| 2 | 대파/WHOLESALE | rmse | 182.97472 | 186.68449 | 3.7097731 | price | -2.0274785 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0558989 | 1.0950999 | 0.039200956 | ratio | -3.7125671 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.728634 | 3.305139 | 0.57650499 | %p | -21.127971 | worsened |
| 7 | 양파/WHOLESALE | mae | 497.18972 | 606.4585 | 109.26877 | price | -21.977279 | worsened |
| 7 | 양파/WHOLESALE | rmse | 782.2103 | 931.42353 | 149.21323 | price | -19.075845 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95964998 | 1.1705549 | 0.21090496 | ratio | -21.977279 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5769182 | 4.6243721 | 0.047453948 | %p | -1.0368101 | worsened |
| 8 | 양파/RETAIL | mae | 102.04382 | 103.05578 | 1.0119522 | price | -0.99168391 | worsened |
| 8 | 양파/RETAIL | rmse | 160.99468 | 161.34281 | 0.34812935 | price | -0.21623655 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0139747 | 1.0240301 | 0.010055424 | ratio | -0.99168391 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.010062 | 1.4359685 | 0.42590653 | %p | -42.166374 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1620.5357 | 2237.9241 | 617.38839 | price | -38.097796 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2724.0606 | 3218.7465 | 494.68589 | price | -18.159871 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2168957 | 1.6805062 | 0.46361046 | ratio | -38.097796 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5739886 | 3.5994958 | 0.025507187 | %p | -0.71368966 | worsened |
| 10 | 깐마늘/RETAIL | mae | 381.96443 | 384.90514 | 2.9407115 | price | -0.76989145 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 572.99301 | 568.72483 | -4.2681749 | price | 0.74489127 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0374677 | 1.045455 | 0.0079873748 | ratio | -0.76989145 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7408145 | 4.9067067 | 0.16589217 | %p | -3.4992334 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59524 | 233.51984 | 10.924603 | price | -4.9078333 | worsened |
| 9001 | 배추/RETAIL | rmse | 355.715 | 384.34712 | 28.632126 | price | -8.0491759 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89198085 | 0.93575779 | 0.043776933 | ratio | -4.9078333 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9415835 | 8.1610011 | 0.21941755 | %p | -2.7628941 | worsened |
| 9002 | 배추/WHOLESALE | mae | 954.7747 | 983.50198 | 28.727273 | price | -3.0088012 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1695.6307 | 1761.1001 | 65.469382 | price | -3.8610637 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.90997035 | 0.93734955 | 0.027379199 | ratio | -3.0088012 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.4647414 | 3.6466819 | 0.18194049 | %p | -5.2511998 | worsened |
| 9011 | 무/RETAIL | mae | 91.932806 | 96.474308 | 4.541502 | price | -4.9400232 | worsened |
| 9011 | 무/RETAIL | rmse | 142.69508 | 145.90134 | 3.2062636 | price | -2.2469336 | worsened |
| 9011 | 무/RETAIL | rmae | 0.95735748 | 1.0046512 | 0.047293682 | ratio | -4.9400232 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0657298 | 7.0604246 | -0.0053051838 | %p | 0.075083311 | improved |
| 9012 | 무/WHOLESALE | mae | 1413.1621 | 1416.2767 | 3.1146245 | price | -0.22040109 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2293.156 | 2328.0895 | 34.933477 | price | -1.5233799 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0423585 | 1.0446558 | 0.0022973694 | ratio | -0.22040109 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T150636830843Z-21ff0766e98b4a5aa33a7ee445f744b1

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150636830843Z-21ff0766e98b4a5aa33a7ee445f744b1 | market_alpha1 | 4.5029176 | 558.39263 | 915.83773 | 0.99522387 | 2.2435094 (direct) | 2.261118 (direct) | 8 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5029176 | -0.10417173 | %p | 2.261118 | improved |
| mae | 532.31701 | 558.39263 | 26.075626 | price | -4.8985146 | worsened |
| rmse | 943.1701 | 915.83773 | -27.33237 | price | 2.8979258 | improved |
| rmae | 1 | 0.99522387 | -0.004776133 | ratio | 0.4776133 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4239159 | -0.34458061 | %p | 7.2261898 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 128.67984 | -9.5889328 | price | 6.9349951 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 191.4758 | -19.310255 | price | 9.1610686 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93065005 | -0.069349951 | ratio | 6.9349951 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7375411 | 0.23547936 | %p | -4.2798385 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.61265 | 3.8616601 | price | -3.3361789 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.94432 | 9.8082271 | price | -5.7312441 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0333618 | 0.033361789 | ratio | -3.3361789 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7337523 | -0.15965109 | %p | 5.5177613 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 493.75889 | -24.335968 | price | 4.6972032 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 787.81351 | -40.649973 | price | 4.9066705 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95302797 | -0.046972032 | ratio | 4.6972032 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4293509 | -0.077291011 | %p | 1.7150466 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.948207 | -1.689243 | price | 1.6785432 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.79677 | -0.066321659 | price | 0.041747682 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.98321457 | -0.016785432 | ratio | 1.6785432 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0428321 | 0.2454864 | %p | -30.787952 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1684.7143 | 353.01786 | price | -26.508884 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2793.7867 | -79.403742 | price | 2.7636087 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2650888 | 0.26508884 | ratio | -26.508884 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4583287 | 0.0086446442 | %p | -0.25059235 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 369.93676 | 1.7667984 | price | -0.47988663 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 551.78873 | -0.56569897 | price | 0.10241594 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0047989 | 0.0047988663 | ratio | -0.47988663 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7576878 | -0.57411348 | %p | 10.767721 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.74603 | -26.805556 | price | 10.741489 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 357.13737 | -52.919113 | price | 12.905323 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89258511 | -0.10741489 | ratio | 10.741489 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9402009 | -0.64639285 | %p | 7.527931 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 959.98024 | -89.256917 | price | 8.5068391 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1709.3856 | -121.47302 | price | 6.634757 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91493161 | -0.085068391 | ratio | 8.5068391 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3584706 | -0.2690873 | %p | 7.4178635 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.300395 | -6.7272727 | price | 7.0055567 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.17938 | -13.703506 | price | 8.8476567 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.92994443 | -0.070055567 | ratio | 7.0055567 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.147096 | 0.53978867 | %p | -8.1695712 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1416.249 | 60.513834 | price | -4.4635438 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2286.0691 | 44.959703 | price | -2.006136 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0446354 | 0.044635438 | ratio | -4.4635438 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5029176 | -0.10334187 | %p | 2.2435094 | improved |
| mae | 565.55167 | 558.39263 | -7.1590402 | price | 1.2658508 | improved |
| rmse | 926.40586 | 915.83773 | -10.568129 | price | 1.1407666 | improved |
| rmae | 1.0199316 | 0.99522387 | -0.024707701 | ratio | 2.4224862 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4239159 | -0.30589508 | %p | 6.4673849 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 128.67984 | -9.1501976 | price | 6.6387543 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 191.4758 | -17.703147 | price | 8.4631593 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93065005 | -0.066176891 | ratio | 6.6387543 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7375411 | 0.0053848013 | %p | -0.093940238 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.61265 | -0.051383399 | price | 0.042939719 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.94432 | 2.2053327 | price | -1.2338286 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0333618 | -0.00044391327 | ratio | 0.042939719 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7337523 | 0.053313718 | %p | -1.9889923 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 493.75889 | 3.1541502 | price | -0.64291066 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 787.81351 | 8.7316494 | price | -1.1207615 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95302797 | 0.0060879782 | ratio | -0.64291066 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4293509 | -0.16164934 | %p | 3.5210049 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.948207 | -4.0079681 | price | 3.8928875 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.79677 | -6.2382975 | price | 3.779983 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.98321457 | -0.039825812 | ratio | 3.8928875 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0428321 | -0.023839072 | %p | 2.2349036 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1684.7143 | -26.754464 | price | 1.5632459 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2793.7867 | -45.153507 | price | 1.5905057 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2650888 | -0.020090513 | ratio | 1.5632459 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4583287 | -0.080364873 | %p | 2.2710323 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 369.93676 | -8.1383399 | price | 2.1525723 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 551.78873 | -13.585301 | price | 2.4028873 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0047989 | -0.022104845 | ratio | 2.1525723 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7576878 | -0.020807971 | %p | 0.43545023 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.74603 | -2.4761905 | price | 1.0994432 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 357.13737 | -16.202285 | price | 4.3398242 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89258511 | -0.0099225595 | ratio | 1.0994432 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9402009 | -0.13853109 | %p | 1.7147627 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 959.98024 | -4.1620553 | price | 0.43168476 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1709.3856 | 5.4153318 | price | -0.31780671 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91493161 | -0.0039667441 | ratio | 0.43168476 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3584706 | -0.29053263 | %p | 7.9619725 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.300395 | -7.8418972 | price | 8.0725882 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.17938 | -13.981804 | price | 9.011148 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.92994443 | -0.081662894 | ratio | 8.0725882 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.147096 | -0.070497128 | %p | 0.97674012 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1416.249 | -12.162055 | price | 0.85143945 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2286.0691 | -9.169263 | price | 0.39949066 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0446354 | -0.0089708193 | ratio | 0.85143945 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 8, 'worsened': 2, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5029176 | 0.0017763083 | %p | -0.039463508 | worsened |
| mae | 557.9753 | 558.39263 | 0.41732806 | price | -0.074793285 | worsened |
| rmse | 915.84853 | 915.83773 | -0.010806376 | price | 0.0011799305 | improved |
| rmae | 0.99470404 | 0.99522387 | 0.00051982219 | ratio | -0.05225898 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4239159 | -0.002511816 | %p | 0.056745894 | improved |
| 1 | 대파/RETAIL | mae | 128.74704 | 128.67984 | -0.067193676 | price | 0.052190464 | improved |
| 1 | 대파/RETAIL | rmse | 191.58023 | 191.4758 | -0.10443369 | price | 0.054511724 | improved |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93065005 | -0.00048596421 | ratio | 0.052190464 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.7375411 | 0.0046266113 | %p | -0.080702603 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 119.61265 | 0.09486166 | price | -0.079370329 | worsened |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 180.94432 | 0.072231074 | price | -0.039934893 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0333618 | 0.00081953218 | ratio | -0.079370329 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7337523 | -0.00056290677 | %p | 0.020586755 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 493.75889 | -0.015810277 | price | 0.0032019212 | improved |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 787.81351 | -0.44438307 | price | 0.056375341 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.95302797 | -3.0516181e-05 | ratio | 0.0032019212 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.4293509 | 0.0041623853 | %p | -0.094061197 | worsened |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.948207 | 0.087649402 | price | -0.088659628 | worsened |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.79677 | 0.083794523 | price | -0.052796265 | worsened |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.98321457 | 0.0008709422 | ratio | -0.088659628 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0428321 | 0.0019326857 | %p | -0.1856746 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1684.7143 | 3.0178571 | price | -0.17945315 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2793.7867 | -0.62160853 | price | 0.022244728 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2650888 | 0.002266175 | ratio | -0.17945315 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4583287 | 0.00063733543 | %p | -0.018432398 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 369.93676 | 0.083003953 | price | -0.022442371 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 551.78873 | 0.20136903 | price | -0.036507186 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0047989 | 0.0002254501 | ratio | -0.022442371 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7576878 | 0.0034155731 | %p | -0.071842187 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 222.74603 | 0.1468254 | price | -0.065959533 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 357.13737 | -0.12695161 | price | 0.035534365 | improved |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89258511 | 0.00058835689 | ratio | -0.065959533 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9402009 | 0.00040781851 | %p | -0.0051363872 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 959.98024 | 0.13438735 | price | -0.014000931 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1709.3856 | -0.49831045 | price | 0.02914294 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.91493161 | 0.00012808101 | ratio | -0.014000931 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.3584706 | 0.0013881694 | %p | -0.04135047 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 89.300395 | 0.031620553 | price | -0.03542174 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 141.17938 | 0.048498768 | price | -0.034364392 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.92994443 | 0.00032928586 | ratio | -0.03542174 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.147096 | 0.0042672269 | %p | -0.059741414 | worsened |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1416.249 | 0.66007905 | price | -0.046629289 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2286.0691 | 1.2817302 | price | -0.056098444 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0446354 | 0.00048687905 | ratio | -0.046629289 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 2, 'worsened': 8, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T150711389344Z-db8f29a8582042238df33c872ee6c2bd

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150711389344Z-db8f29a8582042238df33c872ee6c2bd | market_alpha100 | 4.4912665 | 555.59925 | 916.80348 | 0.99189299 | 2.4964496 (direct) | 2.5140126 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4912665 | -0.11582281 | %p | 2.5140126 | improved |
| mae | 532.31701 | 555.59925 | 23.282248 | price | -4.3737562 | worsened |
| rmse | 943.1701 | 916.80348 | -26.366614 | price | 2.7955312 | improved |
| rmae | 1 | 0.99189299 | -0.0081070077 | ratio | 0.81070077 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4368173 | -0.33167927 | %p | 6.9556362 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.01186 | -9.256917 | price | 6.6948716 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.05094 | -18.735106 | price | 8.8882095 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93305128 | -0.066948716 | ratio | 6.6948716 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7068277 | 0.20476593 | %p | -3.7216218 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.02767 | 3.2766798 | price | -2.8308008 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.44333 | 9.3072377 | price | -5.4385008 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.028308 | 0.028308008 | ratio | -2.8308008 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.740216 | -0.15318741 | %p | 5.2943674 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 494.12253 | -23.972332 | price | 4.627016 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 792.80326 | -35.660217 | price | 4.30438 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95372984 | -0.04627016 | ratio | 4.627016 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4088952 | -0.09774667 | %p | 2.1689469 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.501992 | -2.1354582 | price | 2.1219319 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.25039 | -0.61269807 | price | 0.38567679 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.97878068 | -0.021219319 | ratio | 2.1219319 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0311302 | 0.23378456 | %p | -29.320353 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1666.1205 | 334.42411 | price | -25.112638 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2804.8795 | -68.31094 | price | 2.3775291 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2511264 | 0.25112638 | ratio | -25.112638 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4541526 | 0.0044685658 | %p | -0.12953551 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 369.41502 | 1.2450593 | price | -0.33817514 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 550.60557 | -1.7488656 | price | 0.31662019 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0033818 | 0.0033817514 | ratio | -0.33817514 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.73088 | -0.60092124 | %p | 11.270511 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 221.61111 | -27.940476 | price | 11.196273 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 358.84957 | -51.206913 | price | 12.487771 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.88803727 | -0.11196273 | ratio | 11.196273 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9411167 | -0.64547707 | %p | 7.5172657 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 959.05138 | -90.185771 | price | 8.5953657 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1714.1025 | -116.75607 | price | 6.3771212 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91404634 | -0.085953657 | ratio | 8.5953657 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3518812 | -0.27567677 | %p | 7.5995139 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.158103 | -6.8695652 | price | 7.1537353 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 140.8945 | -13.988381 | price | 9.0315859 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.92846265 | -0.071537353 | ratio | 7.1537353 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1107486 | 0.50344128 | %p | -7.6194622 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1409.9723 | 54.237154 | price | -4.0005714 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2275.1552 | 34.045814 | price | -1.51915 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0400057 | 0.040005714 | ratio | -4.0005714 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.4912665 | -0.11499295 | %p | 2.4964496 | improved |
| mae | 565.55167 | 555.59925 | -9.9524181 | price | 1.7597717 | improved |
| rmse | 926.40586 | 916.80348 | -9.6023732 | price | 1.0365191 | improved |
| rmae | 1.0199316 | 0.99189299 | -0.028038576 | ratio | 2.7490644 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4368173 | -0.29299374 | %p | 6.1946184 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.01186 | -8.8181818 | price | 6.3978664 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.05094 | -17.127998 | price | 8.1882039 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93305128 | -0.063775656 | ratio | 6.3978664 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7068277 | -0.025328626 | %p | 0.44186906 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.02767 | -0.63636364 | price | 0.53179191 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.44333 | 1.7043433 | price | -0.95353752 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.028308 | -0.0054976951 | ratio | 0.53179191 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.740216 | 0.059777403 | %p | -2.2301352 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 494.12253 | 3.5177866 | price | -0.71703069 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 792.80326 | 13.721406 | price | -1.7612278 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95372984 | 0.0067898503 | ratio | -0.71703069 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4088952 | -0.182105 | %p | 3.9665649 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.501992 | -4.4541833 | price | 4.3262905 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.25039 | -6.7846739 | price | 4.1110499 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.97878068 | -0.044259699 | ratio | 4.3262905 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0311302 | -0.035540912 | %p | 3.3319465 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1666.1205 | -45.348214 | price | 2.6496665 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2804.8795 | -34.060704 | price | 1.1997683 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2511264 | -0.034052967 | ratio | 2.6496665 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4541526 | -0.084540951 | %p | 2.3890442 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 369.41502 | -8.6600791 | price | 2.2905711 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 550.60557 | -14.768467 | price | 2.6121588 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0033818 | -0.02352196 | ratio | 2.2905711 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.73088 | -0.047615729 | %p | 0.99645855 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 221.61111 | -3.6111111 | price | 1.6033547 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 358.84957 | -14.490085 | price | 3.881207 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.88803727 | -0.014470399 | ratio | 1.6033547 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9411167 | -0.1376153 | %p | 1.703427 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 959.05138 | -5.0909091 | price | 0.52802466 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1714.1025 | 10.132277 | price | -0.5946276 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91404634 | -0.0048520099 | ratio | 0.52802466 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3518812 | -0.29712211 | %p | 8.1425553 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.158103 | -7.9841897 | price | 8.2190666 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 140.8945 | -14.266678 | price | 9.1947472 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.92846265 | -0.08314468 | ratio | 8.2190666 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1107486 | -0.10684452 | %p | 1.4803345 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1409.9723 | -18.438735 | price | 1.2908564 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2275.1552 | -20.083152 | price | 0.87499198 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0400057 | -0.013600543 | ratio | 1.2908564 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 9, 'worsened': 1, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.4912665 | -0.0098747735 | %p | 0.21938377 | improved |
| mae | 557.9753 | 555.59925 | -2.3760498 | price | 0.42583423 | improved |
| rmse | 915.84853 | 916.80348 | 0.95494935 | price | -0.10426935 | worsened |
| rmae | 0.99470404 | 0.99189299 | -0.0028110525 | ratio | 0.2826019 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4368173 | 0.010389523 | %p | -0.23471575 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.01186 | 0.26482213 | price | -0.20569183 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 192.05094 | 0.47071521 | price | -0.24570135 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93305128 | 0.0019152707 | ratio | -0.20569183 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.7068277 | -0.026086816 | %p | 0.45503584 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 119.02767 | -0.49011858 | price | 0.41008003 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 180.44333 | -0.42875834 | price | 0.23705058 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.028308 | -0.0042342496 | ratio | 0.41008003 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.740216 | 0.0059007785 | %p | -0.21580462 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 494.12253 | 0.34782609 | price | -0.070442265 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 792.80326 | 4.5453737 | price | -0.57663536 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.95372984 | 0.00067135599 | ratio | -0.070442265 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.4088952 | -0.016293274 | %p | 0.36819389 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.501992 | -0.35856574 | price | 0.36269848 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.25039 | -0.46258189 | price | 0.29145814 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.97878068 | -0.0035629454 | ratio | 0.36269848 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0311302 | -0.0097691549 | %p | 0.93853018 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1666.1205 | -15.575893 | price | 0.92620122 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2804.8795 | 10.471194 | price | -0.37471954 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2511264 | -0.011696279 | ratio | 0.92620122 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4541526 | -0.003538743 | %p | 0.1023441 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 369.41502 | -0.43873518 | price | 0.11862396 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 550.60557 | -0.98179765 | price | 0.17799495 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0033818 | -0.0011916648 | ratio | 0.11862396 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.73088 | -0.023392186 | %p | 0.49202453 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 221.61111 | -0.98809524 | price | 0.44388983 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 358.84957 | 1.5852482 | price | -0.44371858 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.88803727 | -0.0039594829 | ratio | 0.44388983 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9411167 | 0.0013236053 | %p | -0.016670526 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 959.05138 | -0.7944664 | price | 0.082770208 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1714.1025 | 4.2186351 | price | -0.24672056 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.91404634 | -0.00075718478 | ratio | 0.082770208 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.3518812 | -0.0052013035 | %p | 0.15493523 | improved |
| 9011 | 무/RETAIL | mae | 89.268775 | 89.158103 | -0.11067194 | price | 0.12397609 | improved |
| 9011 | 무/RETAIL | rmse | 141.13088 | 140.8945 | -0.236376 | price | 0.16748709 | improved |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.92846265 | -0.0011525005 | ratio | 0.12397609 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.1107486 | -0.032080165 | %p | 0.4491241 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1409.9723 | -5.6166008 | price | 0.39676778 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2275.1552 | -9.6321587 | price | 0.4215779 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0400057 | -0.0041428451 | ratio | 0.39676778 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T150744343872Z-e965bd15283144b594792d92462703de

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150744343872Z-e965bd15283144b594792d92462703de | market_alpha1000 | 4.4906086 | 559.8397 | 927.41807 | 0.99451228 | 2.5107331 (direct) | 2.5282936 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4906086 | -0.11648074 | %p | 2.5282936 | improved |
| mae | 532.31701 | 559.8397 | 27.522698 | price | -5.1703586 | worsened |
| rmse | 943.1701 | 927.41807 | -15.752031 | price | 1.6701156 | improved |
| rmae | 1 | 0.99451228 | -0.0054877232 | ratio | 0.54877232 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4782806 | -0.29021596 | %p | 6.0861103 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 130.05138 | -8.2173913 | price | 5.9430564 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 193.98283 | -16.803216 | price | 7.9716926 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.94056944 | -0.059430564 | ratio | 5.9430564 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6029446 | 0.10088281 | %p | -1.8335456 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 117.17391 | 1.4229249 | price | -1.2292983 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.39129 | 7.2551952 | price | -4.2394303 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.012293 | 0.012292983 | ratio | -1.2292983 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7700325 | -0.12337083 | %p | 4.2638657 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 497.99209 | -20.102767 | price | 3.8801324 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 807.96176 | -20.501721 | price | 2.474668 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.96119868 | -0.038801324 | ratio | 3.8801324 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3868009 | -0.11984099 | %p | 2.6592082 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.015936 | -2.6215139 | price | 2.6049089 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 157.66013 | -1.2029605 | price | 0.75723096 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.97395091 | -0.026049089 | ratio | 2.6049089 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0629683 | 0.26562264 | %p | -33.313361 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1706.6071 | 374.91071 | price | -28.152866 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2882.1995 | 9.0091171 | price | -0.31355795 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2815287 | 0.28152866 | ratio | -28.152866 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4638734 | 0.014189403 | %p | -0.41132473 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 370.49802 | 2.3280632 | price | -0.63233384 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 551.43195 | -0.92248402 | price | 0.16700944 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0063233 | 0.0063233384 | ratio | -0.63233384 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.6918547 | -0.63994654 | %p | 12.002446 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 219.80952 | -29.742063 | price | 11.918202 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 367.48615 | -42.570334 | price | 10.381578 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.88081798 | -0.11918202 | ratio | 11.918202 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0317426 | -0.55485117 | %p | 6.461831 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 967.50988 | -81.727273 | price | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1732.7925 | -98.066145 | price | 5.3562926 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92210791 | -0.077892088 | ratio | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3654318 | -0.26212614 | %p | 7.2259671 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.577075 | -6.4505929 | price | 6.7174316 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.52555 | -13.35733 | price | 8.6241486 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.93282568 | -0.067174316 | ratio | 6.7174316 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0521567 | 0.44484935 | %p | -6.7326875 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1401.1621 | 45.426877 | price | -3.3507191 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2260.749 | 19.639569 | price | -0.87633243 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0335072 | 0.033507191 | ratio | -3.3507191 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.4906086 | -0.11565088 | %p | 2.5107331 | improved |
| mae | 565.55167 | 559.8397 | -5.7119683 | price | 1.0099817 | improved |
| rmse | 926.40586 | 927.41807 | 1.0122099 | price | -0.10926204 | worsened |
| rmae | 1.0199316 | 0.99451228 | -0.025419291 | ratio | 2.4922546 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4782806 | -0.25153043 | %p | 5.3179806 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 130.05138 | -7.7786561 | price | 5.6436581 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 193.98283 | -15.196109 | price | 7.2646455 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.94056944 | -0.056257504 | ratio | 5.6436581 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6029446 | -0.12921174 | %p | 2.254156 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 117.17391 | -2.4901186 | price | 2.0809249 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.39129 | -0.34769921 | price | 0.19452903 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.012293 | -0.02151272 | ratio | 2.0809249 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7700325 | 0.089593974 | %p | -3.3425117 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 497.99209 | 7.3873518 | price | -1.5057644 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 807.96176 | 28.879902 | price | -3.706915 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.96119868 | 0.014258686 | ratio | -1.5057644 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3868009 | -0.20419932 | %p | 4.4478178 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.015936 | -4.940239 | price | 4.7983902 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 157.66013 | -7.3749364 | price | 4.4687087 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.97395091 | -0.04908947 | ratio | 4.7983902 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0629683 | -0.0037028306 | %p | 0.34713891 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1706.6071 | -4.8616071 | price | 0.28406053 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2882.1995 | 43.259352 | price | -1.5237853 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2815287 | -0.0036506872 | ratio | 0.28406053 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4638734 | -0.074820114 | %p | 2.1143428 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 370.49802 | -7.5770751 | price | 2.0041191 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 551.43195 | -13.942086 | price | 2.4659933 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0063233 | -0.020580373 | ratio | 2.0041191 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.6918547 | -0.086641032 | %p | 1.8131445 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 219.80952 | -5.4126984 | price | 2.4032701 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 367.48615 | -5.8535063 | price | 1.5678769 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.88081798 | -0.021689697 | ratio | 2.4032701 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0317426 | -0.046989408 | %p | 0.58164336 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 967.50988 | 3.3675889 | price | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1732.7925 | 28.822206 | price | -1.6914735 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92210791 | 0.0032095594 | ratio | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3654318 | -0.28357148 | %p | 7.7712038 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.577075 | -7.5652174 | price | 7.7877691 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.52555 | -13.635628 | price | 8.7880407 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.93282568 | -0.078781642 | ratio | 7.7877691 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0521567 | -0.16543645 | %p | 2.2921276 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1401.1621 | -27.249012 | price | 1.907645 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2260.749 | -34.489397 | price | 1.5026499 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0335072 | -0.020099067 | ratio | 1.907645 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 9, 'worsened': 1, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.4906086 | -0.010532708 | %p | 0.23400083 | improved |
| mae | 557.9753 | 559.8397 | 1.8643999 | price | -0.33413664 | worsened |
| rmse | 915.84853 | 927.41807 | 11.569532 | price | -1.2632583 | worsened |
| rmae | 0.99470404 | 0.99451228 | -0.00019176808 | ratio | 0.019278908 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4782806 | 0.051852835 | %p | -1.1714375 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 130.05138 | 1.3043478 | price | -1.013109 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 193.98283 | 2.402605 | price | -1.2540986 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.94056944 | 0.0094334229 | ratio | -1.013109 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6029446 | -0.12996993 | %p | 2.2670831 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 117.17391 | -2.3438735 | price | 1.9611085 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 178.39129 | -2.4808008 | price | 1.3715775 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.012293 | -0.020249274 | ratio | 1.9611085 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7700325 | 0.035717349 | %p | -1.3062631 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 497.99209 | 4.2173913 | price | -0.85411247 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 807.96176 | 19.703869 | price | -2.499673 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.96119868 | 0.0081401913 | ratio | -0.85411247 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3868009 | -0.038387596 | %p | 0.86747935 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.015936 | -0.84462151 | price | 0.85435641 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 157.66013 | -1.0528443 | price | 0.66336374 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.97395091 | -0.0083927158 | ratio | 0.85435641 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0629683 | 0.022068927 | %p | -2.1201787 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1706.6071 | 24.910714 | price | -1.4812848 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2882.1995 | 87.79125 | price | -3.1416759 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2815287 | 0.018706001 | ratio | -1.4812848 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4638734 | 0.0061820947 | %p | -0.17879255 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 370.49802 | 0.64426877 | price | -0.17419555 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 551.43195 | -0.15541603 | price | 0.02817614 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0063233 | 0.0017499222 | ratio | -0.17419555 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.6918547 | -0.062417488 | %p | 1.3128716 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 219.80952 | -2.7896825 | price | 1.2532311 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 367.48615 | 10.221827 | price | -2.8611384 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.88081798 | -0.011178781 | ratio | 1.2532311 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.0317426 | 0.091949497 | %p | -1.1580843 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 967.50988 | 7.6640316 | price | -0.79846484 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1732.7925 | 22.908564 | price | -1.3397731 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.92210791 | 0.0073043845 | ratio | -0.79846484 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.3654318 | 0.0083493253 | %p | -0.24870778 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 89.577075 | 0.3083004 | price | -0.34536197 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 141.52555 | 0.39467459 | price | -0.27965148 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.93282568 | 0.0032105371 | ratio | -0.34536197 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.0521567 | -0.090672092 | %p | 1.2694143 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1401.1621 | -14.426877 | price | 1.0191431 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2260.749 | -24.038404 | price | 1.0521068 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0335072 | -0.010641368 | ratio | 1.0191431 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261118T150814414112Z-eaefa901772c430390ce7a0eaa984a44

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150814414112Z-eaefa901772c430390ce7a0eaa984a44 | market_alpha10000 | 4.5033712 | 545.55261 | 923.9768 | 0.98770075 | 2.2336624 (direct) | 2.2512727 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5033712 | -0.10371814 | %p | 2.2512727 | improved |
| mae | 532.31701 | 545.55261 | 13.235601 | price | -2.4864134 | worsened |
| rmse | 943.1701 | 923.9768 | -19.193301 | price | 2.0349777 | improved |
| rmae | 1 | 0.98770075 | -0.012299247 | ratio | 1.2299247 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5687861 | -0.19971048 | %p | 4.1881227 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 132.49407 | -5.7747036 | price | 4.1764336 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 200.90905 | -9.8769994 | price | 4.6857937 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.95823566 | -0.041764336 | ratio | 4.1764336 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.5281898 | 0.026128048 | %p | -0.47487741 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 116.08696 | 0.33596838 | price | -0.29025098 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 175.78636 | 4.6502743 | price | -2.7172961 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0029025 | 0.0029025098 | ratio | -0.29025098 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7230932 | -0.17031014 | %p | 5.8861527 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 488.77075 | -29.324111 | price | 5.6599887 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 804.6988 | -23.764679 | price | 2.8685246 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94340011 | -0.056599887 | ratio | 5.6599887 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3949205 | -0.11172142 | %p | 2.4790392 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.01992 | -2.6175299 | price | 2.6009501 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.02765 | -0.83544575 | price | 0.5258904 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.9739905 | -0.026009501 | ratio | 2.6009501 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 0.95503869 | 0.15769302 | %p | -19.777246 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1550.8616 | 219.16518 | price | -16.457593 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2781.8648 | -91.325642 | price | 3.1785447 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.1645759 | 0.16457593 | ratio | -16.457593 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4713873 | 0.021703222 | %p | -0.62913651 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 371.00791 | 2.8379447 | price | -0.77082461 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 555.61058 | 3.2561494 | price | -0.58950362 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0077082 | 0.0077082461 | ratio | -0.77082461 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7823904 | -0.54941088 | %p | 10.304414 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 224.06746 | -25.484127 | price | 10.211967 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 387.53829 | -22.518198 | price | 5.4914868 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89788033 | -0.10211967 | ratio | 10.211967 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.2351398 | -0.3514539 | %p | 4.0930538 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 992.64427 | -56.592885 | price | 5.3937172 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1769.3735 | -61.485152 | price | 3.3582687 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.94606283 | -0.053937172 | ratio | 5.3937172 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4514485 | -0.17610937 | %p | 4.8547639 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.920949 | -4.1067194 | price | 4.2766001 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 147.1154 | -7.7674839 | price | 5.0150693 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.957234 | -0.042766001 | ratio | 4.2766001 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9233178 | 0.31601047 | %p | -4.7827422 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1389.6522 | 33.916996 | price | -2.501742 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2258.8436 | 17.734166 | price | -0.79131192 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0250174 | 0.02501742 | ratio | -2.501742 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5033712 | -0.10288828 | %p | 2.2336624 | improved |
| mae | 565.55167 | 545.55261 | -19.999065 | price | 3.5362047 | improved |
| rmse | 926.40586 | 923.9768 | -2.4290601 | price | 0.26220259 | improved |
| rmae | 1.0199316 | 0.98770075 | -0.032230815 | ratio | 3.1600958 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5687861 | -0.16102495 | %p | 3.4044691 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 132.49407 | -5.3359684 | price | 3.8714118 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 200.90905 | -8.269892 | price | 3.9535012 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.95823566 | -0.038591276 | ratio | 3.8714118 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.5281898 | -0.20396651 | %p | 3.5582858 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 116.08696 | -3.5770751 | price | 2.9892651 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 175.78636 | -2.9526201 | price | 1.6519172 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0029025 | -0.030903193 | ratio | 2.9892651 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7230932 | 0.042654667 | %p | -1.5913316 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 488.77075 | -1.8339921 | price | 0.37382274 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 804.6988 | 25.616944 | price | -3.288094 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94340011 | -0.003539877 | ratio | 0.37382274 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3949205 | -0.19607975 | %p | 4.2709593 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.01992 | -4.936255 | price | 4.7945205 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.02765 | -7.0074216 | price | 4.2460198 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.9739905 | -0.049049881 | ratio | 4.7945205 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 0.95503869 | -0.11163246 | %p | 10.465499 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1550.8616 | -160.60714 | price | 9.3841703 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2781.8648 | -57.075407 | price | 2.0104477 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.1645759 | -0.12060342 | ratio | 9.3841703 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4713873 | -0.067306295 | %p | 1.9020097 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 371.00791 | -7.0671937 | price | 1.8692566 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 555.61058 | -9.7634523 | price | 1.7269014 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0077082 | -0.019195465 | ratio | 1.8692566 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7823904 | 0.003894636 | %p | -0.081503389 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 224.06746 | -1.1547619 | price | 0.51272112 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 387.53829 | 14.19863 | price | -3.8031401 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89788033 | -0.0046273475 | ratio | 0.51272112 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.2351398 | 0.15640786 | %p | -1.9360447 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 992.64427 | 28.501976 | price | -2.9562002 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1769.3735 | 65.403199 | price | -3.8382829 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.94606283 | 0.027164475 | ratio | -2.9562002 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4514485 | -0.19755471 | %p | 5.4139363 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.920949 | -5.2213439 | price | 5.3749441 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 147.1154 | -8.0457817 | price | 5.1854347 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.957234 | -0.054373328 | ratio | 5.3749441 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9233178 | -0.29427533 | %p | 4.0771947 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1389.6522 | -38.758893 | price | 2.7134271 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2258.8436 | -36.3948 | price | 1.5856654 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0250174 | -0.028588838 | ratio | 2.7134271 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5033712 | 0.0022298911 | %p | -0.049540571 | worsened |
| mae | 557.9753 | 545.55261 | -12.422697 | price | 2.2263883 | improved |
| rmse | 915.84853 | 923.9768 | 8.1282625 | price | -0.88751165 | worsened |
| rmae | 0.99470404 | 0.98770075 | -0.0070032915 | ratio | 0.70405781 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.5687861 | 0.14235831 | %p | -3.2160993 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 132.49407 | 3.7470356 | price | -2.9103859 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 200.90905 | 9.3288215 | price | -4.8694072 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.95823566 | 0.027099651 | ratio | -2.9103859 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.5281898 | -0.2047247 | %p | 3.5710404 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 116.08696 | -3.43083 | price | 2.8705602 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 175.78636 | -5.0857217 | price | 2.8117781 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0029025 | -0.029639747 | ratio | 2.8705602 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7230932 | -0.011221958 | %p | 0.410412 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 488.77075 | -5.0039526 | price | 1.013408 | improved |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 804.6988 | 16.440912 | price | -2.0857275 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.94340011 | -0.0096583714 | ratio | 1.013408 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3949205 | -0.030268025 | %p | 0.68399403 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.01992 | -0.84063745 | price | 0.85032643 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.02765 | -0.68532957 | price | 0.43180437 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.9739905 | -0.0083531275 | ratio | 0.85032643 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 0.95503869 | -0.0858607 | %p | 8.2487031 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1550.8616 | -130.83482 | price | 7.779931 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2781.8648 | -12.543509 | price | 0.44887889 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.1645759 | -0.098246731 | ratio | 7.779931 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4713873 | 0.013695913 | %p | -0.39609993 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 371.00791 | 1.1541502 | price | -0.31205583 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 555.61058 | 4.0232174 | price | -0.72938897 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0077082 | 0.0031348299 | ratio | -0.31205583 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7823904 | 0.02811818 | %p | -0.59142974 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 224.06746 | 1.468254 | price | -0.65959533 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 387.53829 | 30.273963 | price | -8.4738277 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89788033 | 0.0058835689 | ratio | -0.65959533 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.2351398 | 0.29534677 | %p | -3.7198295 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 992.64427 | 32.798419 | price | -3.4170507 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1769.3735 | 59.489557 | price | -3.4791577 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.94606283 | 0.0312593 | ratio | -3.4170507 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4514485 | 0.094366092 | %p | -2.8109554 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 91.920949 | 2.6521739 | price | -2.9709985 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 147.1154 | 5.9845207 | price | -4.2404049 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.957234 | 0.027618852 | ratio | -2.9709985 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.9233178 | -0.21951097 | %p | 3.0731658 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1389.6522 | -25.936759 | price | 1.8322239 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2258.8436 | -25.943807 | price | 1.135502 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0250174 | -0.01913114 | ratio | 1.8322239 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

