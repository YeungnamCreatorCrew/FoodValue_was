
## ridge-v2-20261117T063442610545Z-403a4226c28d494da7ad3beac15d8917

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063442610545Z-403a4226c28d494da7ad3beac15d8917 | all | 4.99034 | 674.96363 | 1034.3299 | 1.1614981 | -8.3382308 (direct) | -8.3187162 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.99034 | 0.38325069 | %p | -8.3187162 | worsened |
| mae | 532.31701 | 674.96363 | 142.64663 | price | -26.797308 | worsened |
| rmse | 943.1701 | 1034.3299 | 91.159776 | price | -9.665253 | worsened |
| rmae | 1 | 1.1614981 | 0.16149809 | ratio | -16.149809 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1339656 | 0.36546902 | %p | -7.6642401 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.81423 | 10.545455 | price | -7.6267795 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.82191 | -0.96414175 | price | 0.45740301 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0762678 | 0.076267795 | ratio | -7.6267795 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.156616 | 0.65455417 | %p | -11.896525 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 127.86561 | 12.114625 | price | -10.466109 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 187.06358 | 15.927489 | price | -9.3069143 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1046611 | 0.10466109 | ratio | -10.466109 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5948894 | 0.70148599 | %p | -24.244321 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 662.83004 | 144.73518 | price | -27.936038 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1001.9734 | 173.50992 | price | -20.943581 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2793604 | 0.27936038 | ratio | -27.936038 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.837687 | 0.33104508 | %p | -7.3457151 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 107.0239 | 6.3864542 | price | -6.3460016 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.63444 | 5.7713453 | price | -3.632905 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.06346 | 0.063460016 | ratio | -6.3460016 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.5738864 | 0.77654069 | %p | -97.390719 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2432.3571 | 1100.6607 | price | -82.651022 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3515.0122 | 641.82181 | price | -22.338297 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.8265102 | 0.82651022 | ratio | -82.651022 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0461042 | 0.59642017 | %p | -17.289125 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 433.83399 | 65.664032 | price | -17.83525 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 606.74616 | 54.391726 | price | -9.8472508 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1783525 | 0.1783525 | ratio | -17.83525 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9851036 | -0.34669764 | %p | 6.5024486 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 242.5873 | -6.9642857 | price | 2.7907199 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 379.49001 | -30.566477 | price | 7.4542113 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.9720928 | -0.027907199 | ratio | 2.7907199 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8057032 | 0.21910948 | %p | -2.5517626 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1077.834 | 28.596838 | price | -2.7254885 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1854.9909 | 24.132251 | price | -1.3180838 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0272549 | 0.027254885 | ratio | -2.7254885 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7444897 | 0.11693183 | %p | -3.223431 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 100.08696 | 4.0592885 | price | -4.2272072 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.11063 | -10.772254 | price | 6.9550964 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0422721 | 0.042272072 | ratio | -4.2272072 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0249554 | 0.41764809 | %p | -6.321003 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1416.4032 | 60.667984 | price | -4.4749141 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2279.4555 | 38.346086 | price | -1.7110314 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0447491 | 0.044749141 | ratio | -4.4749141 | worsened |
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
| mape | 4.6062595 | 4.99034 | 0.38408055 | %p | -8.3382308 | worsened |
| mae | 565.55167 | 674.96363 | 109.41196 | price | -19.346059 | worsened |
| rmse | 926.40586 | 1034.3299 | 107.92402 | price | -11.649755 | worsened |
| rmae | 1.0199316 | 1.1614981 | 0.14156652 | ratio | -13.880002 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1339656 | 0.40415455 | %p | -8.5448351 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.81423 | 10.98419 | price | -7.9693728 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.82191 | 0.64296567 | price | -0.30737591 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0762678 | 0.079440855 | ratio | -7.9693728 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.156616 | 0.42445962 | %p | -7.4048855 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 127.86561 | 8.201581 | price | -6.8538398 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 187.06358 | 8.3245948 | price | -4.657403 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1046611 | 0.070855387 | ratio | -6.8538398 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5948894 | 0.9144508 | %p | -34.115716 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 662.83004 | 172.2253 | price | -35.104695 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1001.9734 | 222.89154 | price | -28.609515 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2793604 | 0.33242039 | ratio | -35.104695 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.837687 | 0.24668674 | %p | -5.3732679 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 107.0239 | 4.0677291 | price | -3.9509326 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.63444 | -0.40063062 | price | 0.24275484 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.06346 | 0.040419636 | ratio | -3.9509326 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.5738864 | 0.50721521 | %p | -47.551226 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2432.3571 | 720.88839 | price | -42.121037 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3515.0122 | 676.07205 | price | -23.814241 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.8265102 | 0.54133087 | ratio | -42.121037 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0461042 | 0.50741066 | %p | -14.338926 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 433.83399 | 55.758893 | price | -14.7481 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 606.74616 | 41.372125 | price | -7.3176556 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1783525 | 0.15144879 | ratio | -14.7481 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9851036 | 0.20660787 | %p | -4.3237011 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 242.5873 | 17.365079 | price | -7.710198 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 379.49001 | 6.150351 | price | -1.6473875 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.9720928 | 0.069585129 | ratio | -7.710198 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8057032 | 0.72697125 | %p | -8.9985811 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1077.834 | 113.6917 | price | -11.792004 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1854.9909 | 151.0206 | price | -8.8628661 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0272549 | 0.10835653 | ratio | -11.792004 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7444897 | 0.095486488 | %p | -2.6167828 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 100.08696 | 2.944664 | price | -3.0312894 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.11063 | -11.050552 | price | 7.1219821 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0422721 | 0.030664746 | ratio | -3.0312894 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0249554 | -0.19263771 | %p | 2.6690021 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1416.4032 | -12.007905 | price | 0.84064772 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2279.4555 | -15.782879 | price | 0.68763574 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0447491 | -0.008857117 | ratio | 0.84064772 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

