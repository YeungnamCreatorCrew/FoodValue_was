
## ridge-v2-20261118T150814414112Z-eaefa901772c430390ce7a0eaa984a44

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150814414112Z-eaefa901772c430390ce7a0eaa984a44 | market_alpha10000 | 4.5033712 | 545.55261 | 923.9768 | 0.98770075 | 2.2336624 (direct) | 2.2512727 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.5033712 | -0.10371814 | %p | 2.2512727 | improved |
| mae | 532.31701 | 545.55261 | 13.235601 | price | -2.4864134 | worsened |
| rmse | 943.1701 | 923.9768 | -19.193301 | price | 2.0349777 | improved |
| rmae | 1 | 0.98770075 | -0.012299247 | ratio | 1.2299247 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.5687861 | -0.19971048 | %p | 4.1881227 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 132.49407 | -5.7747036 | price | 4.1764336 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 200.90905 | -9.8769994 | price | 4.6857937 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.95823566 | -0.041764336 | ratio | 4.1764336 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.5281898 | 0.026128048 | %p | -0.47487741 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 116.08696 | 0.33596838 | price | -0.29025098 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 175.78636 | 4.6502743 | price | -2.7172961 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0029025 | 0.0029025098 | ratio | -0.29025098 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.7230932 | -0.17031014 | %p | 5.8861527 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 488.77075 | -29.324111 | price | 5.6599887 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 804.6988 | -23.764679 | price | 2.8685246 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94340011 | -0.056599887 | ratio | 5.6599887 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.3949205 | -0.11172142 | %p | 2.4790392 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.01992 | -2.6175299 | price | 2.6009501 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.02765 | -0.83544575 | price | 0.5258904 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.9739905 | -0.026009501 | ratio | 2.6009501 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 0.95503869 | 0.15769302 | %p | -19.777246 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1550.8616 | 219.16518 | price | -16.457593 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2781.8648 | -91.325642 | price | 3.1785447 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.1645759 | 0.16457593 | ratio | -16.457593 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4713873 | 0.021703222 | %p | -0.62913651 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 371.00791 | 2.8379447 | price | -0.77082461 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 555.61058 | 3.2561494 | price | -0.58950362 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0077082 | 0.0077082461 | ratio | -0.77082461 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7823904 | -0.54941088 | %p | 10.304414 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 224.06746 | -25.484127 | price | 10.211967 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 387.53829 | -22.518198 | price | 5.4914868 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89788033 | -0.10211967 | ratio | 10.211967 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.2351398 | -0.3514539 | %p | 4.0930538 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 992.64427 | -56.592885 | price | 5.3937172 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1769.3735 | -61.485152 | price | 3.3582687 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.94606283 | -0.053937172 | ratio | 5.3937172 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.4514485 | -0.17610937 | %p | 4.8547639 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 91.920949 | -4.1067194 | price | 4.2766001 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 147.1154 | -7.7674839 | price | 5.0150693 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.957234 | -0.042766001 | ratio | 4.2766001 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 6.9233178 | 0.31601047 | %p | -4.7827422 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1389.6522 | 33.916996 | price | -2.501742 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2258.8436 | 17.734166 | price | -0.79131192 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0250174 | 0.02501742 | ratio | -2.501742 | worsened |
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
| mape | 4.6062595 | 4.5033712 | -0.10288828 | %p | 2.2336624 | improved |
| mae | 565.55167 | 545.55261 | -19.999065 | price | 3.5362047 | improved |
| rmse | 926.40586 | 923.9768 | -2.4290601 | price | 0.26220259 | improved |
| rmae | 1.0199316 | 0.98770075 | -0.032230815 | ratio | 3.1600958 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.5687861 | -0.16102495 | %p | 3.4044691 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 132.49407 | -5.3359684 | price | 3.8714118 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 200.90905 | -8.269892 | price | 3.9535012 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.95823566 | -0.038591276 | ratio | 3.8714118 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.5281898 | -0.20396651 | %p | 3.5582858 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 116.08696 | -3.5770751 | price | 2.9892651 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 175.78636 | -2.9526201 | price | 1.6519172 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0029025 | -0.030903193 | ratio | 2.9892651 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.7230932 | 0.042654667 | %p | -1.5913316 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 488.77075 | -1.8339921 | price | 0.37382274 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 804.6988 | 25.616944 | price | -3.288094 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94340011 | -0.003539877 | ratio | 0.37382274 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.3949205 | -0.19607975 | %p | 4.2709593 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.01992 | -4.936255 | price | 4.7945205 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.02765 | -7.0074216 | price | 4.2460198 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.9739905 | -0.049049881 | ratio | 4.7945205 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 0.95503869 | -0.11163246 | %p | 10.465499 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1550.8616 | -160.60714 | price | 9.3841703 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2781.8648 | -57.075407 | price | 2.0104477 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.1645759 | -0.12060342 | ratio | 9.3841703 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4713873 | -0.067306295 | %p | 1.9020097 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 371.00791 | -7.0671937 | price | 1.8692566 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 555.61058 | -9.7634523 | price | 1.7269014 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0077082 | -0.019195465 | ratio | 1.8692566 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7823904 | 0.003894636 | %p | -0.081503389 | worsened |
| 9001 | 배추/RETAIL | mae | 225.22222 | 224.06746 | -1.1547619 | price | 0.51272112 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 387.53829 | 14.19863 | price | -3.8031401 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89788033 | -0.0046273475 | ratio | 0.51272112 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.2351398 | 0.15640786 | %p | -1.9360447 | worsened |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 992.64427 | 28.501976 | price | -2.9562002 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1769.3735 | 65.403199 | price | -3.8382829 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.94606283 | 0.027164475 | ratio | -2.9562002 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.4514485 | -0.19755471 | %p | 5.4139363 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 91.920949 | -5.2213439 | price | 5.3749441 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 147.1154 | -8.0457817 | price | 5.1854347 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.957234 | -0.054373328 | ratio | 5.3749441 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 6.9233178 | -0.29427533 | %p | 4.0771947 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1389.6522 | -38.758893 | price | 2.7134271 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2258.8436 | -36.3948 | price | 1.5856654 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0250174 | -0.028588838 | ratio | 2.7134271 | improved |
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
| mape | 4.5011413 | 4.5033712 | 0.0022298911 | %p | -0.049540571 | worsened |
| mae | 557.9753 | 545.55261 | -12.422697 | price | 2.2263883 | improved |
| rmse | 915.84853 | 923.9768 | 8.1282625 | price | -0.88751165 | worsened |
| rmae | 0.99470404 | 0.98770075 | -0.0070032915 | ratio | 0.70405781 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.5687861 | 0.14235831 | %p | -3.2160993 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 132.49407 | 3.7470356 | price | -2.9103859 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 200.90905 | 9.3288215 | price | -4.8694072 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.95823566 | 0.027099651 | ratio | -2.9103859 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.5281898 | -0.2047247 | %p | 3.5710404 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 116.08696 | -3.43083 | price | 2.8705602 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 175.78636 | -5.0857217 | price | 2.8117781 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.0029025 | -0.029639747 | ratio | 2.8705602 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.7230932 | -0.011221958 | %p | 0.410412 | improved |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 488.77075 | -5.0039526 | price | 1.013408 | improved |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 804.6988 | 16.440912 | price | -2.0857275 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.94340011 | -0.0096583714 | ratio | 1.013408 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.3949205 | -0.030268025 | %p | 0.68399403 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.01992 | -0.84063745 | price | 0.85032643 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.02765 | -0.68532957 | price | 0.43180437 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.9739905 | -0.0083531275 | ratio | 0.85032643 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 0.95503869 | -0.0858607 | %p | 8.2487031 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1550.8616 | -130.83482 | price | 7.779931 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2781.8648 | -12.543509 | price | 0.44887889 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.1645759 | -0.098246731 | ratio | 7.779931 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4713873 | 0.013695913 | %p | -0.39609993 | worsened |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 371.00791 | 1.1541502 | price | -0.31205583 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 555.61058 | 4.0232174 | price | -0.72938897 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0077082 | 0.0031348299 | ratio | -0.31205583 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.7823904 | 0.02811818 | %p | -0.59142974 | worsened |
| 9001 | 배추/RETAIL | mae | 222.59921 | 224.06746 | 1.468254 | price | -0.65959533 | worsened |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 387.53829 | 30.273963 | price | -8.4738277 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.89788033 | 0.0058835689 | ratio | -0.65959533 | worsened |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 8.2351398 | 0.29534677 | %p | -3.7198295 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 992.64427 | 32.798419 | price | -3.4170507 | worsened |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1769.3735 | 59.489557 | price | -3.4791577 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.94606283 | 0.0312593 | ratio | -3.4170507 | worsened |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.4514485 | 0.094366092 | %p | -2.8109554 | worsened |
| 9011 | 무/RETAIL | mae | 89.268775 | 91.920949 | 2.6521739 | price | -2.9709985 | worsened |
| 9011 | 무/RETAIL | rmse | 141.13088 | 147.1154 | 5.9845207 | price | -4.2404049 | worsened |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.957234 | 0.027618852 | ratio | -2.9709985 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 6.9233178 | -0.21951097 | %p | 3.0731658 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1389.6522 | -25.936759 | price | 1.8322239 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2258.8436 | -25.943807 | price | 1.135502 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0250174 | -0.01913114 | ratio | 1.8322239 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

