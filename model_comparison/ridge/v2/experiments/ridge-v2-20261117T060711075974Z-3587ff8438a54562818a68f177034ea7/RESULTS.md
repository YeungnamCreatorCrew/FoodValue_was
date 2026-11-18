
## ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7 | control | 4.4689544 | 540.2 | 808.30059 | 1.5241743 | N/A | 11.221361 (direct) | N/A |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 5.0338172 | 4.4689544 | -0.56486279 | %p | 11.221361 | improved |
| mae | 482.872 | 540.2 | 57.328 | price | -11.872297 | worsened |
| rmse | 749.19896 | 808.30059 | 59.101631 | price | -7.888643 | worsened |
| rmae | 1 | 1.5241743 | 0.52417429 | ratio | -52.417429 | worsened |
| success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| valid_predictions | 250 | 250 | 0 | count | 0 | count_change |
| failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 6.106342 | 6.5641646 | 0.45782263 | %p | -7.4974941 | worsened |
| 1 | 대파/RETAIL | mae | 196.72 | 213.36 | 16.64 | price | -8.4587231 | worsened |
| 1 | 대파/RETAIL | rmse | 283.12386 | 289.32528 | 6.2014242 | price | -2.1903573 | worsened |
| 1 | 대파/RETAIL | rmae | 1 | 1.0845872 | 0.084587231 | ratio | -8.4587231 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5210907 | 5.0420888 | -0.47900194 | %p | 8.675857 | improved |
| 2 | 대파/WHOLESALE | mae | 150.08 | 136.32 | -13.76 | price | 9.1684435 | improved |
| 2 | 대파/WHOLESALE | rmse | 189.01259 | 169.29832 | -19.714276 | price | 10.430139 | improved |
| 2 | 대파/WHOLESALE | rmae | 1 | 0.90831557 | -0.091684435 | ratio | 9.1684435 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 0.56964827 | 0.68135753 | 0.11170926 | %p | -19.610216 | worsened |
| 7 | 양파/WHOLESALE | mae | 114.4 | 136.84 | 22.44 | price | -19.615385 | worsened |
| 7 | 양파/WHOLESALE | rmse | 147.34992 | 179.70765 | 32.357728 | price | -21.959786 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1961538 | 0.19615385 | ratio | -19.615385 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.1840015 | 4.1329238 | -0.051077748 | %p | 1.220787 | improved |
| 8 | 양파/RETAIL | mae | 77.88 | 76.88 | -1 | price | 1.2840267 | improved |
| 8 | 양파/RETAIL | rmse | 131.22332 | 133.47599 | 2.2526693 | price | -1.7166684 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 0.98715973 | -0.012840267 | ratio | 1.2840267 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.10934516 | 0.75002305 | 0.6406779 | %p | -585.92252 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 152 | 1040 | 888 | price | -584.21053 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 317.49016 | 1229.5211 | 912.03092 | price | -287.26274 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 6.8421053 | 5.8421053 | ratio | -584.21053 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.3761182 | 4.5765013 | 0.20038315 | %p | -4.579016 | worsened |
| 10 | 깐마늘/RETAIL | mae | 377.76 | 395.96 | 18.2 | price | -4.8178738 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 666.29849 | 672.90329 | 6.6048 | price | -0.99126745 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0481787 | 0.048178738 | ratio | -4.8178738 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 9.9534525 | 5.8179989 | -4.1354536 | %p | 41.547931 | improved |
| 9001 | 배추/RETAIL | mae | 371.48 | 212.4 | -159.08 | price | 42.823301 | improved |
| 9001 | 배추/RETAIL | rmse | 473.53754 | 275.16599 | -198.37155 | price | 41.89141 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.57176699 | -0.42823301 | ratio | 42.823301 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 6.2502244 | 4.5333827 | -1.7168417 | %p | 27.46848 | improved |
| 9002 | 배추/WHOLESALE | mae | 703.36 | 520.96 | -182.4 | price | 25.932666 | improved |
| 9002 | 배추/WHOLESALE | rmse | 940.17769 | 816.08671 | -124.09097 | price | 13.198673 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.74067334 | -0.25932666 | ratio | 25.932666 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 4.5469793 | 3.864617 | -0.68236232 | %p | 15.006937 | improved |
| 9011 | 무/RETAIL | mae | 122.92 | 106 | -16.92 | price | 13.76505 | improved |
| 9011 | 무/RETAIL | rmse | 189.77176 | 151.12008 | -38.651673 | price | 20.367453 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.8623495 | -0.1376505 | ratio | 13.76505 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 8.7209703 | 8.7264866 | 0.0055163464 | %p | -0.063253815 | worsened |
| 9012 | 무/WHOLESALE | mae | 2562.12 | 2563.28 | 1.16 | price | -0.045275007 | worsened |
| 9012 | 무/WHOLESALE | rmse | 4154.0043 | 4166.4015 | 12.397246 | price | -0.29844087 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0004528 | 0.00045275007 | ratio | -0.045275007 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 25 | 25 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

