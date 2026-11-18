
## ridge-v2-20261117T063047774540Z-d401f8626477400d9dfb139f97324230

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063047774540Z-d401f8626477400d9dfb139f97324230 | origin_weather | 5.0913068 | 712.79368 | 1087.8161 | 1.1999771 | -10.530177 (direct) | -10.510267 (direct) | 0 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 5.0913068 | 0.4842174 | %p | -10.510267 | worsened |
| mae | 532.31701 | 712.79368 | 180.47667 | price | -33.903984 | worsened |
| rmse | 943.1701 | 1087.8161 | 144.64602 | price | -15.336154 | worsened |
| rmae | 1 | 1.1999771 | 0.19997705 | ratio | -19.997705 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.2181644 | 0.44966788 | %p | -9.4299718 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 151.0751 | 12.806324 | price | -9.2619061 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 218.8498 | 8.0637459 | price | -3.8255596 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0926191 | 0.092619061 | ratio | -9.2619061 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1630874 | 0.66102561 | %p | -12.014144 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 128.11858 | 12.367589 | price | -10.684651 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 186.33683 | 15.200742 | price | -8.882254 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1068465 | 0.10684651 | ratio | -10.684651 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.6586647 | 0.76526136 | %p | -26.448485 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 681.90909 | 163.81423 | price | -31.618578 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 976.49545 | 148.03196 | price | -17.868255 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.3161858 | 0.31618578 | ratio | -31.618578 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.958481 | 0.45183912 | %p | -10.026071 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 110.3745 | 9.7370518 | price | -9.6753761 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 169.60134 | 10.738245 | price | -6.7594334 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0967538 | 0.096753761 | ratio | -9.6753761 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.7765191 | 0.97917344 | %p | -122.80413 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2733.6339 | 1401.9375 | price | -105.27456 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3993.3283 | 1120.1379 | price | -38.985857 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 2.0527456 | 1.0527456 | ratio | -105.27456 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0730022 | 0.62331821 | %p | -18.068849 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 437.90909 | 69.73913 | price | -18.942102 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 612.88829 | 60.533854 | price | -10.959241 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.189421 | 0.18942102 | ratio | -18.942102 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9419598 | -0.38984142 | %p | 7.311627 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 236.86905 | -12.68254 | price | 5.0821314 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 387.15903 | -22.897455 | price | 5.5839758 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.94917869 | -0.050821314 | ratio | 5.0821314 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.945138 | 0.3585443 | %p | -4.175629 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1087.2846 | 38.047431 | price | -3.6261993 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1858.3277 | 27.469095 | price | -1.5003395 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.036262 | 0.036261993 | ratio | -3.6261993 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8994196 | 0.27186168 | %p | -7.4943444 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 104.22925 | 8.201581 | price | -8.540852 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 152.84935 | -2.0335296 | price | 1.3129466 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0854085 | 0.08540852 | ratio | -8.540852 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2786311 | 0.67132379 | %p | -10.160323 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1456.5336 | 100.79842 | price | -7.4349637 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2322.3251 | 81.215652 | price | -3.6239039 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0743496 | 0.074349637 | ratio | -7.4349637 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 5.0913068 | 0.48504726 | %p | -10.530177 | worsened |
| mae | 565.55167 | 712.79368 | 147.24201 | price | -26.035111 | worsened |
| rmse | 926.40586 | 1087.8161 | 161.41026 | price | -17.423278 | worsened |
| rmae | 1.0199316 | 1.1999771 | 0.18004548 | ratio | -17.652702 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.2181644 | 0.48835341 | %p | -10.325009 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 151.0751 | 13.245059 | price | -9.6097043 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 218.8498 | 9.6708534 | price | -4.6232442 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0926191 | 0.095792122 | ratio | -9.6097043 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1630874 | 0.43093106 | %p | -7.5177827 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 128.11858 | 8.4545455 | price | -7.0652353 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 186.33683 | 7.5978479 | price | -4.2508062 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1068465 | 0.073040806 | ratio | -7.0652353 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.6586647 | 0.97822616 | %p | -36.495004 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 681.90909 | 191.30435 | price | -38.993579 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 976.49545 | 197.41359 | price | -25.339261 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.3161858 | 0.36924579 | ratio | -38.993579 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.958481 | 0.36748079 | %p | -8.0043732 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 110.3745 | 7.4183267 | price | -7.2053247 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 169.60134 | 4.566269 | price | -2.7668477 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0967538 | 0.073713381 | ratio | -7.2053247 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.7765191 | 0.70984797 | %p | -66.547968 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2733.6339 | 1022.1652 | price | -59.724443 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3993.3283 | 1154.3881 | price | -40.662644 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 2.0527456 | 0.76756621 | ratio | -59.724443 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0730022 | 0.5343087 | %p | -15.099038 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 437.90909 | 59.833992 | price | -15.825954 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 612.88829 | 47.514252 | price | -8.4040386 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.189421 | 0.16251731 | ratio | -15.825954 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9419598 | 0.16346409 | %p | -3.4208274 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 236.86905 | 11.646825 | price | -5.1712594 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 387.15903 | 13.819373 | price | -3.7015551 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.94917869 | 0.046671013 | ratio | -5.1712594 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.945138 | 0.86640606 | %p | -10.72453 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1087.2846 | 123.14229 | price | -12.772211 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1858.3277 | 154.35745 | price | -9.0586936 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.036262 | 0.11736364 | ratio | -12.772211 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8994196 | 0.25041635 | %p | -6.8625959 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 104.22925 | 7.0869565 | price | -7.2954388 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 152.84935 | -2.3118274 | price | 1.4899522 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0854085 | 0.073801194 | ratio | -7.2954388 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2786311 | 0.061037986 | %p | -0.84568339 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1456.5336 | 28.12253 | price | -1.9687981 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2322.3251 | 27.086687 | price | -1.1801252 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0743496 | 0.02074338 | ratio | -1.9687981 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 0, 'worsened': 10, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

