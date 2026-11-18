
## ridge-v2-20261117T063413283030Z-d27ee144542a46ee82a0211d9b9ff9e4

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063413283030Z-d27ee144542a46ee82a0211d9b9ff9e4 | no_series_id | 4.6472089 | 577.16884 | 935.57139 | 1.0334384 | -0.88899391 (direct) | -0.87082111 (direct) | 4 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6472089 | 0.040119507 | %p | -0.87082111 | worsened |
| mae | 532.31701 | 577.16884 | 44.851832 | price | -8.4257748 | worsened |
| rmse | 943.1701 | 935.57139 | -7.5987035 | price | 0.80565568 | improved |
| rmae | 1 | 1.0334384 | 0.033438382 | ratio | -3.3438382 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7275609 | -0.040935673 | %p | 0.85846078 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.19368 | -1.0750988 | price | 0.77754274 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 211.01816 | 0.23211039 | price | -0.11011658 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 0.99222457 | -0.0077754274 | ratio | 0.77754274 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.4877337 | -0.014328087 | %p | 0.26041305 | improved |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 115.32016 | -0.43083004 | price | 0.3722042 | improved |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 173.61663 | 2.4805429 | price | -1.4494563 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 0.99627796 | -0.003722042 | ratio | 0.3722042 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7407721 | -0.15263122 | %p | 5.275145 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 500.34783 | -17.747036 | price | 3.4254413 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 790.03977 | -38.423706 | price | 4.6379481 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.96574559 | -0.034254413 | ratio | 3.4254413 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5609501 | 0.0543082 | %p | -1.2050702 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.09163 | 1.4541833 | price | -1.4449723 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 163.75332 | 4.8902326 | price | -3.0782686 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0144497 | 0.014449723 | ratio | -1.4449723 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1243898 | 0.32704412 | %p | -41.016605 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1794.875 | 463.17857 | price | -34.781093 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2871.0216 | -2.1687965 | price | 0.07548391 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3478109 | 0.34781093 | ratio | -34.781093 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4951859 | 0.045501897 | %p | -1.3190164 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 373.32806 | 5.1581028 | price | -1.4010113 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 554.72073 | 2.3662929 | price | -0.42840117 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0140101 | 0.014010113 | ratio | -1.4010113 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0007314 | -0.33106986 | %p | 6.2093436 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 235.59921 | -13.952381 | price | 5.5909806 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 399.48599 | -10.570492 | price | 2.5778135 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.94409019 | -0.055909806 | ratio | 5.5909806 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.2079508 | -0.37864291 | %p | 4.4096987 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 979.44269 | -69.794466 | price | 6.6519248 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1722.0024 | -108.85625 | price | 5.9456395 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.93348075 | -0.066519248 | ratio | 6.6519248 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8719777 | 0.24441974 | %p | -6.7378589 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 102.8498 | 6.8221344 | price | -7.1043425 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 161.89091 | 7.0080306 | price | -4.5247289 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0710434 | 0.071043425 | ratio | -7.1043425 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2548362 | 0.64752886 | %p | -9.8001929 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1430.6403 | 74.905138 | price | -5.5250568 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2308.1644 | 67.055003 | price | -2.992045 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0552506 | 0.055250568 | ratio | -5.5250568 | worsened |
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
| mape | 4.6062595 | 4.6472089 | 0.040949366 | %p | -0.88899391 | worsened |
| mae | 565.55167 | 577.16884 | 11.617166 | price | -2.0541298 | worsened |
| rmse | 926.40586 | 935.57139 | 9.1655374 | price | -0.98936523 | worsened |
| rmae | 1.0199316 | 1.0334384 | 0.013506814 | ratio | -1.3242863 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7275609 | -0.0022501438 | %p | 0.047573652 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.19368 | -0.63636364 | price | 0.4617017 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 211.01816 | 1.8392178 | price | -0.87925571 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99222457 | -0.0046023669 | ratio | 0.4617017 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.4877337 | -0.24442264 | %p | 4.264061 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 115.32016 | -4.3438735 | price | 3.6300578 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 173.61663 | -5.1223515 | price | 2.8658278 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 0.99627796 | -0.037527745 | ratio | 3.6300578 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7407721 | 0.060333585 | %p | -2.2508848 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 500.34783 | 9.743083 | price | -1.9859333 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 790.03977 | 10.957917 | price | -1.4065167 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.96574559 | 0.018805597 | ratio | -1.9859333 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5609501 | -0.030050132 | %p | 0.65454433 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.09163 | -0.86454183 | price | 0.83971829 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 163.75332 | -1.2817433 | price | 0.77664904 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0144497 | -0.0085906572 | ratio | 0.83971829 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1243898 | 0.057718649 | %p | -5.4111006 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1794.875 | 83.40625 | price | -4.8733727 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2871.0216 | 32.081439 | price | -1.1300498 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3478109 | 0.062631579 | ratio | -4.8733727 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4951859 | -0.04350762 | %p | 1.2294825 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 373.32806 | -4.7470356 | price | 1.2555801 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 554.72073 | -10.653309 | price | 1.884294 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0140101 | -0.012893598 | ratio | 1.2555801 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0007314 | 0.22223565 | %p | -4.650745 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 235.59921 | 10.376984 | price | -4.6074424 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 399.48599 | 26.146336 | price | -7.0033643 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.94409019 | 0.041582521 | ratio | -4.6074424 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.2079508 | 0.12921885 | %p | -1.5994942 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 979.44269 | 15.300395 | price | -1.5869437 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1722.0024 | 18.032098 | price | -1.0582402 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.93348075 | 0.014582399 | ratio | -1.5869437 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8719777 | 0.2229744 | %p | -6.1105563 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 102.8498 | 5.7075099 | price | -5.875412 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 161.89091 | 6.7297328 | price | -4.3372529 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0710434 | 0.059436098 | ratio | -5.875412 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2548362 | 0.037243061 | %p | -0.51600389 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1430.6403 | 2.229249 | price | -0.15606495 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2308.1644 | 12.926037 | price | -0.56316752 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0552506 | 0.0016443101 | ratio | -0.15606495 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

