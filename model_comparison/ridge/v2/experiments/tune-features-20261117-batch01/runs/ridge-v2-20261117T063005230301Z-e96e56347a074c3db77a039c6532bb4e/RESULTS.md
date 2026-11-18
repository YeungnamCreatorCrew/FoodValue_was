
## ridge-v2-20261117T063005230301Z-e96e56347a074c3db77a039c6532bb4e

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063005230301Z-e96e56347a074c3db77a039c6532bb4e | garak | 4.6169588 | 559.85903 | 898.55804 | 1.0160597 | -0.23227687 (direct) | -0.21422236 (direct) | 4 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6169588 | 0.0098694156 | %p | -0.21422236 | worsened |
| mae | 532.31701 | 559.85903 | 27.542028 | price | -5.17399 | worsened |
| rmse | 943.1701 | 898.55804 | -44.612059 | price | 4.7300121 | improved |
| rmae | 1 | 1.0160597 | 0.016059737 | ratio | -1.6059737 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7009918 | -0.067504788 | %p | 1.4156409 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 136.86166 | -1.4071146 | price | 1.0176662 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.47347 | -2.3125847 | price | 1.0971241 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.98982334 | -0.010176662 | ratio | 1.0176662 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6946245 | 0.19256271 | %p | -3.4998283 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 118.79842 | 3.0474308 | price | -2.6327471 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 176.98067 | 5.8445817 | price | -3.4151661 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0263275 | 0.026327471 | ratio | -2.6327471 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7409848 | -0.15241861 | %p | 5.2677969 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 503.37549 | -14.719368 | price | 2.8410565 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 780.40258 | -48.060904 | price | 5.8012097 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.97158944 | -0.028410565 | ratio | 2.8410565 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4905463 | -0.016095613 | %p | 0.35715314 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 100.35458 | -0.28286853 | price | 0.2810768 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 162.41076 | 3.5476678 | price | -2.2331605 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 0.99718923 | -0.002810768 | ratio | 0.2810768 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0136052 | 0.21625953 | %p | -27.122432 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1612.9196 | 281.22321 | price | -21.117667 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2502.3642 | -370.82621 | price | 12.906426 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2111767 | 0.21117667 | ratio | -21.117667 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5824185 | 0.13273448 | %p | -3.8477286 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 381.89328 | 13.72332 | price | -3.7274416 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 575.29326 | 22.938828 | price | -4.1529183 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0372744 | 0.037274416 | ratio | -3.7274416 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8314138 | -0.50038749 | %p | 9.3849615 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 228.97619 | -20.575397 | price | 8.2449473 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 385.03961 | -25.016877 | price | 6.1008369 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91755053 | -0.082449473 | ratio | 8.2449473 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.223061 | -0.36353269 | %p | 4.2337241 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 984.77075 | -64.466403 | price | 6.1441213 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1752.556 | -78.302563 | price | 4.276822 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.93855879 | -0.061441213 | ratio | 6.1441213 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6510424 | 0.02348446 | %p | -0.64739036 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.363636 | 1.3359684 | price | -1.3912328 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 156.70055 | 1.8176696 | price | -1.1735768 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0139123 | 0.013912328 | ratio | -1.3912328 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2408995 | 0.63359217 | %p | -9.5892644 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1433.2767 | 77.541502 | price | -5.7195169 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2285.3592 | 44.249796 | price | -1.9744594 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0571952 | 0.057195169 | ratio | -5.7195169 | worsened |
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
| mape | 4.6062595 | 4.6169588 | 0.010699275 | %p | -0.23227687 | worsened |
| mae | 565.55167 | 559.85903 | -5.6926377 | price | 1.0065637 | improved |
| rmse | 926.40586 | 898.55804 | -27.847818 | price | 3.0060063 | improved |
| rmae | 1.0199316 | 1.0160597 | -0.0038718312 | ratio | 0.37961676 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7009918 | -0.028819259 | %p | 0.609311 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 136.86166 | -0.96837945 | price | 0.70258954 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.47347 | -0.70547724 | price | 0.33726016 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.98982334 | -0.0070036019 | ratio | 0.70258954 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6946245 | -0.037531842 | %p | 0.65475956 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 118.79842 | -0.86561265 | price | 0.72336912 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 176.98067 | -1.7583127 | price | 0.98373209 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0263275 | -0.0074782312 | ratio | 0.72336912 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7409848 | 0.060546197 | %p | -2.2588168 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 503.37549 | 12.770751 | price | -2.6030631 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 780.40258 | 1.3207187 | price | -0.16952246 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.97158944 | 0.024649445 | ratio | -2.6030631 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4905463 | -0.10045395 | %p | 2.1880623 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 100.35458 | -2.6015936 | price | 2.5268942 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 162.41076 | -2.6243081 | price | 1.5901518 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.99718923 | -0.025851148 | ratio | 2.5268942 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0136052 | -0.053065941 | %p | 4.974911 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1612.9196 | -98.549107 | price | 5.7581599 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2502.3642 | -336.57597 | price | 11.855691 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2111767 | -0.074002682 | ratio | 5.7581599 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5824185 | 0.043724961 | %p | -1.2356244 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 381.89328 | 3.8181818 | price | -1.0099004 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 575.29326 | 9.9192268 | price | -1.7544539 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0372744 | 0.010370704 | ratio | -1.0099004 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8314138 | 0.052918017 | %p | -1.10742 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 228.97619 | 3.7539683 | price | -1.6667841 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 385.03961 | 11.699951 | price | -3.1338623 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.91755053 | 0.015042855 | ratio | -1.6667841 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.223061 | 0.14432908 | %p | -1.7865313 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 984.77075 | 20.628458 | price | -2.1395658 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1752.556 | 48.585787 | price | -2.8513284 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.93855879 | 0.019660435 | ratio | -2.1395658 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6510424 | 0.0020391221 | %p | -0.055881618 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.363636 | 0.22134387 | price | -0.22785531 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 156.70055 | 1.5393718 | price | -0.9921114 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0139123 | 0.002305001 | ratio | -0.22785531 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2408995 | 0.023306365 | %p | -0.32291049 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1433.2767 | 4.8656126 | price | -0.34063112 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2285.3592 | -9.8791699 | price | 0.43042021 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0571952 | 0.0035889108 | ratio | -0.34063112 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

