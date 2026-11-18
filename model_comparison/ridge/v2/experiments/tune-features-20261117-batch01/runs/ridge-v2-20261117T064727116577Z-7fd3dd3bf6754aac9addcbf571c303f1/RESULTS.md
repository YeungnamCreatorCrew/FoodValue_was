
## ridge-v2-20261117T064727116577Z-7fd3dd3bf6754aac9addcbf571c303f1

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T064727116577Z-7fd3dd3bf6754aac9addcbf571c303f1 | no_event | 4.9908908 | 685.86685 | 1051.4286 | 1.1683312 | -8.3501867 (direct) | -8.33067 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9908908 | 0.38380141 | %p | -8.33067 | worsened |
| mae | 532.31701 | 685.86685 | 153.54984 | price | -28.845564 | worsened |
| rmse | 943.1701 | 1051.4286 | 108.25849 | price | -11.478151 | worsened |
| rmae | 1 | 1.1683312 | 0.16833122 | ratio | -16.833122 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1209607 | 0.35246419 | %p | -7.391516 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.2332 | 9.9644269 | price | -7.2065634 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.9487 | -1.8373452 | price | 0.87166356 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0720656 | 0.072065634 | ratio | -7.2065634 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.065899 | 0.56383723 | %p | -10.247744 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 125.28854 | 9.5375494 | price | -8.2397132 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 184.92323 | 13.78714 | price | -8.0562432 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0823971 | 0.082397132 | ratio | -8.2397132 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5691292 | 0.67572578 | %p | -23.354012 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 656.89723 | 138.80237 | price | -26.790918 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1006.1718 | 177.70828 | price | -21.450345 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2679092 | 0.26790918 | ratio | -26.790918 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.9042235 | 0.39758159 | %p | -8.8221252 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 108.58964 | 7.9521912 | price | -7.9018211 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 166.4443 | 7.5812083 | price | -4.7721646 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0790182 | 0.079018211 | ratio | -7.9018211 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.6569094 | 0.85956373 | %p | -107.80315 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2563.9107 | 1232.2143 | price | -92.529668 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3682.0653 | 808.87491 | price | -28.152499 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.9252967 | 0.92529668 | ratio | -92.529668 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0626896 | 0.61300559 | %p | -17.769905 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 436.19763 | 68.027668 | price | -18.477246 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 613.42588 | 61.071443 | price | -11.056568 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1847725 | 0.18477246 | ratio | -18.477246 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0016544 | -0.33014687 | %p | 6.1920325 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.53571 | -6.015873 | price | 2.4106731 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 384.04433 | -26.012161 | price | 6.3435555 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97589327 | -0.024106731 | ratio | 2.4106731 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8158647 | 0.22927094 | %p | -2.6701035 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1079.6403 | 30.403162 | price | -2.8976444 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1865.1871 | 34.328496 | price | -1.8749944 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0289764 | 0.028976444 | ratio | -2.8976444 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7329852 | 0.10542732 | %p | -2.9062892 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.549407 | 3.5217391 | price | -3.6674213 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.095 | -10.787888 | price | 6.9651907 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0366742 | 0.036674213 | ratio | -3.6674213 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9785919 | 0.37128459 | %p | -5.6193026 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1396.8261 | 41.090909 | price | -3.030895 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2258.9802 | 17.870822 | price | -0.79740961 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0303089 | 0.03030895 | ratio | -3.030895 | worsened |
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
| mape | 4.6062595 | 4.9908908 | 0.38463127 | %p | -8.3501867 | worsened |
| mae | 565.55167 | 685.86685 | 120.31518 | price | -21.273949 | worsened |
| rmse | 926.40586 | 1051.4286 | 125.02273 | price | -13.49546 | worsened |
| rmae | 1.0199316 | 1.1683312 | 0.14839965 | ratio | -14.549961 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1209607 | 0.39114972 | %p | -8.2698804 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.2332 | 10.403162 | price | -7.5478191 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.9487 | -0.23023776 | price | 0.11006737 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0720656 | 0.075238694 | ratio | -7.5478191 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.065899 | 0.33374268 | %p | -5.8222884 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 125.28854 | 5.6245059 | price | -4.7002477 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 184.92323 | 6.1842452 | price | -3.4599308 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0823971 | 0.048591429 | ratio | -4.7002477 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5691292 | 0.88869059 | %p | -33.154671 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 656.89723 | 166.29249 | price | -33.89541 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1006.1718 | 227.0899 | price | -29.148401 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2679092 | 0.32096919 | ratio | -33.89541 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.9042235 | 0.31322326 | %p | -6.8225494 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 108.58964 | 5.6334661 | price | -5.4717127 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 166.4443 | 1.4092324 | price | -0.85389877 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0790182 | 0.055977831 | ratio | -5.4717127 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.6569094 | 0.59023825 | %p | -55.334604 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2563.9107 | 852.44196 | price | -49.807627 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3682.0653 | 843.12514 | price | -29.698588 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.9252967 | 0.64011733 | ratio | -49.807627 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0626896 | 0.52399607 | %p | -14.807614 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 436.19763 | 58.12253 | price | -15.373276 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 613.42588 | 48.051841 | price | -8.4991242 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1847725 | 0.15786875 | ratio | -15.373276 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0016544 | 0.22315864 | %p | -4.6700606 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.53571 | 18.313492 | price | -8.1312989 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 384.04433 | 10.704667 | price | -2.8672731 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97589327 | 0.073385596 | ratio | -8.1312989 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8158647 | 0.73713271 | %p | -9.1243615 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1079.6403 | 115.49802 | price | -11.979355 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1865.1871 | 161.21685 | price | -9.4612477 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0289764 | 0.11007809 | ratio | -11.979355 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7329852 | 0.083981986 | %p | -2.3015048 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.549407 | 2.4071146 | price | -2.4779265 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.095 | -11.066186 | price | 7.1320584 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0366742 | 0.025066886 | ratio | -2.4779265 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9785919 | -0.23900121 | %p | 3.31137 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1396.8261 | -31.58498 | price | 2.2111968 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2258.9802 | -36.258144 | price | 1.5797115 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0303089 | -0.023297308 | ratio | 2.2111968 | improved |
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
| mape | 4.99034 | 4.9908908 | 0.00055072062 | %p | -0.011035733 | worsened |
| mae | 674.96363 | 685.86685 | 10.903215 | price | -1.6153781 | worsened |
| rmse | 1034.3299 | 1051.4286 | 17.098714 | price | -1.65312 | worsened |
| rmae | 1.1614981 | 1.1683312 | 0.0068331272 | ratio | -0.58830292 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1209607 | -0.013004836 | %p | 0.25330976 | improved |
| 1 | 대파/RETAIL | mae | 148.81423 | 148.2332 | -0.58102767 | price | 0.39043825 | improved |
| 1 | 대파/RETAIL | rmse | 209.82191 | 208.9487 | -0.87320343 | price | 0.41616409 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0720656 | -0.0042021611 | ratio | 0.39043825 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.065899 | -0.090716939 | %p | 1.4734871 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 125.28854 | -2.5770751 | price | 2.015456 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 184.92323 | -2.1403496 | price | 1.144183 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.0823971 | -0.022263958 | ratio | 2.015456 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5691292 | -0.025760213 | %p | 0.71657875 | improved |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 656.89723 | -5.9328063 | price | 0.89507204 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1006.1718 | 4.1983584 | price | -0.41900896 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2679092 | -0.011451197 | ratio | 0.89507204 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.9042235 | 0.066536516 | %p | -1.3753787 | worsened |
| 8 | 양파/RETAIL | mae | 107.0239 | 108.58964 | 1.5657371 | price | -1.4629788 | worsened |
| 8 | 양파/RETAIL | rmse | 164.63444 | 166.4443 | 1.809863 | price | -1.0993223 | worsened |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0790182 | 0.015558195 | ratio | -1.4629788 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.6569094 | 0.08302304 | %p | -5.275034 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2563.9107 | 131.55357 | price | -5.4084809 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3682.0653 | 167.05309 | price | -4.7525608 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.9252967 | 0.098786457 | ratio | -5.4084809 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0626896 | 0.016585415 | %p | -0.40991072 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 436.19763 | 2.3636364 | price | -0.54482507 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 613.42588 | 6.6797164 | price | -1.1009079 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1847725 | 0.0064199598 | ratio | -0.54482507 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 5.0016544 | 0.016550771 | %p | -0.33200456 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.53571 | 0.9484127 | price | -0.39095727 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 384.04433 | 4.5543165 | price | -1.200115 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97589327 | 0.0038004675 | ratio | -0.39095727 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8158647 | 0.010161457 | %p | -0.11539631 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1079.6403 | 1.8063241 | price | -0.16758834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1865.1871 | 10.196245 | price | -0.54966551 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0289764 | 0.0017215594 | ratio | -0.16758834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7329852 | -0.011504503 | %p | 0.30723819 | improved |
| 9011 | 무/RETAIL | mae | 100.08696 | 99.549407 | -0.53754941 | price | 0.53708238 | improved |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.095 | -0.015634424 | price | 0.010848904 | improved |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0366742 | -0.0055978596 | ratio | 0.53708238 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 6.9785919 | -0.046363502 | %p | 0.65998286 | improved |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1396.8261 | -19.577075 | price | 1.3821683 | improved |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2258.9802 | -20.475264 | price | 0.89825243 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.0303089 | -0.014440191 | ratio | 1.3821683 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

