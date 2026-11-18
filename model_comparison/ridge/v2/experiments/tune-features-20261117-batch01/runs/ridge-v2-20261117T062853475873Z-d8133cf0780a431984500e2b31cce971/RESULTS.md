
## ridge-v2-20261117T062853475873Z-d8133cf0780a431984500e2b31cce971

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062853475873Z-d8133cf0780a431984500e2b31cce971 | macro | 4.6044063 | 567.52067 | 929.91525 | 1.0207438 | 0.040232141 (direct) | 0.058237562 (direct) | 7 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6044063 | -0.0026830565 | %p | 0.058237562 | improved |
| mae | 532.31701 | 567.52067 | 35.203662 | price | -6.613289 | worsened |
| rmse | 943.1701 | 929.91525 | -13.254846 | price | 1.4053505 | improved |
| rmae | 1 | 1.0207438 | 0.020743802 | ratio | -2.0743802 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7212194 | -0.047277186 | %p | 0.99144847 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.66008 | -0.60869565 | price | 0.4402264 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 208.73386 | -2.0521858 | price | 0.9735871 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99559774 | -0.004402264 | ratio | 0.4402264 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7617093 | 0.25964749 | %p | -4.7190944 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 120.36364 | 4.6126482 | price | -3.9849752 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.12762 | 8.9915328 | price | -5.2540249 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.0398498 | 0.039849752 | ratio | -3.9849752 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6675295 | -0.22587386 | %p | 7.8065112 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 487.86957 | -30.225296 | price | 5.8339309 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 773.03746 | -55.426022 | price | 6.6902191 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.94166069 | -0.058339309 | ratio | 5.8339309 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.5871734 | 0.080531466 | %p | -1.7869506 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 102.8247 | 2.187251 | price | -2.1733967 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.84484 | 5.9817461 | price | -3.7653466 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.021734 | 0.021733967 | ratio | -2.1733967 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.080293 | 0.2829473 | %p | -35.486152 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1735.4062 | 403.70982 | price | -30.315454 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2879.2952 | 6.1047671 | price | -0.21247346 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3031545 | 0.30315454 | ratio | -30.315454 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5228175 | 0.07313344 | %p | -2.120004 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 376.26482 | 8.0948617 | price | -2.1986752 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 563.40851 | 11.054079 | price | -2.0012655 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0219868 | 0.021986752 | ratio | -2.1986752 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7682384 | -0.56356283 | %p | 10.569839 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 224.85714 | -24.694444 | price | 9.8955269 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 372.72672 | -37.329768 | price | 9.1035672 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.90104473 | -0.098955269 | ratio | 9.8955269 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0569359 | -0.52965785 | %p | 6.168428 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 961.19368 | -88.043478 | price | 8.3911895 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1701.8576 | -129.00104 | price | 7.0459314 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.9160881 | -0.083911895 | ratio | 8.3911895 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.6433939 | 0.015836019 | %p | -0.43654764 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 97.011858 | 0.98418972 | price | -1.0249022 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 155.15885 | 0.27596693 | price | -0.17817781 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.010249 | 0.010249022 | ratio | -1.0249022 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.2347528 | 0.62744545 | %p | -9.4962354 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1431.7549 | 76.019763 | price | -5.6072723 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2299.9619 | 58.852464 | price | -2.6260415 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0560727 | 0.056072723 | ratio | -5.6072723 | worsened |
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
| mape | 4.6062595 | 4.6044063 | -0.0018531968 | %p | 0.040232141 | improved |
| mae | 565.55167 | 567.52067 | 1.9689958 | price | -0.3481549 | worsened |
| rmse | 926.40586 | 929.91525 | 3.5093947 | price | -0.37881828 | worsened |
| rmae | 1.0199316 | 1.0207438 | 0.00081223386 | ratio | -0.079636114 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7212194 | -0.0085916571 | %p | 0.18164906 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.66008 | -0.16996047 | price | 0.12331163 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 208.73386 | -0.44507837 | price | 0.21277399 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99559774 | -0.0012292036 | ratio | 0.12331163 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7617093 | 0.029552936 | %p | -0.51556402 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 120.36364 | 0.69960474 | price | -0.58464079 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.12762 | 1.3886384 | price | -0.77690855 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.0398498 | 0.0060440499 | ratio | -0.58464079 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6675295 | -0.012909051 | %p | 0.48160218 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 487.86957 | -2.7351779 | price | 0.5575115 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 773.03746 | -6.044399 | price | 0.77583619 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.94166069 | -0.0052792993 | ratio | 0.5575115 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.5871734 | -0.0038268667 | %p | 0.083355838 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 102.8247 | -0.1314741 | price | 0.12769909 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.84484 | -0.1902298 | price | 0.11526629 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.021734 | -0.0013064133 | ratio | 0.12769909 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.080293 | 0.013621822 | %p | -1.2770405 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1735.4062 | 23.9375 | price | -1.3986525 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2879.2952 | 40.355002 | price | -1.4214812 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3031545 | 0.017975193 | ratio | -1.3986525 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5228175 | -0.015876077 | %p | 0.44864233 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 376.26482 | -1.8102767 | price | 0.47881405 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 563.40851 | -1.9655231 | price | 0.34765006 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0219868 | -0.0049169592 | ratio | 0.47881405 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7682384 | -0.01025732 | %p | 0.21465583 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 224.85714 | -0.36507937 | price | 0.1620974 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 372.72672 | -0.61293963 | price | 0.16417748 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.90104473 | -0.0014629415 | ratio | 0.1620974 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0569359 | -0.021796089 | %p | 0.26979592 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 961.19368 | -2.9486166 | price | 0.30582795 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1701.8576 | -2.1126912 | price | 0.12398639 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.9160881 | -0.002810248 | ratio | 0.30582795 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.6433939 | -0.0056093195 | %p | 0.15372196 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 97.011858 | -0.13043478 | price | 0.13427188 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 155.15885 | -0.0023308845 | price | 0.0015022343 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.010249 | -0.0013583042 | ratio | 0.13427188 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.2347528 | 0.017159654 | %p | -0.2377476 | worsened |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1431.7549 | 3.3438735 | price | -0.23409742 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2299.9619 | 4.7234988 | price | -0.20579557 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0560727 | 0.0024664651 | ratio | -0.23409742 | worsened |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

