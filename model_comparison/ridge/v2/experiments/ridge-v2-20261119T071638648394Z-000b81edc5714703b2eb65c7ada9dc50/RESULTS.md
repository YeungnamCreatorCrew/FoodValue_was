
## ridge-v2-20261119T071638648394Z-000b81edc5714703b2eb65c7ada9dc50

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071638648394Z-000b81edc5714703b2eb65c7ada9dc50 | market_pricedyn | 4.4506682 | 553.23161 | 935.52427 | 0.9848346 | 3.3778233 (direct) | 3.3952275 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4506682 | -0.15642116 | %p | 3.3952275 | improved |
| mae | 532.31701 | 553.23161 | 20.914609 | price | -3.9289764 | worsened |
| rmse | 943.1701 | 935.52427 | -7.6458292 | price | 0.81065221 | improved |
| rmae | 1 | 0.9848346 | -0.015165404 | ratio | 1.5165404 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.3696509 | -0.39884564 | %p | 8.3641801 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 126.98024 | -11.288538 | price | 8.1641987 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 188.28836 | -22.497692 | price | 10.673236 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.91835801 | -0.081641987 | ratio | 8.1641987 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6167728 | 0.11471098 | %p | -2.0848726 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 117.37549 | 1.6245059 | price | -1.4034489 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 175.6796 | 4.5435053 | price | -2.6549077 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0140345 | 0.014034489 | ratio | -1.4034489 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6982202 | -0.19518313 | %p | 6.7457975 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 488.72332 | -29.371542 | price | 5.6691436 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 812.08509 | -16.378391 | price | 1.9769599 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94330856 | -0.056691436 | ratio | 5.6691436 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4263814 | -0.080260478 | %p | 1.7809376 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 99.414343 | -1.2231076 | price | 1.2153603 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.14932 | -0.713773 | price | 0.44930071 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.9878464 | -0.012153603 | ratio | 1.2153603 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0526305 | 0.25528482 | %p | -32.016831 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1695.3884 | 363.69196 | price | -27.310426 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3048.9585 | 175.76805 | price | -6.1175217 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2731043 | 0.27310426 | ratio | -27.310426 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.357354 | -0.092330068 | %p | 2.676479 | improved |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 359.19763 | -8.972332 | price | 2.4370082 | improved |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 539.70516 | -12.649268 | price | 2.2900637 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 0.97562992 | -0.024370082 | ratio | 2.4370082 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.5836562 | -0.74814506 | %p | 14.031751 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 213.89286 | -35.65873 | price | 14.289122 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 338.74031 | -71.316178 | price | 17.391794 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.85710878 | -0.14289122 | ratio | 14.289122 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9330853 | -0.65350846 | %p | 7.6107998 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 952.04743 | -97.189723 | price | 9.2628938 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1681.0031 | -149.85549 | price | 8.1849842 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.90737106 | -0.092628938 | ratio | 9.2628938 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4290786 | -0.19847933 | %p | 5.471431 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 90.992095 | -5.0355731 | price | 5.2438773 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 139.27081 | -15.612069 | price | 10.079919 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.94756123 | -0.052438773 | ratio | 5.2438773 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.039852 | 0.43254472 | %p | -6.5464599 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1388.3043 | 32.56917 | price | -2.4023254 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2273.3624 | 32.253013 | price | -1.4391539 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0240233 | 0.024023254 | ratio | -2.4023254 | worsened |
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
| mape | 4.6062595 | 4.4506682 | -0.1555913 | %p | 3.3778233 | improved |
| mae | 565.55167 | 553.23161 | -12.320057 | price | 2.178414 | improved |
| rmse | 926.40586 | 935.52427 | 9.1184117 | price | -0.98427829 | worsened |
| rmae | 1.0199316 | 0.9848346 | -0.035096972 | ratio | 3.4411105 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.3696509 | -0.36016011 | %p | 7.6146829 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 126.98024 | -10.849802 | price | 7.8718706 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 188.28836 | -20.890584 | price | 9.9869442 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.91835801 | -0.078468927 | ratio | 7.8718706 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6167728 | -0.11538358 | %p | 2.0129174 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 117.37549 | -2.2885375 | price | 1.912469 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 175.6796 | -3.0593891 | price | 1.7116518 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0140345 | -0.019771214 | ratio | 1.912469 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6982202 | 0.017781676 | %p | -0.66338683 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 488.72332 | -1.8814229 | price | 0.38349057 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 812.08509 | 33.003232 | price | -4.23617 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94330856 | -0.0036314256 | ratio | 0.38349057 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4263814 | -0.16461881 | %p | 3.5856851 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 99.414343 | -3.5418327 | price | 3.4401362 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.14932 | -6.8857489 | price | 4.1722944 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.9878464 | -0.035193983 | ratio | 3.4401362 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0526305 | -0.014040655 | %p | 1.3163059 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1695.3884 | -16.080357 | price | 0.93956475 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3048.9585 | 210.01828 | price | -7.3977706 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2731043 | -0.012075092 | ratio | 0.93956475 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.357354 | -0.18133959 | %p | 5.1244784 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 359.19763 | -18.87747 | price | 4.9930478 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 539.70516 | -25.66887 | price | 4.5401572 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 0.97562992 | -0.051273793 | ratio | 4.9930478 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.5836562 | -0.19483955 | %p | 4.0774244 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 213.89286 | -11.329365 | price | 5.0303052 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 338.74031 | -34.59935 | price | 9.267526 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.85710878 | -0.04539889 | ratio | 5.0303052 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9330853 | -0.14564669 | %p | 1.802841 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 952.04743 | -12.094862 | price | 1.2544685 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1681.0031 | -22.967137 | price | 1.3478602 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.90737106 | -0.011527291 | ratio | 1.2544685 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4290786 | -0.21992467 | %p | 6.0269792 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 90.992095 | -6.1501976 | price | 6.3311226 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 139.27081 | -15.890367 | price | 10.2412 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.94756123 | -0.0640461 | ratio | 6.3311226 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.039852 | -0.17774108 | %p | 2.4626087 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1388.3043 | -40.106719 | price | 2.8077855 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2273.3624 | -21.875952 | price | 0.95310154 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0240233 | -0.029583004 | ratio | 2.8077855 | improved |
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
| mape | 4.5011413 | 4.4506682 | -0.050473129 | %p | 1.1213407 | improved |
| mae | 557.9753 | 553.23161 | -4.7436885 | price | 0.85016101 | improved |
| rmse | 915.84853 | 935.52427 | 19.675734 | price | -2.1483612 | worsened |
| rmae | 0.99470404 | 0.9848346 | -0.0098694485 | ratio | 0.99219949 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.3696509 | -0.056776842 | %p | 1.2826786 | improved |
| 1 | 대파/RETAIL | mae | 128.74704 | 126.98024 | -1.7667984 | price | 1.3723022 | improved |
| 1 | 대파/RETAIL | rmse | 191.58023 | 188.28836 | -3.2918707 | price | 1.7182726 | improved |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.91835801 | -0.012778 | ratio | 1.3723022 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6167728 | -0.11614177 | %p | 2.0258764 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 117.37549 | -2.1422925 | price | 1.7924466 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 175.6796 | -5.1924907 | price | 2.8708082 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0140345 | -0.018507768 | ratio | 1.7924466 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.6982202 | -0.036094948 | %p | 1.3200727 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 488.72332 | -5.0513834 | price | 1.0230138 | improved |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 812.08509 | 23.8272 | price | -3.022767 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.94330856 | -0.0097499199 | ratio | 1.0230138 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.4263814 | 0.0011929178 | %p | -0.026957445 | worsened |
| 8 | 양파/RETAIL | mae | 98.860558 | 99.414343 | 0.55378486 | price | -0.56016765 | worsened |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.14932 | -0.56365682 | price | 0.35514224 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.9878464 | 0.0055027712 | ratio | -0.56016765 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0526305 | 0.011731103 | %p | -1.127016 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1695.3884 | 13.691964 | price | -0.81417574 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 3048.9585 | 254.55018 | price | -9.1092695 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2731043 | 0.010281596 | ratio | -0.81417574 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.357354 | -0.10033738 | %p | 2.9018604 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 359.19763 | -10.656126 | price | 2.881173 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 539.70516 | -11.8822 | price | 2.1541828 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 0.97562992 | -0.028943498 | ratio | 2.881173 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.5836562 | -0.17061601 | %p | 3.5886882 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 213.89286 | -8.7063492 | price | 3.911222 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 338.74031 | -18.524017 | price | 5.1849613 | improved |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.85710878 | -0.034887974 | ratio | 3.911222 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9330853 | -0.006707785 | %p | 0.084483121 | improved |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 952.04743 | -7.798419 | price | 0.81246577 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1681.0031 | -28.880779 | price | 1.6890491 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.90737106 | -0.0074324655 | ratio | 0.81246577 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4290786 | 0.071996136 | %p | -2.1446043 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 90.992095 | 1.7233202 | price | -1.9304848 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 139.27081 | -1.8600644 | price | 1.3179713 | improved |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.94756123 | 0.017946079 | ratio | -1.9304848 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.039852 | -0.10297672 | %p | 1.4416799 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1388.3043 | -27.284585 | price | 1.927437 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2273.3624 | -11.424959 | price | 0.50004474 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0240233 | -0.020125306 | ratio | 1.927437 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

