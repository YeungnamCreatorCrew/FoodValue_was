
## ridge-v2-20261117T063241156076Z-a25576dc81694b6fb4082998fdc8da75

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063241156076Z-a25576dc81694b6fb4082998fdc8da75 | weather_anom | 4.8059657 | 616.2228 | 972.60069 | 1.087739 | -4.3355391 (direct) | -4.3167455 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.8059657 | 0.19887632 | %p | -4.3167455 | worsened |
| mae | 532.31701 | 616.2228 | 83.905799 | price | -15.762374 | worsened |
| rmse | 943.1701 | 972.60069 | 29.430594 | price | -3.1203909 | worsened |
| rmae | 1 | 1.087739 | 0.087739022 | ratio | -8.7739022 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.8720194 | 0.10352286 | %p | -2.1709749 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 141.94466 | 3.6758893 | price | -2.6585101 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 213.53122 | 2.7451679 | price | -1.302348 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0265851 | 0.026585101 | ratio | -2.6585101 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.963735 | 0.46167319 | %p | -8.3909125 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 123.94071 | 8.1897233 | price | -7.0752945 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 183.19044 | 12.054355 | price | -7.0437247 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0707529 | 0.070752945 | ratio | -7.0752945 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.1444822 | 0.2510788 | %p | -8.6776286 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 579.083 | 60.988142 | price | -11.771617 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 925.43569 | 96.97221 | price | -11.705068 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1177162 | 0.11771617 | ratio | -11.771617 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.7509414 | 0.24429951 | %p | -5.420877 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 106.49004 | 5.8525896 | price | -5.8155186 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 167.77165 | 8.9085582 | price | -5.6076953 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0581552 | 0.058155186 | ratio | -5.8155186 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.29674 | 0.49939436 | %p | -62.632103 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2050.9018 | 719.20536 | price | -54.006705 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3038.1954 | 165.005 | price | -5.7429192 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.540067 | 0.54006705 | ratio | -54.006705 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.6758177 | 0.22613369 | %p | -6.5552001 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 394.15415 | 25.98419 | price | -7.0576615 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 572.54688 | 20.192443 | price | -3.655704 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0705766 | 0.070576615 | ratio | -7.0576615 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0011151 | -0.33068611 | %p | 6.2021462 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 236.56349 | -12.988095 | price | 5.2045733 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 397.05752 | -12.998965 | price | 3.1700426 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.94795427 | -0.052045733 | ratio | 5.2045733 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.386301 | -0.20029273 | %p | 2.3326215 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1008.0474 | -41.189723 | price | 3.9256829 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1768.5474 | -62.311247 | price | 3.4033894 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.96074317 | -0.039256829 | ratio | 3.9256829 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7677228 | 0.14016483 | %p | -3.8638896 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.509881 | 3.4822134 | price | -3.6262605 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 154.81975 | -0.063135917 | price | 0.040763651 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0362626 | 0.036262605 | ratio | -3.6262605 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2007821 | 0.59347482 | %p | -8.982098 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1421.5929 | 65.857708 | price | -4.8577118 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2304.911 | 63.801553 | price | -2.8468736 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0485771 | 0.048577118 | ratio | -4.8577118 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 2, 'worsened': 8, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.8059657 | 0.19970618 | %p | -4.3355391 | worsened |
| mae | 565.55167 | 616.2228 | 50.671133 | price | -8.9595939 | worsened |
| rmse | 926.40586 | 972.60069 | 46.194835 | price | -4.9864576 | worsened |
| rmae | 1.0199316 | 1.087739 | 0.067807454 | ratio | -6.6482357 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.8720194 | 0.14220839 | %p | -3.0066401 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 141.94466 | 4.1146245 | price | -2.9852886 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 213.53122 | 4.3522753 | price | -2.080647 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0265851 | 0.029758161 | ratio | -2.9852886 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.963735 | 0.23157864 | %p | -4.0399916 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 123.94071 | 4.2766798 | price | -3.5739059 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 183.19044 | 4.4514607 | price | -2.4904811 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0707529 | 0.036947243 | ratio | -3.5739059 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.1444822 | 0.46404361 | %p | -17.312227 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 579.083 | 88.478261 | price | -18.03453 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 925.43569 | 146.35383 | price | -18.785424 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.1177162 | 0.17077618 | ratio | -18.03453 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.7509414 | 0.15994118 | %p | -3.4837981 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 106.49004 | 3.5338645 | price | -3.4323969 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 167.77165 | 2.7365823 | price | -1.6581823 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0581552 | 0.035114806 | ratio | -3.4323969 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.29674 | 0.23006889 | %p | -21.568868 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2050.9018 | 339.43304 | price | -19.83285 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3038.1954 | 199.25524 | price | -7.0186487 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.540067 | 0.2548877 | ratio | -19.83285 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.6758177 | 0.13712417 | %p | -3.8749943 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 394.15415 | 16.079051 | price | -4.2528724 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 572.54688 | 7.1728416 | price | -1.2686896 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0705766 | 0.043672904 | ratio | -4.2528724 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0011151 | 0.2226194 | %p | -4.6587758 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 236.56349 | 11.34127 | price | -5.035591 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 397.05752 | 23.717863 | price | -6.3528914 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.94795427 | 0.045446595 | ratio | -5.035591 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.386301 | 0.30756903 | %p | -3.8071449 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1008.0474 | 43.905138 | price | -4.5538028 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1768.5474 | 64.577104 | price | -3.7898023 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.96074317 | 0.041844819 | ratio | -4.5538028 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7677228 | 0.1187195 | %p | -3.2534774 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.509881 | 2.3675889 | price | -2.4372381 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 154.81975 | -0.34143373 | price | 0.220051 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0362626 | 0.024655279 | ratio | -2.4372381 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2007821 | -0.016810985 | %p | 0.23291677 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1421.5929 | -6.8181818 | price | 0.47732631 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2304.911 | 9.6725877 | price | -0.42141974 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0485771 | -0.0050291399 | ratio | 0.47732631 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

