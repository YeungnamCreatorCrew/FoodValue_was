
## ridge-v2-20261119T084708506807Z-5eb236c29d114fb1a29f58ce1fe8c4ef

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T084708506807Z-5eb236c29d114fb1a29f58ce1fe8c4ef | no_ow | 5.0025012 | 637.7138 | 994.90324 | 1.0562536 | N/A | -1.8311162 (direct) | N/A |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.9125468 | 5.0025012 | 0.089954437 | %p | -1.8311162 | worsened |
| mae | 569.79222 | 637.7138 | 67.921577 | price | -11.920411 | worsened |
| rmse | 989.64537 | 994.90324 | 5.2578757 | price | -0.53128887 | worsened |
| rmae | 1 | 1.0562536 | 0.056253581 | ratio | -5.6253581 | worsened |
| success_rate_pct | 100 | 99.201774 | -0.79822616 | %p | -0.79822616 | worsened |
| valid_predictions | 11275 | 11185 | -90 | count | -0.79822616 | count_change |
| failed_predictions | 0 | 90 | 90 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1984334 | 4.9718494 | -0.22658403 | %p | 4.3586984 | improved |
| 1 | 대파/RETAIL | mae | 149.08566 | 143.56993 | -5.5157343 | price | 3.699708 | improved |
| 1 | 대파/RETAIL | rmse | 216.99605 | 205.79299 | -11.203065 | price | 5.1627968 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.96300292 | -0.03699708 | ratio | 3.699708 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.9408146 | 6.4407329 | 0.49991834 | %p | -8.4149797 | worsened |
| 2 | 대파/WHOLESALE | mae | 124.70979 | 133.43182 | 8.722028 | price | -6.9938599 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.65144 | 188.56164 | 9.9102013 | price | -5.5472272 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0699386 | 0.069938599 | ratio | -6.9938599 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.183793 | 3.4821235 | 0.2983305 | %p | -9.3702858 | worsened |
| 7 | 양파/WHOLESALE | mae | 574.59965 | 631.5778 | 56.978147 | price | -9.9161472 | worsened |
| 7 | 양파/WHOLESALE | rmse | 921.70243 | 967.20419 | 45.501756 | price | -4.9367078 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.0991615 | 0.099161472 | ratio | -9.9161472 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.8732295 | 4.9703306 | 0.097101059 | %p | -1.9925402 | worsened |
| 8 | 양파/RETAIL | mae | 108.3254 | 109.74427 | 1.4188713 | price | -1.3098233 | worsened |
| 8 | 양파/RETAIL | rmse | 170.67764 | 169.05435 | -1.6232917 | price | 0.95108631 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 1.0130982 | 0.013098233 | ratio | -1.3098233 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 1134 | 1134 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79998097 | 1.233205 | 0.43322399 | %p | -54.154287 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1336.6197 | 1946.7837 | 610.16398 | price | -45.649782 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2880.4307 | 2934.2328 | 53.802052 | price | -1.8678474 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.4564978 | 0.45649782 | ratio | -45.649782 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 90.945674 | -9.054326 | %p | -9.054326 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 994 | 904 | -90 | count | -9.054326 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 90 | 90 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.8302262 | 4.0419281 | 0.21170194 | %p | -5.5271394 | worsened |
| 10 | 깐마늘/RETAIL | mae | 408.16434 | 428.80332 | 20.638986 | price | -5.0565383 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 568.62765 | 603.48841 | 34.860756 | price | -6.1306825 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0505654 | 0.050565383 | ratio | -5.0565383 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.2405422 | 4.6990516 | -0.54149062 | %p | 10.332721 | improved |
| 9001 | 배추/RETAIL | mae | 240.76558 | 219.37752 | -21.38806 | price | 8.8833542 | improved |
| 9001 | 배추/RETAIL | rmse | 389.84049 | 346.13609 | -43.704397 | price | 11.210841 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.91116646 | -0.088833542 | ratio | 8.8833542 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 1139 | 1139 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.1934766 | 7.0881637 | -0.1053129 | %p | 1.4640056 | improved |
| 9002 | 배추/WHOLESALE | mae | 1004.0428 | 983.2535 | -20.789336 | price | 2.0705626 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1655.5564 | 1606.9724 | -48.583961 | price | 2.9346002 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.97929437 | -0.020705626 | ratio | 2.0705626 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 4.2492996 | 4.239191 | -0.010108629 | %p | 0.23788929 | improved |
| 9011 | 무/RETAIL | mae | 111.17308 | 111.42832 | 0.25524476 | price | -0.22959224 | worsened |
| 9011 | 무/RETAIL | rmse | 175.91296 | 169.52038 | -6.3925785 | price | 3.633944 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0022959 | 0.0022959224 | ratio | -0.22959224 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 8.6156715 | 8.8584362 | 0.24276473 | %p | -2.817711 | worsened |
| 9012 | 무/WHOLESALE | mae | 1640.4362 | 1669.1678 | 28.731643 | price | -1.7514636 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2738.0579 | 2758.0692 | 20.011286 | price | -0.73085695 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0175146 | 0.017514636 | ratio | -1.7514636 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 1144 | 1144 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

