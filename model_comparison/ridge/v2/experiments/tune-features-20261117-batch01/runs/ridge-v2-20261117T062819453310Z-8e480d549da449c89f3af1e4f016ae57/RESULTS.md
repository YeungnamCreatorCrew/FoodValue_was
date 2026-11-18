
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

