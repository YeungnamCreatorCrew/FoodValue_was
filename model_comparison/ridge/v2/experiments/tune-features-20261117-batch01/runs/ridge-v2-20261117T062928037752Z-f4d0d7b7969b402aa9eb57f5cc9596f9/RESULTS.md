
## ridge-v2-20261117T062928037752Z-f4d0d7b7969b402aa9eb57f5cc9596f9

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062928037752Z-f4d0d7b7969b402aa9eb57f5cc9596f9 | production | 4.6070909 | 568.42594 | 928.85113 | 1.021895 | -0.018048907 (direct) | -3.2987938e-05 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6070909 | 1.5197838e-06 | %p | -3.2987938e-05 | worsened |
| mae | 532.31701 | 568.42594 | 36.108936 | price | -6.783352 | worsened |
| rmse | 943.1701 | 928.85113 | -14.318964 | price | 1.5181741 | improved |
| rmae | 1 | 1.021895 | 0.021894961 | ratio | -2.1894961 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7259855 | -0.042511046 | %p | 0.89149788 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.71937 | -0.54940711 | price | 0.39734721 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 209.07577 | -1.7102841 | price | 0.81138393 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99602653 | -0.0039734721 | ratio | 0.39734721 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7351679 | 0.23310615 | %p | -4.2367054 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.71937 | 3.9683794 | price | -3.4283763 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 178.81911 | 7.6830163 | price | -4.4894191 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0342838 | 0.034283763 | ratio | -3.4283763 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6785051 | -0.2148983 | %p | 7.4271808 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 490.20158 | -27.893281 | price | 5.3838173 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 778.86814 | -49.595337 | price | 5.9864241 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94616183 | -0.053838173 | ratio | 5.3838173 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5906037 | 0.083961805 | %p | -1.863068 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.94422 | 2.3067729 | price | -2.2921615 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 165.04602 | 6.1829233 | price | -3.8919822 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0229216 | 0.022921615 | ratio | -2.2921615 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0866032 | 0.28925749 | %p | -36.277551 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1741.0223 | 409.32589 | price | -30.737177 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2864.0397 | -9.1506988 | price | 0.31848564 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3073718 | 0.30737177 | ratio | -30.737177 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5414678 | 0.091783722 | %p | -2.6606414 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 378.39526 | 10.225296 | price | -2.7773305 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 565.37581 | 13.021381 | price | -2.3574321 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0277733 | 0.027773305 | ratio | -2.7773305 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7760186 | -0.55578268 | %p | 10.42392 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 225.09524 | -24.456349 | price | 9.8001177 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 373.24115 | -36.815341 | price | 8.9781144 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90199882 | -0.098001177 | ratio | 9.8001177 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0771641 | -0.50942959 | %p | 5.9328484 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 963.93676 | -85.300395 | price | 8.1297536 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1703.9284 | -126.93017 | price | 6.9328222 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91870246 | -0.081297536 | ratio | 8.1297536 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6437059 | 0.016148026 | %p | -0.44514867 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.011858 | 0.98418972 | price | -1.0249022 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.00598 | 0.12309653 | price | -0.079477171 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.010249 | 0.010249022 | ratio | -1.0249022 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2156869 | 0.60837963 | %p | -9.2076787 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1428.2134 | 72.478261 | price | -5.3460486 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2295.1112 | 54.001777 | price | -2.4096002 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0534605 | 0.053460486 | ratio | -5.3460486 | worsened |
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
| mape | 4.6062595 | 4.6070909 | 0.00083137949 | %p | -0.018048907 | worsened |
| mae | 565.55167 | 568.42594 | 2.8742698 | price | -0.50822409 | worsened |
| rmse | 926.40586 | 928.85113 | 2.445277 | price | -0.2639531 | worsened |
| rmae | 1.0199316 | 1.021895 | 0.0019633924 | ratio | -0.19250237 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7259855 | -0.0038255167 | %p | 0.080880962 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.71937 | -0.11067194 | price | 0.080295948 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 209.07577 | -0.10317672 | price | 0.049324622 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99602653 | -0.00080041164 | ratio | 0.080295948 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7351679 | 0.0030115949 | %p | -0.052538603 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.71937 | 0.055335968 | price | -0.046242775 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 178.81911 | 0.080121866 | price | -0.044826184 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0342838 | 0.00047806044 | ratio | -0.046242775 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6785051 | -0.0019334925 | %p | 0.07213344 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 490.20158 | -0.40316206 | price | 0.082176551 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 778.86814 | -0.21371451 | price | 0.027431586 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94616183 | -0.00077816262 | ratio | 0.082176551 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5906037 | -0.00039652709 | %p | 0.0086370522 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.94422 | -0.011952191 | price | 0.011609009 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 165.04602 | 0.010947449 | price | -0.0066334077 | worsened |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0229216 | -0.00011876485 | ratio | 0.011609009 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0866032 | 0.019932011 | %p | -1.8686182 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1741.0223 | 29.553571 | price | -1.7267959 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2864.0397 | 25.099536 | price | -0.88411642 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3073718 | 0.022192424 | ratio | -1.7267959 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5414678 | 0.0027742053 | %p | -0.078396314 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 378.39526 | 0.3201581 | price | -0.084681087 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 565.37581 | 0.0017792244 | price | -0.00031469864 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0277733 | 0.00086959322 | ratio | -0.084681087 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7760186 | -0.0024771713 | %p | 0.051839981 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 225.09524 | -0.12698413 | price | 0.056381704 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 373.24115 | -0.098512604 | price | 0.026386858 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90199882 | -0.00050884921 | ratio | 0.056381704 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0771641 | -0.0015678237 | %p | 0.019406805 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 963.93676 | -0.2055336 | price | 0.021317766 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1703.9284 | -0.041821002 | price | 0.002454327 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91870246 | -0.0001958886 | ratio | 0.021317766 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6437059 | -0.0052973123 | %p | 0.14517149 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.011858 | -0.13043478 | price | 0.13427188 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 155.00598 | -0.15520128 | price | 0.10002584 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.010249 | -0.0013583042 | ratio | 0.13427188 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2156869 | -0.0019061729 | %p | 0.02641009 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1428.2134 | -0.19762846 | price | 0.013835545 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2295.1112 | -0.12718898 | price | 0.0055414281 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0534605 | -0.00014577217 | ratio | 0.013835545 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

