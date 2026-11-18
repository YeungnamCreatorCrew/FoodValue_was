
## ridge-v2-20261117T065817086357Z-c7af6a37f3b64b39a775f084652d6e52

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065817086357Z-c7af6a37f3b64b39a775f084652d6e52 | no_cross_item | 4.9623906 | 686.58336 | 1033.0742 | 1.1603789 | -7.7314604 (direct) | -7.7120551 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9623906 | 0.35530127 | %p | -7.7120551 | worsened |
| mae | 532.31701 | 686.58336 | 154.26636 | price | -28.980167 | worsened |
| rmse | 943.1701 | 1033.0742 | 89.90414 | price | -9.5321237 | worsened |
| rmae | 1 | 1.1603789 | 0.16037892 | ratio | -16.037892 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.0647954 | 0.29629887 | %p | -6.2136749 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 146.95257 | 8.6837945 | price | -6.2803728 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 207.75218 | -3.0338698 | price | 1.4393124 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0628037 | 0.062803728 | ratio | -6.2803728 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1789751 | 0.67691334 | %p | -12.302903 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 129.19763 | 13.44664 | price | -11.616869 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 187.69725 | 16.561158 | price | -9.6771862 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1161687 | 0.11616869 | ratio | -11.616869 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5312177 | 0.63781429 | %p | -22.043739 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 652.40711 | 134.31225 | price | -25.924259 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 949.61301 | 121.14953 | price | -14.6234 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2592426 | 0.25924259 | ratio | -25.924259 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6643931 | 0.15775117 | %p | -3.500415 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.61355 | 1.9760956 | price | -1.9635788 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.79055 | -0.072543871 | price | 0.045664396 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 1.0196358 | 0.019635788 | ratio | -1.9635788 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.6573274 | 0.85998176 | %p | -107.85557 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2551.6696 | 1219.9732 | price | -91.610459 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3518.4367 | 645.24632 | price | -22.457485 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.9161046 | 0.91610459 | ratio | -91.610459 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.9552015 | 0.50551751 | %p | -14.654023 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 423.62846 | 55.458498 | price | -15.063287 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 599.40341 | 47.04898 | price | -8.5178967 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1506329 | 0.15063287 | ratio | -15.063287 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9513494 | -0.38045187 | %p | 7.1355223 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 239.25794 | -10.293651 | price | 4.1248589 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 379.91583 | -30.140659 | price | 7.3503675 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.95875141 | -0.041248589 | ratio | 4.1248589 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.7597765 | 0.17318279 | %p | -2.0168975 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1071.1186 | 21.881423 | price | -2.0854602 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1878.7387 | 47.880058 | price | -2.6151696 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0208546 | 0.020854602 | ratio | -2.0854602 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6914296 | 0.063871719 | %p | -1.760736 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 98.909091 | 2.8814229 | price | -3.0006174 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.93031 | -12.952571 | price | 8.3628165 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0300062 | 0.030006174 | ratio | -3.0006174 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1694404 | 0.56213311 | %p | -8.5077488 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1450.0791 | 94.343874 | price | -6.9588718 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2308.4644 | 67.354999 | price | -3.0054311 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0695887 | 0.069588718 | ratio | -6.9588718 | worsened |
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
| mape | 4.6062595 | 4.9623906 | 0.35613113 | %p | -7.7314604 | worsened |
| mae | 565.55167 | 686.58336 | 121.03169 | price | -21.400642 | worsened |
| rmse | 926.40586 | 1033.0742 | 106.66838 | price | -11.514217 | worsened |
| rmae | 1.0199316 | 1.1603789 | 0.14044735 | ratio | -13.770272 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.0647954 | 0.3349844 | %p | -7.0824056 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 146.95257 | 9.1225296 | price | -6.6186803 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 207.75218 | -1.4267624 | price | 0.68207746 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0628037 | 0.065976788 | ratio | -6.6186803 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1789751 | 0.44681878 | %p | -7.7949511 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 129.19763 | 9.5335968 | price | -7.9669694 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 187.69725 | 8.9582637 | price | -5.0119249 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1161687 | 0.082362984 | ratio | -7.9669694 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5312177 | 0.8507791 | %p | -31.740295 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 652.40711 | 161.80237 | price | -32.980189 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 949.61301 | 170.53115 | price | -21.888734 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2592426 | 0.3123026 | ratio | -32.980189 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6643931 | 0.073392838 | %p | -1.5986241 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.61355 | -0.34262948 | price | 0.33279158 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.79055 | -6.2445198 | price | 3.7837532 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0196358 | -0.0034045922 | ratio | 0.33279158 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.6573274 | 0.59065628 | %p | -55.373794 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2551.6696 | 840.20089 | price | -49.092389 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3518.4367 | 679.49656 | price | -23.934867 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.9161046 | 0.63092524 | ratio | -49.092389 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.9552015 | 0.41650799 | %p | -11.770106 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 423.62846 | 45.55336 | price | -12.04876 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 599.40341 | 34.029378 | price | -6.0189142 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1506329 | 0.12372916 | ratio | -12.04876 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9513494 | 0.17285364 | %p | -3.6173234 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 239.25794 | 14.035714 | price | -6.2319402 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 379.91583 | 6.5761695 | price | -1.7614441 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.95875141 | 0.056243739 | ratio | -6.2319402 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.7597765 | 0.68104456 | %p | -8.4300923 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1071.1186 | 106.97628 | price | -11.095487 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1878.7387 | 174.76841 | price | -10.256541 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0208546 | 0.10195625 | ratio | -11.095487 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6914296 | 0.042426381 | %p | -1.1626841 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 98.909091 | 1.7667984 | price | -1.8187737 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.93031 | -13.230869 | price | 8.5271774 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0300062 | 0.018398847 | ratio | -1.8187737 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1694404 | -0.048152688 | %p | 0.66715714 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1450.0791 | 21.667984 | price | -1.5169292 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2308.4644 | 13.226033 | price | -0.5762379 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0695887 | 0.015982461 | ratio | -1.5169292 | worsened |
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
| mape | 4.99034 | 4.9623906 | -0.027949419 | %p | 0.56007043 | improved |
| mae | 674.96363 | 686.58336 | 11.619728 | price | -1.721534 | worsened |
| rmse | 1034.3299 | 1033.0742 | -1.2556354 | price | 0.12139603 | improved |
| rmae | 1.1614981 | 1.1603789 | -0.0011191742 | ratio | 0.096356094 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.0647954 | -0.06917015 | %p | 1.3473045 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 146.95257 | -1.8616601 | price | 1.250996 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 207.75218 | -2.0697281 | price | 0.98642135 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0628037 | -0.013464067 | ratio | 1.250996 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1789751 | 0.022359167 | %p | -0.363173 | worsened |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 129.19763 | 1.3320158 | price | -1.0417311 | worsened |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 187.69725 | 0.63366897 | price | -0.33874524 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1161687 | 0.011507598 | ratio | -1.0417311 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5312177 | -0.0636717 | %p | 1.7711727 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 652.40711 | -10.422925 | price | 1.5724883 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 949.61301 | -52.360388 | price | 5.2257264 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2592426 | -0.020117792 | ratio | 1.5724883 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.6643931 | -0.17329391 | %p | 3.5821645 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 102.61355 | -4.4103586 | price | 4.1209098 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 158.79055 | -5.8438891 | price | 3.5496153 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0196358 | -0.043824228 | ratio | 4.1209098 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.6573274 | 0.08344107 | %p | -5.3015943 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2551.6696 | 119.3125 | price | -4.9052213 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3518.4367 | 3.4245087 | price | -0.097425228 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.9161046 | 0.089594368 | ratio | -4.9052213 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 3.9552015 | -0.090902666 | %p | 2.2466714 | improved |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 423.62846 | -10.205534 | price | 2.3524052 | improved |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 599.40341 | -7.3427465 | price | 1.2101843 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1506329 | -0.027719626 | ratio | 2.3524052 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9513494 | -0.03375423 | %p | 0.67710187 | improved |
| 9001 | 배추/RETAIL | mae | 242.5873 | 239.25794 | -3.3293651 | price | 1.37244 | improved |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 379.91583 | 0.42581849 | price | -0.11220809 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.95875141 | -0.01334139 | ratio | 1.37244 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.7597765 | -0.04592669 | %p | 0.52155619 | improved |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1071.1186 | -6.715415 | price | 0.62304725 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1878.7387 | 23.747806 | price | -1.2802115 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0208546 | -0.0064002833 | ratio | 0.62304725 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.6914296 | -0.053060107 | %p | 1.4170184 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 98.909091 | -1.1778656 | price | 1.1768423 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 141.93031 | -2.1803175 | price | 1.5129471 | improved |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0300062 | -0.012265898 | ratio | 1.1768423 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.1694404 | 0.14448502 | %p | -2.0567393 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1450.0791 | 33.675889 | price | -2.3775638 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2308.4644 | 29.008913 | price | -1.2726247 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0695887 | 0.024839578 | ratio | -2.3775638 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

