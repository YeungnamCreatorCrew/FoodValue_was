
## ridge-v2-20261117T064456555488Z-5ae9944aafc44182a4a82114ed57d03a

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064456555488Z-5ae9944aafc44182a4a82114ed57d03a | no_national_weather | 4.9890974 | 673.1964 | 1029.5406 | 1.1581542 | -8.3112539 (direct) | -8.2917442 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9890974 | 0.38200806 | %p | -8.2917442 | worsened |
| mae | 532.31701 | 673.1964 | 140.87939 | price | -26.465319 | worsened |
| rmse | 943.1701 | 1029.5406 | 86.370517 | price | -9.1574698 | worsened |
| rmae | 1 | 1.1581542 | 0.15815423 | ratio | -15.815423 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.0669886 | 0.2984921 | %p | -6.2596689 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 146.94466 | 8.6758893 | price | -6.2746555 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.23196 | -2.5540895 | price | 1.2116976 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0627466 | 0.062746555 | ratio | -6.2746555 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1146823 | 0.61262052 | %p | -11.134381 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 126.98024 | 11.229249 | price | -9.7012122 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 185.85908 | 14.722988 | price | -8.6030878 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0970121 | 0.097012122 | ratio | -9.7012122 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.6009562 | 0.70755281 | %p | -24.453998 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 662.51383 | 144.41897 | price | -27.875006 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 997.11023 | 168.64675 | price | -20.35657 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2787501 | 0.27875006 | ratio | -27.875006 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.8331754 | 0.32653352 | %p | -7.2456061 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 107.06375 | 6.4262948 | price | -6.3855899 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.66093 | 5.7978415 | price | -3.6495837 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0638559 | 0.063855899 | ratio | -6.3855899 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.5600241 | 0.76267845 | %p | -95.652172 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2402.4509 | 1070.7545 | price | -80.405297 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3452.2451 | 579.05464 | price | -20.153716 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.804053 | 0.80405297 | ratio | -80.405297 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0716165 | 0.62193248 | %p | -18.02868 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 436 | 67.83004 | price | -18.423567 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 609.00912 | 56.654683 | price | -10.256944 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1842357 | 0.18423567 | ratio | -18.423567 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0167214 | -0.31507984 | %p | 5.9094446 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.67857 | -5.8730159 | price | 2.3534276 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 384.48695 | -25.569531 | price | 6.2356119 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97646572 | -0.023534276 | ratio | 2.3534276 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8549578 | 0.26836403 | %p | -3.125384 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1086.9328 | 37.695652 | price | -3.5926723 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1869.9704 | 39.111789 | price | -2.1362539 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0359267 | 0.035926723 | ratio | -3.5926723 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7063939 | 0.078835952 | %p | -2.1732514 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 98.98419 | 2.9565217 | price | -3.0788228 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 143.21756 | -11.665326 | price | 7.5317075 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0307882 | 0.030788228 | ratio | -3.0788228 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0654579 | 0.45815063 | %p | -6.9339991 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1420.415 | 64.679842 | price | -4.7708316 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2280.6148 | 39.505424 | price | -1.7627619 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0477083 | 0.047708316 | ratio | -4.7708316 | worsened |
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
| mape | 4.6062595 | 4.9890974 | 0.38283792 | %p | -8.3112539 | worsened |
| mae | 565.55167 | 673.1964 | 107.64472 | price | -19.033579 | worsened |
| rmse | 926.40586 | 1029.5406 | 103.13476 | price | -11.132783 | worsened |
| rmae | 1.0199316 | 1.1581542 | 0.13822266 | ratio | -13.55215 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.0669886 | 0.33717762 | %p | -7.1287758 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 146.94466 | 9.1146245 | price | -6.6129449 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.23196 | -0.94698205 | price | 0.45271385 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0627466 | 0.065919616 | ratio | -6.6129449 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1146823 | 0.38252596 | %p | -6.6733344 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 126.98024 | 7.3162055 | price | -6.1139554 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 185.85908 | 7.1200936 | price | -3.9835146 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0970121 | 0.06320642 | ratio | -6.1139554 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.6009562 | 0.92051762 | %p | -34.342052 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 662.51383 | 171.90909 | price | -35.040242 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 997.11023 | 218.02837 | price | -27.985297 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2787501 | 0.33181007 | ratio | -35.040242 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.8331754 | 0.24217519 | %p | -5.2749984 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 107.06375 | 4.1075697 | price | -3.9896293 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.66093 | -0.37413434 | price | 0.22669991 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0638559 | 0.040815519 | ratio | -3.9896293 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.5600241 | 0.49335298 | %p | -46.251647 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2402.4509 | 690.98214 | price | -40.373635 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3452.2451 | 613.30488 | price | -21.603304 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.804053 | 0.51887362 | ratio | -40.373635 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0716165 | 0.53292296 | %p | -15.059879 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 436 | 57.924901 | price | -15.321004 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 609.00912 | 43.635081 | price | -7.7179139 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1842357 | 0.15733196 | ratio | -15.321004 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0167214 | 0.23822567 | %p | -4.9853696 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.67857 | 18.456349 | price | -8.1947283 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 384.48695 | 11.147297 | price | -2.9858325 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97646572 | 0.073958052 | ratio | -8.1947283 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8549578 | 0.77622579 | %p | -9.6082627 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1086.9328 | 122.79051 | price | -12.735725 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1869.9704 | 166.00014 | price | -9.7419623 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0359267 | 0.11702837 | ratio | -12.735725 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7063939 | 0.057390614 | %p | -1.5727751 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 98.98419 | 1.8418972 | price | -1.8960817 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 143.21756 | -11.943624 | price | 7.697559 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0307882 | 0.019180901 | ratio | -1.8960817 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0654579 | -0.15213517 | %p | 2.107838 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1420.415 | -7.9960474 | price | 0.55978616 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2280.6148 | -14.623542 | price | 0.63712519 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0477083 | -0.005897942 | ratio | 0.55978616 | improved |
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
| mape | 4.99034 | 4.9890974 | -0.0012426242 | %p | 0.024900592 | improved |
| mae | 674.96363 | 673.1964 | -1.7672373 | price | 0.26182704 | improved |
| rmse | 1034.3299 | 1029.5406 | -4.7892587 | price | 0.4630301 | improved |
| rmae | 1.1614981 | 1.1581542 | -0.003343864 | ratio | 0.28789234 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.0669886 | -0.066976927 | %p | 1.3045847 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 146.94466 | -1.8695652 | price | 1.2563081 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 208.23196 | -1.5899477 | price | 0.75776058 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0627466 | -0.013521239 | ratio | 1.2563081 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1146823 | -0.041933654 | %p | 0.68111531 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 126.98024 | -0.88537549 | price | 0.69242658 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 185.85908 | -1.2045012 | price | 0.64389934 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0970121 | -0.007648967 | ratio | 0.69242658 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.6009562 | 0.006066814 | %p | -0.16876219 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 662.51383 | -0.31620553 | price | 0.047705372 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 997.11023 | -4.8631689 | price | 0.48535909 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2787501 | -0.00061032362 | ratio | 0.047705372 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.8331754 | -0.0045115551 | %p | 0.093258516 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 107.06375 | 0.039840637 | price | -0.037225924 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 164.66093 | 0.026496272 | price | -0.016094003 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0638559 | 0.00039588282 | ratio | -0.037225924 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.5600241 | -0.013862233 | %p | 0.88076454 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2402.4509 | -29.90625 | price | 1.2295172 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3452.2451 | -62.767171 | price | 1.7856886 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.804053 | -0.022457258 | ratio | 1.2295172 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0716165 | 0.025512306 | %p | -0.63054001 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 436 | 2.1660079 | price | -0.49927114 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 609.00912 | 2.2629567 | price | -0.37296598 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1842357 | 0.0058831739 | ratio | -0.49927114 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 5.0167214 | 0.031617799 | %p | -0.63424558 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.67857 | 1.0912698 | price | -0.44984623 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 384.48695 | 4.9969459 | price | -1.316753 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97646572 | 0.0043729229 | ratio | -0.44984623 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8549578 | 0.049254543 | %p | -0.55934821 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1086.9328 | 9.0988142 | price | -0.84417585 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1869.9704 | 14.979538 | price | -0.80752623 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0359267 | 0.0086718376 | ratio | -0.84417585 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7063939 | -0.038095875 | %p | 1.0173849 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 98.98419 | -1.1027668 | price | 1.1018087 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 143.21756 | -0.89307195 | price | 0.61971275 | improved |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0307882 | -0.011483844 | ratio | 1.1018087 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.0654579 | 0.040502539 | %p | -0.57655225 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1420.415 | 4.0118577 | price | -0.28324264 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2280.6148 | 1.1593374 | price | -0.050860278 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0477083 | 0.002959175 | ratio | -0.28324264 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

