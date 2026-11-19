
## ridge-v2-20261119T071507226244Z-d25300ae926d4849bcb9d333658e1457

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071507226244Z-d25300ae926d4849bcb9d333658e1457 | market_w1095 | 4.4740934 | 547.13572 | 905.10261 | 0.98437208 | 2.8692717 (direct) | 2.8867675 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4740934 | -0.13299596 | %p | 2.8867675 | improved |
| mae | 532.31701 | 547.13572 | 14.81871 | price | -2.7838131 | worsened |
| rmse | 943.1701 | 905.10261 | -38.067486 | price | 4.036121 | improved |
| rmae | 1 | 0.98437208 | -0.015627919 | ratio | 1.5627919 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4789178 | -0.28957877 | %p | 6.0727479 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 130.2253 | -8.0434783 | price | 5.8172775 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 193.39622 | -17.389828 | price | 8.2499898 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.94182723 | -0.058172775 | ratio | 5.8172775 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6420098 | 0.13994805 | %p | -2.5435565 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 117.53755 | 1.7865613 | price | -1.5434523 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 179.14689 | 8.0108015 | price | -4.6809539 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0154345 | 0.015434523 | ratio | -1.5434523 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7721383 | -0.1212651 | %p | 4.1910888 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 497.69565 | -20.399209 | price | 3.9373503 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 780.00111 | -48.462369 | price | 5.8496687 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.9606265 | -0.039373503 | ratio | 3.9373503 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3404477 | -0.16619425 | %p | 3.6877625 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 96.972112 | -3.6653386 | price | 3.6421219 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 154.78166 | -4.0814313 | price | 2.5691501 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.96357878 | -0.036421219 | ratio | 3.6421219 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 0.99076824 | 0.19342257 | %p | -24.258308 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1599.942 | 268.24554 | price | -20.143144 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2709.7253 | -163.46515 | price | 5.6893252 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2014314 | 0.20143144 | ratio | -20.143144 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.3809871 | -0.068696973 | %p | 1.991399 | improved |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 362.13834 | -6.0316206 | price | 1.6382707 | improved |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 534.16947 | -18.184961 | price | 3.2922631 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 0.98361729 | -0.016382707 | ratio | 1.6382707 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7581164 | -0.57368481 | %p | 10.759681 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.09921 | -27.452381 | price | 11.000684 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 362.771 | -47.285487 | price | 11.531457 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.88999316 | -0.11000684 | ratio | 11.000684 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0267942 | -0.55979955 | %p | 6.51946 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 971.64032 | -77.596838 | price | 7.3955481 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1734.6243 | -96.234323 | price | 5.25624 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92604452 | -0.073955481 | ratio | 7.3955481 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4018057 | -0.22575226 | %p | 6.2232573 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 90.387352 | -5.6403162 | price | 5.8736366 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.9757 | -12.907185 | price | 8.333513 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.94126363 | -0.058736366 | ratio | 5.8736366 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9489488 | 0.34164151 | %p | -5.1706618 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1382.7194 | 26.98419 | price | -1.9903732 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2260.4345 | 19.32507 | price | -0.86229927 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0199037 | 0.019903732 | ratio | -1.9903732 | worsened |
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
| mape | 4.6062595 | 4.4740934 | -0.1321661 | %p | 2.8692717 | improved |
| mae | 565.55167 | 547.13572 | -18.415956 | price | 3.2562817 | improved |
| rmse | 926.40586 | 905.10261 | -21.303245 | price | 2.2995586 | improved |
| rmae | 1.0199316 | 0.98437208 | -0.035559487 | ratio | 3.4864581 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4789178 | -0.25089324 | %p | 5.3045089 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 130.2253 | -7.6047431 | price | 5.5174787 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 193.39622 | -15.78272 | price | 7.5450808 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.94182723 | -0.054999714 | ratio | 5.5174787 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6420098 | -0.090146505 | %p | 1.5726456 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 117.53755 | -2.1264822 | price | 1.7770438 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 179.14689 | 0.4079071 | price | -0.22821384 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0154345 | -0.01837118 | ratio | 1.7770438 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7721383 | 0.091699704 | %p | -3.4210709 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 497.69565 | 7.0909091 | price | -1.4453405 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 780.00111 | 0.91925427 | price | -0.117992 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.9606265 | 0.013686507 | ratio | -1.4453405 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3404477 | -0.25055258 | %p | 5.4574727 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 96.972112 | -5.9840637 | price | 5.8122436 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 154.78166 | -10.253407 | price | 6.2128657 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.96357878 | -0.059461599 | ratio | 5.8122436 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 0.99076824 | -0.075902904 | %p | 7.1158673 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1599.942 | -111.52679 | price | 6.5164372 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2709.7253 | -129.21491 | price | 4.5515194 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2014314 | -0.083747905 | ratio | 6.5164372 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.3809871 | -0.15770649 | %p | 4.4566303 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 362.13834 | -15.936759 | price | 4.2152363 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 534.16947 | -31.204563 | price | 5.5192777 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 0.98361729 | -0.043286418 | ratio | 4.2152363 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7581164 | -0.020379294 | %p | 0.42647927 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.09921 | -3.1230159 | price | 1.3866375 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 362.771 | -10.568659 | price | 2.8308428 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.88999316 | -0.01251451 | ratio | 1.3866375 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0267942 | -0.05193778 | %p | 0.6428952 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 971.64032 | 7.4980237 | price | -0.7776885 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1734.6243 | 30.654027 | price | -1.7989767 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92604452 | 0.0071461668 | ratio | -0.7776885 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4018057 | -0.2471976 | %p | 6.774387 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 90.387352 | -6.7549407 | price | 6.9536559 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.9757 | -13.185483 | price | 8.4979265 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.94126363 | -0.070343692 | ratio | 6.9536559 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9489488 | -0.26864429 | %p | 3.7220758 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1382.7194 | -45.6917 | price | 3.198778 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2260.4345 | -34.803895 | price | 1.5163521 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0199037 | -0.033702526 | ratio | 3.198778 | improved |
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
| mape | 4.5011413 | 4.4740934 | -0.027047923 | %p | 0.60091255 | improved |
| mae | 557.9753 | 547.13572 | -10.839587 | price | 1.9426644 | improved |
| rmse | 915.84853 | 905.10261 | -10.745923 | price | 1.1733297 | improved |
| rmae | 0.99470404 | 0.98437208 | -0.010331964 | ratio | 1.0386973 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4789178 | 0.052490022 | %p | -1.1858326 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 130.2253 | 1.4782609 | price | -1.1481902 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 193.39622 | 1.8159932 | price | -0.94790221 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.94182723 | 0.010691213 | ratio | -1.1481902 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6420098 | -0.090904695 | %p | 1.5856628 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 117.53755 | -1.9802372 | price | 1.6568556 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 179.14689 | -1.7251945 | price | 0.95382022 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0154345 | -0.017107734 | ratio | 1.6568556 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7721383 | 0.03782308 | %p | -1.3832743 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 497.69565 | 3.9209486 | price | -0.79407645 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 780.00111 | -8.2567782 | price | 1.0474717 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.9606265 | 0.0075680129 | ratio | -0.79407645 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3404477 | -0.084740855 | %p | 1.914966 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 96.972112 | -1.8884462 | price | 1.910212 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 154.78166 | -3.9313151 | price | 2.4769967 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.96357878 | -0.018764846 | ratio | 1.910212 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 0.99076824 | -0.050131146 | %p | 4.8161375 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1599.942 | -81.754464 | price | 4.8614282 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2709.7253 | -84.683014 | price | 3.0304453 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2014314 | -0.061391217 | ratio | 4.8614282 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.3809871 | -0.076704281 | %p | 2.2183669 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 362.13834 | -7.715415 | price | 2.0860718 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 534.16947 | -17.417893 | price | 3.157776 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 0.98361729 | -0.020956123 | ratio | 2.0860718 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7581164 | 0.0038442503 | %p | -0.080858861 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 222.09921 | -0.5 | price | 0.22461895 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 362.771 | 5.5066743 | price | -1.5413446 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.88999316 | -0.0020035937 | ratio | 0.22461895 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.0267942 | 0.087001125 | %p | -1.0957606 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 971.64032 | 11.794466 | price | -1.2287876 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1734.6243 | 24.740385 | price | -1.4469044 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.92604452 | 0.011240992 | ratio | -1.2287876 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4018057 | 0.044723201 | %p | -1.3322044 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 90.387352 | 1.1185771 | price | -1.2530441 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 141.9757 | 0.84481935 | price | -0.59860702 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.94126363 | 0.011648487 | ratio | -1.2530441 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.9489488 | -0.19387993 | %p | 2.7143298 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1382.7194 | -32.869565 | price | 2.3219711 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2260.4345 | -24.352902 | price | 1.0658717 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0199037 | -0.024244827 | ratio | 2.3219711 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

