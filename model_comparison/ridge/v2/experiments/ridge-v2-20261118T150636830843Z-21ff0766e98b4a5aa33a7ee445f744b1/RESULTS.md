
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

