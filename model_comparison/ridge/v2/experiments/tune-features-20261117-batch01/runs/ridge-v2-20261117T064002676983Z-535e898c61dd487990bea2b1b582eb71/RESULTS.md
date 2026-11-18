
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

