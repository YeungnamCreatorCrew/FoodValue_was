
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

