
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

