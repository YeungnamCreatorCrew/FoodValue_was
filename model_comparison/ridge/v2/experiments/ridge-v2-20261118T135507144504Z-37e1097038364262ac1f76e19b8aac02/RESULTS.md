
## ridge-v2-20261118T135507144504Z-37e1097038364262ac1f76e19b8aac02

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135507144504Z-37e1097038364262ac1f76e19b8aac02 | v1feat_garak | 4.54983 | 555.1525 | 885.59494 | 1.0052831 | 1.2250618 (direct) | 1.2428538 (direct) | 6 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.54983 | -0.057259385 | %p | 1.2428538 | improved |
| mae | 532.31701 | 555.1525 | 22.835495 | price | -4.2898301 | worsened |
| rmse | 943.1701 | 885.59494 | -57.57516 | price | 6.1044302 | improved |
| rmae | 1 | 1.0052831 | 0.0052830556 | ratio | -0.52830556 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4253069 | -0.34318965 | %p | 7.19702 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 128.86166 | -9.4071146 | price | 6.8034989 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.22089 | -18.565163 | price | 8.807586 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93196501 | -0.068034989 | ratio | 6.8034989 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8086218 | 0.30655997 | %p | -5.571729 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.25692 | 5.5059289 | price | -4.7567014 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 181.54615 | 10.410058 | price | -6.0829124 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.047567 | 0.047567014 | ratio | -4.7567014 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8174596 | -0.075943772 | %p | 2.6247212 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 516.35968 | -1.7351779 | price | 0.33491509 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 794.4573 | -34.006182 | price | 4.1047292 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.99665085 | -0.0033491509 | ratio | 0.33491509 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5117569 | 0.0051149934 | %p | -0.113499 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 100.44622 | -0.19123506 | price | 0.19002375 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.85283 | -0.010257478 | price | 0.0064568037 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.99809976 | -0.0019002375 | ratio | 0.19002375 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0135551 | 0.21620939 | %p | -27.116142 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1609.8438 | 278.14732 | price | -20.886691 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2420.8858 | -452.30464 | price | 15.742244 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2088669 | 0.20886691 | ratio | -20.886691 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.6180703 | 0.16838628 | %p | -4.8812087 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 385.8498 | 17.679842 | price | -4.802087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 582.52646 | 30.172026 | price | -5.4624394 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0480209 | 0.04802087 | ratio | -4.802087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8017184 | -0.53008286 | %p | 9.9419096 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 226.46429 | -23.087302 | price | 9.2515146 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 367.27408 | -42.782405 | price | 10.433296 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90748485 | -0.092515146 | ratio | 9.2515146 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0250786 | -0.56151513 | %p | 6.5394398 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 967.50988 | -81.727273 | price | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1741.1694 | -89.689234 | price | 4.8987526 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92210791 | -0.077892088 | ratio | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4539222 | -0.17363572 | %p | 4.7865732 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.916996 | -4.1106719 | price | 4.2807162 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 142.35358 | -12.529304 | price | 8.0895343 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.95719284 | -0.042807162 | ratio | 4.2807162 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.02281 | 0.41550265 | %p | -6.2885322 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1403.0158 | 47.280632 | price | -3.4874534 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2274.6629 | 33.553506 | price | -1.4971828 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0348745 | 0.034874534 | ratio | -3.4874534 | worsened |
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
| mape | 4.6062595 | 4.54983 | -0.056429525 | %p | 1.2250618 | improved |
| mae | 565.55167 | 555.1525 | -10.399171 | price | 1.8387659 | improved |
| rmse | 926.40586 | 885.59494 | -40.810919 | price | 4.4052959 | improved |
| rmae | 1.0199316 | 1.0052831 | -0.014648513 | ratio | 1.436225 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4253069 | -0.30450412 | %p | 6.4379764 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 128.86166 | -8.9683794 | price | 6.5068395 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.22089 | -16.958055 | price | 8.106961 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93196501 | -0.064861929 | ratio | 6.5068395 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8086218 | 0.07646542 | %p | -1.333973 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.25692 | 1.5928854 | price | -1.3311313 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 181.54615 | 2.807164 | price | -1.5705382 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.047567 | 0.013761311 | ratio | -1.3311313 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8174596 | 0.13702104 | %p | -5.1118887 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 516.35968 | 25.754941 | price | -5.2496314 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 794.4573 | 15.375441 | price | -1.9735334 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.99665085 | 0.049710859 | ratio | -5.2496314 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5117569 | -0.079243339 | %p | 1.7260583 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 100.44622 | -2.5099602 | price | 2.4378918 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.85283 | -6.1822334 | price | 3.7460119 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.99809976 | -0.024940618 | ratio | 2.4378918 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0135551 | -0.053116089 | %p | 4.9796125 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1609.8438 | -101.625 | price | 5.9378823 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2420.8858 | -418.05441 | price | 14.725721 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2088669 | -0.076312437 | ratio | 5.9378823 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.6180703 | 0.07937676 | %p | -2.2431092 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 385.8498 | 7.7747036 | price | -2.0563913 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 582.52646 | 17.152425 | price | -3.033819 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0480209 | 0.021117159 | ratio | -2.0563913 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8017184 | 0.023222649 | %p | -0.48598241 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 226.46429 | 1.2420635 | price | -0.55148354 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 367.27408 | -6.0655775 | price | 1.6246807 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90748485 | 0.0049771813 | ratio | -0.55148354 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0250786 | -0.053653365 | %p | 0.66413102 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 967.50988 | 3.3675889 | price | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1741.1694 | 37.199116 | price | -2.1830848 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92210791 | 0.0032095594 | ratio | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4539222 | -0.19508105 | %p | 5.3461463 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.916996 | -5.2252964 | price | 5.3790129 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 142.35358 | -12.807602 | price | 8.2543854 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.95719284 | -0.054414489 | ratio | 5.3790129 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.02281 | -0.19478315 | %p | 2.6987272 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1403.0158 | -25.395257 | price | 1.7778676 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2274.6629 | -20.57546 | price | 0.8964411 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0348745 | -0.018731724 | ratio | 1.7778676 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### V1FEAT: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5391348 | 4.54983 | 0.010695177 | %p | -0.23562149 | worsened |
| mae | 553.57874 | 555.1525 | 1.5737577 | price | -0.28428795 | worsened |
| rmse | 910.2849 | 885.59494 | -24.689963 | price | 2.7123336 | improved |
| rmae | 1.0021178 | 1.0052831 | 0.0031652387 | ratio | -0.31585495 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.439733 | 4.4253069 | -0.014426129 | %p | 0.32493235 | improved |
| 1 | 대파/RETAIL | mae | 129.36759 | 128.86166 | -0.50592885 | price | 0.39107852 | improved |
| 1 | 대파/RETAIL | rmse | 192.41889 | 192.22089 | -0.19799851 | price | 0.10289973 | improved |
| 1 | 대파/RETAIL | rmae | 0.93562404 | 0.93196501 | -0.0036590246 | ratio | 0.39107852 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.8491429 | 5.8086218 | -0.040521176 | %p | 0.69277117 | improved |
| 2 | 대파/WHOLESALE | mae | 122.22134 | 121.25692 | -0.96442688 | price | 0.78908221 | improved |
| 2 | 대파/WHOLESALE | rmse | 182.97472 | 181.54615 | -1.4285687 | price | 0.78074648 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0558989 | 1.047567 | -0.0083319105 | ratio | 0.78908221 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.728634 | 2.8174596 | 0.088825604 | %p | -3.255314 | worsened |
| 7 | 양파/WHOLESALE | mae | 497.18972 | 516.35968 | 19.16996 | price | -3.8556631 | worsened |
| 7 | 양파/WHOLESALE | rmse | 782.2103 | 794.4573 | 12.246994 | price | -1.5656907 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95964998 | 0.99665085 | 0.03700087 | ratio | -3.8556631 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5769182 | 4.5117569 | -0.06516126 | %p | 1.4236929 | improved |
| 8 | 양파/RETAIL | mae | 102.04382 | 100.44622 | -1.5976096 | price | 1.5656112 | improved |
| 8 | 양파/RETAIL | rmse | 160.99468 | 158.85283 | -2.1418448 | price | 1.3303824 | improved |
| 8 | 양파/RETAIL | rmae | 1.0139747 | 0.99809976 | -0.015874901 | ratio | 1.5656112 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.010062 | 1.0135551 | 0.0034930472 | %p | -0.34582503 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1620.5357 | 1609.8438 | -10.691964 | price | 0.65977961 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2724.0606 | 2420.8858 | -303.17481 | price | 11.129518 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2168957 | 1.2088669 | -0.00802883 | ratio | 0.65977961 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5739886 | 3.6180703 | 0.044081714 | %p | -1.2334039 | worsened |
| 10 | 깐마늘/RETAIL | mae | 381.96443 | 385.8498 | 3.8853755 | price | -1.0172087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 572.99301 | 582.52646 | 9.5334534 | price | -1.6637993 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0374677 | 1.0480209 | 0.010553212 | ratio | -1.0172087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7408145 | 4.8017184 | 0.06090386 | %p | -1.2846708 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59524 | 226.46429 | 3.8690476 | price | -1.7381538 | worsened |
| 9001 | 배추/RETAIL | rmse | 355.715 | 367.27408 | 11.559084 | price | -3.2495351 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89198085 | 0.90748485 | 0.015503999 | ratio | -1.7381538 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9415835 | 8.0250786 | 0.08349506 | %p | -1.0513654 | worsened |
| 9002 | 배추/WHOLESALE | mae | 954.7747 | 967.50988 | 12.735178 | price | -1.3338411 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1695.6307 | 1741.1694 | 45.538654 | price | -2.6856469 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.90997035 | 0.92210791 | 0.012137559 | ratio | -1.3338411 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.4647414 | 3.4539222 | -0.010819155 | %p | 0.31226444 | improved |
| 9011 | 무/RETAIL | mae | 91.932806 | 91.916996 | -0.015810277 | price | 0.017197644 | improved |
| 9011 | 무/RETAIL | rmse | 142.69508 | 142.35358 | -0.34149915 | price | 0.2393209 | improved |
| 9011 | 무/RETAIL | rmae | 0.95735748 | 0.95719284 | -0.00016464293 | ratio | 0.017197644 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0657298 | 7.02281 | -0.042919795 | %p | 0.60743612 | improved |
| 9012 | 무/WHOLESALE | mae | 1413.1621 | 1403.0158 | -10.146245 | price | 0.71798171 | improved |
| 9012 | 무/WHOLESALE | rmse | 2293.156 | 2274.6629 | -18.493087 | price | 0.80644695 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0423585 | 1.0348745 | -0.0074839432 | ratio | 0.71798171 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

