
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

