
## ridge-v2-20261117T063704285612Z-7765d136cfd743d18134df8db852fc6f

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063704285612Z-7765d136cfd743d18134df8db852fc6f | all_weather_anom | 5.0194518 | 723.1169 | 1107.3446 | 1.1994075 | -8.9702344 (direct) | -8.950606 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 5.0194518 | 0.41236242 | %p | -8.950606 | worsened |
| mae | 532.31701 | 723.1169 | 190.79989 | price | -35.843283 | worsened |
| rmse | 943.1701 | 1107.3446 | 164.17455 | price | -17.406675 | worsened |
| rmae | 1 | 1.1994075 | 0.19940746 | ratio | -19.940746 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.0048157 | 0.23631917 | %p | -4.9558423 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 144.88538 | 6.6166008 | price | -4.7853182 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 204.33256 | -6.4534915 | price | 3.0616312 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0478532 | 0.047853182 | ratio | -4.7853182 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1664076 | 0.66434585 | %p | -12.074489 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 126.98024 | 11.229249 | price | -9.7012122 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 185.14195 | 14.00586 | price | -8.184048 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0970121 | 0.097012122 | ratio | -9.7012122 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5511956 | 0.65779221 | %p | -22.734204 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 649.71146 | 131.6166 | price | -25.403958 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 933.10491 | 104.64143 | price | -12.630783 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2540396 | 0.25403958 | ratio | -25.403958 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.8622818 | 0.35563992 | %p | -7.8914617 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 107.84861 | 7.2111554 | price | -7.165479 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.76916 | 5.906069 | price | -3.71771 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0716548 | 0.07165479 | ratio | -7.165479 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.843251 | 1.0459053 | %p | -131.17338 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2913.8884 | 1582.192 | price | -118.81026 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 4342.1867 | 1468.9963 | price | -51.127704 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 2.1881026 | 1.1881026 | ratio | -118.81026 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.2811436 | 0.83145955 | %p | -24.102484 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 462.90514 | 94.735178 | price | -25.731371 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 642.26734 | 89.912911 | price | -16.278119 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.2573137 | 0.25731371 | ratio | -25.731371 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9623986 | -0.36940267 | %p | 6.9282903 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.28968 | -6.2619048 | price | 2.5092626 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 385.69774 | -24.358741 | price | 5.940338 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97490737 | -0.025092626 | ratio | 2.5092626 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.854066 | 0.26747231 | %p | -3.114999 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1084.1186 | 34.881423 | price | -3.3244556 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1845.9617 | 15.103073 | price | -0.82491749 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0332446 | 0.033244556 | ratio | -3.3244556 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7290453 | 0.10148738 | %p | -2.7976776 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.766798 | 3.7391304 | price | -3.8938053 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.81116 | -10.071721 | price | 6.5027979 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0389381 | 0.038938053 | ratio | -3.8938053 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9399125 | 0.33260516 | %p | -5.0338988 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1397.7747 | 42.039526 | price | -3.1008656 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2225.1733 | -15.936152 | price | 0.71108317 | improved |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0310087 | 0.031008656 | ratio | -3.1008656 | worsened |
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
| mape | 4.6062595 | 5.0194518 | 0.41319228 | %p | -8.9702344 | worsened |
| mae | 565.55167 | 723.1169 | 157.56523 | price | -27.860447 | worsened |
| rmse | 926.40586 | 1107.3446 | 180.93879 | price | -19.531266 | worsened |
| rmae | 1.0199316 | 1.1994075 | 0.17947589 | ratio | -17.596856 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.0048157 | 0.2750047 | %p | -5.8142851 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 144.88538 | 7.055336 | price | -5.1188667 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 204.33256 | -4.8463841 | price | 2.3168604 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0478532 | 0.051026242 | ratio | -5.1188667 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1664076 | 0.43425129 | %p | -7.5757057 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 126.98024 | 7.3162055 | price | -6.1139554 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 185.14195 | 6.4029653 | price | -3.5822993 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0970121 | 0.06320642 | ratio | -6.1139554 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5511956 | 0.87075702 | %p | -32.485618 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 649.71146 | 159.10672 | price | -32.430734 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 933.10491 | 154.02305 | price | -19.769816 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2540396 | 0.30709959 | ratio | -32.430734 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.8622818 | 0.27128159 | %p | -5.9089866 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 107.84861 | 4.8924303 | price | -4.7519542 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.76916 | -0.26590687 | price | 0.16112144 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0716548 | 0.04861441 | ratio | -4.7519542 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.843251 | 0.7765798 | %p | -72.804051 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2913.8884 | 1202.4196 | price | -70.256594 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 4342.1867 | 1503.2465 | price | -52.950975 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 2.1881026 | 0.90292323 | ratio | -70.256594 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.2811436 | 0.74245003 | %p | -20.980908 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 462.90514 | 84.83004 | price | -22.437352 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 642.26734 | 76.893309 | price | -13.600432 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.2573137 | 0.23041 | ratio | -22.437352 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9623986 | 0.18390284 | %p | -3.8485509 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.28968 | 18.06746 | price | -8.0220593 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 385.69774 | 12.358087 | price | -3.3101457 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97490737 | 0.072399701 | ratio | -8.0220593 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.854066 | 0.77533407 | %p | -9.5972249 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1084.1186 | 119.97628 | price | -12.443836 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1845.9617 | 141.99142 | price | -8.3329755 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0332446 | 0.1143462 | ratio | -12.443836 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7290453 | 0.080042038 | %p | -2.1935316 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.766798 | 2.6245059 | price | -2.701713 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.81116 | -10.350019 | price | 6.6704949 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0389381 | 0.027330726 | ratio | -2.701713 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9399125 | -0.27768064 | %p | 3.8472747 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1397.7747 | -30.636364 | price | 2.1447862 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2225.1733 | -70.065118 | price | 3.0526292 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0310087 | -0.022597602 | ratio | 2.1447862 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### ALL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.99034 | 5.0194518 | 0.029111727 | %p | -0.5833616 | worsened |
| mae | 674.96363 | 723.1169 | 48.153264 | price | -7.1342013 | worsened |
| rmse | 1034.3299 | 1107.3446 | 73.014776 | price | -7.0591383 | worsened |
| rmae | 1.1614981 | 1.1994075 | 0.03790937 | ratio | -3.263834 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.0048157 | -0.12914985 | %p | 2.5155964 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 144.88538 | -3.9288538 | price | 2.6401062 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 204.33256 | -5.4893498 | price | 2.6161948 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0478532 | -0.028414613 | ratio | 2.6401062 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1664076 | 0.0097916798 | %p | -0.15904321 | worsened |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 126.98024 | -0.88537549 | price | 0.69242658 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 185.14195 | -1.9216295 | price | 1.0272601 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0970121 | -0.007648967 | ratio | 0.69242658 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5511956 | -0.043693782 | %p | 1.2154416 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 649.71146 | -13.118577 | price | 1.9791766 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 933.10491 | -68.868492 | price | 6.8732854 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2540396 | -0.025320801 | ratio | 1.9791766 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.8622818 | 0.024594844 | %p | -0.50840089 | worsened |
| 8 | 양파/RETAIL | mae | 107.0239 | 107.84861 | 0.8247012 | price | -0.77057663 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 164.76916 | 0.13472374 | price | -0.081832055 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0716548 | 0.0081947743 | ratio | -0.77057663 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.843251 | 0.26936459 | %p | -17.114615 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2913.8884 | 481.53125 | price | -19.796897 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 4342.1867 | 827.17447 | price | -23.53262 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 2.1881026 | 0.36159236 | ratio | -19.796897 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.2811436 | 0.23503938 | %p | -5.8090293 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 462.90514 | 29.071146 | price | -6.700984 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 642.26734 | 35.521184 | price | -5.8543732 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.2573137 | 0.078961212 | ratio | -6.700984 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9623986 | -0.022705033 | %p | 0.45545759 | improved |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.28968 | 0.70238095 | price | -0.28953739 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 385.69774 | 6.2077357 | price | -1.6358101 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97490737 | 0.0028145722 | ratio | -0.28953739 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.854066 | 0.048362825 | %p | -0.54922161 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1084.1186 | 6.284585 | price | -0.58307541 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1845.9617 | -9.0291785 | price | 0.48675057 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0332446 | 0.0059896706 | ratio | -0.58307541 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7290453 | -0.01544445 | %p | 0.41245808 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 99.766798 | -0.3201581 | price | 0.31987995 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.81116 | 0.70053286 | price | -0.4861077 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0389381 | -0.0033340193 | ratio | 0.31987995 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 6.9399125 | -0.085042927 | %p | 1.2105832 | improved |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1397.7747 | -18.628458 | price | 1.3151946 | improved |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2225.1733 | -54.282238 | price | 2.3813686 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0310087 | -0.013740485 | ratio | 1.3151946 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

