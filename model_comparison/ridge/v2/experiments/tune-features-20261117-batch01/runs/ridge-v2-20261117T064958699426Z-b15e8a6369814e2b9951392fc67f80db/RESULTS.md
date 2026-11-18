
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

