
## ridge-v2-20261119T071447105414Z-d5b1a17be6304a33950e68f315e35b0e

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071447105414Z-d5b1a17be6304a33950e68f315e35b0e | market_w730 | 4.5281307 | 554.48788 | 908.27189 | 0.99585915 | 1.6961449 (direct) | 1.713852 (direct) | 8 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5281307 | -0.078958694 | %p | 1.713852 | improved |
| mae | 532.31701 | 554.48788 | 22.170871 | price | -4.1649751 | worsened |
| rmse | 943.1701 | 908.27189 | -34.898203 | price | 3.7000964 | improved |
| rmae | 1 | 0.99585915 | -0.0041408544 | ratio | 0.41408544 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5143682 | -0.25412834 | %p | 5.3293179 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 131.1502 | -7.1185771 | price | 5.148362 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 194.24235 | -16.543699 | price | 7.848574 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.94851638 | -0.05148362 | ratio | 5.148362 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6767171 | 0.17465528 | %p | -3.1743605 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 118.16206 | 2.4110672 | price | -2.0829776 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.41648 | 9.2803914 | price | -5.4228137 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0208298 | 0.020829776 | ratio | -2.0829776 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8490079 | -0.044395473 | %p | 1.5343686 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 511.02767 | -7.0671937 | price | 1.3640733 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 776.16565 | -52.297832 | price | 6.3126297 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.98635927 | -0.013640733 | ratio | 1.3640733 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3325655 | -0.17407644 | %p | 3.8626641 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 97.047809 | -3.5896414 | price | 3.5669042 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 153.53836 | -5.3247326 | price | 3.3517745 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.96433096 | -0.035669042 | ratio | 3.5669042 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 0.99760887 | 0.2002632 | %p | -25.116233 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1606.8571 | 275.16071 | price | -20.66242 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2714.1601 | -159.03036 | price | 5.5349745 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2066242 | 0.2066242 | ratio | -20.66242 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.3681079 | -0.081576169 | %p | 2.3647432 | improved |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 361.35573 | -6.8142292 | price | 1.8508379 | improved |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 531.65732 | -20.697112 | price | 3.7470709 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 0.98149162 | -0.018508379 | ratio | 1.8508379 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8569905 | -0.47481077 | %p | 8.9052601 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 228.37302 | -21.178571 | price | 8.4866507 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 368.92545 | -41.13104 | price | 10.030579 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91513349 | -0.084866507 | ratio | 8.4866507 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0718832 | -0.51471058 | %p | 5.9943511 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 981.81028 | -67.426877 | price | 6.4262762 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1741.5083 | -89.350265 | price | 4.8802384 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.93573724 | -0.064262762 | ratio | 6.4262762 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4551199 | -0.17243802 | %p | 4.7535567 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.612648 | -4.4150198 | price | 4.5976538 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.55506 | -10.327821 | price | 6.6681487 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.95402346 | -0.045976538 | ratio | 4.5976538 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1589377 | 0.55163038 | %p | -8.3487925 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1417.4822 | 61.747036 | price | -4.5545057 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2277.5499 | 36.440439 | price | -1.626 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0455451 | 0.045545057 | ratio | -4.5545057 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5281307 | -0.078128834 | %p | 1.6961449 | improved |
| mae | 565.55167 | 554.48788 | -11.063795 | price | 1.9562838 | improved |
| rmse | 926.40586 | 908.27189 | -18.133962 | price | 1.9574533 | improved |
| rmae | 1.0199316 | 0.99585915 | -0.024072423 | ratio | 2.3601998 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5143682 | -0.21544281 | %p | 4.5549983 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 131.1502 | -6.6798419 | price | 4.846434 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 194.24235 | -14.936592 | price | 7.1405809 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.94851638 | -0.04831056 | ratio | 4.846434 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6767171 | -0.055439277 | %p | 0.96716268 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 118.16206 | -1.5019763 | price | 1.255161 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.41648 | 1.677497 | price | -0.93851769 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0208298 | -0.012975926 | ratio | 1.255161 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8490079 | 0.16856934 | %p | -6.2888714 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 511.02767 | 20.422925 | price | -4.1628062 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 776.16565 | -2.9162091 | price | 0.37431356 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.98635927 | 0.039419277 | ratio | -4.1628062 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3325655 | -0.25843477 | %p | 5.6291605 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 97.047809 | -5.9083665 | price | 5.7387199 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 153.53836 | -11.496708 | price | 6.9662215 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.96433096 | -0.058709422 | ratio | 5.7387199 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 0.99760887 | -0.069062278 | %p | 6.4745614 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1606.8571 | -104.61161 | price | 6.1123878 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2714.1601 | -124.78012 | price | 4.3953064 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2066242 | -0.078555146 | ratio | 6.1123878 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.3681079 | -0.17058569 | %p | 4.8205837 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 361.35573 | -16.719368 | price | 4.4222345 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 531.65732 | -33.716714 | price | 5.9636121 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 0.98149162 | -0.045412091 | ratio | 4.4222345 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8569905 | 0.078494744 | %p | -1.6426664 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 228.37302 | 3.1507937 | price | -1.398971 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 368.92545 | -4.4142125 | price | 1.1823583 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.91513349 | 0.012625821 | ratio | -1.398971 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0718832 | -0.0068488141 | %p | 0.084775855 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 981.81028 | 17.667984 | price | -1.832508 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1741.5083 | 37.538086 | price | -2.2029778 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.93573724 | 0.016838885 | ratio | -1.832508 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4551199 | -0.19388336 | %p | 5.3133238 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.612648 | -5.5296443 | price | 5.692314 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.55506 | -10.606119 | price | 6.8355492 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.95402346 | -0.057583865 | ratio | 5.692314 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1589377 | -0.058655421 | %p | 0.81267287 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1417.4822 | -10.928854 | price | 0.76510565 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2277.5499 | -17.688526 | price | 0.77066184 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0455451 | -0.008061201 | ratio | 0.76510565 | improved |
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
| mape | 4.5011413 | 4.5281307 | 0.026989341 | %p | -0.59961106 | worsened |
| mae | 557.9753 | 554.48788 | -3.4874273 | price | 0.62501463 | improved |
| rmse | 915.84853 | 908.27189 | -7.5766393 | price | 0.82728083 | improved |
| rmae | 0.99470404 | 0.99585915 | 0.0011551007 | ratio | -0.11612506 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.5143682 | 0.087940455 | %p | -1.9867139 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 131.1502 | 2.4031621 | price | -1.8665766 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 194.24235 | 2.6621218 | price | -1.3895598 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.94851638 | 0.017380367 | ratio | -1.8665766 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6767171 | -0.056197467 | %p | 0.98025998 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 118.16206 | -1.3557312 | price | 1.1343343 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 180.41648 | -0.45560463 | price | 0.25189328 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0208298 | -0.011712481 | ratio | 1.1343343 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.8490079 | 0.11469271 | %p | -4.194568 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 511.02767 | 17.252964 | price | -3.4940965 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 776.16565 | -12.092242 | price | 1.5340464 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.98635927 | 0.033300783 | ratio | -3.4940965 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3325655 | -0.092623043 | %p | 2.0930869 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 97.047809 | -1.812749 | price | 1.8336423 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 153.53836 | -5.1746164 | price | 3.2603613 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.96433096 | -0.018012668 | ratio | 1.8336423 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 0.99760887 | -0.043290521 | %p | 4.1589534 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1606.8571 | -74.839286 | price | 4.4502256 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2714.1601 | -80.248223 | price | 2.8717429 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2066242 | -0.056198458 | ratio | 4.4502256 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.3681079 | -0.089583477 | %p | 2.5908466 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 361.35573 | -8.4980237 | price | 2.2976713 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 531.65732 | -19.930044 | price | 3.6132163 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 0.98149162 | -0.023081795 | ratio | 2.2976713 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.8569905 | 0.10271829 | %p | -2.1605471 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 228.37302 | 5.7738095 | price | -2.5938141 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 368.92545 | 11.661121 | price | -3.2640037 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.91513349 | 0.023136737 | ratio | -2.5938141 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.0718832 | 0.13209009 | %p | -1.6636465 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 981.81028 | 21.964427 | price | -2.2883286 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1741.5083 | 31.624444 | price | -1.8495082 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.93573724 | 0.020933711 | ratio | -2.2883286 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4551199 | 0.098037444 | %p | -2.9203168 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 91.612648 | 2.3438735 | price | -2.6256365 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 144.55506 | 3.4241836 | price | -2.4262469 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.95402346 | 0.024408314 | ratio | -2.6256365 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.1589377 | 0.016108933 | %p | -0.22552596 | worsened |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1417.4822 | 1.8932806 | price | -0.13374509 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2277.5499 | -7.2375332 | price | 0.31677053 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0455451 | 0.0013964974 | ratio | -0.13374509 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

