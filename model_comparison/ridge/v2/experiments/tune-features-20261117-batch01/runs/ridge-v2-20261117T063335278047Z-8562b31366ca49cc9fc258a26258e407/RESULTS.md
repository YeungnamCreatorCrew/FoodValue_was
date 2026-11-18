
## ridge-v2-20261117T063335278047Z-8562b31366ca49cc9fc258a26258e407

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063335278047Z-8562b31366ca49cc9fc258a26258e407 | cross_item | 4.677918 | 586.57225 | 967.82469 | 1.0506457 | -1.5556774 (direct) | -1.5373845 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.677918 | 0.070828677 | %p | -1.5373845 | worsened |
| mae | 532.31701 | 586.57225 | 54.255246 | price | -10.192281 | worsened |
| rmse | 943.1701 | 967.82469 | 24.654595 | price | -2.6140137 | worsened |
| rmae | 1 | 1.0506457 | 0.050645665 | ratio | -5.0645665 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.8895908 | 0.12109428 | %p | -2.5394646 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 143.3834 | 5.1146245 | price | -3.6990452 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 216.11041 | 5.3243558 | price | -2.5259526 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0369905 | 0.036990452 | ratio | -3.6990452 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7679989 | 0.26593711 | %p | -4.8334083 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 120.25296 | 4.5019763 | price | -3.8893632 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 179.42484 | 8.2887488 | price | -4.8433669 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0388936 | 0.038893632 | ratio | -3.8893632 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8223885 | -0.071014894 | %p | 2.4543724 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 513.4664 | -4.6284585 | price | 0.8933612 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 802.03283 | -26.430646 | price | 3.1903212 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.99106639 | -0.008933612 | ratio | 0.8933612 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6917356 | 0.18509369 | %p | -4.107131 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 105.16733 | 4.5298805 | price | -4.5011876 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 167.88999 | 9.026895 | price | -5.6821851 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0450119 | 0.045011876 | ratio | -4.5011876 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1686589 | 0.3713132 | %p | -46.568661 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1893.9598 | 562.26339 | price | -42.221589 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3219.7292 | 346.53876 | price | -12.061114 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.4222159 | 0.42221589 | ratio | -42.221589 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5469216 | 0.097237606 | %p | -2.8187395 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 378.96838 | 10.798419 | price | -2.9329984 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 567.03222 | 14.677787 | price | -2.6573131 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.02933 | 0.029329984 | ratio | -2.9329984 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8514657 | -0.4803355 | %p | 9.0088786 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 228.62698 | -20.924603 | price | 8.3848808 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 381.71504 | -28.341444 | price | 6.9115951 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91615119 | -0.083848808 | ratio | 8.3848808 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.1236648 | -0.46292896 | %p | 5.3912993 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 970.44269 | -78.794466 | price | 7.5096908 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1695.7792 | -135.07941 | price | 7.3779272 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92490309 | -0.075096908 | ratio | 7.5096908 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8005024 | 0.17294452 | %p | -4.7675192 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 102.00791 | 5.9802372 | price | -6.2276189 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 163.62366 | 8.7407812 | price | -5.6434779 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0622762 | 0.062276189 | ratio | -6.2276189 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.116253 | 0.50894573 | %p | -7.7027706 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1409.4466 | 53.711462 | price | -3.961796 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2284.9095 | 43.800128 | price | -1.9543949 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.039618 | 0.03961796 | ratio | -3.961796 | worsened |
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
| mape | 4.6062595 | 4.677918 | 0.071658537 | %p | -1.5556774 | worsened |
| mae | 565.55167 | 586.57225 | 21.02058 | price | -3.7168275 | worsened |
| rmse | 926.40586 | 967.82469 | 41.418836 | price | -4.4709169 | worsened |
| rmae | 1.0199316 | 1.0506457 | 0.030714097 | ratio | -3.011388 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.8895908 | 0.15977981 | %p | -3.3781436 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 143.3834 | 5.5533597 | price | -4.029136 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 216.11041 | 6.9314632 | price | -3.3136525 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0369905 | 0.040163513 | ratio | -4.029136 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7679989 | 0.035842559 | %p | -0.62528927 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 120.25296 | 0.58893281 | price | -0.49215524 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 179.42484 | 0.68585436 | price | -0.3837184 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0388936 | 0.005087929 | ratio | -0.49215524 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8223885 | 0.14194992 | %p | -5.295772 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 513.4664 | 22.86166 | price | -4.6598938 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 802.03283 | 22.950977 | price | -2.9459005 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.99106639 | 0.044126398 | ratio | -4.6598938 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6917356 | 0.10073535 | %p | -2.1941919 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 105.16733 | 2.2111554 | price | -2.1476666 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 167.88999 | 2.8549191 | price | -1.7298863 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0450119 | 0.021971496 | ratio | -2.1476666 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1686589 | 0.10198773 | %p | -9.5613093 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1893.9598 | 182.49107 | price | -10.662834 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3219.7292 | 380.789 | price | -13.413069 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.4222159 | 0.13703654 | ratio | -10.662834 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5469216 | 0.0082280889 | %p | -0.2325177 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 378.96838 | 0.89328063 | price | -0.23627069 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 567.03222 | 1.6581851 | price | -0.29328992 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.02933 | 0.0024262725 | ratio | -0.23627069 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8514657 | 0.072970008 | %p | -1.5270498 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 228.62698 | 3.4047619 | price | -1.5117344 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 381.71504 | 8.375384 | price | -2.2433684 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.91615119 | 0.013643519 | ratio | -1.5117344 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.1236648 | 0.044932801 | %p | -0.55618631 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 970.44269 | 6.3003953 | price | -0.65347152 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1695.7792 | -8.191064 | price | 0.48070463 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92490309 | 0.006004739 | ratio | -0.65347152 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8005024 | 0.15149918 | %p | -4.1517963 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 102.00791 | 4.8656126 | price | -5.008748 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 163.62366 | 8.4624834 | price | -5.4539952 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0622762 | 0.050668862 | ratio | -5.008748 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.116253 | -0.10134007 | %p | 1.4040702 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1409.4466 | -18.964427 | price | 1.3276589 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2284.9095 | -10.328838 | price | 0.45001155 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.039618 | -0.013988297 | ratio | 1.3276589 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

