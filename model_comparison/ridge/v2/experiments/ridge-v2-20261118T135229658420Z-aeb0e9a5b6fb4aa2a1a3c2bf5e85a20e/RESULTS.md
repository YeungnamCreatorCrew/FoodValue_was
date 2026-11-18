
## ridge-v2-20261118T135229658420Z-aeb0e9a5b6fb4aa2a1a3c2bf5e85a20e

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T135229658420Z-aeb0e9a5b6fb4aa2a1a3c2bf5e85a20e | v1feat | 4.5391348 | 553.57874 | 910.2849 | 1.0021178 | 1.4572497 (direct) | 1.4749999 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5391348 | -0.067954562 | %p | 1.4749999 | improved |
| mae | 532.31701 | 553.57874 | 21.261737 | price | -3.9941872 | worsened |
| rmse | 943.1701 | 910.2849 | -32.885197 | price | 3.4866666 | improved |
| rmae | 1 | 1.0021178 | 0.0021178169 | ratio | -0.21178169 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.439733 | -0.32876352 | %p | 6.89449 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.36759 | -8.9011858 | price | 6.4375965 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.41889 | -18.367164 | price | 8.7136526 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93562404 | -0.064375965 | ratio | 6.4375965 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8491429 | 0.34708115 | %p | -6.3082016 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 122.22134 | 6.4703557 | price | -5.5898924 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 182.97472 | 11.838627 | price | -6.9176683 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0558989 | 0.055898924 | ratio | -5.5898924 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.728634 | -0.16476938 | %p | 5.6946563 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 497.18972 | -20.905138 | price | 4.0350021 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 782.2103 | -46.253176 | price | 5.5830073 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95964998 | -0.040350021 | ratio | 4.0350021 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5769182 | 0.070276253 | %p | -1.5593929 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.04382 | 1.4063745 | price | -1.3974663 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 160.99468 | 2.1315874 | price | -1.3417763 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0139747 | 0.013974663 | ratio | -1.3974663 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.010062 | 0.21271634 | %p | -26.678058 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1620.5357 | 288.83929 | price | -21.689574 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2724.0606 | -149.12983 | price | 5.1903914 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2168957 | 0.21689574 | ratio | -21.689574 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5739886 | 0.12430456 | %p | -3.6033608 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 381.96443 | 13.794466 | price | -3.7467659 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 572.99301 | 20.638573 | price | -3.7364728 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0374677 | 0.037467659 | ratio | -3.7467659 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7408145 | -0.59098672 | %p | 11.084185 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 222.59524 | -26.956349 | price | 10.801915 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 355.715 | -54.341489 | price | 13.252196 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89198085 | -0.10801915 | ratio | 10.801915 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9415835 | -0.64501019 | %p | 7.5118284 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 954.7747 | -94.462451 | price | 9.0029647 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1695.6307 | -135.22789 | price | 7.3860367 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.90997035 | -0.090029647 | ratio | 9.0029647 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4647414 | -0.16281656 | %p | 4.4883242 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.932806 | -4.0948617 | price | 4.2642519 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 142.69508 | -12.187805 | price | 7.8690457 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.95735748 | -0.042642519 | ratio | 4.2642519 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0657298 | 0.45842245 | %p | -6.938113 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1413.1621 | 57.426877 | price | -4.2358477 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2293.156 | 52.046592 | price | -2.3223584 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0423585 | 0.042358477 | ratio | -4.2358477 | worsened |
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
| mape | 4.6062595 | 4.5391348 | -0.067124702 | %p | 1.4572497 | improved |
| mae | 565.55167 | 553.57874 | -11.972929 | price | 2.1170353 | improved |
| rmse | 926.40586 | 910.2849 | -16.120956 | price | 1.7401613 | improved |
| rmae | 1.0199316 | 1.0021178 | -0.017813751 | ratio | 1.7465634 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.439733 | -0.29007799 | %p | 6.1329721 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.36759 | -8.4624506 | price | 6.1397723 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.41889 | -16.760057 | price | 8.0123059 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93562404 | -0.061202904 | ratio | 6.1397723 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8491429 | 0.1169866 | %p | -2.0408829 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 122.22134 | 2.5573123 | price | -2.1370768 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 182.97472 | 4.2357326 | price | -2.3697867 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0558989 | 0.022093222 | ratio | -2.1370768 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.728634 | 0.048195432 | %p | -1.7980428 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 497.18972 | 6.5849802 | price | -1.342217 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 782.2103 | 3.1284465 | price | -0.40155556 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95964998 | 0.012709989 | ratio | -1.342217 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5769182 | -0.014082079 | %p | 0.30673227 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.04382 | -0.9123506 | price | 0.88615432 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 160.99468 | -4.0403885 | price | 2.4482 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0139747 | -0.0090657165 | ratio | 0.88615432 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.010062 | -0.056609137 | %p | 5.3070843 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1620.5357 | -90.933036 | price | 5.3131578 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2724.0606 | -114.87959 | price | 4.0465661 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2168957 | -0.068283607 | ratio | 5.3131578 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5739886 | 0.035295045 | %p | -0.99740327 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 381.96443 | 3.8893281 | price | -1.0287184 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 572.99301 | 7.6189713 | price | -1.3475984 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0374677 | 0.010563947 | ratio | -1.0287184 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7408145 | -0.037681211 | %p | 0.78855801 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 222.59524 | -2.6269841 | price | 1.1663965 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 355.715 | -17.624661 | price | 4.7208114 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89198085 | -0.010526818 | ratio | 1.1663965 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9415835 | -0.13714842 | %p | 1.6976479 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 954.7747 | -9.3675889 | price | 0.97159818 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1695.6307 | -8.3395372 | price | 0.489418 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.90997035 | -0.0089279996 | ratio | 0.97159818 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4647414 | -0.1842619 | %p | 5.0496502 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.932806 | -5.2094862 | price | 5.3627375 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 142.69508 | -12.466103 | price | 8.0342922 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.95735748 | -0.054249846 | ratio | 5.3627375 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0657298 | -0.15186335 | %p | 2.104072 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1413.1621 | -15.249012 | price | 1.0675507 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2293.156 | -2.0823735 | price | 0.090725806 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0423585 | -0.011247781 | ratio | 1.0675507 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.5391348 | 0.037993473 | %p | -0.84408532 | worsened |
| mae | 557.9753 | 553.57874 | -4.3965605 | price | 0.78794895 | improved |
| rmse | 915.84853 | 910.2849 | -5.5636336 | price | 0.60748403 | improved |
| rmae | 0.99470404 | 1.0021178 | 0.0074137721 | ratio | -0.74532441 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.439733 | 0.013305276 | %p | -0.30058722 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.36759 | 0.62055336 | price | -0.48199429 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 192.41889 | 0.83865682 | price | -0.4377575 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93562404 | 0.0044880224 | ratio | -0.48199429 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.8491429 | 0.11622841 | %p | -2.0273877 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 122.22134 | 2.7035573 | price | -2.2620544 | worsened |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 182.97472 | 2.102631 | price | -1.1624961 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0558989 | 0.023356667 | ratio | -2.2620544 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.728634 | -0.0056811921 | %p | 0.20777386 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 497.18972 | 3.4150198 | price | -0.69161497 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 782.2103 | -6.047586 | price | 0.76720907 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.95964998 | 0.0065914951 | ratio | -0.69161497 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.5769182 | 0.15172965 | %p | -3.4287726 | worsened |
| 8 | 양파/RETAIL | mae | 98.860558 | 102.04382 | 3.1832669 | price | -3.2199565 | worsened |
| 8 | 양파/RETAIL | rmse | 158.71298 | 160.99468 | 2.2817035 | price | -1.4376289 | worsened |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 1.0139747 | 0.031631037 | ratio | -3.2199565 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.010062 | -0.030837379 | %p | 2.9625706 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1620.5357 | -61.160714 | price | 3.6368463 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2724.0606 | -70.347694 | price | 2.5174451 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2168957 | -0.045926919 | ratio | 3.6368463 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.5739886 | 0.11629725 | %p | -3.3634365 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 381.96443 | 12.110672 | price | -3.2744488 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 572.99301 | 21.405641 | price | -3.8807345 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0374677 | 0.032894242 | ratio | -3.2744488 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7408145 | -0.013457667 | %p | 0.28306471 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 222.59524 | -0.003968254 | price | 0.0017826901 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 355.715 | -1.5493281 | price | 0.43366437 | improved |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89198085 | -1.5901538e-05 | ratio | 0.0017826901 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9415835 | 0.0017904802 | %p | -0.022550716 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 954.7747 | -5.0711462 | price | 0.52832924 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1695.6307 | -14.253179 | price | 0.83357586 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.90997035 | -0.0048331745 | ratio | 0.52832924 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4647414 | 0.1076589 | %p | -3.2069187 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 91.932806 | 2.6640316 | price | -2.9842816 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 142.69508 | 1.5641997 | price | -1.1083327 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.95735748 | 0.027742334 | ratio | -2.9842816 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.0657298 | -0.077099 | %p | 1.0793903 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1413.1621 | -2.4268775 | price | 0.17143942 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2293.156 | 8.3686197 | price | -0.36627564 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0423585 | -0.0017900822 | ratio | 0.17143942 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

