
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

