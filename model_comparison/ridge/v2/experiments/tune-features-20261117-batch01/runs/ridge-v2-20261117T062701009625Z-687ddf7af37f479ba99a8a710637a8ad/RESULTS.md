
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

