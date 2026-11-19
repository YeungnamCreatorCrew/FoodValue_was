
## ridge-v2-20261119T084634364391Z-fe6c5bac24aa4b5795455f62f2d4c2fa

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T084634364391Z-fe6c5bac24aa4b5795455f62f2d4c2fa | no_ow_w1095 | 5.0256149 | 673.25961 | 1040.3136 | 1.0820577 | N/A | -2.3016198 (direct) | N/A |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.9125468 | 5.0256149 | 0.11306815 | %p | -2.3016198 | worsened |
| mae | 569.79222 | 673.25961 | 103.46739 | price | -18.158792 | worsened |
| rmse | 989.64537 | 1040.3136 | 50.668185 | price | -5.1198324 | worsened |
| rmae | 1 | 1.0820577 | 0.082057697 | ratio | -8.2057697 | worsened |
| success_rate_pct | 100 | 99.201774 | -0.79822616 | %p | -0.79822616 | worsened |
| valid_predictions | 11275 | 11185 | -90 | count | -0.79822616 | count_change |
| failed_predictions | 0 | 90 | 90 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1984334 | 5.0153245 | -0.18310888 | %p | 3.5223859 | improved |
| 1 | 대파/RETAIL | mae | 149.08566 | 144.68706 | -4.3986014 | price | 2.9503852 | improved |
| 1 | 대파/RETAIL | rmse | 216.99605 | 206.44659 | -10.549463 | price | 4.8615923 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.97049615 | -0.029503852 | ratio | 2.9503852 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.9408146 | 6.3617979 | 0.42098334 | %p | -7.0862898 | worsened |
| 2 | 대파/WHOLESALE | mae | 124.70979 | 131.77448 | 7.0646853 | price | -5.6649003 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.65144 | 186.32215 | 7.6707102 | price | -4.2936738 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.056649 | 0.056649003 | ratio | -5.6649003 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.183793 | 3.6006523 | 0.41685931 | %p | -13.093166 | worsened |
| 7 | 양파/WHOLESALE | mae | 574.59965 | 653.09091 | 78.491259 | price | -13.660165 | worsened |
| 7 | 양파/WHOLESALE | rmse | 921.70243 | 985.05607 | 63.353641 | price | -6.8735461 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1366016 | 0.13660165 | ratio | -13.660165 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.8732295 | 4.8530827 | -0.020146815 | %p | 0.41341815 | improved |
| 8 | 양파/RETAIL | mae | 108.3254 | 106.67196 | -1.6534392 | price | 1.5263633 | improved |
| 8 | 양파/RETAIL | rmse | 170.67764 | 163.86548 | -6.8121677 | price | 3.9912478 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.98473637 | -0.015263633 | ratio | 1.5263633 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 1134 | 1134 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79998097 | 1.4529708 | 0.65298987 | %p | -81.625675 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1336.6197 | 2286.2414 | 949.62173 | price | -71.046515 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2880.4307 | 3388.2468 | 507.81602 | price | -17.629864 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.7104652 | 0.71046515 | ratio | -71.046515 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 90.945674 | -9.054326 | %p | -9.054326 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 994 | 904 | -90 | count | -9.054326 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 90 | 90 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.8302262 | 3.8879836 | 0.057757391 | %p | -1.5079368 | worsened |
| 10 | 깐마늘/RETAIL | mae | 408.16434 | 410.54371 | 2.3793706 | price | -0.58294428 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 568.62765 | 572.03407 | 3.4064159 | price | -0.59905913 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0058294 | 0.0058294428 | ratio | -0.58294428 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.2405422 | 4.8436732 | -0.39686901 | %p | 7.5730524 | improved |
| 9001 | 배추/RETAIL | mae | 240.76558 | 225.40123 | -15.364355 | price | 6.381458 | improved |
| 9001 | 배추/RETAIL | rmse | 389.84049 | 357.1766 | -32.663889 | price | 8.3787831 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.93618542 | -0.06381458 | ratio | 6.381458 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 1139 | 1139 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.1934766 | 7.1406158 | -0.052860859 | %p | 0.73484438 | improved |
| 9002 | 배추/WHOLESALE | mae | 1004.0428 | 989.88199 | -14.160839 | price | 1.410382 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1655.5564 | 1625.7467 | -29.809699 | price | 1.8005849 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.98589618 | -0.01410382 | ratio | 1.410382 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 4.2492996 | 4.2900494 | 0.040749776 | %p | -0.95897631 | worsened |
| 9011 | 무/RETAIL | mae | 111.17308 | 112.81731 | 1.6442308 | price | -1.4789829 | worsened |
| 9011 | 무/RETAIL | rmse | 175.91296 | 170.21935 | -5.6936092 | price | 3.2366058 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0147898 | 0.014789829 | ratio | -1.4789829 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 8.6156715 | 8.8099989 | 0.19432737 | %p | -2.2555105 | worsened |
| 9012 | 무/WHOLESALE | mae | 1640.4362 | 1671.486 | 31.049825 | price | -1.8927786 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2738.0579 | 2748.0218 | 9.9638895 | price | -0.36390354 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0189278 | 0.018927786 | ratio | -1.8927786 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

