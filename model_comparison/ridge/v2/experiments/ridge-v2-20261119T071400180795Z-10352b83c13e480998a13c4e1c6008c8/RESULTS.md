
## ridge-v2-20261119T071400180795Z-10352b83c13e480998a13c4e1c6008c8

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071400180795Z-10352b83c13e480998a13c4e1c6008c8 | no_ow_w1095 | 4.5840538 | 593.09087 | 935.81308 | 1.0373233 | 0.48207553 (direct) | 0.50000136 (direct) | 5 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5840538 | -0.023035509 | %p | 0.50000136 | improved |
| mae | 532.31701 | 593.09087 | 60.773867 | price | -11.416856 | worsened |
| rmse | 943.1701 | 935.81308 | -7.3570156 | price | 0.78003062 | improved |
| rmae | 1 | 1.0373233 | 0.03732334 | ratio | -3.732334 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.3569852 | -0.41151134 | %p | 8.6297922 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 126.72727 | -11.541502 | price | 8.34715 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 194.35071 | -16.435342 | price | 7.7971679 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.9165285 | -0.0834715 | ratio | 8.34715 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7299948 | 0.22793305 | %p | -4.1426843 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 118.83004 | 3.0790514 | price | -2.6600649 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.6853 | 7.5492055 | price | -4.4112294 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0266006 | 0.026600649 | ratio | -2.6600649 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.0823124 | 0.18890906 | %p | -6.528957 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 552.1502 | 34.055336 | price | -6.5731854 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 841.6217 | 13.158222 | price | -1.5882682 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.0657319 | 0.065731854 | ratio | -6.5731854 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3346761 | -0.17196586 | %p | 3.8158314 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 95.430279 | -5.2071713 | price | 5.1741884 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 153.70154 | -5.1615524 | price | 3.249057 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.94825812 | -0.051741884 | ratio | 5.1741884 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.2666733 | 0.4693276 | %p | -58.861247 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1999.9464 | 668.25 | price | -50.180355 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2876.0563 | 2.8658754 | price | -0.099745406 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.5018036 | 0.50180355 | ratio | -50.180355 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4599644 | 0.01028038 | %p | -0.29800933 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 366.49407 | -1.6758893 | price | 0.45519448 | improved |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 553.54559 | 1.1911604 | price | -0.21565147 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 0.99544806 | -0.0045519448 | ratio | 0.45519448 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9285168 | -0.40328441 | %p | 7.5637555 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 234.59921 | -14.952381 | price | 5.9916994 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 401.0594 | -8.9970899 | price | 2.1941099 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.94008301 | -0.059916994 | ratio | 5.9916994 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.2574769 | -0.32911679 | %p | 3.8329144 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 996.28063 | -52.956522 | price | 5.0471451 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1790.7143 | -40.144302 | price | 2.192649 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.94952855 | -0.050471451 | ratio | 5.0471451 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7521892 | 0.12463126 | %p | -3.4356793 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.913043 | 3.8853755 | price | -4.0461 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 150.32368 | -4.5592008 | price | 2.9436441 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.040461 | 0.040461 | ratio | -4.0461 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.6717493 | 0.064441957 | %p | -0.97531345 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1340.5375 | -15.197628 | price | 1.120988 | improved |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2218.0723 | -23.037131 | price | 1.0279343 | improved |
| 9012 | 무/WHOLESALE | rmae | 1 | 0.98879012 | -0.01120988 | ratio | 1.120988 | improved |
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
| mape | 4.6062595 | 4.5840538 | -0.02220565 | %p | 0.48207553 | improved |
| mae | 565.55167 | 593.09087 | 27.539201 | price | -4.8694403 | worsened |
| rmse | 926.40586 | 935.81308 | 9.4072253 | price | -1.015454 | worsened |
| rmae | 1.0199316 | 1.0373233 | 0.017391772 | ratio | -1.7051901 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.3569852 | -0.37282582 | %p | 7.8824675 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 126.72727 | -11.102767 | price | 8.0554042 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 194.35071 | -14.828235 | price | 7.0887799 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.9165285 | -0.080298439 | ratio | 8.0554042 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7299948 | -0.0021615055 | %p | 0.037708418 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 118.83004 | -0.83399209 | price | 0.69694467 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.6853 | -0.053688919 | price | 0.03003761 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0266006 | -0.0072050538 | ratio | 0.69694467 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.0823124 | 0.40187387 | %p | -14.99284 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 552.1502 | 61.545455 | price | -12.544814 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 841.6217 | 62.539845 | price | -8.0273779 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.0657319 | 0.11879186 | ratio | -12.544814 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3346761 | -0.25632419 | %p | 5.5831883 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 95.430279 | -7.5258964 | price | 7.3098057 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 153.70154 | -11.333528 | price | 6.8673455 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.94825812 | -0.074782264 | ratio | 7.3098057 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.2666733 | 0.20000213 | %p | -18.750121 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1999.9464 | 288.47768 | price | -16.855562 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2876.0563 | 37.116111 | price | -1.3073932 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.5018036 | 0.2166242 | ratio | -16.855562 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4599644 | -0.078729137 | %p | 2.224808 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 366.49407 | -11.581028 | price | 3.0631554 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 553.54559 | -11.828441 | price | 2.0921444 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 0.99544806 | -0.031455656 | ratio | 3.0631554 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9285168 | 0.1500211 | %p | -3.1395048 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 234.59921 | 9.3769841 | price | -4.1634365 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 401.0594 | 27.719738 | price | -7.4248041 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.94008301 | 0.037575334 | ratio | -4.1634365 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.2574769 | 0.17874498 | %p | -2.2125375 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 996.28063 | 32.13834 | price | -3.3333607 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1790.7143 | 86.744048 | price | -5.090702 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.94952855 | 0.030630196 | ratio | -3.3333607 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7521892 | 0.10318592 | %p | -2.8277836 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.913043 | 2.770751 | price | -2.8522602 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 150.32368 | -4.8374986 | price | 3.1177248 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.040461 | 0.028853674 | ratio | -2.8522602 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.6717493 | -0.54584384 | %p | 7.5626852 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1340.5375 | -87.873518 | price | 6.1518368 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2218.0723 | -77.166097 | price | 3.362008 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 0.98879012 | -0.064816138 | ratio | 6.1518368 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5840538 | 0.082912526 | %p | -1.8420334 | worsened |
| mae | 557.9753 | 593.09087 | 35.115569 | price | -6.2933913 | worsened |
| rmse | 915.84853 | 935.81308 | 19.964548 | price | -2.1798963 | worsened |
| rmae | 0.99470404 | 1.0373233 | 0.042619295 | ratio | -4.2846207 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.3569852 | -0.06944255 | %p | 1.568817 | improved |
| 1 | 대파/RETAIL | mae | 128.74704 | 126.72727 | -2.0197628 | price | 1.568784 | improved |
| 1 | 대파/RETAIL | rmse | 191.58023 | 194.35071 | 2.7704787 | price | -1.4461193 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.9165285 | -0.014607512 | ratio | 1.568784 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.7299948 | -0.0029196955 | %p | 0.050928642 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 118.83004 | -0.68774704 | price | 0.57543488 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 178.6853 | -2.1867905 | price | 1.209026 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0266006 | -0.0059416083 | ratio | 0.57543488 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 3.0823124 | 0.34799725 | %p | -12.727035 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 552.1502 | 58.375494 | price | -11.822293 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 841.6217 | 53.363812 | price | -6.7698418 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 1.0657319 | 0.11267337 | ratio | -11.822293 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3346761 | -0.090512462 | %p | 2.0453922 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 95.430279 | -3.4302789 | price | 3.4698154 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 153.70154 | -5.0114362 | price | 3.1575466 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.94825812 | -0.034085511 | ratio | 3.4698154 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.2666733 | 0.22577389 | %p | -21.69027 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1999.9464 | 318.25 | price | -18.924343 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2876.0563 | 81.648009 | price | -2.9218353 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.5018036 | 0.23898089 | ratio | -18.924343 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4599644 | 0.0022730716 | %p | -0.065739575 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 366.49407 | -3.3596838 | price | 0.90838169 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 553.54559 | 1.9582284 | price | -0.35501691 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 0.99544806 | -0.009125361 | ratio | 0.90838169 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.9285168 | 0.17424465 | %p | -3.665012 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 234.59921 | 12 | price | -5.3908548 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 401.0594 | 43.795071 | price | -12.258451 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.94008301 | 0.04808625 | ratio | -5.3908548 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.2574769 | 0.31768388 | %p | -4.0011607 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 996.28063 | 36.434783 | price | -3.7958994 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1790.7143 | 80.830406 | price | -4.7272453 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.94952855 | 0.034725021 | ratio | -3.7958994 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.7521892 | 0.39510672 | %p | -11.769348 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 99.913043 | 10.644269 | price | -11.923843 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 150.32368 | 9.1928038 | price | -6.5136729 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 1.040461 | 0.11084585 | ratio | -11.923843 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.6717493 | -0.47107949 | %p | 6.595139 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1340.5375 | -75.051383 | price | 5.3017781 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2218.0723 | -66.715104 | price | 2.9199699 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 0.98879012 | -0.055358439 | ratio | 5.3017781 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

