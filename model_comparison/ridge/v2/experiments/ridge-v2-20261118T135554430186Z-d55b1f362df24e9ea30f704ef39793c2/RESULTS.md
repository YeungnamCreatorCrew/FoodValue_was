
## ridge-v2-20261118T135554430186Z-d55b1f362df24e9ea30f704ef39793c2

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135554430186Z-d55b1f362df24e9ea30f704ef39793c2 | v1feat_cross | 4.5686864 | 561.06115 | 923.10566 | 1.015589 | 0.81569688 (direct) | 0.83356262 (direct) | 6 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5686864 | -0.038402975 | %p | 0.83356262 | improved |
| mae | 532.31701 | 561.06115 | 28.744148 | price | -5.3998177 | worsened |
| rmse | 943.1701 | 923.10566 | -20.064436 | price | 2.1273401 | improved |
| rmae | 1 | 1.015589 | 0.015588998 | ratio | -1.5588998 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5485647 | -0.21993183 | %p | 4.6121839 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 132.79447 | -5.4743083 | price | 3.959179 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 198.25985 | -12.526199 | price | 5.9426131 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.96040821 | -0.03959179 | ratio | 3.959179 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8303609 | 0.32829912 | %p | -5.9668381 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 121.3083 | 5.5573123 | price | -4.8010927 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 181.99011 | 10.854018 | price | -6.3423312 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0480109 | 0.048010927 | ratio | -4.8010927 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.8337759 | -0.059627473 | %p | 2.0608075 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 508.80237 | -9.2924901 | price | 1.7935886 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 835.12668 | 6.6631953 | price | -0.80428352 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.98206411 | -0.017935886 | ratio | 1.7935886 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6185251 | 0.11188322 | %p | -2.4826294 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.77689 | 2.1394422 | price | -2.1258907 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 163.61714 | 4.7540515 | price | -2.9925462 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0212589 | 0.021258907 | ratio | -2.1258907 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0652587 | 0.26791303 | %p | -33.600612 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1707.75 | 376.05357 | price | -28.238686 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2807.0542 | -66.136243 | price | 2.3018399 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2823869 | 0.28238686 | ratio | -28.238686 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5657216 | 0.11603754 | %p | -3.363715 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 381.35968 | 13.189723 | price | -3.5825094 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 573.98502 | 21.630583 | price | -3.9160695 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0358251 | 0.035825094 | ratio | -3.5825094 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7257219 | -0.60607933 | %p | 11.367253 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 223.4127 | -26.138889 | price | 10.474343 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 362.53961 | -47.516876 | price | 11.587886 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89525657 | -0.10474343 | ratio | 10.474343 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9574773 | -0.62911647 | %p | 7.3267292 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 956.29249 | -92.944664 | price | 8.8583085 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1684.8676 | -145.99104 | price | 7.9739114 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91141691 | -0.088583085 | ratio | 8.8583085 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6201683 | -0.0073896053 | %p | 0.20370744 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 96.162055 | 0.13438735 | price | -0.13994649 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 148.72224 | -6.1606443 | price | 3.9776147 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0013995 | 0.0013994649 | ratio | -0.13994649 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9212894 | 0.31398206 | %p | -4.7520426 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1379.9526 | 24.217391 | price | -1.7862922 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2274.8942 | 33.7848 | price | -1.5075034 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0178629 | 0.017862922 | ratio | -1.7862922 | worsened |
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
| mape | 4.6062595 | 4.5686864 | -0.037573115 | %p | 0.81569688 | improved |
| mae | 565.55167 | 561.06115 | -4.4905185 | price | 0.79400676 | improved |
| rmse | 926.40586 | 923.10566 | -3.300195 | price | 0.35623641 | improved |
| rmae | 1.0199316 | 1.015589 | -0.0043425698 | ratio | 0.4257707 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5485647 | -0.1812463 | %p | 3.8319988 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 132.79447 | -5.0355731 | price | 3.6534656 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 198.25985 | -10.919092 | price | 5.2199767 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.96040821 | -0.03641873 | ratio | 3.6534656 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8303609 | 0.098204567 | %p | -1.7132221 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 121.3083 | 1.6442688 | price | -1.374071 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 181.99011 | 3.2511232 | price | -1.8189223 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0480109 | 0.014205225 | ratio | -1.374071 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.8337759 | 0.15333734 | %p | -5.7206062 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 508.80237 | 18.197628 | price | -3.7092239 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 835.12668 | 56.044818 | price | -7.1937008 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.98206411 | 0.035124125 | ratio | -3.7092239 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6185251 | 0.027524884 | %p | -0.59954003 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.77689 | -0.17928287 | price | 0.17413513 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 163.61714 | -1.4179244 | price | 0.85916551 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0212589 | -0.0017814727 | ratio | 0.17413513 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0652587 | -0.0014124485 | %p | 0.13241649 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1707.75 | -3.71875 | price | 0.21728413 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2807.0542 | -31.886007 | price | 1.1231659 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2823869 | -0.0027924908 | ratio | 0.21728413 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5657216 | 0.027028023 | %p | -0.76378535 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 381.35968 | 3.284585 | price | -0.86876522 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 573.98502 | 8.6109818 | price | -1.5230593 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0358251 | 0.0089213823 | ratio | -0.86876522 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7257219 | -0.052773823 | %p | 1.1044024 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 223.4127 | -1.8095238 | price | 0.80343928 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 362.53961 | -10.800048 | price | 2.8928211 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89525657 | -0.0072511012 | ratio | 0.80343928 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9574773 | -0.1212547 | %p | 1.5009125 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 956.29249 | -7.8498024 | price | 0.81417467 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1684.8676 | -19.102693 | price | 1.1210696 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91141691 | -0.0074814377 | ratio | 0.81417467 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6201683 | -0.028834943 | %p | 0.79021424 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 96.162055 | -0.98023715 | price | 1.0090735 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 148.72224 | -6.4389421 | price | 4.1498409 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0013995 | -0.010207862 | ratio | 1.0090735 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9212894 | -0.29630374 | %p | 4.1052985 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1379.9526 | -48.458498 | price | 3.3924757 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2274.8942 | -20.344165 | price | 0.88636394 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0178629 | -0.035743336 | ratio | 3.3924757 | improved |
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
| mape | 4.5391348 | 4.5686864 | 0.029551587 | %p | -0.65104009 | worsened |
| mae | 553.57874 | 561.06115 | 7.4824102 | price | -1.3516433 | worsened |
| rmse | 910.2849 | 923.10566 | 12.820761 | price | -1.4084339 | worsened |
| rmae | 1.0021178 | 1.015589 | 0.013471182 | ratio | -1.3442712 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.439733 | 4.5485647 | 0.10883169 | %p | -2.4513116 | worsened |
| 1 | 대파/RETAIL | mae | 129.36759 | 132.79447 | 3.4268775 | price | -2.6489459 | worsened |
| 1 | 대파/RETAIL | rmse | 192.41889 | 198.25985 | 5.8409647 | price | -3.0355465 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93562404 | 0.96040821 | 0.024784175 | ratio | -2.6489459 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.8491429 | 5.8303609 | -0.018782029 | %p | 0.32110738 | improved |
| 2 | 대파/WHOLESALE | mae | 122.22134 | 121.3083 | -0.91304348 | price | 0.74704094 | improved |
| 2 | 대파/WHOLESALE | rmse | 182.97472 | 181.99011 | -0.98460948 | price | 0.53811231 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0558989 | 1.0480109 | -0.0078879973 | ratio | 0.74704094 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.728634 | 2.8337759 | 0.1051419 | %p | -3.8532798 | worsened |
| 7 | 양파/WHOLESALE | mae | 497.18972 | 508.80237 | 11.612648 | price | -2.3356573 | worsened |
| 7 | 양파/WHOLESALE | rmse | 782.2103 | 835.12668 | 52.916372 | price | -6.7649801 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95964998 | 0.98206411 | 0.022414135 | ratio | -2.3356573 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5769182 | 4.6185251 | 0.041606963 | %p | -0.90906068 | worsened |
| 8 | 양파/RETAIL | mae | 102.04382 | 102.77689 | 0.73306773 | price | -0.7183852 | worsened |
| 8 | 양파/RETAIL | rmse | 160.99468 | 163.61714 | 2.6224641 | price | -1.6289135 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0139747 | 1.0212589 | 0.0072842439 | ratio | -0.7183852 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.010062 | 1.0652587 | 0.055196688 | %p | -5.4646831 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1620.5357 | 1707.75 | 87.214286 | price | -5.3818182 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2724.0606 | 2807.0542 | 82.993585 | price | -3.0466864 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2168957 | 1.2823869 | 0.065491116 | ratio | -5.3818182 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5739886 | 3.5657216 | -0.0082670225 | %p | 0.23131082 | improved |
| 10 | 깐마늘/RETAIL | mae | 381.96443 | 381.35968 | -0.60474308 | price | 0.15832445 | improved |
| 10 | 깐마늘/RETAIL | rmse | 572.99301 | 573.98502 | 0.99201049 | price | -0.17312785 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0374677 | 1.0358251 | -0.001642565 | ratio | 0.15832445 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7408145 | 4.7257219 | -0.015092612 | %p | 0.31835483 | improved |
| 9001 | 배추/RETAIL | mae | 222.59524 | 223.4127 | 0.81746032 | price | -0.3672407 | worsened |
| 9001 | 배추/RETAIL | rmse | 355.715 | 362.53961 | 6.8246127 | price | -1.918562 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89198085 | 0.89525657 | 0.0032757168 | ratio | -0.3672407 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9415835 | 7.9574773 | 0.015893724 | %p | -0.20013293 | worsened |
| 9002 | 배추/WHOLESALE | mae | 954.7747 | 956.29249 | 1.5177866 | price | -0.15896803 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1695.6307 | 1684.8676 | -10.763156 | price | 0.63475825 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.90997035 | 0.91141691 | 0.001446562 | ratio | -0.15896803 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.4647414 | 3.6201683 | 0.15542696 | %p | -4.4859613 | worsened |
| 9011 | 무/RETAIL | mae | 91.932806 | 96.162055 | 4.229249 | price | -4.6003697 | worsened |
| 9011 | 무/RETAIL | rmse | 142.69508 | 148.72224 | 6.0271606 | price | -4.2238041 | worsened |
| 9011 | 무/RETAIL | rmae | 0.95735748 | 1.0013995 | 0.044041984 | ratio | -4.6003697 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0657298 | 6.9212894 | -0.14444039 | %p | 2.0442388 | improved |
| 9012 | 무/WHOLESALE | mae | 1413.1621 | 1379.9526 | -33.209486 | price | 2.3500126 | improved |
| 9012 | 무/WHOLESALE | rmse | 2293.156 | 2274.8942 | -18.261792 | price | 0.79636064 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0423585 | 1.0178629 | -0.024495555 | ratio | 2.3500126 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

