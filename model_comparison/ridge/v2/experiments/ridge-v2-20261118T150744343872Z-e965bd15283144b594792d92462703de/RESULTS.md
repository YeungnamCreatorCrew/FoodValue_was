
## ridge-v2-20261118T150744343872Z-e965bd15283144b594792d92462703de

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150744343872Z-e965bd15283144b594792d92462703de | market_alpha1000 | 4.4906086 | 559.8397 | 927.41807 | 0.99451228 | 2.5107331 (direct) | 2.5282936 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4906086 | -0.11648074 | %p | 2.5282936 | improved |
| mae | 532.31701 | 559.8397 | 27.522698 | price | -5.1703586 | worsened |
| rmse | 943.1701 | 927.41807 | -15.752031 | price | 1.6701156 | improved |
| rmae | 1 | 0.99451228 | -0.0054877232 | ratio | 0.54877232 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4782806 | -0.29021596 | %p | 6.0861103 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 130.05138 | -8.2173913 | price | 5.9430564 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 193.98283 | -16.803216 | price | 7.9716926 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.94056944 | -0.059430564 | ratio | 5.9430564 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.6029446 | 0.10088281 | %p | -1.8335456 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 117.17391 | 1.4229249 | price | -1.2292983 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.39129 | 7.2551952 | price | -4.2394303 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.012293 | 0.012292983 | ratio | -1.2292983 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7700325 | -0.12337083 | %p | 4.2638657 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 497.99209 | -20.102767 | price | 3.8801324 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 807.96176 | -20.501721 | price | 2.474668 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.96119868 | -0.038801324 | ratio | 3.8801324 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3868009 | -0.11984099 | %p | 2.6592082 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.015936 | -2.6215139 | price | 2.6049089 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 157.66013 | -1.2029605 | price | 0.75723096 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.97395091 | -0.026049089 | ratio | 2.6049089 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0629683 | 0.26562264 | %p | -33.313361 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1706.6071 | 374.91071 | price | -28.152866 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2882.1995 | 9.0091171 | price | -0.31355795 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2815287 | 0.28152866 | ratio | -28.152866 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4638734 | 0.014189403 | %p | -0.41132473 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 370.49802 | 2.3280632 | price | -0.63233384 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 551.43195 | -0.92248402 | price | 0.16700944 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0063233 | 0.0063233384 | ratio | -0.63233384 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.6918547 | -0.63994654 | %p | 12.002446 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 219.80952 | -29.742063 | price | 11.918202 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 367.48615 | -42.570334 | price | 10.381578 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.88081798 | -0.11918202 | ratio | 11.918202 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0317426 | -0.55485117 | %p | 6.461831 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 967.50988 | -81.727273 | price | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1732.7925 | -98.066145 | price | 5.3562926 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.92210791 | -0.077892088 | ratio | 7.7892088 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3654318 | -0.26212614 | %p | 7.2259671 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.577075 | -6.4505929 | price | 6.7174316 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 141.52555 | -13.35733 | price | 8.6241486 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.93282568 | -0.067174316 | ratio | 6.7174316 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.0521567 | 0.44484935 | %p | -6.7326875 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1401.1621 | 45.426877 | price | -3.3507191 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2260.749 | 19.639569 | price | -0.87633243 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0335072 | 0.033507191 | ratio | -3.3507191 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 6, 'worsened': 4, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### CONTROL: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6062595 | 4.4906086 | -0.11565088 | %p | 2.5107331 | improved |
| mae | 565.55167 | 559.8397 | -5.7119683 | price | 1.0099817 | improved |
| rmse | 926.40586 | 927.41807 | 1.0122099 | price | -0.10926204 | worsened |
| rmae | 1.0199316 | 0.99451228 | -0.025419291 | ratio | 2.4922546 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4782806 | -0.25153043 | %p | 5.3179806 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 130.05138 | -7.7786561 | price | 5.6436581 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 193.98283 | -15.196109 | price | 7.2646455 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.94056944 | -0.056257504 | ratio | 5.6436581 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.6029446 | -0.12921174 | %p | 2.254156 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 117.17391 | -2.4901186 | price | 2.0809249 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.39129 | -0.34769921 | price | 0.19452903 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.012293 | -0.02151272 | ratio | 2.0809249 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7700325 | 0.089593974 | %p | -3.3425117 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 497.99209 | 7.3873518 | price | -1.5057644 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 807.96176 | 28.879902 | price | -3.706915 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.96119868 | 0.014258686 | ratio | -1.5057644 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3868009 | -0.20419932 | %p | 4.4478178 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.015936 | -4.940239 | price | 4.7983902 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 157.66013 | -7.3749364 | price | 4.4687087 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.97395091 | -0.04908947 | ratio | 4.7983902 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0629683 | -0.0037028306 | %p | 0.34713891 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1706.6071 | -4.8616071 | price | 0.28406053 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2882.1995 | 43.259352 | price | -1.5237853 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2815287 | -0.0036506872 | ratio | 0.28406053 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4638734 | -0.074820114 | %p | 2.1143428 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 370.49802 | -7.5770751 | price | 2.0041191 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 551.43195 | -13.942086 | price | 2.4659933 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0063233 | -0.020580373 | ratio | 2.0041191 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.6918547 | -0.086641032 | %p | 1.8131445 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 219.80952 | -5.4126984 | price | 2.4032701 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 367.48615 | -5.8535063 | price | 1.5678769 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.88081798 | -0.021689697 | ratio | 2.4032701 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0317426 | -0.046989408 | %p | 0.58164336 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 967.50988 | 3.3675889 | price | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1732.7925 | 28.822206 | price | -1.6914735 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.92210791 | 0.0032095594 | ratio | -0.3492834 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3654318 | -0.28357148 | %p | 7.7712038 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.577075 | -7.5652174 | price | 7.7877691 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 141.52555 | -13.635628 | price | 8.7880407 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.93282568 | -0.078781642 | ratio | 7.7877691 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.0521567 | -0.16543645 | %p | 2.2921276 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1401.1621 | -27.249012 | price | 1.907645 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2260.749 | -34.489397 | price | 1.5026499 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0335072 | -0.020099067 | ratio | 1.907645 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 9, 'worsened': 1, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.4906086 | -0.010532708 | %p | 0.23400083 | improved |
| mae | 557.9753 | 559.8397 | 1.8643999 | price | -0.33413664 | worsened |
| rmse | 915.84853 | 927.41807 | 11.569532 | price | -1.2632583 | worsened |
| rmae | 0.99470404 | 0.99451228 | -0.00019176808 | ratio | 0.019278908 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4782806 | 0.051852835 | %p | -1.1714375 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 130.05138 | 1.3043478 | price | -1.013109 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 193.98283 | 2.402605 | price | -1.2540986 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.94056944 | 0.0094334229 | ratio | -1.013109 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.6029446 | -0.12996993 | %p | 2.2670831 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 117.17391 | -2.3438735 | price | 1.9611085 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 178.39129 | -2.4808008 | price | 1.3715775 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.012293 | -0.020249274 | ratio | 1.9611085 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7700325 | 0.035717349 | %p | -1.3062631 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 497.99209 | 4.2173913 | price | -0.85411247 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 807.96176 | 19.703869 | price | -2.499673 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.96119868 | 0.0081401913 | ratio | -0.85411247 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3868009 | -0.038387596 | %p | 0.86747935 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.015936 | -0.84462151 | price | 0.85435641 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 157.66013 | -1.0528443 | price | 0.66336374 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.97395091 | -0.0083927158 | ratio | 0.85435641 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0629683 | 0.022068927 | %p | -2.1201787 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1706.6071 | 24.910714 | price | -1.4812848 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2882.1995 | 87.79125 | price | -3.1416759 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2815287 | 0.018706001 | ratio | -1.4812848 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4638734 | 0.0061820947 | %p | -0.17879255 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 370.49802 | 0.64426877 | price | -0.17419555 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 551.43195 | -0.15541603 | price | 0.02817614 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0063233 | 0.0017499222 | ratio | -0.17419555 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.6918547 | -0.062417488 | %p | 1.3128716 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 219.80952 | -2.7896825 | price | 1.2532311 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 367.48615 | 10.221827 | price | -2.8611384 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.88081798 | -0.011178781 | ratio | 1.2532311 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.0317426 | 0.091949497 | %p | -1.1580843 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 967.50988 | 7.6640316 | price | -0.79846484 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1732.7925 | 22.908564 | price | -1.3397731 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.92210791 | 0.0073043845 | ratio | -0.79846484 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.3654318 | 0.0083493253 | %p | -0.24870778 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 89.577075 | 0.3083004 | price | -0.34536197 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 141.52555 | 0.39467459 | price | -0.27965148 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.93282568 | 0.0032105371 | ratio | -0.34536197 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.0521567 | -0.090672092 | %p | 1.2694143 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1401.1621 | -14.426877 | price | 1.0191431 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2260.749 | -24.038404 | price | 1.0521068 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0335072 | -0.010641368 | ratio | 1.0191431 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 4, 'worsened': 6, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

