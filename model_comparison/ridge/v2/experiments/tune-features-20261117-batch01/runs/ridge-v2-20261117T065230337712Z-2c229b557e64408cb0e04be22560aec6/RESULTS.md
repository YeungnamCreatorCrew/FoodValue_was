
## ridge-v2-20261117T065230337712Z-2c229b557e64408cb0e04be22560aec6

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T065230337712Z-2c229b557e64408cb0e04be22560aec6 | no_production | 4.9924315 | 675.52627 | 1035.3211 | 1.1623651 | -8.3836354 (direct) | -8.3641126 (direct) | 1 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.9924315 | 0.38534214 | %p | -8.3641126 | worsened |
| mae | 532.31701 | 675.52627 | 143.20926 | price | -26.903004 | worsened |
| rmse | 943.1701 | 1035.3211 | 92.150975 | price | -9.7703453 | worsened |
| rmae | 1 | 1.1623651 | 0.16236505 | ratio | -16.236505 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 5.1377168 | 0.36922029 | %p | -7.7429077 | worsened |
| 1 | 대파/RETAIL | mae | 138.26877 | 148.96047 | 10.6917 | price | -7.7325482 | worsened |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.74962 | -1.0364252 | price | 0.49169533 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 1.0773255 | 0.077325482 | ratio | -7.7325482 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 6.1443932 | 0.64233138 | %p | -11.674376 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 127.64427 | 11.893281 | price | -10.274885 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 186.70026 | 15.564173 | price | -9.0946176 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.1027488 | 0.10274885 | ratio | -10.274885 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.5954239 | 0.7020205 | %p | -24.262794 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 662.81028 | 144.71542 | price | -27.932224 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 1001.7818 | 173.31832 | price | -20.920454 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.2793222 | 0.27932224 | ratio | -27.932224 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.8358947 | 0.32925281 | %p | -7.3059457 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 107.00398 | 6.3665339 | price | -6.3262074 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.59989 | 5.7367969 | price | -3.6111578 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0632621 | 0.063262074 | ratio | -6.3262074 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.574827 | 0.77748135 | %p | -97.508694 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2436.808 | 1105.1116 | price | -82.98525 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3523.7297 | 650.53923 | price | -22.641703 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.8298525 | 0.8298525 | ratio | -82.98525 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 4.0497631 | 0.60007905 | %p | -17.395189 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 434.3004 | 66.130435 | price | -17.961931 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 606.68177 | 54.327335 | price | -9.8355932 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.1796193 | 0.17961931 | ratio | -17.961931 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.9915675 | -0.34023376 | %p | 6.3812161 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 243.01984 | -6.531746 | price | 2.6173931 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 380.18887 | -29.867618 | price | 7.2837813 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.97382607 | -0.026173931 | ratio | 2.6173931 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.8068299 | 0.22023618 | %p | -2.5648841 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1077.8024 | 28.565217 | price | -2.7224748 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1854.8915 | 24.032938 | price | -1.3126594 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 1 | 1.0272247 | 0.027224748 | ratio | -2.7224748 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7593102 | 0.1317523 | %p | -3.6319834 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 100.41107 | 4.3833992 | price | -4.5647253 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 144.29252 | -10.590361 | price | 6.8376573 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0456473 | 0.045647253 | ratio | -4.5647253 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0285886 | 0.4212813 | %p | -6.3759907 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1416.502 | 60.766798 | price | -4.4822027 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2280.5948 | 39.485358 | price | -1.7618666 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.044822 | 0.044822027 | ratio | -4.4822027 | worsened |
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
| mape | 4.6062595 | 4.9924315 | 0.386172 | %p | -8.3836354 | worsened |
| mae | 565.55167 | 675.52627 | 109.9746 | price | -19.445544 | worsened |
| rmse | 926.40586 | 1035.3211 | 108.91522 | price | -11.75675 | worsened |
| rmae | 1.0199316 | 1.1623651 | 0.14243349 | ratio | -13.965004 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 5.1377168 | 0.40790581 | %p | -8.6241462 | worsened |
| 1 | 대파/RETAIL | mae | 137.83004 | 148.96047 | 11.130435 | price | -8.0754782 | worsened |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.74962 | 0.57068225 | price | -0.27282013 | worsened |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 1.0773255 | 0.080498542 | ratio | -8.0754782 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 6.1443932 | 0.41223683 | %p | -7.1916536 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 127.64427 | 7.9802372 | price | -6.6688687 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 186.70026 | 7.9612785 | price | -4.4541366 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.1027488 | 0.068943145 | ratio | -6.6688687 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.5954239 | 0.9149853 | %p | -34.135657 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 662.81028 | 172.20553 | price | -35.100666 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 1001.7818 | 222.69995 | price | -28.584923 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.2793222 | 0.33238225 | ratio | -35.100666 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.8358947 | 0.24489448 | %p | -5.3342293 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 107.00398 | 4.0478088 | price | -3.9315842 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.59989 | -0.43517896 | price | 0.26368878 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0632621 | 0.040221694 | ratio | -3.9315842 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.574827 | 0.50815588 | %p | -47.639413 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2436.808 | 725.33929 | price | -42.3811 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3523.7297 | 684.78947 | price | -24.121307 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.8298525 | 0.54467315 | ratio | -42.3811 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 4.0497631 | 0.51106953 | %p | -14.442322 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 434.3004 | 56.225296 | price | -14.871462 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 606.68177 | 41.307733 | price | -7.3062664 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.1796193 | 0.1527156 | ratio | -14.871462 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.9915675 | 0.21307175 | %p | -4.4589712 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 243.01984 | 17.797619 | price | -7.9022482 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 380.18887 | 6.8492104 | price | -1.8345788 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.97382607 | 0.071318396 | ratio | -7.9022482 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.8068299 | 0.72809794 | %p | -9.0125275 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1077.8024 | 113.66008 | price | -11.788725 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1854.8915 | 150.92129 | price | -8.8570377 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 1.0272247 | 0.1083264 | ratio | -11.788725 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7593102 | 0.11030696 | %p | -3.0229341 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 100.41107 | 3.2687747 | price | -3.3649347 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 144.29252 | -10.868659 | price | 7.0047537 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0456473 | 0.034039926 | ratio | -3.3649347 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0285886 | -0.1890045 | %p | 2.6186638 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1416.502 | -11.909091 | price | 0.83372995 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2280.5948 | -14.643608 | price | 0.63799944 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.044822 | -0.0087842309 | ratio | 0.83372995 | improved |
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
| mape | 4.99034 | 4.9924315 | 0.0020914513 | %p | -0.041909996 | worsened |
| mae | 674.96363 | 675.52627 | 0.56263581 | price | -0.083357944 | worsened |
| rmse | 1034.3299 | 1035.3211 | 0.9911995 | price | -0.095830114 | worsened |
| rmae | 1.1614981 | 1.1623651 | 0.00086696432 | ratio | -0.074641906 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 5.1339656 | 5.1377168 | 0.0037512629 | %p | -0.07306755 | worsened |
| 1 | 대파/RETAIL | mae | 148.81423 | 148.96047 | 0.14624506 | price | -0.098273572 | worsened |
| 1 | 대파/RETAIL | rmse | 209.82191 | 209.74962 | -0.072283415 | price | 0.034449889 | improved |
| 1 | 대파/RETAIL | rmae | 1.0762678 | 1.0773255 | 0.0010576868 | ratio | -0.098273572 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 6.156616 | 6.1443932 | -0.012222786 | %p | 0.19853091 | improved |
| 2 | 대파/WHOLESALE | mae | 127.86561 | 127.64427 | -0.22134387 | price | 0.17310665 | improved |
| 2 | 대파/WHOLESALE | rmse | 187.06358 | 186.70026 | -0.36331622 | price | 0.19422071 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.1046611 | 1.1027488 | -0.0019122418 | ratio | 0.17310665 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 3.5948894 | 3.5954239 | 0.00053450102 | %p | -0.014868358 | worsened |
| 7 | 양파/WHOLESALE | mae | 662.83004 | 662.81028 | -0.019762846 | price | 0.0029815857 | improved |
| 7 | 양파/WHOLESALE | rmse | 1001.9734 | 1001.7818 | -0.19159481 | price | 0.019121746 | improved |
| 7 | 양파/WHOLESALE | rmae | 1.2793604 | 1.2793222 | -3.8145227e-05 | ratio | 0.0029815857 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.837687 | 4.8358947 | -0.0017922641 | %p | 0.037047955 | improved |
| 8 | 양파/RETAIL | mae | 107.0239 | 107.00398 | -0.019920319 | price | 0.018612962 | improved |
| 8 | 양파/RETAIL | rmse | 164.63444 | 164.59989 | -0.034548348 | price | 0.020984885 | improved |
| 8 | 양파/RETAIL | rmae | 1.06346 | 1.0632621 | -0.00019794141 | ratio | 0.018612962 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.5738864 | 1.574827 | 0.00094066441 | %p | -0.059766984 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 2432.3571 | 2436.808 | 4.4508929 | price | -0.18298681 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 3515.0122 | 3523.7297 | 8.7174194 | price | -0.24800538 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.8265102 | 1.8298525 | 0.0033422729 | ratio | -0.18298681 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 4.0461042 | 4.0497631 | 0.0036588741 | %p | -0.090429557 | worsened |
| 10 | 깐마늘/RETAIL | mae | 433.83399 | 434.3004 | 0.46640316 | price | -0.10750729 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 606.74616 | 606.68177 | -0.064391453 | price | 0.010612585 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.1783525 | 1.1796193 | 0.0012668148 | ratio | -0.10750729 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.9851036 | 4.9915675 | 0.0064638772 | %p | -0.12966385 | worsened |
| 9001 | 배추/RETAIL | mae | 242.5873 | 243.01984 | 0.43253968 | price | -0.17830269 | worsened |
| 9001 | 배추/RETAIL | rmse | 379.49001 | 380.18887 | 0.69885941 | price | -0.18415753 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.9720928 | 0.97382607 | 0.0017332676 | ratio | -0.17830269 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.8057032 | 8.8068299 | 0.0011266941 | %p | -0.012795049 | worsened |
| 9002 | 배추/WHOLESALE | mae | 1077.834 | 1077.8024 | -0.031620553 | price | 0.0029337128 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1854.9909 | 1854.8915 | -0.099313845 | price | 0.0053538725 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1.0272549 | 1.0272247 | -3.0136708e-05 | ratio | 0.0029337128 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.7444897 | 3.7593102 | 0.014820476 | %p | -0.39579429 | worsened |
| 9011 | 무/RETAIL | mae | 100.08696 | 100.41107 | 0.32411067 | price | -0.32382908 | worsened |
| 9011 | 무/RETAIL | rmse | 144.11063 | 144.29252 | 0.18189294 | price | -0.12621758 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0422721 | 1.0456473 | 0.0033751801 | ratio | -0.32382908 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.0249554 | 7.0285886 | 0.0036332125 | %p | -0.051718656 | worsened |
| 9012 | 무/WHOLESALE | mae | 1416.4032 | 1416.502 | 0.098814229 | price | -0.0069764197 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2279.4555 | 2280.5948 | 1.1392713 | price | -0.049979975 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0447491 | 1.044822 | 7.2886085e-05 | ratio | -0.0069764197 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 2, 'worsened': 8, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

