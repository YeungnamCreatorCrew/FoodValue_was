
## ridge-v2-20261119T071321190532Z-271fab3c870f446797f421d84901ce7d

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261119T071321190532Z-271fab3c870f446797f421d84901ce7d | no_ow_w730 | 4.6946164 | 610.47958 | 966.24522 | 1.0623702 | -1.9181919 (direct) | -1.8998337 (direct) | 3 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6946164 | 0.087527036 | %p | -1.8998337 | worsened |
| mae | 532.31701 | 610.47958 | 78.162571 | price | -14.683463 | worsened |
| rmse | 943.1701 | 966.24522 | 23.075122 | price | -2.4465494 | worsened |
| rmae | 1 | 1.0623702 | 0.062370224 | ratio | -6.2370224 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.457701 | -0.31079558 | %p | 6.5176849 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.94862 | -8.3201581 | price | 6.0173804 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 195.98021 | -14.805844 | price | 7.0241101 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.9398262 | -0.060173804 | ratio | 6.0173804 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7839442 | 0.28188243 | %p | -5.1232145 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.83794 | 4.0869565 | price | -3.5308178 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.07079 | 8.9347021 | price | -5.220817 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0353082 | 0.035308178 | ratio | -3.5308178 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 3.1892301 | 0.29582677 | %p | -10.22418 | worsened |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 575 | 56.905138 | price | -10.983537 | worsened |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 839.96234 | 11.498858 | price | -1.3879741 | worsened |
| 7 | 양파/WHOLESALE | rmae | 1 | 1.1098354 | 0.10983537 | ratio | -10.983537 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3331261 | -0.17351582 | %p | 3.8502243 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 95.768924 | -4.8685259 | price | 4.837688 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 150.26818 | -8.5949123 | price | 5.4102638 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.95162312 | -0.04837688 | ratio | 4.837688 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.2777011 | 0.48035547 | %p | -60.244319 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 2024.7411 | 693.04464 | price | -52.042239 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 3082.7088 | 209.51839 | price | -7.2921861 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.5204224 | 0.52042239 | ratio | -52.042239 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.6123373 | 0.16265327 | %p | -4.7150193 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 384.68775 | 16.517787 | price | -4.4864569 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 578.66159 | 26.307162 | price | -4.7627322 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0448646 | 0.044864569 | ratio | -4.4864569 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 5.0895557 | -0.24224557 | %p | 4.5434096 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 245.29762 | -4.2539683 | price | 1.7046448 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 401.33782 | -8.7186683 | price | 2.1262115 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.98295355 | -0.017046448 | ratio | 1.7046448 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.5044096 | -0.082184114 | %p | 0.95712126 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 1037.9447 | -11.29249 | price | 1.0762572 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1818.4087 | -12.449866 | price | 0.6800015 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.98923743 | -0.010762572 | ratio | 1.0762572 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7138837 | 0.086325781 | %p | -2.3797216 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 98.12253 | 2.0948617 | price | -2.1815188 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 146.94089 | -7.9419954 | price | 5.1277425 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 1.0218152 | 0.021815188 | ratio | -2.1815188 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.984275 | 0.37696773 | %p | -5.7053155 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1393.4466 | 37.711462 | price | -2.7816245 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2268.1128 | 27.003394 | price | -1.2049119 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0278162 | 0.027816245 | ratio | -2.7816245 | worsened |
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
| mape | 4.6062595 | 4.6946164 | 0.088356895 | %p | -1.9181919 | worsened |
| mae | 565.55167 | 610.47958 | 44.927904 | price | -7.9440848 | worsened |
| rmse | 926.40586 | 966.24522 | 39.839363 | price | -4.3004222 | worsened |
| rmae | 1.0199316 | 1.0623702 | 0.042438655 | ratio | -4.1609316 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.457701 | -0.27211005 | %p | 5.7530851 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.94862 | -7.8814229 | price | 5.7182186 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 195.98021 | -13.198737 | price | 6.3097827 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.9398262 | -0.057000743 | ratio | 5.7182186 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7839442 | 0.051787871 | %p | -0.90346229 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.83794 | 0.17391304 | price | -0.14533443 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.07079 | 1.3318077 | price | -0.74511315 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0353082 | 0.0015024757 | ratio | -0.14533443 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 3.1892301 | 0.50879157 | %p | -18.981654 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 575 | 84.395257 | price | -17.202291 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 839.96234 | 60.880481 | price | -7.8143882 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 1.1098354 | 0.16289538 | ratio | -17.202291 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3331261 | -0.25787416 | %p | 5.6169493 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 95.768924 | -7.187251 | price | 6.9808838 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 150.26818 | -14.766888 | price | 8.9477275 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.95162312 | -0.07141726 | ratio | 6.9808838 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.2777011 | 0.21103 | %p | -19.783979 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 2024.7411 | 313.27232 | price | -18.304297 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 3082.7088 | 243.76863 | price | -8.5866066 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.5204224 | 0.23524304 | ratio | -18.304297 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.6123373 | 0.073643752 | %p | -2.0811 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 384.68775 | 6.6126482 | price | -1.7490303 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 578.66159 | 13.287561 | price | -2.3502248 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0448646 | 0.017960858 | ratio | -1.7490303 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 5.0895557 | 0.31105994 | %p | -6.5095787 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 245.29762 | 20.075397 | price | -8.913595 | worsened |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 401.33782 | 27.99816 | price | -7.49938 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.98295355 | 0.080445879 | ratio | -8.913595 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.5044096 | 0.42567765 | %p | -5.2691147 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 1037.9447 | 73.802372 | price | -7.6547178 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1818.4087 | 114.43848 | price | -6.7159907 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.98923743 | 0.070339076 | ratio | -7.6547178 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7138837 | 0.064880443 | %p | -1.7780319 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 98.12253 | 0.98023715 | price | -1.0090735 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 146.94089 | -8.2202932 | price | 5.2979058 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0218152 | 0.010207862 | ratio | -1.0090735 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.984275 | -0.23331807 | %p | 3.2326299 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1393.4466 | -34.964427 | price | 2.4477847 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2268.1128 | -27.125572 | price | 1.1818194 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0278162 | -0.025790012 | ratio | 2.4477847 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 3, 'worsened': 7, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.


### MARKET: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.5011413 | 4.6946164 | 0.19347507 | %p | -4.2983558 | worsened |
| mae | 557.9753 | 610.47958 | 52.504273 | price | -9.4097843 | worsened |
| rmse | 915.84853 | 966.24522 | 50.396686 | price | -5.5027315 | worsened |
| rmae | 0.99470404 | 1.0623702 | 0.067666179 | ratio | -6.8026444 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.457701 | 0.031273215 | %p | -0.70651136 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.94862 | 1.201581 | price | -0.93328831 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 195.98021 | 4.3999768 | price | -2.2966758 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.9398262 | 0.0086901835 | ratio | -0.93328831 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.7839442 | 0.051029681 | %p | -0.89011759 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 119.83794 | 0.3201581 | price | -0.26787486 | worsened |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 180.07079 | -0.80129395 | price | 0.44301692 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0353082 | 0.0027659211 | ratio | -0.26787486 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 3.1892301 | 0.45491495 | %p | -16.637254 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 575 | 81.225296 | price | -16.44987 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 839.96234 | 51.704449 | price | -6.5593316 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 1.1098354 | 0.15677688 | ratio | -16.44987 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3331261 | -0.092062427 | %p | 2.0804182 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 95.768924 | -3.0916335 | price | 3.1272669 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 150.26818 | -8.4447961 | price | 5.3207975 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.95162312 | -0.030720507 | ratio | 3.1272669 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.2777011 | 0.23680176 | %p | -22.749726 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 2024.7411 | 343.04464 | price | -20.398726 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 3082.7088 | 288.30052 | price | -10.317051 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.5204224 | 0.25759973 | ratio | -20.398726 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.6123373 | 0.15464596 | %p | -4.4725207 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 384.68775 | 14.833992 | price | -4.0107723 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 578.66159 | 27.07423 | price | -4.908421 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0448646 | 0.040291153 | ratio | -4.0107723 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 5.0895557 | 0.33528348 | %p | -7.0522568 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 245.29762 | 22.698413 | price | -10.196987 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 401.33782 | 44.073493 | price | -12.336382 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.98295355 | 0.090956796 | ratio | -10.196987 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.5044096 | 0.56461656 | %p | -7.1112251 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 1037.9447 | 78.098814 | price | -8.1365997 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1818.4087 | 108.52484 | price | -6.3469129 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.98923743 | 0.074433901 | ratio | -8.1365997 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.7138837 | 0.35680125 | %p | -10.628313 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 98.12253 | 8.8537549 | price | -9.9180872 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 146.94089 | 5.8100092 | price | -4.1167526 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 1.0218152 | 0.092200041 | ratio | -9.9180872 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.984275 | -0.15855372 | %p | 2.2197608 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1393.4466 | -22.142292 | price | 1.5641753 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2268.1128 | -16.674578 | price | 0.72980876 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0278162 | -0.016332314 | ratio | 1.5641753 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 2, 'worsened': 8, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

