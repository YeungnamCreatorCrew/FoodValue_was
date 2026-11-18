
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

