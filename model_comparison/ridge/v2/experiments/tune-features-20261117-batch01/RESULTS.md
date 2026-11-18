
## ridge-v2-20261117T062701009625Z-687ddf7af37f479ba99a8a710637a8ad

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062701009625Z-687ddf7af37f479ba99a8a710637a8ad | market | 4.5011413 | 557.9753 | 915.84853 | 0.99470404 | 2.2820724 (direct) | 2.299674 (direct) | 8 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5011413 | -0.10594803 | %p | 2.299674 | improved |
| mae | 532.31701 | 557.9753 | 25.658298 | price | -4.8201162 | worsened |
| rmse | 943.1701 | 915.84853 | -27.321563 | price | 2.8967801 | improved |
| rmae | 1 | 0.99470404 | -0.0052959551 | ratio | 0.52959551 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4264277 | -0.34206879 | %p | 7.1735146 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 128.74704 | -9.5217391 | price | 6.8863987 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 191.58023 | -19.205821 | price | 9.1115237 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93113601 | -0.068863987 | ratio | 6.8863987 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7329145 | 0.23085274 | %p | -4.1957498 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.51779 | 3.7667984 | price | -3.2542257 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.87209 | 9.735996 | price | -5.6890373 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0325423 | 0.032542257 | ratio | -3.2542257 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7343152 | -0.15908818 | %p | 5.4983064 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 493.7747 | -24.320158 | price | 4.6941516 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 788.25789 | -40.20559 | price | 4.8530311 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95305848 | -0.046941516 | ratio | 4.6941516 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4251885 | -0.081453396 | %p | 1.8074078 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.860558 | -1.7768924 | price | 1.7656374 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.71298 | -0.15011618 | price | 0.094494058 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.98234363 | -0.017656374 | ratio | 1.7656374 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0408994 | 0.24355372 | %p | -30.545562 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1681.6964 | 350 | price | -26.282266 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2794.4083 | -78.782133 | price | 2.741974 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2628227 | 0.26282266 | ratio | -26.282266 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4576913 | 0.0080073088 | %p | -0.23211716 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 369.85375 | 1.6837945 | price | -0.45734162 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 551.58736 | -0.76706799 | price | 0.13887242 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0045734 | 0.0045734162 | ratio | -0.45734162 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7542722 | -0.57752906 | %p | 10.831781 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.59921 | -26.952381 | price | 10.800324 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 357.26432 | -52.792161 | price | 12.874363 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89199676 | -0.10800324 | ratio | 10.800324 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9397931 | -0.64680067 | %p | 7.5326805 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 959.84585 | -89.391304 | price | 8.5196472 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1709.8839 | -120.97471 | price | 6.6075396 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91480353 | -0.085196472 | ratio | 8.5196472 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3570825 | -0.27047547 | %p | 7.4561309 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.268775 | -6.7588933 | price | 7.0384853 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.13088 | -13.752005 | price | 8.8789699 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.92961515 | -0.070384853 | ratio | 7.0384853 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1428288 | 0.53552145 | %p | -8.1049877 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1415.5889 | 59.853755 | price | -4.4148559 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2284.7874 | 43.677972 | price | -1.9489442 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0441486 | 0.044148559 | ratio | -4.4148559 | worsened |
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
| mape | 4.6062595 | 4.5011413 | -0.10511818 | %p | 2.2820724 | improved |
| mae | 565.55167 | 557.9753 | -7.5763682 | price | 1.3396421 | improved |
| rmse | 926.40586 | 915.84853 | -10.557323 | price | 1.1396002 | improved |
| rmae | 1.0199316 | 0.99470404 | -0.025227523 | ratio | 2.4734526 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4264277 | -0.30338327 | %p | 6.4142788 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 128.74704 | -9.083004 | price | 6.5900032 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 191.58023 | -17.598714 | price | 8.4132338 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93113601 | -0.065690927 | ratio | 6.5900032 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7329145 | 0.00075819006 | %p | -0.013226961 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.51779 | -0.14624506 | price | 0.12221305 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.87209 | 2.1331016 | price | -1.1934171 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0325423 | -0.0012634454 | ratio | 0.12221305 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7343152 | 0.053876624 | %p | -2.0099929 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 493.7747 | 3.1699605 | price | -0.64613327 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 788.25789 | 9.1760325 | price | -1.1778008 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95305848 | 0.0061184943 | ratio | -0.64613327 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4251885 | -0.16581173 | %p | 3.6116689 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.860558 | -4.0956175 | price | 3.9780203 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.71298 | -6.3220921 | price | 3.8307568 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.98234363 | -0.040696754 | ratio | 3.9780203 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0408994 | -0.025771757 | %p | 2.4160921 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1681.6964 | -29.772321 | price | 1.7395773 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2794.4083 | -44.531898 | price | 1.5686099 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2628227 | -0.022356688 | ratio | 1.7395773 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4576913 | -0.081002208 | %p | 2.2890428 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 369.85375 | -8.2213439 | price | 2.1745267 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 551.58736 | -13.78667 | price | 2.4385042 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0045734 | -0.022330295 | ratio | 2.1745267 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7542722 | -0.024223544 | %p | 0.50692823 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.59921 | -2.6230159 | price | 1.1646346 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 357.26432 | -16.075333 | price | 4.3058199 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89199676 | -0.010510916 | ratio | 1.1646346 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9397931 | -0.1389389 | %p | 1.7198108 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 959.84585 | -4.2964427 | price | 0.4456233 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1709.8839 | 5.9136423 | price | -0.34705079 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91480353 | -0.0040948252 | ratio | 0.4456233 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3570825 | -0.2919208 | %p | 8.0000149 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.268775 | -7.8735178 | price | 8.105139 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.13088 | -14.030302 | price | 9.042405 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.92961515 | -0.081992179 | ratio | 8.105139 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1428288 | -0.074764355 | %p | 1.0358627 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1415.5889 | -12.822134 | price | 0.89765017 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2284.7874 | -10.450993 | price | 0.45533367 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0441486 | -0.0094576984 | ratio | 0.89765017 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 8, 'worsened': 2, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T062737690863Z-ddfade71413c4456b57b0f07faa038b0

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062737690863Z-ddfade71413c4456b57b0f07faa038b0 | national_weather | 4.6210401 | 569.84518 | 929.25162 | 1.0259097 | -0.32088125 (direct) | -0.30281078 (direct) | 5 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6210401 | 0.013950763 | %p | -0.30281078 | worsened |
| mae | 532.31701 | 569.84518 | 37.528171 | price | -7.0499665 | worsened |
| rmse | 943.1701 | 929.25162 | -13.918476 | price | 1.4757122 | improved |
| rmae | 1 | 1.0259097 | 0.025909733 | ratio | -2.5909733 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7231356 | -0.045360937 | %p | 0.95126288 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.54545 | -0.72332016 | price | 0.52312618 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 206.43594 | -4.3501074 | price | 2.0637549 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99476874 | -0.0052312618 | ratio | 0.52312618 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8595996 | 0.35753778 | %p | -6.4982509 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 122.41107 | 6.6600791 | price | -5.7537989 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 182.78387 | 11.647784 | price | -6.8061531 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.057538 | 0.057537989 | ratio | -5.7537989 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6076633 | -0.28574003 | %p | 9.8755684 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 475.56917 | -42.525692 | price | 8.2080898 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 759.36063 | -69.102846 | price | 8.3410854 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.9179191 | -0.082080898 | ratio | 8.2080898 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6295193 | 0.12287739 | %p | -2.7265842 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 103.51394 | 2.876494 | price | -2.858274 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.93674 | 6.0736456 | price | -3.8231949 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0285827 | 0.02858274 | ratio | -2.858274 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1189229 | 0.32157724 | %p | -40.330969 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1781.4018 | 449.70536 | price | -33.76936 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2892.6796 | 19.48922 | price | -0.67831287 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3376936 | 0.3376936 | ratio | -33.76936 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5556084 | 0.10592439 | %p | -3.0705534 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 379.73913 | 11.56917 | price | -3.1423449 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 574.06736 | 21.712929 | price | -3.9309777 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0314234 | 0.031423449 | ratio | -3.1423449 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7466166 | -0.58518467 | %p | 10.975365 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 223.61508 | -25.936508 | price | 10.393245 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 370.59867 | -39.457812 | price | 9.6225309 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89606755 | -0.10393245 | ratio | 10.393245 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0174615 | -0.56913225 | %p | 6.6281492 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 952.86561 | -96.371542 | price | 9.1849151 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1695.3055 | -135.55309 | price | 7.4037987 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.90815085 | -0.091849151 | ratio | 9.1849151 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7572296 | 0.12967167 | %p | -3.5746272 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.675889 | 3.6482213 | price | -3.7991356 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 156.6686 | 1.7857205 | price | -1.1529489 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0379914 | 0.037991356 | ratio | -3.7991356 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1946444 | 0.58733705 | %p | -8.8892044 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1422.1146 | 66.379447 | price | -4.8961956 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2289.6792 | 48.569791 | price | -2.1672208 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.048962 | 0.048961956 | ratio | -4.8961956 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.6210401 | 0.014780623 | %p | -0.32088125 | worsened |
| mae | 565.55167 | 569.84518 | 4.2935045 | price | -0.75917104 | worsened |
| rmse | 926.40586 | 929.25162 | 2.8457649 | price | -0.30718338 | worsened |
| rmae | 1.0199316 | 1.0259097 | 0.0059781643 | ratio | -0.58613386 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7231356 | -0.0066754085 | %p | 0.14113478 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.54545 | -0.28458498 | price | 0.20647529 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 206.43594 | -2.743 | price | 1.3113175 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99476874 | -0.0020582014 | ratio | 0.20647529 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8595996 | 0.12744322 | %p | -2.2233033 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 122.41107 | 2.7470356 | price | -2.2956235 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 182.78387 | 4.0448899 | price | -2.2630149 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.057538 | 0.023732286 | ratio | -2.2956235 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6076633 | -0.072775222 | %p | 2.7150491 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 475.56917 | -15.035573 | price | 3.0647019 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 759.36063 | -19.721224 | price | 2.5313417 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.9179191 | -0.029020888 | ratio | 3.0647019 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6295193 | 0.038519056 | %p | -0.83901228 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 103.51394 | 0.55776892 | price | -0.54175373 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.93674 | -0.098330265 | price | 0.059581437 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0285827 | 0.0055423595 | ratio | -0.54175373 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1189229 | 0.052251761 | %p | -4.8985821 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1781.4018 | 69.933036 | price | -4.0861416 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2892.6796 | 53.739456 | price | -1.8929407 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3376936 | 0.052514247 | ratio | -4.0861416 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5556084 | 0.016914874 | %p | -0.4779977 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 379.73913 | 1.6640316 | price | -0.44013256 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 574.06736 | 8.6933278 | price | -1.5376242 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0314234 | 0.0045197376 | ratio | -0.44013256 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7466166 | -0.031879158 | %p | 0.66713794 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 223.61508 | -1.6071429 | price | 0.71358094 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 370.59867 | -2.7409839 | price | 0.73417969 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89606755 | -0.0064401228 | ratio | 0.71358094 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0174615 | -0.061270482 | %p | 0.75841707 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 952.86561 | -11.27668 | price | 1.1696074 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1695.3055 | -8.6647345 | price | 0.50850268 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.90815085 | -0.010747503 | ratio | 1.1696074 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7572296 | 0.10822633 | %p | -2.965915 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.675889 | 2.5335968 | price | -2.6081296 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 156.6686 | 1.5074227 | price | -0.9715205 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0379914 | 0.02638403 | ratio | -2.6081296 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1946444 | -0.022948748 | %p | 0.31795569 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1422.1146 | -6.2964427 | price | 0.44080047 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2289.6792 | -5.5591751 | price | 0.24220469 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.048962 | -0.0046443013 | ratio | 0.44080047 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T062819453310Z-8e480d549da449c89f3af1e4f016ae57

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062819453310Z-8e480d549da449c89f3af1e4f016ae57 | event | 4.6485779 | 572.60405 | 932.80398 | 1.0326247 | -0.9187149 (direct) | -0.90053675 (direct) | 0 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6485779 | 0.041488533 | %p | -0.90053675 | worsened |
| mae | 532.31701 | 572.60405 | 40.287045 | price | -7.5682432 | worsened |
| rmse | 943.1701 | 932.80398 | -10.366112 | price | 1.0990713 | improved |
| rmae | 1 | 1.0326247 | 0.032624673 | ratio | -3.2624673 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7500886 | -0.018407968 | %p | 0.38603296 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 138.58498 | 0.31620553 | price | -0.22868904 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 210.48395 | -0.30209799 | price | 0.14331973 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0022869 | 0.0022868904 | ratio | -0.22868904 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7943643 | 0.2923025 | %p | -5.3125994 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.19763 | 5.4466403 | price | -4.7054806 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.93257 | 7.7964829 | price | -4.5557211 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0470548 | 0.047054806 | ratio | -4.7054806 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7714058 | -0.12199756 | %p | 4.2164035 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 509.63241 | -8.4624506 | price | 1.6333786 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 788.28257 | -40.18091 | price | 4.8500521 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.98366621 | -0.016333786 | ratio | 1.6333786 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6214755 | 0.11483357 | %p | -2.5480961 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 103.64542 | 3.0079681 | price | -2.9889153 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 165.48992 | 6.6268239 | price | -4.1714056 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0298892 | 0.029889153 | ratio | -2.9889153 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0795498 | 0.28220414 | %p | -35.392948 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1731.0223 | 399.32589 | price | -29.986255 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2863.7978 | -9.392636 | price | 0.32690614 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2998626 | 0.29986255 | ratio | -29.986255 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5917466 | 0.14206258 | %p | -4.1181331 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 382.94071 | 14.770751 | price | -4.0119381 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 573.20131 | 20.846875 | price | -3.7741845 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0401194 | 0.040119381 | ratio | -4.0119381 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8191485 | -0.51265278 | %p | 9.6150017 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 227.30952 | -22.242063 | price | 8.9128119 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 375.71833 | -34.338158 | price | 8.3740067 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91087188 | -0.089128119 | ratio | 8.9128119 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.1276836 | -0.45891011 | %p | 5.3444955 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 970.4664 | -78.770751 | price | 7.5074306 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1703.4231 | -127.43551 | price | 6.9604233 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92492569 | -0.075074306 | ratio | 7.5074306 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.68927 | 0.061712077 | %p | -1.7012017 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 98.256917 | 2.229249 | price | -2.3214653 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.76065 | 0.87776473 | price | -0.56672804 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0232147 | 0.023214653 | ratio | -2.3214653 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2410462 | 0.63373889 | %p | -9.591485 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1442.9842 | 87.249012 | price | -6.4355498 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2312.9497 | 71.840247 | price | -3.2055662 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0643555 | 0.064355498 | ratio | -6.4355498 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.6485779 | 0.042318393 | %p | -0.9187149 | worsened |
| mae | 565.55167 | 572.60405 | 7.0523792 | price | -1.2469911 | worsened |
| rmse | 926.40586 | 932.80398 | 6.398129 | price | -0.69063996 | worsened |
| rmae | 1.0199316 | 1.0326247 | 0.012693104 | ratio | -1.2445055 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7500886 | 0.020277561 | %p | -0.4287182 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 138.58498 | 0.75494071 | price | -0.54773307 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 210.48395 | 1.3050094 | price | -0.62387227 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0022869 | 0.0054599508 | ratio | -0.54773307 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7943643 | 0.062207945 | %p | -1.0852451 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.19763 | 1.5335968 | price | -1.2815855 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.93257 | 0.19358852 | price | -0.10830794 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0470548 | 0.013249104 | ratio | -1.2815855 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7714058 | 0.090967248 | %p | -3.3937449 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 509.63241 | 19.027668 | price | -3.8784109 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 788.28257 | 9.2007125 | price | -1.1809687 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.98366621 | 0.036726224 | ratio | -3.8784109 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6214755 | 0.030475235 | %p | -0.66380383 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 103.64542 | 0.68924303 | price | -0.66945283 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 165.48992 | 0.45484805 | price | -0.27560691 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0298892 | 0.0068487728 | ratio | -0.66945283 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0795498 | 0.012878662 | %p | -1.2073695 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1731.0223 | 19.553571 | price | -1.1425024 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2863.7978 | 24.857599 | price | -0.87559433 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2998626 | 0.014683205 | ratio | -1.1425024 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5917466 | 0.053053064 | %p | -1.4992274 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 382.94071 | 4.8656126 | price | -1.2869434 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 573.20131 | 7.8272736 | price | -1.3844416 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0401194 | 0.01321567 | ratio | -1.2869434 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8191485 | 0.04065273 | %p | -0.85074325 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 227.30952 | 2.0873016 | price | -0.92677426 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 375.71833 | 2.3786702 | price | -0.63713301 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.91087188 | 0.0083642088 | ratio | -0.92677426 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.1276836 | 0.048951653 | %p | -0.60593238 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 970.4664 | 6.3241107 | price | -0.65593126 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1703.4231 | -0.54715941 | price | 0.032110855 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92492569 | 0.0060273415 | ratio | -0.65593126 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.68927 | 0.040266739 | %p | -1.1034997 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 98.256917 | 1.1146245 | price | -1.1474142 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 155.76065 | 0.59946692 | price | -0.3863511 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0232147 | 0.011607327 | ratio | -1.1474142 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2410462 | 0.023453089 | %p | -0.32494335 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1442.9842 | 14.573123 | price | -1.0202331 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2312.9497 | 17.711281 | price | -0.77165322 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0643555 | 0.01074924 | ratio | -1.0202331 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 0, 'worsened': 10, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T062853475873Z-d8133cf0780a431984500e2b31cce971

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062853475873Z-d8133cf0780a431984500e2b31cce971 | macro | 4.6044063 | 567.52067 | 929.91525 | 1.0207438 | 0.040232141 (direct) | 0.058237562 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6044063 | -0.0026830565 | %p | 0.058237562 | improved |
| mae | 532.31701 | 567.52067 | 35.203662 | price | -6.613289 | worsened |
| rmse | 943.1701 | 929.91525 | -13.254846 | price | 1.4053505 | improved |
| rmae | 1 | 1.0207438 | 0.020743802 | ratio | -2.0743802 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7212194 | -0.047277186 | %p | 0.99144847 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.66008 | -0.60869565 | price | 0.4402264 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.73386 | -2.0521858 | price | 0.9735871 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99559774 | -0.004402264 | ratio | 0.4402264 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7617093 | 0.25964749 | %p | -4.7190944 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 120.36364 | 4.6126482 | price | -3.9849752 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.12762 | 8.9915328 | price | -5.2540249 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0398498 | 0.039849752 | ratio | -3.9849752 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6675295 | -0.22587386 | %p | 7.8065112 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 487.86957 | -30.225296 | price | 5.8339309 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 773.03746 | -55.426022 | price | 6.6902191 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94166069 | -0.058339309 | ratio | 5.8339309 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5871734 | 0.080531466 | %p | -1.7869506 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.8247 | 2.187251 | price | -2.1733967 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.84484 | 5.9817461 | price | -3.7653466 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.021734 | 0.021733967 | ratio | -2.1733967 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.080293 | 0.2829473 | %p | -35.486152 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1735.4062 | 403.70982 | price | -30.315454 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2879.2952 | 6.1047671 | price | -0.21247346 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3031545 | 0.30315454 | ratio | -30.315454 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5228175 | 0.07313344 | %p | -2.120004 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 376.26482 | 8.0948617 | price | -2.1986752 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 563.40851 | 11.054079 | price | -2.0012655 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0219868 | 0.021986752 | ratio | -2.1986752 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7682384 | -0.56356283 | %p | 10.569839 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 224.85714 | -24.694444 | price | 9.8955269 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 372.72672 | -37.329768 | price | 9.1035672 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90104473 | -0.098955269 | ratio | 9.8955269 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0569359 | -0.52965785 | %p | 6.168428 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 961.19368 | -88.043478 | price | 8.3911895 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1701.8576 | -129.00104 | price | 7.0459314 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.9160881 | -0.083911895 | ratio | 8.3911895 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6433939 | 0.015836019 | %p | -0.43654764 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.011858 | 0.98418972 | price | -1.0249022 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.15885 | 0.27596693 | price | -0.17817781 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.010249 | 0.010249022 | ratio | -1.0249022 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2347528 | 0.62744545 | %p | -9.4962354 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1431.7549 | 76.019763 | price | -5.6072723 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2299.9619 | 58.852464 | price | -2.6260415 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0560727 | 0.056072723 | ratio | -5.6072723 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.6044063 | -0.0018531968 | %p | 0.040232141 | improved |
| mae | 565.55167 | 567.52067 | 1.9689958 | price | -0.3481549 | worsened |
| rmse | 926.40586 | 929.91525 | 3.5093947 | price | -0.37881828 | worsened |
| rmae | 1.0199316 | 1.0207438 | 0.00081223386 | ratio | -0.079636114 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7212194 | -0.0085916571 | %p | 0.18164906 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.66008 | -0.16996047 | price | 0.12331163 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.73386 | -0.44507837 | price | 0.21277399 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99559774 | -0.0012292036 | ratio | 0.12331163 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7617093 | 0.029552936 | %p | -0.51556402 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 120.36364 | 0.69960474 | price | -0.58464079 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.12762 | 1.3886384 | price | -0.77690855 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0398498 | 0.0060440499 | ratio | -0.58464079 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6675295 | -0.012909051 | %p | 0.48160218 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 487.86957 | -2.7351779 | price | 0.5575115 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 773.03746 | -6.044399 | price | 0.77583619 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94166069 | -0.0052792993 | ratio | 0.5575115 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5871734 | -0.0038268667 | %p | 0.083355838 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.8247 | -0.1314741 | price | 0.12769909 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.84484 | -0.1902298 | price | 0.11526629 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.021734 | -0.0013064133 | ratio | 0.12769909 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.080293 | 0.013621822 | %p | -1.2770405 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1735.4062 | 23.9375 | price | -1.3986525 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2879.2952 | 40.355002 | price | -1.4214812 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3031545 | 0.017975193 | ratio | -1.3986525 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5228175 | -0.015876077 | %p | 0.44864233 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 376.26482 | -1.8102767 | price | 0.47881405 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 563.40851 | -1.9655231 | price | 0.34765006 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0219868 | -0.0049169592 | ratio | 0.47881405 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7682384 | -0.01025732 | %p | 0.21465583 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 224.85714 | -0.36507937 | price | 0.1620974 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 372.72672 | -0.61293963 | price | 0.16417748 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90104473 | -0.0014629415 | ratio | 0.1620974 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0569359 | -0.021796089 | %p | 0.26979592 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 961.19368 | -2.9486166 | price | 0.30582795 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1701.8576 | -2.1126912 | price | 0.12398639 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.9160881 | -0.002810248 | ratio | 0.30582795 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6433939 | -0.0056093195 | %p | 0.15372196 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.011858 | -0.13043478 | price | 0.13427188 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 155.15885 | -0.0023308845 | price | 0.0015022343 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.010249 | -0.0013583042 | ratio | 0.13427188 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2347528 | 0.017159654 | %p | -0.2377476 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1431.7549 | 3.3438735 | price | -0.23409742 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2299.9619 | 4.7234988 | price | -0.20579557 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0560727 | 0.0024664651 | ratio | -0.23409742 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T062928037752Z-f4d0d7b7969b402aa9eb57f5cc9596f9

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062928037752Z-f4d0d7b7969b402aa9eb57f5cc9596f9 | production | 4.6070909 | 568.42594 | 928.85113 | 1.021895 | -0.018048907 (direct) | -3.2987938e-05 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6070909 | 1.5197838e-06 | %p | -3.2987938e-05 | worsened |
| mae | 532.31701 | 568.42594 | 36.108936 | price | -6.783352 | worsened |
| rmse | 943.1701 | 928.85113 | -14.318964 | price | 1.5181741 | improved |
| rmae | 1 | 1.021895 | 0.021894961 | ratio | -2.1894961 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7259855 | -0.042511046 | %p | 0.89149788 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.71937 | -0.54940711 | price | 0.39734721 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.07577 | -1.7102841 | price | 0.81138393 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99602653 | -0.0039734721 | ratio | 0.39734721 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7351679 | 0.23310615 | %p | -4.2367054 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.71937 | 3.9683794 | price | -3.4283763 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.81911 | 7.6830163 | price | -4.4894191 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0342838 | 0.034283763 | ratio | -3.4283763 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6785051 | -0.2148983 | %p | 7.4271808 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 490.20158 | -27.893281 | price | 5.3838173 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 778.86814 | -49.595337 | price | 5.9864241 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94616183 | -0.053838173 | ratio | 5.3838173 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5906037 | 0.083961805 | %p | -1.863068 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.94422 | 2.3067729 | price | -2.2921615 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 165.04602 | 6.1829233 | price | -3.8919822 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0229216 | 0.022921615 | ratio | -2.2921615 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0866032 | 0.28925749 | %p | -36.277551 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1741.0223 | 409.32589 | price | -30.737177 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2864.0397 | -9.1506988 | price | 0.31848564 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3073718 | 0.30737177 | ratio | -30.737177 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5414678 | 0.091783722 | %p | -2.6606414 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 378.39526 | 10.225296 | price | -2.7773305 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 565.37581 | 13.021381 | price | -2.3574321 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0277733 | 0.027773305 | ratio | -2.7773305 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7760186 | -0.55578268 | %p | 10.42392 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 225.09524 | -24.456349 | price | 9.8001177 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 373.24115 | -36.815341 | price | 8.9781144 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90199882 | -0.098001177 | ratio | 9.8001177 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0771641 | -0.50942959 | %p | 5.9328484 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 963.93676 | -85.300395 | price | 8.1297536 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1703.9284 | -126.93017 | price | 6.9328222 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91870246 | -0.081297536 | ratio | 8.1297536 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6437059 | 0.016148026 | %p | -0.44514867 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.011858 | 0.98418972 | price | -1.0249022 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.00598 | 0.12309653 | price | -0.079477171 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.010249 | 0.010249022 | ratio | -1.0249022 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2156869 | 0.60837963 | %p | -9.2076787 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1428.2134 | 72.478261 | price | -5.3460486 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2295.1112 | 54.001777 | price | -2.4096002 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0534605 | 0.053460486 | ratio | -5.3460486 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.6070909 | 0.00083137949 | %p | -0.018048907 | worsened |
| mae | 565.55167 | 568.42594 | 2.8742698 | price | -0.50822409 | worsened |
| rmse | 926.40586 | 928.85113 | 2.445277 | price | -0.2639531 | worsened |
| rmae | 1.0199316 | 1.021895 | 0.0019633924 | ratio | -0.19250237 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7259855 | -0.0038255167 | %p | 0.080880962 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.71937 | -0.11067194 | price | 0.080295948 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.07577 | -0.10317672 | price | 0.049324622 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99602653 | -0.00080041164 | ratio | 0.080295948 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7351679 | 0.0030115949 | %p | -0.052538603 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.71937 | 0.055335968 | price | -0.046242775 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.81911 | 0.080121866 | price | -0.044826184 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0342838 | 0.00047806044 | ratio | -0.046242775 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6785051 | -0.0019334925 | %p | 0.07213344 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 490.20158 | -0.40316206 | price | 0.082176551 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 778.86814 | -0.21371451 | price | 0.027431586 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94616183 | -0.00077816262 | ratio | 0.082176551 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5906037 | -0.00039652709 | %p | 0.0086370522 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.94422 | -0.011952191 | price | 0.011609009 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 165.04602 | 0.010947449 | price | -0.0066334077 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0229216 | -0.00011876485 | ratio | 0.011609009 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0866032 | 0.019932011 | %p | -1.8686182 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1741.0223 | 29.553571 | price | -1.7267959 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2864.0397 | 25.099536 | price | -0.88411642 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3073718 | 0.022192424 | ratio | -1.7267959 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5414678 | 0.0027742053 | %p | -0.078396314 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 378.39526 | 0.3201581 | price | -0.084681087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 565.37581 | 0.0017792244 | price | -0.00031469864 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0277733 | 0.00086959322 | ratio | -0.084681087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7760186 | -0.0024771713 | %p | 0.051839981 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 225.09524 | -0.12698413 | price | 0.056381704 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 373.24115 | -0.098512604 | price | 0.026386858 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90199882 | -0.00050884921 | ratio | 0.056381704 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0771641 | -0.0015678237 | %p | 0.019406805 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 963.93676 | -0.2055336 | price | 0.021317766 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1703.9284 | -0.041821002 | price | 0.002454327 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91870246 | -0.0001958886 | ratio | 0.021317766 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6437059 | -0.0052973123 | %p | 0.14517149 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.011858 | -0.13043478 | price | 0.13427188 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 155.00598 | -0.15520128 | price | 0.10002584 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.010249 | -0.0013583042 | ratio | 0.13427188 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2156869 | -0.0019061729 | %p | 0.02641009 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1428.2134 | -0.19762846 | price | 0.013835545 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2295.1112 | -0.12718898 | price | 0.0055414281 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0534605 | -0.00014577217 | ratio | 0.013835545 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


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


## ridge-v2-20261117T063413283030Z-d27ee144542a46ee82a0211d9b9ff9e4

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T063413283030Z-d27ee144542a46ee82a0211d9b9ff9e4 | no_series_id | 4.6472089 | 577.16884 | 935.57139 | 1.0334384 | -0.88899391 (direct) | -0.87082111 (direct) | 4 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6472089 | 0.040119507 | %p | -0.87082111 | worsened |
| mae | 532.31701 | 577.16884 | 44.851832 | price | -8.4257748 | worsened |
| rmse | 943.1701 | 935.57139 | -7.5987035 | price | 0.80565568 | improved |
| rmae | 1 | 1.0334384 | 0.033438382 | ratio | -3.3438382 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7275609 | -0.040935673 | %p | 0.85846078 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.19368 | -1.0750988 | price | 0.77754274 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 211.01816 | 0.23211039 | price | -0.11011658 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 0.99222457 | -0.0077754274 | ratio | 0.77754274 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.4877337 | -0.014328087 | %p | 0.26041305 | improved |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 115.32016 | -0.43083004 | price | 0.3722042 | improved |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 173.61663 | 2.4805429 | price | -1.4494563 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 0.99627796 | -0.003722042 | ratio | 0.3722042 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7407721 | -0.15263122 | %p | 5.275145 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 500.34783 | -17.747036 | price | 3.4254413 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 790.03977 | -38.423706 | price | 4.6379481 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.96574559 | -0.034254413 | ratio | 3.4254413 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5609501 | 0.0543082 | %p | -1.2050702 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.09163 | 1.4541833 | price | -1.4449723 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 163.75332 | 4.8902326 | price | -3.0782686 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0144497 | 0.014449723 | ratio | -1.4449723 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1243898 | 0.32704412 | %p | -41.016605 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1794.875 | 463.17857 | price | -34.781093 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2871.0216 | -2.1687965 | price | 0.07548391 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3478109 | 0.34781093 | ratio | -34.781093 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4951859 | 0.045501897 | %p | -1.3190164 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 373.32806 | 5.1581028 | price | -1.4010113 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 554.72073 | 2.3662929 | price | -0.42840117 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0140101 | 0.014010113 | ratio | -1.4010113 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0007314 | -0.33106986 | %p | 6.2093436 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 235.59921 | -13.952381 | price | 5.5909806 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 399.48599 | -10.570492 | price | 2.5778135 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.94409019 | -0.055909806 | ratio | 5.5909806 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.2079508 | -0.37864291 | %p | 4.4096987 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 979.44269 | -69.794466 | price | 6.6519248 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1722.0024 | -108.85625 | price | 5.9456395 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.93348075 | -0.066519248 | ratio | 6.6519248 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8719777 | 0.24441974 | %p | -6.7378589 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 102.8498 | 6.8221344 | price | -7.1043425 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 161.89091 | 7.0080306 | price | -4.5247289 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0710434 | 0.071043425 | ratio | -7.1043425 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2548362 | 0.64752886 | %p | -9.8001929 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1430.6403 | 74.905138 | price | -5.5250568 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2308.1644 | 67.055003 | price | -2.992045 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0552506 | 0.055250568 | ratio | -5.5250568 | worsened |
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
| mape | 4.6062595 | 4.6472089 | 0.040949366 | %p | -0.88899391 | worsened |
| mae | 565.55167 | 577.16884 | 11.617166 | price | -2.0541298 | worsened |
| rmse | 926.40586 | 935.57139 | 9.1655374 | price | -0.98936523 | worsened |
| rmae | 1.0199316 | 1.0334384 | 0.013506814 | ratio | -1.3242863 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7275609 | -0.0022501438 | %p | 0.047573652 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.19368 | -0.63636364 | price | 0.4617017 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 211.01816 | 1.8392178 | price | -0.87925571 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99222457 | -0.0046023669 | ratio | 0.4617017 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.4877337 | -0.24442264 | %p | 4.264061 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 115.32016 | -4.3438735 | price | 3.6300578 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 173.61663 | -5.1223515 | price | 2.8658278 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 0.99627796 | -0.037527745 | ratio | 3.6300578 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7407721 | 0.060333585 | %p | -2.2508848 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 500.34783 | 9.743083 | price | -1.9859333 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 790.03977 | 10.957917 | price | -1.4065167 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.96574559 | 0.018805597 | ratio | -1.9859333 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5609501 | -0.030050132 | %p | 0.65454433 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.09163 | -0.86454183 | price | 0.83971829 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 163.75332 | -1.2817433 | price | 0.77664904 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0144497 | -0.0085906572 | ratio | 0.83971829 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1243898 | 0.057718649 | %p | -5.4111006 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1794.875 | 83.40625 | price | -4.8733727 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2871.0216 | 32.081439 | price | -1.1300498 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3478109 | 0.062631579 | ratio | -4.8733727 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4951859 | -0.04350762 | %p | 1.2294825 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 373.32806 | -4.7470356 | price | 1.2555801 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 554.72073 | -10.653309 | price | 1.884294 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0140101 | -0.012893598 | ratio | 1.2555801 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0007314 | 0.22223565 | %p | -4.650745 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 235.59921 | 10.376984 | price | -4.6074424 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 399.48599 | 26.146336 | price | -7.0033643 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.94409019 | 0.041582521 | ratio | -4.6074424 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.2079508 | 0.12921885 | %p | -1.5994942 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 979.44269 | 15.300395 | price | -1.5869437 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1722.0024 | 18.032098 | price | -1.0582402 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.93348075 | 0.014582399 | ratio | -1.5869437 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8719777 | 0.2229744 | %p | -6.1105563 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 102.8498 | 5.7075099 | price | -5.875412 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 161.89091 | 6.7297328 | price | -4.3372529 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0710434 | 0.059436098 | ratio | -5.875412 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2548362 | 0.037243061 | %p | -0.51600389 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1430.6403 | 2.229249 | price | -0.15606495 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2308.1644 | 12.926037 | price | -0.56316752 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0552506 | 0.0016443101 | ratio | -0.15606495 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


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


## ridge-v2-20261117T064002676983Z-535e898c61dd487990bea2b1b582eb71

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064002676983Z-535e898c61dd487990bea2b1b582eb71 | all_no_series_id | 4.99971 | 676.76725 | 1031.5212 | 1.1624391 | -8.541649 (direct) | -8.5220978 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.99971 | 0.39262066 | %p | -8.5220978 | worsened |
| mae | 532.31701 | 676.76725 | 144.45024 | price | -27.136132 | worsened |
| rmse | 943.1701 | 1031.5212 | 88.351141 | price | -9.3674663 | worsened |
| rmae | 1 | 1.1624391 | 0.16243906 | ratio | -16.243906 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.0785968 | 0.31010021 | %p | -6.5031024 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 145.96047 | 7.6916996 | price | -5.5628609 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.28502 | -1.5010259 | price | 0.71210873 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0556286 | 0.055628609 | ratio | -5.5628609 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.0177235 | 0.5156617 | %p | -9.3721539 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 125.67589 | 9.9249012 | price | -8.5743555 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 184.4605 | 13.32441 | price | -7.7858561 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0857436 | 0.085743555 | ratio | -8.5743555 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.6649194 | 0.77151603 | %p | -26.664655 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 674.10672 | 156.01186 | price | -30.112605 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1010.667 | 182.20351 | price | -21.992944 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.301126 | 0.30112605 | ratio | -30.112605 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.7464128 | 0.23977086 | %p | -5.3203886 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 104.69721 | 4.059761 | price | -4.0340459 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 161.96814 | 3.1050444 | price | -1.9545411 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0403405 | 0.040340459 | ratio | -4.0340459 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.5757649 | 0.77841927 | %p | -97.626325 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2426.8214 | 1095.125 | price | -82.235334 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3474.6059 | 601.41544 | price | -20.931973 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.8223533 | 0.82235334 | ratio | -82.235334 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0093445 | 0.55966051 | %p | -16.22353 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 429.70751 | 61.537549 | price | -16.714441 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 596.61225 | 44.257815 | price | -8.0125754 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1671444 | 0.16714441 | ratio | -16.714441 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.1050161 | -0.22678512 | %p | 4.2534429 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 248.92063 | -0.63095238 | price | 0.25283445 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 391.35466 | -18.701828 | price | 4.5607931 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.99747166 | -0.0025283445 | ratio | 0.25283445 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8999287 | 0.31333498 | %p | -3.6491185 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1089.9368 | 40.699605 | price | -3.878971 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1860.0567 | 29.198078 | price | -1.5947751 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0387897 | 0.03878971 | ratio | -3.878971 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8492952 | 0.22173725 | %p | -6.1125764 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 102.65217 | 6.6245059 | price | -6.8985388 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 146.4542 | -8.4286788 | price | 5.4419692 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0689854 | 0.068985388 | ratio | -6.8985388 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0500982 | 0.44279089 | %p | -6.7015332 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1419.1937 | 63.458498 | price | -4.6807444 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2279.7481 | 38.638645 | price | -1.7240856 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0468074 | 0.046807444 | ratio | -4.6807444 | worsened |
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
| mape | 4.6062595 | 4.99971 | 0.39345052 | %p | -8.541649 | worsened |
| mae | 565.55167 | 676.76725 | 111.21558 | price | -19.664972 | worsened |
| rmse | 926.40586 | 1031.5212 | 105.11538 | price | -11.34658 | worsened |
| rmae | 1.0199316 | 1.1624391 | 0.14250749 | ratio | -13.97226 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.0785968 | 0.34878574 | %p | -7.3742004 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 145.96047 | 8.1304348 | price | -5.8988845 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.28502 | 0.10608155 | price | -0.0507133 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0556286 | 0.058801669 | ratio | -5.8988845 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.0177235 | 0.28556714 | %p | -4.981845 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 125.67589 | 6.0118577 | price | -5.0239472 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 184.4605 | 5.7215152 | price | -3.201045 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0857436 | 0.051937852 | ratio | -5.0239472 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.6649194 | 0.98448084 | %p | -36.728349 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 674.10672 | 183.50198 | price | -37.403221 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1010.667 | 231.58513 | price | -29.725392 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.301126 | 0.35418606 | ratio | -37.403221 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.7464128 | 0.15541253 | %p | -3.3851562 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 104.69721 | 1.7410359 | price | -1.6910456 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 161.96814 | -3.0669315 | price | 1.8583514 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0403405 | 0.017300079 | ratio | -1.6910456 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.5757649 | 0.5090938 | %p | -47.727343 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2426.8214 | 715.35268 | price | -41.797589 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3474.6059 | 635.66567 | price | -22.39095 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.8223533 | 0.53717399 | ratio | -41.797589 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0093445 | 0.470651 | %p | -13.300134 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 429.70751 | 51.632411 | price | -13.656655 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 596.61225 | 31.238213 | price | -5.5252296 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1671444 | 0.14024069 | ratio | -13.656655 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.1050161 | 0.32652039 | %p | -6.8331208 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 248.92063 | 23.698413 | price | -10.522236 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 391.35466 | 18.015 | price | -4.8253647 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.99747166 | 0.094963983 | ratio | -10.522236 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8999287 | 0.82119675 | %p | -10.164921 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1089.9368 | 125.79447 | price | -13.047293 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1860.0567 | 156.08643 | price | -9.1601616 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0387897 | 0.11989136 | ratio | -13.047293 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8492952 | 0.20029191 | %p | -5.4889486 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 102.65217 | 5.5098814 | price | -5.6719697 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 146.4542 | -8.7069766 | price | 5.6115689 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0689854 | 0.057378061 | ratio | -5.6719697 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0500982 | -0.16749491 | %p | 2.3206477 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1419.1937 | -9.2173913 | price | 0.64528983 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2279.7481 | -15.490321 | price | 0.67488941 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0468074 | -0.006798814 | ratio | 0.64528983 | improved |
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
| mape | 4.99034 | 4.99971 | 0.0093699704 | %p | -0.18776216 | worsened |
| mae | 674.96363 | 676.76725 | 1.8036143 | price | -0.26721652 | worsened |
| rmse | 1034.3299 | 1031.5212 | -2.8086352 | price | 0.27154153 | improved |
| rmae | 1.1614981 | 1.1624391 | 0.00094097072 | ratio | -0.08101354 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.0785968 | -0.05536881 | %p | 1.0784804 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 145.96047 | -2.8537549 | price | 1.9176627 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 209.28502 | -0.53688412 | price | 0.2558761 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0556286 | -0.020639186 | ratio | 1.9176627 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.0177235 | -0.13889247 | %p | 2.2559873 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 125.67589 | -2.1897233 | price | 1.7125193 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 184.4605 | -2.6030795 | price | 1.391548 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0857436 | -0.018917535 | ratio | 1.7125193 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.6649194 | 0.070030033 | %p | -1.9480442 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 674.10672 | 11.27668 | price | -1.7012928 | worsened |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1010.667 | 8.6935904 | price | -0.86764682 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.301126 | 0.021765666 | ratio | -1.7012928 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.7464128 | -0.091274215 | %p | 1.8867326 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 104.69721 | -2.3266932 | price | 2.173994 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 161.96814 | -2.6663008 | price | 1.619528 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0403405 | -0.023119557 | ratio | 2.173994 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.5757649 | 0.0018785886 | %p | -0.11935986 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2426.8214 | -5.5357143 | price | 0.22758641 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3474.6059 | -40.406376 | price | 1.1495373 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.8223533 | -0.004156889 | ratio | 0.22758641 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0093445 | -0.036759661 | %p | 0.90851987 | improved |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 429.70751 | -4.1264822 | price | 0.95116618 | improved |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 596.61225 | -10.133911 | price | 1.6702061 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1671444 | -0.01120809 | ratio | 0.95116618 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 5.1050161 | 0.11991251 | %p | -2.4054167 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 248.92063 | 6.3333333 | price | -2.610744 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 391.35466 | 11.864649 | price | -3.1264721 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.99747166 | 0.025378854 | ratio | -2.610744 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8999287 | 0.0942255 | %p | -1.0700508 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1089.9368 | 12.102767 | price | -1.1228786 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1860.0567 | 5.0658266 | price | -0.27309173 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0387897 | 0.011534825 | ratio | -1.1228786 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.8492952 | 0.10480542 | %p | -2.7989241 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 102.65217 | 2.5652174 | price | -2.5629887 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 146.4542 | 2.343575 | price | -1.6262333 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0689854 | 0.026713315 | ratio | -2.5629887 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.0500982 | 0.025142803 | %p | -0.35790694 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1419.1937 | 2.7905138 | price | -0.19701409 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2279.7481 | 0.29255855 | price | -0.012834581 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0468074 | 0.002058303 | ratio | -0.19701409 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T064226965751Z-89709e52dd9340109ab84989a3c0e5f8

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064226965751Z-89709e52dd9340109ab84989a3c0e5f8 | no_market | 5.1159489 | 708.31052 | 1082.6341 | 1.2056631 | -11.065147 (direct) | -11.045142 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 5.1159489 | 0.50885955 | %p | -11.045142 | worsened |
| mae | 532.31701 | 708.31052 | 175.99351 | price | -33.061787 | worsened |
| rmse | 943.1701 | 1082.6341 | 139.46401 | price | -14.78673 | worsened |
| rmae | 1 | 1.2056631 | 0.2056631 | ratio | -20.56631 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.3249966 | 0.55650005 | %p | -11.670346 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 153.92095 | 15.652174 | price | -11.320107 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 219.60399 | 8.8179414 | price | -4.183361 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.1132011 | 0.11320107 | ratio | -11.320107 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.2364602 | 0.73439841 | %p | -13.347695 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 129.25692 | 13.505929 | price | -11.668089 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 187.40951 | 16.273419 | price | -9.5090517 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1166809 | 0.11668089 | ratio | -11.668089 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.7873598 | 0.89395642 | %p | -30.896363 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 705.29644 | 187.20158 | price | -36.132684 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1038.3147 | 209.85123 | price | -25.330173 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.3613268 | 0.36132684 | ratio | -36.132684 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.9737326 | 0.46709065 | %p | -10.364494 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 110.65339 | 10.015936 | price | -9.9524941 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 171.19021 | 12.327117 | price | -7.759585 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0995249 | 0.099524941 | ratio | -9.9524941 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.7387363 | 0.94139062 | %p | -118.06556 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2673.8438 | 1342.1473 | price | -100.78478 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3873.188 | 999.99757 | price | -34.804431 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 2.0078478 | 1.0078478 | ratio | -100.78478 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.1482031 | 0.69851903 | %p | -20.248783 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 444.67589 | 76.505929 | price | -20.780057 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 623.66478 | 71.310348 | price | -12.910252 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.2078006 | 0.20780057 | ratio | -20.780057 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9844187 | -0.34738251 | %p | 6.5152936 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 241.8373 | -7.7142857 | price | 3.0912589 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 386.36172 | -23.694768 | price | 5.7784156 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.96908741 | -0.030912589 | ratio | 3.0912589 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.9496893 | 0.36309554 | %p | -4.2286331 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1090.4071 | 41.16996 | price | -3.9237993 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1866.2571 | 35.39852 | price | -1.9334382 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.039238 | 0.039237993 | ratio | -3.9237993 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.9103698 | 0.28281192 | %p | -7.7962068 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 104.48617 | 8.458498 | price | -8.8083968 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 153.42878 | -1.4541007 | price | 0.93883886 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.088084 | 0.088083968 | ratio | -8.8083968 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1055226 | 0.49821533 | %p | -7.5403686 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1428.7273 | 72.992095 | price | -5.3839493 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2306.9223 | 65.812864 | price | -2.9366199 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0538395 | 0.053839493 | ratio | -5.3839493 | worsened |
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
| mape | 4.6062595 | 5.1159489 | 0.50968941 | %p | -11.065147 | worsened |
| mae | 565.55167 | 708.31052 | 142.75885 | price | -25.242406 | worsened |
| rmse | 926.40586 | 1082.6341 | 156.22826 | price | -16.863911 | worsened |
| rmae | 1.0199316 | 1.2056631 | 0.18573153 | ratio | -18.210195 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.3249966 | 0.59518557 | %p | -12.583707 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 153.92095 | 16.090909 | price | -11.674457 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 219.60399 | 10.425049 | price | -4.9837946 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.1132011 | 0.11637414 | ratio | -11.674457 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.2364602 | 0.50430385 | %p | -8.7978035 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 129.25692 | 9.5928854 | price | -8.0165153 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 187.40951 | 8.6705248 | price | -4.8509422 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1166809 | 0.082875192 | ratio | -8.0165153 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.7873598 | 1.1069212 | %p | -41.296273 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 705.29644 | 214.6917 | price | -43.760625 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1038.3147 | 259.23285 | price | -33.274148 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.3613268 | 0.41438685 | ratio | -43.760625 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.9737326 | 0.38273232 | %p | -8.3365781 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 110.65339 | 7.6972112 | price | -7.4762015 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 171.19021 | 6.1551409 | price | -3.7295957 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0995249 | 0.076484561 | ratio | -7.4762015 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.7387363 | 0.67206514 | %p | -63.005843 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2673.8438 | 962.375 | price | -56.230942 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3873.188 | 1034.2478 | price | -36.430771 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 2.0078478 | 0.72266845 | ratio | -56.230942 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.1482031 | 0.60950952 | %p | -17.22414 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 444.67589 | 66.600791 | price | -17.615757 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 623.66478 | 58.290747 | price | -10.310121 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.2078006 | 0.18089686 | ratio | -17.615757 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9844187 | 0.205923 | %p | -4.3093688 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 241.8373 | 16.615079 | price | -7.3771936 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 386.36172 | 13.02206 | price | -3.4879927 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.96908741 | 0.066579738 | ratio | -7.3771936 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.9496893 | 0.87095731 | %p | -10.780867 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1090.4071 | 126.26482 | price | -13.096078 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1866.2571 | 162.28687 | price | -9.5240436 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.039238 | 0.12033964 | ratio | -13.096078 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.9103698 | 0.26136658 | %p | -7.1626842 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 104.48617 | 7.3438735 | price | -7.5599137 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 153.42878 | -1.7323985 | price | 1.1165154 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.088084 | 0.076476641 | ratio | -7.5599137 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1055226 | -0.11207047 | %p | 1.5527403 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1428.7273 | 0.31620553 | price | -0.022136872 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2306.9223 | 11.683898 | price | -0.50904945 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0538395 | 0.00023323547 | ratio | -0.022136872 | worsened |
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
| mape | 4.99034 | 5.1159489 | 0.12560886 | %p | -2.51704 | worsened |
| mae | 674.96363 | 708.31052 | 33.346886 | price | -4.9405455 | worsened |
| rmse | 1034.3299 | 1082.6341 | 48.304238 | price | -4.6700999 | worsened |
| rmae | 1.1614981 | 1.2056631 | 0.044165009 | ratio | -3.8024177 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.3249966 | 0.19103102 | %p | -3.7209253 | worsened |
| 1 | 대파/RETAIL | mae | 148.81423 | 153.92095 | 5.1067194 | price | -3.4316069 | worsened |
| 1 | 대파/RETAIL | rmse | 209.82191 | 219.60399 | 9.7820831 | price | -4.6620885 | worsened |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.1132011 | 0.03693328 | ratio | -3.4316069 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.2364602 | 0.079844238 | %p | -1.2968851 | worsened |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 129.25692 | 1.3913043 | price | -1.0880989 | worsened |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 187.40951 | 0.34593007 | price | -0.18492647 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1166809 | 0.012019805 | ratio | -1.0880989 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.7873598 | 0.19247042 | %p | -5.3540013 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 705.29644 | 42.466403 | price | -6.4068314 | worsened |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1038.3147 | 36.34131 | price | -3.6269735 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.3613268 | 0.081966463 | ratio | -6.4068314 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.9737326 | 0.13604558 | %p | -2.8122029 | worsened |
| 8 | 양파/RETAIL | mae | 107.0239 | 110.65339 | 3.6294821 | price | -3.3912817 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 171.19021 | 6.5557715 | price | -3.9820171 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0995249 | 0.036064925 | ratio | -3.3912817 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.7387363 | 0.16484993 | %p | -10.474068 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2673.8438 | 241.48661 | price | -9.92809 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3873.188 | 358.17576 | price | -10.189886 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 2.0078478 | 0.18133758 | ratio | -9.92809 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.1482031 | 0.10209886 | %p | -2.5233868 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 444.67589 | 10.841897 | price | -2.4990889 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 623.66478 | 16.918622 | price | -2.7884185 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.2078006 | 0.029448077 | ratio | -2.4990889 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9844187 | -0.00068486916 | %p | 0.013738314 | improved |
| 9001 | 배추/RETAIL | mae | 242.5873 | 241.8373 | -0.75 | price | 0.30916705 | improved |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 386.36172 | 6.8717092 | price | -1.8107747 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.96908741 | -0.0030053906 | ratio | 0.30916705 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.9496893 | 0.14398606 | %p | -1.6351455 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1090.4071 | 12.573123 | price | -1.1665175 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1866.2571 | 11.266269 | price | -0.60734903 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.039238 | 0.011983108 | ratio | -1.1665175 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.9103698 | 0.16588009 | %p | -4.4299785 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 104.48617 | 4.3992095 | price | -4.3953874 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 153.42878 | 9.3181531 | price | -6.4659721 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.088084 | 0.045811895 | ratio | -4.3953874 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.1055226 | 0.080567236 | %p | -1.1468719 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1428.7273 | 12.324111 | price | -0.87009907 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2306.9223 | 27.466778 | price | -1.204971 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0538395 | 0.0090903525 | ratio | -0.87009907 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 1, 'worsened': 9, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


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


## ridge-v2-20261117T064727116577Z-7fd3dd3bf6754aac9addcbf571c303f1

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064727116577Z-7fd3dd3bf6754aac9addcbf571c303f1 | no_event | 4.9908908 | 685.86685 | 1051.4286 | 1.1683312 | -8.3501867 (direct) | -8.33067 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9908908 | 0.38380141 | %p | -8.33067 | worsened |
| mae | 532.31701 | 685.86685 | 153.54984 | price | -28.845564 | worsened |
| rmse | 943.1701 | 1051.4286 | 108.25849 | price | -11.478151 | worsened |
| rmae | 1 | 1.1683312 | 0.16833122 | ratio | -16.833122 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1209607 | 0.35246419 | %p | -7.391516 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.2332 | 9.9644269 | price | -7.2065634 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.9487 | -1.8373452 | price | 0.87166356 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0720656 | 0.072065634 | ratio | -7.2065634 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.065899 | 0.56383723 | %p | -10.247744 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 125.28854 | 9.5375494 | price | -8.2397132 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 184.92323 | 13.78714 | price | -8.0562432 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0823971 | 0.082397132 | ratio | -8.2397132 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5691292 | 0.67572578 | %p | -23.354012 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 656.89723 | 138.80237 | price | -26.790918 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1006.1718 | 177.70828 | price | -21.450345 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2679092 | 0.26790918 | ratio | -26.790918 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.9042235 | 0.39758159 | %p | -8.8221252 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 108.58964 | 7.9521912 | price | -7.9018211 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 166.4443 | 7.5812083 | price | -4.7721646 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0790182 | 0.079018211 | ratio | -7.9018211 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.6569094 | 0.85956373 | %p | -107.80315 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2563.9107 | 1232.2143 | price | -92.529668 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3682.0653 | 808.87491 | price | -28.152499 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.9252967 | 0.92529668 | ratio | -92.529668 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0626896 | 0.61300559 | %p | -17.769905 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 436.19763 | 68.027668 | price | -18.477246 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 613.42588 | 61.071443 | price | -11.056568 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1847725 | 0.18477246 | ratio | -18.477246 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0016544 | -0.33014687 | %p | 6.1920325 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.53571 | -6.015873 | price | 2.4106731 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 384.04433 | -26.012161 | price | 6.3435555 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97589327 | -0.024106731 | ratio | 2.4106731 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8158647 | 0.22927094 | %p | -2.6701035 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1079.6403 | 30.403162 | price | -2.8976444 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1865.1871 | 34.328496 | price | -1.8749944 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0289764 | 0.028976444 | ratio | -2.8976444 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7329852 | 0.10542732 | %p | -2.9062892 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.549407 | 3.5217391 | price | -3.6674213 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.095 | -10.787888 | price | 6.9651907 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0366742 | 0.036674213 | ratio | -3.6674213 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9785919 | 0.37128459 | %p | -5.6193026 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1396.8261 | 41.090909 | price | -3.030895 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2258.9802 | 17.870822 | price | -0.79740961 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0303089 | 0.03030895 | ratio | -3.030895 | worsened |
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
| mape | 4.6062595 | 4.9908908 | 0.38463127 | %p | -8.3501867 | worsened |
| mae | 565.55167 | 685.86685 | 120.31518 | price | -21.273949 | worsened |
| rmse | 926.40586 | 1051.4286 | 125.02273 | price | -13.49546 | worsened |
| rmae | 1.0199316 | 1.1683312 | 0.14839965 | ratio | -14.549961 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1209607 | 0.39114972 | %p | -8.2698804 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.2332 | 10.403162 | price | -7.5478191 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.9487 | -0.23023776 | price | 0.11006737 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0720656 | 0.075238694 | ratio | -7.5478191 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.065899 | 0.33374268 | %p | -5.8222884 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 125.28854 | 5.6245059 | price | -4.7002477 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 184.92323 | 6.1842452 | price | -3.4599308 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0823971 | 0.048591429 | ratio | -4.7002477 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5691292 | 0.88869059 | %p | -33.154671 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 656.89723 | 166.29249 | price | -33.89541 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1006.1718 | 227.0899 | price | -29.148401 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2679092 | 0.32096919 | ratio | -33.89541 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.9042235 | 0.31322326 | %p | -6.8225494 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 108.58964 | 5.6334661 | price | -5.4717127 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 166.4443 | 1.4092324 | price | -0.85389877 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0790182 | 0.055977831 | ratio | -5.4717127 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.6569094 | 0.59023825 | %p | -55.334604 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2563.9107 | 852.44196 | price | -49.807627 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3682.0653 | 843.12514 | price | -29.698588 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.9252967 | 0.64011733 | ratio | -49.807627 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0626896 | 0.52399607 | %p | -14.807614 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 436.19763 | 58.12253 | price | -15.373276 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 613.42588 | 48.051841 | price | -8.4991242 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1847725 | 0.15786875 | ratio | -15.373276 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0016544 | 0.22315864 | %p | -4.6700606 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.53571 | 18.313492 | price | -8.1312989 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 384.04433 | 10.704667 | price | -2.8672731 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97589327 | 0.073385596 | ratio | -8.1312989 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8158647 | 0.73713271 | %p | -9.1243615 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1079.6403 | 115.49802 | price | -11.979355 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1865.1871 | 161.21685 | price | -9.4612477 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0289764 | 0.11007809 | ratio | -11.979355 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7329852 | 0.083981986 | %p | -2.3015048 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.549407 | 2.4071146 | price | -2.4779265 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.095 | -11.066186 | price | 7.1320584 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0366742 | 0.025066886 | ratio | -2.4779265 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9785919 | -0.23900121 | %p | 3.31137 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1396.8261 | -31.58498 | price | 2.2111968 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2258.9802 | -36.258144 | price | 1.5797115 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0303089 | -0.023297308 | ratio | 2.2111968 | improved |
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
| mape | 4.99034 | 4.9908908 | 0.00055072062 | %p | -0.011035733 | worsened |
| mae | 674.96363 | 685.86685 | 10.903215 | price | -1.6153781 | worsened |
| rmse | 1034.3299 | 1051.4286 | 17.098714 | price | -1.65312 | worsened |
| rmae | 1.1614981 | 1.1683312 | 0.0068331272 | ratio | -0.58830292 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1209607 | -0.013004836 | %p | 0.25330976 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 148.2332 | -0.58102767 | price | 0.39043825 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 208.9487 | -0.87320343 | price | 0.41616409 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0720656 | -0.0042021611 | ratio | 0.39043825 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.065899 | -0.090716939 | %p | 1.4734871 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 125.28854 | -2.5770751 | price | 2.015456 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 184.92323 | -2.1403496 | price | 1.144183 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0823971 | -0.022263958 | ratio | 2.015456 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5691292 | -0.025760213 | %p | 0.71657875 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 656.89723 | -5.9328063 | price | 0.89507204 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1006.1718 | 4.1983584 | price | -0.41900896 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2679092 | -0.011451197 | ratio | 0.89507204 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.9042235 | 0.066536516 | %p | -1.3753787 | worsened |
| 8 | 양파/RETAIL | mae | 107.0239 | 108.58964 | 1.5657371 | price | -1.4629788 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 166.4443 | 1.809863 | price | -1.0993223 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0790182 | 0.015558195 | ratio | -1.4629788 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.6569094 | 0.08302304 | %p | -5.275034 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2563.9107 | 131.55357 | price | -5.4084809 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3682.0653 | 167.05309 | price | -4.7525608 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.9252967 | 0.098786457 | ratio | -5.4084809 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0626896 | 0.016585415 | %p | -0.40991072 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 436.19763 | 2.3636364 | price | -0.54482507 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 613.42588 | 6.6797164 | price | -1.1009079 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1847725 | 0.0064199598 | ratio | -0.54482507 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 5.0016544 | 0.016550771 | %p | -0.33200456 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.53571 | 0.9484127 | price | -0.39095727 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 384.04433 | 4.5543165 | price | -1.200115 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97589327 | 0.0038004675 | ratio | -0.39095727 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8158647 | 0.010161457 | %p | -0.11539631 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1079.6403 | 1.8063241 | price | -0.16758834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1865.1871 | 10.196245 | price | -0.54966551 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0289764 | 0.0017215594 | ratio | -0.16758834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7329852 | -0.011504503 | %p | 0.30723819 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 99.549407 | -0.53754941 | price | 0.53708238 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.095 | -0.015634424 | price | 0.010848904 | improved |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0366742 | -0.0055978596 | ratio | 0.53708238 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 6.9785919 | -0.046363502 | %p | 0.65998286 | improved |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1396.8261 | -19.577075 | price | 1.3821683 | improved |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2258.9802 | -20.475264 | price | 0.89825243 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0303089 | -0.014440191 | ratio | 1.3821683 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T064958699426Z-b15e8a6369814e2b9951392fc67f80db

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064958699426Z-b15e8a6369814e2b9951392fc67f80db | no_macro | 4.988793 | 670.74288 | 1026.3115 | 1.1584473 | -8.3046459 (direct) | -8.2851373 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.988793 | 0.38170368 | %p | -8.2851373 | worsened |
| mae | 532.31701 | 670.74288 | 138.42588 | price | -26.004406 | worsened |
| rmse | 943.1701 | 1026.3115 | 83.141452 | price | -8.8151068 | worsened |
| rmae | 1 | 1.1584473 | 0.15844727 | ratio | -15.844727 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1157538 | 0.34725728 | %p | -7.2823221 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.41107 | 10.142292 | price | -7.335201 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.45197 | -1.334083 | price | 0.6329086 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.073352 | 0.07335201 | ratio | -7.335201 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1365284 | 0.63446665 | %p | -11.531434 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 127.56522 | 11.814229 | price | -10.20659 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 186.9161 | 15.78001 | price | -9.2207378 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1020659 | 0.1020659 | ratio | -10.20659 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.6280721 | 0.73466875 | %p | -25.391162 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 668.13834 | 150.04348 | price | -28.960619 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1006.2208 | 177.75729 | price | -21.456262 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2896062 | 0.28960619 | ratio | -28.960619 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.8292931 | 0.3226512 | %p | -7.1594595 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 106.79283 | 6.1553785 | price | -6.1163895 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.19776 | 5.3346678 | price | -3.3580284 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0611639 | 0.061163895 | ratio | -6.1163895 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.5517548 | 0.75440916 | %p | -94.615069 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2389.9062 | 1058.2098 | price | -79.463292 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3438.6807 | 565.49032 | price | -19.681617 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.7946329 | 0.79463292 | ratio | -79.463292 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0257228 | 0.5760388 | %p | -16.698306 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 431.5415 | 63.371542 | price | -17.212578 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 602.03589 | 49.681461 | price | -8.9944895 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1721258 | 0.17212578 | ratio | -17.212578 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9872468 | -0.34455446 | %p | 6.4622524 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 242.62698 | -6.9246032 | price | 2.7748183 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 380.72298 | -29.33351 | price | 7.1535291 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97225182 | -0.027748183 | ratio | 2.7748183 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8513612 | 0.26476747 | %p | -3.0834983 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1082.253 | 33.01581 | price | -3.146649 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1860.4996 | 29.641003 | price | -1.6189674 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0314665 | 0.03146649 | ratio | -3.146649 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7615963 | 0.13403834 | %p | -3.695002 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 100.64822 | 4.6205534 | price | -4.8116896 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.2754 | -10.607482 | price | 6.8487118 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0481169 | 0.048116896 | ratio | -4.8116896 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0006009 | 0.39329359 | %p | -5.9524035 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1409.5455 | 53.810277 | price | -3.9690846 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2270.1142 | 29.004833 | price | -1.2942176 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0396908 | 0.039690846 | ratio | -3.9690846 | worsened |
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
| mape | 4.6062595 | 4.988793 | 0.38253354 | %p | -8.3046459 | worsened |
| mae | 565.55167 | 670.74288 | 105.19121 | price | -18.599753 | worsened |
| rmse | 926.40586 | 1026.3115 | 99.905693 | price | -10.784225 | worsened |
| rmae | 1.0199316 | 1.1584473 | 0.13851571 | ratio | -13.580882 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1157538 | 0.38594281 | %p | -8.1597934 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.41107 | 10.581028 | price | -7.6768662 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.45197 | 0.27302438 | price | -0.13052192 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.073352 | 0.07652507 | ratio | -7.6768662 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1365284 | 0.40437209 | %p | -7.0544498 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 127.56522 | 7.9011858 | price | -6.6028076 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 186.9161 | 8.1771158 | price | -4.5748921 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1020659 | 0.068260201 | ratio | -6.6028076 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.6280721 | 0.94763356 | %p | -35.353676 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 668.13834 | 177.5336 | price | -36.186686 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1006.2208 | 227.13892 | price | -29.154692 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2896062 | 0.3426662 | ratio | -36.186686 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.8292931 | 0.23829287 | %p | -5.1904347 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 106.79283 | 3.8366534 | price | -3.7264918 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.19776 | -0.83730813 | price | 0.50735164 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0611639 | 0.038123515 | ratio | -3.7264918 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.5517548 | 0.48508369 | %p | -45.476405 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2389.9062 | 678.4375 | price | -39.64066 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3438.6807 | 599.74056 | price | -21.125509 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.7946329 | 0.50945357 | ratio | -39.64066 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0257228 | 0.48702928 | %p | -13.762969 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 431.5415 | 53.466403 | price | -14.141742 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 602.03589 | 36.66186 | price | -6.4845319 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1721258 | 0.14522207 | ratio | -14.141742 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9872468 | 0.20875105 | %p | -4.3685517 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 242.62698 | 17.404762 | price | -7.7278173 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 380.72298 | 7.3833179 | price | -1.9776409 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97225182 | 0.069744144 | ratio | -7.7278173 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8513612 | 0.77262924 | %p | -9.5637439 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1082.253 | 118.11067 | price | -12.250336 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1860.4996 | 156.52935 | price | -9.1861553 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0314665 | 0.11256814 | ratio | -12.250336 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7615963 | 0.112593 | %p | -3.0855823 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 100.64822 | 3.5059289 | price | -3.6090654 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.2754 | -10.88578 | price | 7.0157884 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0481169 | 0.03650957 | ratio | -3.6090654 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0006009 | -0.21699221 | %p | 3.0064345 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1409.5455 | -18.865613 | price | 1.3207411 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2270.1142 | -25.124133 | price | 1.0946198 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0396908 | -0.013915411 | ratio | 1.3207411 | improved |
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
| mape | 4.99034 | 4.988793 | -0.0015470098 | %p | 0.031000088 | improved |
| mae | 674.96363 | 670.74288 | -4.2207503 | price | 0.62533004 | improved |
| rmse | 1034.3299 | 1026.3115 | -8.0183241 | price | 0.77521923 | improved |
| rmae | 1.1614981 | 1.1584473 | -0.0030508155 | ratio | 0.26266212 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1157538 | -0.018211745 | %p | 0.35473056 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 148.41107 | -0.40316206 | price | 0.27091633 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 209.45197 | -0.36994129 | price | 0.17631204 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.073352 | -0.0029157853 | ratio | 0.27091633 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1365284 | -0.020087521 | %p | 0.32627536 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 127.56522 | -0.30039526 | price | 0.23493045 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 186.9161 | -0.147479 | price | 0.078838972 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1020659 | -0.0025951852 | ratio | 0.23493045 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.6280721 | 0.033182758 | %p | -0.92305366 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 668.13834 | 5.3083004 | price | -0.80085393 | worsened |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1006.2208 | 4.2473748 | price | -0.42390095 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2896062 | 0.010245808 | ratio | -0.80085393 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.8292931 | -0.0083938731 | %p | 0.17351005 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 106.79283 | -0.2310757 | price | 0.21591036 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 164.19776 | -0.43667751 | price | 0.26524069 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0611639 | -0.0022961203 | ratio | 0.21591036 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.5517548 | -0.022131524 | %p | 1.4061704 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2389.9062 | -42.450893 | price | 1.7452574 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3438.6807 | -76.33149 | price | 2.1715853 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.7946329 | -0.031877305 | ratio | 1.7452574 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0257228 | -0.020381374 | %p | 0.50372834 | improved |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 431.5415 | -2.2924901 | price | 0.52842566 | improved |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 602.03589 | -4.710265 | price | 0.77631559 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1721258 | -0.0062267169 | ratio | 0.52842566 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9872468 | 0.0021431817 | %p | -0.042991718 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 242.62698 | 0.03968254 | price | -0.016358045 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 380.72298 | 1.2329669 | price | -0.32490102 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97225182 | 0.00015901538 | ratio | -0.016358045 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8513612 | 0.045657988 | %p | -0.51850473 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1082.253 | 4.4189723 | price | -0.40998636 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1860.4996 | 5.508752 | price | -0.29696922 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0314665 | 0.0042116049 | ratio | -0.40998636 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7615963 | 0.01710651 | %p | -0.45684488 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 100.64822 | 0.56126482 | price | -0.56077719 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.2754 | 0.16477146 | price | -0.11433678 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0481169 | 0.005844824 | ratio | -0.56077719 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.0006009 | -0.024354498 | %p | 0.34668544 | improved |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1409.5455 | -6.8577075 | price | 0.48416353 | improved |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2270.1142 | -9.3412534 | price | 0.40980196 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0396908 | -0.0050582943 | ratio | 0.48416353 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T065230337712Z-2c229b557e64408cb0e04be22560aec6

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065230337712Z-2c229b557e64408cb0e04be22560aec6 | no_production | 4.9924315 | 675.52627 | 1035.3211 | 1.1623651 | -8.3836354 (direct) | -8.3641126 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9924315 | 0.38534214 | %p | -8.3641126 | worsened |
| mae | 532.31701 | 675.52627 | 143.20926 | price | -26.903004 | worsened |
| rmse | 943.1701 | 1035.3211 | 92.150975 | price | -9.7703453 | worsened |
| rmae | 1 | 1.1623651 | 0.16236505 | ratio | -16.236505 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1377168 | 0.36922029 | %p | -7.7429077 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.96047 | 10.6917 | price | -7.7325482 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.74962 | -1.0364252 | price | 0.49169533 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0773255 | 0.077325482 | ratio | -7.7325482 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1443932 | 0.64233138 | %p | -11.674376 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 127.64427 | 11.893281 | price | -10.274885 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 186.70026 | 15.564173 | price | -9.0946176 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1027488 | 0.10274885 | ratio | -10.274885 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5954239 | 0.7020205 | %p | -24.262794 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 662.81028 | 144.71542 | price | -27.932224 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1001.7818 | 173.31832 | price | -20.920454 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2793222 | 0.27932224 | ratio | -27.932224 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.8358947 | 0.32925281 | %p | -7.3059457 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 107.00398 | 6.3665339 | price | -6.3262074 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.59989 | 5.7367969 | price | -3.6111578 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0632621 | 0.063262074 | ratio | -6.3262074 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.574827 | 0.77748135 | %p | -97.508694 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2436.808 | 1105.1116 | price | -82.98525 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3523.7297 | 650.53923 | price | -22.641703 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.8298525 | 0.8298525 | ratio | -82.98525 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0497631 | 0.60007905 | %p | -17.395189 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 434.3004 | 66.130435 | price | -17.961931 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 606.68177 | 54.327335 | price | -9.8355932 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1796193 | 0.17961931 | ratio | -17.961931 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9915675 | -0.34023376 | %p | 6.3812161 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.01984 | -6.531746 | price | 2.6173931 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 380.18887 | -29.867618 | price | 7.2837813 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97382607 | -0.026173931 | ratio | 2.6173931 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8068299 | 0.22023618 | %p | -2.5648841 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1077.8024 | 28.565217 | price | -2.7224748 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1854.8915 | 24.032938 | price | -1.3126594 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0272247 | 0.027224748 | ratio | -2.7224748 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7593102 | 0.1317523 | %p | -3.6319834 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 100.41107 | 4.3833992 | price | -4.5647253 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.29252 | -10.590361 | price | 6.8376573 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0456473 | 0.045647253 | ratio | -4.5647253 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0285886 | 0.4212813 | %p | -6.3759907 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1416.502 | 60.766798 | price | -4.4822027 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2280.5948 | 39.485358 | price | -1.7618666 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.044822 | 0.044822027 | ratio | -4.4822027 | worsened |
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
| mape | 4.6062595 | 4.9924315 | 0.386172 | %p | -8.3836354 | worsened |
| mae | 565.55167 | 675.52627 | 109.9746 | price | -19.445544 | worsened |
| rmse | 926.40586 | 1035.3211 | 108.91522 | price | -11.75675 | worsened |
| rmae | 1.0199316 | 1.1623651 | 0.14243349 | ratio | -13.965004 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1377168 | 0.40790581 | %p | -8.6241462 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.96047 | 11.130435 | price | -8.0754782 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.74962 | 0.57068225 | price | -0.27282013 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0773255 | 0.080498542 | ratio | -8.0754782 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1443932 | 0.41223683 | %p | -7.1916536 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 127.64427 | 7.9802372 | price | -6.6688687 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 186.70026 | 7.9612785 | price | -4.4541366 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1027488 | 0.068943145 | ratio | -6.6688687 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5954239 | 0.9149853 | %p | -34.135657 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 662.81028 | 172.20553 | price | -35.100666 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1001.7818 | 222.69995 | price | -28.584923 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2793222 | 0.33238225 | ratio | -35.100666 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.8358947 | 0.24489448 | %p | -5.3342293 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 107.00398 | 4.0478088 | price | -3.9315842 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.59989 | -0.43517896 | price | 0.26368878 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0632621 | 0.040221694 | ratio | -3.9315842 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.574827 | 0.50815588 | %p | -47.639413 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2436.808 | 725.33929 | price | -42.3811 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3523.7297 | 684.78947 | price | -24.121307 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.8298525 | 0.54467315 | ratio | -42.3811 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0497631 | 0.51106953 | %p | -14.442322 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 434.3004 | 56.225296 | price | -14.871462 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 606.68177 | 41.307733 | price | -7.3062664 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1796193 | 0.1527156 | ratio | -14.871462 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9915675 | 0.21307175 | %p | -4.4589712 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.01984 | 17.797619 | price | -7.9022482 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 380.18887 | 6.8492104 | price | -1.8345788 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97382607 | 0.071318396 | ratio | -7.9022482 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8068299 | 0.72809794 | %p | -9.0125275 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1077.8024 | 113.66008 | price | -11.788725 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1854.8915 | 150.92129 | price | -8.8570377 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0272247 | 0.1083264 | ratio | -11.788725 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7593102 | 0.11030696 | %p | -3.0229341 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 100.41107 | 3.2687747 | price | -3.3649347 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.29252 | -10.868659 | price | 7.0047537 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0456473 | 0.034039926 | ratio | -3.3649347 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0285886 | -0.1890045 | %p | 2.6186638 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1416.502 | -11.909091 | price | 0.83372995 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2280.5948 | -14.643608 | price | 0.63799944 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.044822 | -0.0087842309 | ratio | 0.83372995 | improved |
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
| mape | 4.99034 | 4.9924315 | 0.0020914513 | %p | -0.041909996 | worsened |
| mae | 674.96363 | 675.52627 | 0.56263581 | price | -0.083357944 | worsened |
| rmse | 1034.3299 | 1035.3211 | 0.9911995 | price | -0.095830114 | worsened |
| rmae | 1.1614981 | 1.1623651 | 0.00086696432 | ratio | -0.074641906 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1377168 | 0.0037512629 | %p | -0.07306755 | worsened |
| 1 | 대파/RETAIL | mae | 148.81423 | 148.96047 | 0.14624506 | price | -0.098273572 | worsened |
| 1 | 대파/RETAIL | rmse | 209.82191 | 209.74962 | -0.072283415 | price | 0.034449889 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0773255 | 0.0010576868 | ratio | -0.098273572 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1443932 | -0.012222786 | %p | 0.19853091 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 127.64427 | -0.22134387 | price | 0.17310665 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 186.70026 | -0.36331622 | price | 0.19422071 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1027488 | -0.0019122418 | ratio | 0.17310665 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5954239 | 0.00053450102 | %p | -0.014868358 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 662.81028 | -0.019762846 | price | 0.0029815857 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1001.7818 | -0.19159481 | price | 0.019121746 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2793222 | -3.8145227e-05 | ratio | 0.0029815857 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.8358947 | -0.0017922641 | %p | 0.037047955 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 107.00398 | -0.019920319 | price | 0.018612962 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 164.59989 | -0.034548348 | price | 0.020984885 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0632621 | -0.00019794141 | ratio | 0.018612962 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.574827 | 0.00094066441 | %p | -0.059766984 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2436.808 | 4.4508929 | price | -0.18298681 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3523.7297 | 8.7174194 | price | -0.24800538 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.8298525 | 0.0033422729 | ratio | -0.18298681 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0497631 | 0.0036588741 | %p | -0.090429557 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 434.3004 | 0.46640316 | price | -0.10750729 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 606.68177 | -0.064391453 | price | 0.010612585 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1796193 | 0.0012668148 | ratio | -0.10750729 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9915675 | 0.0064638772 | %p | -0.12966385 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.01984 | 0.43253968 | price | -0.17830269 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 380.18887 | 0.69885941 | price | -0.18415753 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97382607 | 0.0017332676 | ratio | -0.17830269 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8068299 | 0.0011266941 | %p | -0.012795049 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1077.8024 | -0.031620553 | price | 0.0029337128 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1854.8915 | -0.099313845 | price | 0.0053538725 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0272247 | -3.0136708e-05 | ratio | 0.0029337128 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7593102 | 0.014820476 | %p | -0.39579429 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 100.41107 | 0.32411067 | price | -0.32382908 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.29252 | 0.18189294 | price | -0.12621758 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0456473 | 0.0033751801 | ratio | -0.32382908 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.0285886 | 0.0036332125 | %p | -0.051718656 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1416.502 | 0.098814229 | price | -0.0069764197 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2280.5948 | 1.1392713 | price | -0.049979975 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.044822 | 7.2886085e-05 | ratio | -0.0069764197 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 2, 'worsened': 8, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T065500252334Z-446c7c9c839c4c95aa096773a44e14b7

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065500252334Z-446c7c9c839c4c95aa096773a44e14b7 | no_garak | 5.0574935 | 686.0854 | 1061.2323 | 1.1821971 | -9.7961053 (direct) | -9.7763281 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 5.0574935 | 0.45040417 | %p | -9.7763281 | worsened |
| mae | 532.31701 | 686.0854 | 153.7684 | price | -28.886622 | worsened |
| rmse | 943.1701 | 1061.2323 | 118.06218 | price | -12.517592 | worsened |
| rmae | 1 | 1.1821971 | 0.18219708 | ratio | -18.219708 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1985402 | 0.43004364 | %p | -9.0184325 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 151.03162 | 12.762846 | price | -9.2304614 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 212.88839 | 2.1023395 | price | -0.99738076 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0923046 | 0.092304614 | ratio | -9.2304614 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.2061193 | 0.70405746 | %p | -12.796248 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 128.96443 | 13.213439 | price | -11.4154 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 188.66628 | 17.530188 | price | -10.24342 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.114154 | 0.114154 | ratio | -11.4154 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.681154 | 0.78775066 | %p | -27.225746 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 680.36364 | 162.26877 | price | -31.320283 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1019.1923 | 190.72883 | price | -23.021996 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.3132028 | 0.31320283 | ratio | -31.320283 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.9927473 | 0.48610543 | %p | -10.786422 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 110.84064 | 10.203187 | price | -10.138559 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 169.01058 | 10.147492 | price | -6.3875707 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.1013856 | 0.10138559 | ratio | -10.138559 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.5966515 | 0.79930584 | %p | -100.24584 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2486.2857 | 1154.5893 | price | -86.700637 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3768.2876 | 895.09715 | price | -31.153422 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.8670064 | 0.86700637 | ratio | -86.700637 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.1064518 | 0.65676777 | %p | -19.038491 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 442.05929 | 73.889328 | price | -20.069353 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 611.76625 | 59.411814 | price | -10.756103 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.2006935 | 0.20069353 | ratio | -20.069353 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0695268 | -0.26227447 | %p | 4.9190593 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 246.10714 | -3.4444444 | price | 1.3802535 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 374.61026 | -35.446228 | price | 8.6442305 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.98619747 | -0.013802535 | ratio | 1.3802535 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8095337 | 0.22293994 | %p | -2.5963723 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1076.7115 | 27.474308 | price | -2.6185032 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1811.1218 | -19.736839 | price | 1.07801 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.026185 | 0.026185032 | ratio | -2.6185032 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.8138524 | 0.18629448 | %p | -5.1355341 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 101.90514 | 5.8774704 | price | -6.1206009 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 147.54266 | -7.3402184 | price | 4.7392057 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.061206 | 0.061206009 | ratio | -6.1206009 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1003583 | 0.49305096 | %p | -7.4622071 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1436.585 | 80.849802 | price | -5.9635395 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2309.2367 | 68.127303 | price | -3.0398919 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0596354 | 0.059635395 | ratio | -5.9635395 | worsened |
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
| mape | 4.6062595 | 5.0574935 | 0.45123403 | %p | -9.7961053 | worsened |
| mae | 565.55167 | 686.0854 | 120.53373 | price | -21.312594 | worsened |
| rmse | 926.40586 | 1061.2323 | 134.82642 | price | -14.55371 | worsened |
| rmae | 1.0199316 | 1.1821971 | 0.16226551 | ratio | -15.909451 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1985402 | 0.46872917 | %p | -9.9101036 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 151.03162 | 13.201581 | price | -9.5781595 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 212.88839 | 3.7094469 | price | -1.7733367 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0923046 | 0.095477674 | ratio | -9.5781595 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.2061193 | 0.47396291 | %p | -8.2684923 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 128.96443 | 9.3003953 | price | -7.7720892 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 188.66628 | 9.9272936 | price | -5.554073 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.114154 | 0.080348301 | ratio | -7.7720892 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.681154 | 1.0007155 | %p | -37.33402 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 680.36364 | 189.75889 | price | -38.678569 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1019.1923 | 240.11046 | price | -30.81967 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.3132028 | 0.36626284 | ratio | -38.678569 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.9927473 | 0.4017471 | %p | -8.7507531 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 110.84064 | 7.8844622 | price | -7.658076 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 169.01058 | 3.9755164 | price | -2.4088919 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.1013856 | 0.07834521 | ratio | -7.658076 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.5966515 | 0.52998036 | %p | -49.68545 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2486.2857 | 774.81696 | price | -45.272049 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3768.2876 | 929.34738 | price | -32.735716 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.8670064 | 0.58182702 | ratio | -45.272049 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.1064518 | 0.56775825 | %p | -16.04429 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 442.05929 | 63.98419 | price | -16.923672 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 611.76625 | 46.392213 | price | -8.2055789 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.2006935 | 0.17378982 | ratio | -16.923672 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0695268 | 0.29103105 | %p | -6.0904323 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 246.10714 | 20.884921 | price | -9.2730284 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 374.61026 | 1.2706001 | price | -0.34033355 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.98619747 | 0.083689793 | ratio | -9.2730284 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8095337 | 0.73080171 | %p | -9.0459952 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1076.7115 | 112.56917 | price | -11.675576 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1811.1218 | 107.15151 | price | -6.288344 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.026185 | 0.10728668 | ratio | -11.675576 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.8138524 | 0.16484914 | %p | -4.5176484 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 101.90514 | 4.7628458 | price | -4.9029581 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 147.54266 | -7.6185162 | price | 4.9100659 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.061206 | 0.049598683 | ratio | -4.9029581 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1003583 | -0.11723484 | %p | 1.6242928 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1436.585 | 8.173913 | price | -0.57223815 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2309.2367 | 13.998337 | price | -0.60988599 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0596354 | 0.0060291369 | ratio | -0.57223815 | worsened |
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
| mape | 4.99034 | 5.0574935 | 0.067153482 | %p | -1.3456695 | worsened |
| mae | 674.96363 | 686.0854 | 11.121771 | price | -1.6477586 | worsened |
| rmse | 1034.3299 | 1061.2323 | 26.902408 | price | -2.6009505 | worsened |
| rmae | 1.1614981 | 1.1821971 | 0.020698993 | ratio | -1.7820944 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1985402 | 0.064574619 | %p | -1.2577922 | worsened |
| 1 | 대파/RETAIL | mae | 148.81423 | 151.03162 | 2.2173913 | price | -1.4900398 | worsened |
| 1 | 대파/RETAIL | rmse | 209.82191 | 212.88839 | 3.0664812 | price | -1.4614686 | worsened |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0923046 | 0.016036819 | ratio | -1.4900398 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.2061193 | 0.049503293 | %p | -0.8040666 | worsened |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 128.96443 | 1.0988142 | price | -0.85935085 | worsened |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 188.66628 | 1.6026989 | price | -0.85676692 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.114154 | 0.0094929145 | ratio | -0.85935085 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.681154 | 0.086264666 | %p | -2.3996473 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 680.36364 | 17.533597 | price | -2.6452629 | worsened |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1019.1923 | 17.218913 | price | -1.7185 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.3132028 | 0.033842445 | ratio | -2.6452629 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.9927473 | 0.15506035 | %p | -3.2052581 | worsened |
| 8 | 양파/RETAIL | mae | 107.0239 | 110.84064 | 3.8167331 | price | -3.5662435 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 169.01058 | 4.3761471 | price | -2.6580994 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.1013856 | 0.037925574 | ratio | -3.5662435 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.5966515 | 0.022765151 | %p | -1.4464291 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2486.2857 | 53.928571 | price | -2.2171321 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3768.2876 | 253.27534 | price | -7.2055322 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.8670064 | 0.040496145 | ratio | -2.2171321 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.1064518 | 0.060347596 | %p | -1.4914988 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 442.05929 | 8.2252964 | price | -1.8959548 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 611.76625 | 5.020088 | price | -0.82737862 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.2006935 | 0.022341031 | ratio | -1.8959548 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 5.0695268 | 0.084423172 | %p | -1.6935089 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 246.10714 | 3.5198413 | price | -1.4509586 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 374.61026 | -4.8797509 | price | 1.2858707 | improved |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.98619747 | 0.014104664 | ratio | -1.4509586 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8095337 | 0.0038304552 | %p | -0.043499708 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1076.7115 | -1.1225296 | price | 0.1041468 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1811.1218 | -43.869091 | price | 2.3649222 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.026185 | -0.0010698531 | ratio | 0.1041468 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.8138524 | 0.069362649 | %p | -1.8523925 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 101.90514 | 1.8181818 | price | -1.8166022 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 147.54266 | 3.4320354 | price | -2.3815283 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.061206 | 0.018933937 | ratio | -1.8166022 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.1003583 | 0.075402868 | %p | -1.0733572 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1436.585 | 20.181818 | price | -1.424864 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2309.2367 | 29.781217 | price | -1.3065057 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0596354 | 0.014886254 | ratio | -1.424864 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 0, 'worsened': 10, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T065715205676Z-a7dcb24ce98f447e9d4f2966740e6033

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065715205676Z-a7dcb24ce98f447e9d4f2966740e6033 | no_origin_weather | 4.5967193 | 574.12181 | 908.40521 | 1.0287034 | 0.20711379 (direct) | 0.22508916 (direct) | 5 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5967193 | -0.010370059 | %p | 0.22508916 | improved |
| mae | 532.31701 | 574.12181 | 41.804803 | price | -7.853366 | worsened |
| rmse | 943.1701 | 908.40521 | -34.764885 | price | 3.6859614 | improved |
| rmae | 1 | 1.0287034 | 0.028703366 | ratio | -2.8703366 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4935422 | -0.27495438 | %p | 5.7660601 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 130.96443 | -7.3043478 | price | 5.2827168 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 197.87472 | -12.911334 | price | 6.1253267 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.94717283 | -0.052827168 | ratio | 5.2827168 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8355351 | 0.33347326 | %p | -6.0608782 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.24901 | 5.4980237 | price | -4.7498719 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 182.2756 | 11.139513 | price | -6.5091545 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0474987 | 0.047498719 | ratio | -4.7498719 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.9439951 | 0.05059169 | %p | -1.7485184 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 535.48617 | 17.391304 | price | -3.3567799 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 840.89747 | 12.433988 | price | -1.5008493 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.0335678 | 0.033567799 | ratio | -3.3567799 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5798783 | 0.073236438 | %p | -1.6250778 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 101.63745 | 1 | price | -0.99366587 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 162.15989 | 3.296794 | price | -2.0752422 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0099367 | 0.0099366587 | ratio | -0.99366587 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1339244 | 0.33657872 | %p | -42.212396 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1794.4688 | 462.77232 | price | -34.750587 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2602.9937 | -270.19669 | price | 9.4040648 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3475059 | 0.34750587 | ratio | -34.750587 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.6375575 | 0.18787346 | %p | -5.4461062 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 388.14625 | 19.976285 | price | -5.4258323 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 589.30517 | 36.950742 | price | -6.6896797 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0542583 | 0.054258323 | ratio | -5.4258323 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.8030673 | -0.52873391 | %p | 9.9166095 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 228.30556 | -21.246032 | price | 8.5136833 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 373.87193 | -36.184558 | price | 8.8242862 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91486317 | -0.085136833 | ratio | 8.5136833 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0561361 | -0.53045759 | %p | 6.1777418 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 970.95257 | -78.284585 | price | 7.4610954 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1727.3958 | -103.46278 | price | 5.6510523 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92538905 | -0.074610954 | ratio | 7.4610954 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.5876263 | -0.039931669 | %p | 1.1007865 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 95.343874 | -0.68379447 | price | 0.71208068 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 147.9883 | -6.8945811 | price | 4.4514804 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.99287919 | -0.0071208068 | ratio | 0.71208068 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.8959307 | 0.2886234 | %p | -4.3682454 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1374.664 | 18.928854 | price | -1.3962058 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2259.2895 | 18.180049 | price | -0.81120758 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0139621 | 0.013962058 | ratio | -1.3962058 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.5967193 | -0.0095401988 | %p | 0.20711379 | improved |
| mae | 565.55167 | 574.12181 | 8.5701367 | price | -1.5153587 | worsened |
| rmse | 926.40586 | 908.40521 | -18.000645 | price | 1.9430625 | improved |
| rmae | 1.0199316 | 1.0287034 | 0.0087717981 | ratio | -0.86003791 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4935422 | -0.23626885 | %p | 4.9953127 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 130.96443 | -6.8656126 | price | 4.9812165 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 197.87472 | -11.304227 | price | 5.4040941 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.94717283 | -0.049654108 | ratio | 4.9812165 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8355351 | 0.10337871 | %p | -1.8034872 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.24901 | 1.5849802 | price | -1.3245252 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 182.2756 | 3.5366182 | price | -1.9786496 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0474987 | 0.013693017 | ratio | -1.3245252 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.9439951 | 0.2635565 | %p | -9.8325887 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 535.48617 | 44.881423 | price | -9.1481837 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 840.89747 | 61.815611 | price | -7.934418 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.0335678 | 0.086627809 | ratio | -9.1481837 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5798783 | -0.011121894 | %p | 0.24225427 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 101.63745 | -1.3187251 | price | 1.2808606 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 162.15989 | -2.8751819 | price | 1.7421642 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0099367 | -0.013103721 | ratio | 1.2808606 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1339244 | 0.067253241 | %p | -6.3049649 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1794.4688 | 83 | price | -4.8496357 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2602.9937 | -235.94646 | price | 8.3110752 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3475059 | 0.062326517 | ratio | -4.8496357 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.6375575 | 0.09886394 | %p | -2.7937977 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 388.14625 | 10.071146 | price | -2.6637952 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 589.30517 | 23.931141 | price | -4.232798 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0542583 | 0.027354612 | ratio | -2.6637952 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.8030673 | 0.0245716 | %p | -0.51421204 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 228.30556 | 3.0833333 | price | -1.3690183 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 373.87193 | 0.53226992 | price | -0.14256989 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.91486317 | 0.012355495 | ratio | -1.3690183 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0561361 | -0.022595824 | %p | 0.27969519 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 970.95257 | 6.8102767 | price | -0.70635597 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1727.3958 | 23.425574 | price | -1.3747642 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92538905 | 0.0064906934 | ratio | -0.70635597 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.5876263 | -0.061377007 | %p | 1.6820212 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 95.343874 | -1.798419 | price | 1.8513244 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 147.9883 | -7.1728789 | price | 4.6228566 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.99287919 | -0.018728133 | ratio | 1.8513244 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.8959307 | -0.3216624 | %p | 4.4566436 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1374.664 | -53.747036 | price | 3.7627149 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2259.2895 | -35.948916 | price | 1.5662389 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0139621 | -0.039644199 | ratio | 3.7627149 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### ALL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.99034 | 4.5967193 | -0.39362075 | %p | 7.8876538 | improved |
| mae | 674.96363 | 574.12181 | -100.84183 | price | 14.940335 | improved |
| rmse | 1034.3299 | 908.40521 | -125.92466 | price | 12.174517 | improved |
| rmae | 1.1614981 | 1.0287034 | -0.13279472 | ratio | 11.433056 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 4.4935422 | -0.6404234 | %p | 12.474244 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 130.96443 | -17.849802 | price | 11.994688 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 197.87472 | -11.947192 | price | 5.6939681 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 0.94717283 | -0.12909496 | ratio | 11.994688 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 5.8355351 | -0.32108091 | %p | 5.2152174 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 121.24901 | -6.6166008 | price | 5.1746522 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 182.2756 | -4.7879766 | price | 2.5595451 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0474987 | -0.05716237 | ratio | 5.1746522 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 2.9439951 | -0.6508943 | %p | 18.106101 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 535.48617 | -127.34387 | price | 19.212146 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 840.89747 | -161.07593 | price | 16.075869 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.0335678 | -0.24579258 | ratio | 19.212146 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.5798783 | -0.25780864 | %p | 5.3291715 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 101.63745 | -5.3864542 | price | 5.0329449 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 162.15989 | -2.4745513 | price | 1.5030581 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0099367 | -0.053523357 | ratio | 5.0329449 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.1339244 | -0.43996197 | %p | 27.953859 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 1794.4688 | -637.88839 | price | 26.225112 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 2602.9937 | -912.0185 | price | 25.946382 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.3475059 | -0.47900436 | ratio | 26.225112 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 3.6375575 | -0.40854672 | %p | 10.097286 | improved |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 388.14625 | -45.687747 | price | 10.531159 | improved |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 589.30517 | -17.440984 | price | 2.8745108 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.0542583 | -0.12409417 | ratio | 10.531159 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.8030673 | -0.18203627 | %p | 3.6516046 | improved |
| 9001 | 배추/RETAIL | mae | 242.5873 | 228.30556 | -14.281746 | price | 5.8872604 | improved |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 373.87193 | -5.618081 | price | 1.4804292 | improved |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.91486317 | -0.057229634 | ratio | 5.8872604 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.0561361 | -0.74956707 | %p | 8.5122909 | improved |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 970.95257 | -106.88142 | price | 9.9163158 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1727.3958 | -127.59503 | price | 6.8784721 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 0.92538905 | -0.10186584 | ratio | 9.9163158 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.5876263 | -0.1568635 | %p | 4.1891821 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 95.343874 | -4.743083 | price | 4.7389622 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 147.9883 | 3.8776726 | price | -2.690761 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 0.99287919 | -0.049392879 | ratio | 4.7389622 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 6.8959307 | -0.12902469 | %p | 1.8366621 | improved |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1374.664 | -41.73913 | price | 2.9468397 | improved |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2259.2895 | -20.166037 | price | 0.88468657 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0139621 | -0.030787082 | ratio | 2.9468397 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 10, 'worsened': 0, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


## ridge-v2-20261117T065817086357Z-c7af6a37f3b64b39a775f084652d6e52

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065817086357Z-c7af6a37f3b64b39a775f084652d6e52 | no_cross_item | 4.9623906 | 686.58336 | 1033.0742 | 1.1603789 | -7.7314604 (direct) | -7.7120551 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9623906 | 0.35530127 | %p | -7.7120551 | worsened |
| mae | 532.31701 | 686.58336 | 154.26636 | price | -28.980167 | worsened |
| rmse | 943.1701 | 1033.0742 | 89.90414 | price | -9.5321237 | worsened |
| rmae | 1 | 1.1603789 | 0.16037892 | ratio | -16.037892 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.0647954 | 0.29629887 | %p | -6.2136749 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 146.95257 | 8.6837945 | price | -6.2803728 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 207.75218 | -3.0338698 | price | 1.4393124 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0628037 | 0.062803728 | ratio | -6.2803728 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1789751 | 0.67691334 | %p | -12.302903 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 129.19763 | 13.44664 | price | -11.616869 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 187.69725 | 16.561158 | price | -9.6771862 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1161687 | 0.11616869 | ratio | -11.616869 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5312177 | 0.63781429 | %p | -22.043739 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 652.40711 | 134.31225 | price | -25.924259 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 949.61301 | 121.14953 | price | -14.6234 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2592426 | 0.25924259 | ratio | -25.924259 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6643931 | 0.15775117 | %p | -3.500415 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.61355 | 1.9760956 | price | -1.9635788 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.79055 | -0.072543871 | price | 0.045664396 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 1.0196358 | 0.019635788 | ratio | -1.9635788 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.6573274 | 0.85998176 | %p | -107.85557 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2551.6696 | 1219.9732 | price | -91.610459 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3518.4367 | 645.24632 | price | -22.457485 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.9161046 | 0.91610459 | ratio | -91.610459 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.9552015 | 0.50551751 | %p | -14.654023 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 423.62846 | 55.458498 | price | -15.063287 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 599.40341 | 47.04898 | price | -8.5178967 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1506329 | 0.15063287 | ratio | -15.063287 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9513494 | -0.38045187 | %p | 7.1355223 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 239.25794 | -10.293651 | price | 4.1248589 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 379.91583 | -30.140659 | price | 7.3503675 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.95875141 | -0.041248589 | ratio | 4.1248589 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.7597765 | 0.17318279 | %p | -2.0168975 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1071.1186 | 21.881423 | price | -2.0854602 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1878.7387 | 47.880058 | price | -2.6151696 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0208546 | 0.020854602 | ratio | -2.0854602 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6914296 | 0.063871719 | %p | -1.760736 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 98.909091 | 2.8814229 | price | -3.0006174 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.93031 | -12.952571 | price | 8.3628165 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0300062 | 0.030006174 | ratio | -3.0006174 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1694404 | 0.56213311 | %p | -8.5077488 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1450.0791 | 94.343874 | price | -6.9588718 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2308.4644 | 67.354999 | price | -3.0054311 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0695887 | 0.069588718 | ratio | -6.9588718 | worsened |
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
| mape | 4.6062595 | 4.9623906 | 0.35613113 | %p | -7.7314604 | worsened |
| mae | 565.55167 | 686.58336 | 121.03169 | price | -21.400642 | worsened |
| rmse | 926.40586 | 1033.0742 | 106.66838 | price | -11.514217 | worsened |
| rmae | 1.0199316 | 1.1603789 | 0.14044735 | ratio | -13.770272 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.0647954 | 0.3349844 | %p | -7.0824056 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 146.95257 | 9.1225296 | price | -6.6186803 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 207.75218 | -1.4267624 | price | 0.68207746 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0628037 | 0.065976788 | ratio | -6.6186803 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1789751 | 0.44681878 | %p | -7.7949511 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 129.19763 | 9.5335968 | price | -7.9669694 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 187.69725 | 8.9582637 | price | -5.0119249 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1161687 | 0.082362984 | ratio | -7.9669694 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5312177 | 0.8507791 | %p | -31.740295 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 652.40711 | 161.80237 | price | -32.980189 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 949.61301 | 170.53115 | price | -21.888734 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2592426 | 0.3123026 | ratio | -32.980189 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6643931 | 0.073392838 | %p | -1.5986241 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.61355 | -0.34262948 | price | 0.33279158 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.79055 | -6.2445198 | price | 3.7837532 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0196358 | -0.0034045922 | ratio | 0.33279158 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.6573274 | 0.59065628 | %p | -55.373794 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2551.6696 | 840.20089 | price | -49.092389 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3518.4367 | 679.49656 | price | -23.934867 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.9161046 | 0.63092524 | ratio | -49.092389 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.9552015 | 0.41650799 | %p | -11.770106 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 423.62846 | 45.55336 | price | -12.04876 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 599.40341 | 34.029378 | price | -6.0189142 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1506329 | 0.12372916 | ratio | -12.04876 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9513494 | 0.17285364 | %p | -3.6173234 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 239.25794 | 14.035714 | price | -6.2319402 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 379.91583 | 6.5761695 | price | -1.7614441 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.95875141 | 0.056243739 | ratio | -6.2319402 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.7597765 | 0.68104456 | %p | -8.4300923 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1071.1186 | 106.97628 | price | -11.095487 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1878.7387 | 174.76841 | price | -10.256541 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0208546 | 0.10195625 | ratio | -11.095487 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6914296 | 0.042426381 | %p | -1.1626841 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 98.909091 | 1.7667984 | price | -1.8187737 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.93031 | -13.230869 | price | 8.5271774 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0300062 | 0.018398847 | ratio | -1.8187737 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1694404 | -0.048152688 | %p | 0.66715714 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1450.0791 | 21.667984 | price | -1.5169292 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2308.4644 | 13.226033 | price | -0.5762379 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0695887 | 0.015982461 | ratio | -1.5169292 | worsened |
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
| mape | 4.99034 | 4.9623906 | -0.027949419 | %p | 0.56007043 | improved |
| mae | 674.96363 | 686.58336 | 11.619728 | price | -1.721534 | worsened |
| rmse | 1034.3299 | 1033.0742 | -1.2556354 | price | 0.12139603 | improved |
| rmae | 1.1614981 | 1.1603789 | -0.0011191742 | ratio | 0.096356094 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.0647954 | -0.06917015 | %p | 1.3473045 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 146.95257 | -1.8616601 | price | 1.250996 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 207.75218 | -2.0697281 | price | 0.98642135 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0628037 | -0.013464067 | ratio | 1.250996 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1789751 | 0.022359167 | %p | -0.363173 | worsened |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 129.19763 | 1.3320158 | price | -1.0417311 | worsened |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 187.69725 | 0.63366897 | price | -0.33874524 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1161687 | 0.011507598 | ratio | -1.0417311 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5312177 | -0.0636717 | %p | 1.7711727 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 652.40711 | -10.422925 | price | 1.5724883 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 949.61301 | -52.360388 | price | 5.2257264 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2592426 | -0.020117792 | ratio | 1.5724883 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.6643931 | -0.17329391 | %p | 3.5821645 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 102.61355 | -4.4103586 | price | 4.1209098 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 158.79055 | -5.8438891 | price | 3.5496153 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0196358 | -0.043824228 | ratio | 4.1209098 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.6573274 | 0.08344107 | %p | -5.3015943 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2551.6696 | 119.3125 | price | -4.9052213 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3518.4367 | 3.4245087 | price | -0.097425228 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.9161046 | 0.089594368 | ratio | -4.9052213 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 3.9552015 | -0.090902666 | %p | 2.2466714 | improved |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 423.62846 | -10.205534 | price | 2.3524052 | improved |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 599.40341 | -7.3427465 | price | 1.2101843 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1506329 | -0.027719626 | ratio | 2.3524052 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9513494 | -0.03375423 | %p | 0.67710187 | improved |
| 9001 | 배추/RETAIL | mae | 242.5873 | 239.25794 | -3.3293651 | price | 1.37244 | improved |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 379.91583 | 0.42581849 | price | -0.11220809 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.95875141 | -0.01334139 | ratio | 1.37244 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.7597765 | -0.04592669 | %p | 0.52155619 | improved |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1071.1186 | -6.715415 | price | 0.62304725 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1878.7387 | 23.747806 | price | -1.2802115 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0208546 | -0.0064002833 | ratio | 0.62304725 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.6914296 | -0.053060107 | %p | 1.4170184 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 98.909091 | -1.1778656 | price | 1.1768423 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 141.93031 | -2.1803175 | price | 1.5129471 | improved |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0300062 | -0.012265898 | ratio | 1.1768423 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.1694404 | 0.14448502 | %p | -2.0567393 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1450.0791 | 33.675889 | price | -2.3775638 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2308.4644 | 29.008913 | price | -1.2726247 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0695887 | 0.024839578 | ratio | -2.3775638 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

