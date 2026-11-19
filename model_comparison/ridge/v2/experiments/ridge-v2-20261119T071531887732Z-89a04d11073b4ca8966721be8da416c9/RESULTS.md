
## ridge-v2-20261119T071531887732Z-89a04d11073b4ca8966721be8da416c9

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071531887732Z-89a04d11073b4ca8966721be8da416c9 | no_ow_pricedyn | 4.5712055 | 579.95203 | 934.2908 | 1.0289936 | 0.76100735 (direct) | 0.77888294 (direct) | 6 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5712055 | -0.035883833 | %p | 0.77888294 | improved |
| mae | 532.31701 | 579.95203 | 47.63502 | price | -8.948619 | worsened |
| rmse | 943.1701 | 934.2908 | -8.8793013 | price | 0.94143159 | improved |
| rmae | 1 | 1.0289936 | 0.028993597 | ratio | -2.8993597 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4698804 | -0.29861614 | %p | 6.2622703 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.88142 | -8.3873518 | price | 6.0659768 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 196.69348 | -14.092572 | price | 6.6857235 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93934023 | -0.060659768 | ratio | 6.0659768 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6914844 | 0.18942264 | %p | -3.4427575 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 118.36364 | 2.6126482 | price | -2.2571282 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 175.81669 | 4.6806041 | price | -2.7350187 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0225713 | 0.022571282 | ratio | -2.2571282 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.0870506 | 0.19364726 | %p | -6.6927157 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 557.25296 | 39.158103 | price | -7.5580952 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 871.22298 | 42.759495 | price | -5.1613012 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.075581 | 0.075580952 | ratio | -7.5580952 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.609785 | 0.10314311 | %p | -2.2886912 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.72112 | 2.0836653 | price | -2.0704671 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 162.01641 | 3.1533228 | price | -1.984931 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0207047 | 0.020704671 | ratio | -2.0704671 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1848472 | 0.38750151 | %p | -48.598936 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1874.5357 | 542.83929 | price | -40.76299 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2900.9644 | 27.774007 | price | -0.96666086 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.4076299 | 0.4076299 | ratio | -40.76299 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4270407 | -0.022643312 | %p | 0.656388 | improved |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 364.7668 | -3.4031621 | price | 0.92434539 | improved |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 567.6617 | 15.307265 | price | -2.7712758 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 0.99075655 | -0.0092434539 | ratio | 0.92434539 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.6807361 | -0.65106519 | %p | 12.21098 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.64683 | -26.904762 | price | 10.781243 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 360.47983 | -49.576652 | price | 12.090201 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89218757 | -0.10781243 | ratio | 10.781243 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0197986 | -0.5667951 | %p | 6.6009307 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 964.11858 | -85.118577 | price | 8.112425 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1715.7007 | -115.15793 | price | 6.289832 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91887575 | -0.08112425 | ratio | 8.112425 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6574163 | 0.029858422 | %p | -0.82309979 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.304348 | 1.2766798 | price | -1.3294917 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 147.39839 | -7.4844959 | price | 4.8323583 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0132949 | 0.013294917 | ratio | -1.3294917 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.8840158 | 0.27670846 | %p | -4.1879157 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1367.9289 | 12.193676 | price | -0.89941429 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2244.9534 | 3.8439448 | price | -0.17151973 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0089941 | 0.0089941429 | ratio | -0.89941429 | worsened |
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
| mape | 4.6062595 | 4.5712055 | -0.035053973 | %p | 0.76100735 | improved |
| mae | 565.55167 | 579.95203 | 14.400354 | price | -2.5462491 | worsened |
| rmse | 926.40586 | 934.2908 | 7.8849396 | price | -0.85113231 | worsened |
| rmae | 1.0199316 | 1.0289936 | 0.0090620288 | ratio | -0.88849381 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4698804 | -0.25993061 | %p | 5.4955814 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.88142 | -7.9486166 | price | 5.7669697 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 196.69348 | -12.485465 | price | 5.9687963 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93934023 | -0.057486707 | ratio | 5.7669697 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6914844 | -0.040671911 | %p | 0.70953945 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 118.36364 | -1.3003953 | price | 1.0867052 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 175.81669 | -2.9222903 | price | 1.6349485 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0225713 | -0.01123442 | ratio | 1.0867052 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.0870506 | 0.40661207 | %p | -15.16961 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 557.25296 | 66.648221 | price | -13.584912 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 871.22298 | 92.141118 | price | -11.826885 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.075581 | 0.12864096 | ratio | -13.584912 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.609785 | 0.018784783 | %p | -0.40916536 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.72112 | -0.23505976 | price | 0.2283105 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 162.01641 | -3.0186531 | price | 1.829098 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0207047 | -0.0023357086 | ratio | 0.2283105 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1848472 | 0.11817603 | %p | -11.078957 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1874.5357 | 163.06696 | price | -9.5278961 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2900.9644 | 62.024243 | price | -2.1847675 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.4076299 | 0.12245055 | ratio | -9.5278961 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4270407 | -0.11165283 | %p | 3.1551992 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 364.7668 | -13.3083 | price | 3.5200151 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 567.6617 | 2.287663 | price | -0.40462824 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 0.99075655 | -0.036147165 | ratio | 3.5200151 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.6807361 | -0.097759675 | %p | 2.0458253 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.64683 | -2.5753968 | price | 1.1434914 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 360.47983 | -12.859824 | price | 3.4445374 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89218757 | -0.010320098 | ratio | 1.1434914 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0197986 | -0.058933335 | %p | 0.72948744 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 964.11858 | -0.023715415 | price | 0.0024597422 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1715.7007 | 11.730419 | price | -0.6884169 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91887575 | -2.2602531e-05 | ratio | 0.0024597422 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6574163 | 0.0084130834 | %p | -0.2305584 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.304348 | 0.16205534 | price | -0.16682264 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 147.39839 | -7.7627937 | price | 5.0030514 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0132949 | 0.00168759 | ratio | -0.16682264 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.8840158 | -0.33357734 | %p | 4.6217255 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1367.9289 | -60.482213 | price | 4.2342302 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2244.9534 | -50.285021 | price | 2.1908409 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0089941 | -0.044612115 | ratio | 4.2342302 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5712055 | 0.070064202 | %p | -1.5565875 | worsened |
| mae | 557.9753 | 579.95203 | 21.976723 | price | -3.9386551 | worsened |
| rmse | 915.84853 | 934.2908 | 18.442262 | price | -2.0136804 | worsened |
| rmae | 0.99470404 | 1.0289936 | 0.034289552 | ratio | -3.4472115 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4698804 | 0.043452653 | %p | -0.98166411 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.88142 | 1.1343874 | price | -0.88109784 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 196.69348 | 5.1132484 | price | -2.6689854 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93934023 | 0.0082042193 | ratio | -0.88109784 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6914844 | -0.041430101 | %p | 0.72267083 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 118.36364 | -1.1541502 | price | 0.96567233 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 175.81669 | -5.0553919 | price | 2.7950095 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0225713 | -0.0099709749 | ratio | 0.96567233 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 3.0870506 | 0.35273545 | %p | -12.900321 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 557.25296 | 63.478261 | price | -12.855713 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 871.22298 | 82.965086 | price | -10.52512 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 1.075581 | 0.12252247 | ratio | -12.855713 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.609785 | 0.18459651 | %p | -4.1714948 | worsened |
| 8 | 양파/RETAIL | mae | 98.860558 | 102.72112 | 3.8605578 | price | -3.9050536 | worsened |
| 8 | 양파/RETAIL | rmse | 158.71298 | 162.01641 | 3.3034389 | price | -2.0813918 | worsened |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 1.0207047 | 0.038361045 | ratio | -3.9050536 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.1848472 | 0.14394779 | %p | -13.829174 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1874.5357 | 192.83929 | price | -11.46695 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2900.9644 | 106.55614 | price | -3.8131915 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.4076299 | 0.14480724 | ratio | -11.46695 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4270407 | -0.030650621 | %p | 0.88644757 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 364.7668 | -5.0869565 | price | 1.3753967 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 567.6617 | 16.074333 | price | -2.9141952 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 0.99075655 | -0.01381687 | ratio | 1.3753967 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.6807361 | -0.073536131 | %p | 1.5467379 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 222.64683 | 0.047619048 | price | -0.021392281 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 360.47983 | 3.2155089 | price | -0.90003637 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89218757 | 0.00019081845 | ratio | -0.021392281 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.0197986 | 0.08000557 | %p | -1.0076531 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 964.11858 | 4.2727273 | price | -0.44514724 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1715.7007 | 5.816777 | price | -0.3401855 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.91887575 | 0.0040722226 | ratio | -0.44514724 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.6574163 | 0.30033389 | %p | -8.9462767 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 97.304348 | 8.0355731 | price | -9.0015497 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 147.39839 | 6.2675087 | price | -4.4409195 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 1.0132949 | 0.083679769 | ratio | -9.0015497 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.8840158 | -0.25881298 | %p | 3.6233962 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1367.9289 | -47.660079 | price | 3.3668022 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2244.9534 | -39.834028 | price | 1.7434457 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0089941 | -0.035154416 | ratio | 3.3668022 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

