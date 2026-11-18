
## ridge-v2-20261117T062737690863Z-ddfade71413c4456b57b0f07faa038b0

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261117T062737690863Z-ddfade71413c4456b57b0f07faa038b0 | national_weather | 4.6210401 | 569.84518 | 929.25162 | 1.0259097 | -0.32088125 (direct) | -0.30281078 (direct) | 5 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.6210401 | 0.013950763 | %p | -0.30281078 | worsened |
| mae | 532.31701 | 569.84518 | 37.528171 | price | -7.0499665 | worsened |
| rmse | 943.1701 | 929.25162 | -13.918476 | price | 1.4757122 | improved |
| rmae | 1 | 1.0259097 | 0.025909733 | ratio | -2.5909733 | worsened |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.7231356 | -0.045360937 | %p | 0.95126288 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 137.54545 | -0.72332016 | price | 0.52312618 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 206.43594 | -4.3501074 | price | 2.0637549 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.99476874 | -0.0052312618 | ratio | 0.52312618 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.8595996 | 0.35753778 | %p | -6.4982509 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 122.41107 | 6.6600791 | price | -5.7537989 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 182.78387 | 11.647784 | price | -6.8061531 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.057538 | 0.057537989 | ratio | -5.7537989 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.6076633 | -0.28574003 | %p | 9.8755684 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 475.56917 | -42.525692 | price | 8.2080898 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 759.36063 | -69.102846 | price | 8.3410854 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.9179191 | -0.082080898 | ratio | 8.2080898 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.6295193 | 0.12287739 | %p | -2.7265842 | worsened |
| 8 | 양파/RETAIL | mae | 100.63745 | 103.51394 | 2.876494 | price | -2.858274 | worsened |
| 8 | 양파/RETAIL | rmse | 158.86309 | 164.93674 | 6.0736456 | price | -3.8231949 | worsened |
| 8 | 양파/RETAIL | rmae | 1 | 1.0285827 | 0.02858274 | ratio | -2.858274 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.1189229 | 0.32157724 | %p | -40.330969 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1781.4018 | 449.70536 | price | -33.76936 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2892.6796 | 19.48922 | price | -0.67831287 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.3376936 | 0.3376936 | ratio | -33.76936 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.5556084 | 0.10592439 | %p | -3.0705534 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 379.73913 | 11.56917 | price | -3.1423449 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 574.06736 | 21.712929 | price | -3.9309777 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0314234 | 0.031423449 | ratio | -3.1423449 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.7466166 | -0.58518467 | %p | 10.975365 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 223.61508 | -25.936508 | price | 10.393245 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 370.59867 | -39.457812 | price | 9.6225309 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.89606755 | -0.10393245 | ratio | 10.393245 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 8.0174615 | -0.56913225 | %p | 6.6281492 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 952.86561 | -96.371542 | price | 9.1849151 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1695.3055 | -135.55309 | price | 7.4037987 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.90815085 | -0.091849151 | ratio | 9.1849151 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.7572296 | 0.12967167 | %p | -3.5746272 | worsened |
| 9011 | 무/RETAIL | mae | 96.027668 | 99.675889 | 3.6482213 | price | -3.7991356 | worsened |
| 9011 | 무/RETAIL | rmse | 154.88288 | 156.6686 | 1.7857205 | price | -1.1529489 | worsened |
| 9011 | 무/RETAIL | rmae | 1 | 1.0379914 | 0.037991356 | ratio | -3.7991356 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1946444 | 0.58733705 | %p | -8.8892044 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1422.1146 | 66.379447 | price | -4.8961956 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2289.6792 | 48.569791 | price | -2.1672208 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.048962 | 0.048961956 | ratio | -4.8961956 | worsened |
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
| mape | 4.6062595 | 4.6210401 | 0.014780623 | %p | -0.32088125 | worsened |
| mae | 565.55167 | 569.84518 | 4.2935045 | price | -0.75917104 | worsened |
| rmse | 926.40586 | 929.25162 | 2.8457649 | price | -0.30718338 | worsened |
| rmae | 1.0199316 | 1.0259097 | 0.0059781643 | ratio | -0.58613386 | worsened |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.7231356 | -0.0066754085 | %p | 0.14113478 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 137.54545 | -0.28458498 | price | 0.20647529 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 206.43594 | -2.743 | price | 1.3113175 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.99476874 | -0.0020582014 | ratio | 0.20647529 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.8595996 | 0.12744322 | %p | -2.2233033 | worsened |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 122.41107 | 2.7470356 | price | -2.2956235 | worsened |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 182.78387 | 4.0448899 | price | -2.2630149 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.057538 | 0.023732286 | ratio | -2.2956235 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.6076633 | -0.072775222 | %p | 2.7150491 | improved |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 475.56917 | -15.035573 | price | 3.0647019 | improved |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 759.36063 | -19.721224 | price | 2.5313417 | improved |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.9179191 | -0.029020888 | ratio | 3.0647019 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.6295193 | 0.038519056 | %p | -0.83901228 | worsened |
| 8 | 양파/RETAIL | mae | 102.95618 | 103.51394 | 0.55776892 | price | -0.54175373 | worsened |
| 8 | 양파/RETAIL | rmse | 165.03507 | 164.93674 | -0.098330265 | price | 0.059581437 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 1.0285827 | 0.0055423595 | ratio | -0.54175373 | worsened |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.1189229 | 0.052251761 | %p | -4.8985821 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1781.4018 | 69.933036 | price | -4.0861416 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2892.6796 | 53.739456 | price | -1.8929407 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.3376936 | 0.052514247 | ratio | -4.0861416 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.5556084 | 0.016914874 | %p | -0.4779977 | worsened |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 379.73913 | 1.6640316 | price | -0.44013256 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 574.06736 | 8.6933278 | price | -1.5376242 | worsened |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0314234 | 0.0045197376 | ratio | -0.44013256 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.7466166 | -0.031879158 | %p | 0.66713794 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 223.61508 | -1.6071429 | price | 0.71358094 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 370.59867 | -2.7409839 | price | 0.73417969 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.89606755 | -0.0064401228 | ratio | 0.71358094 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 8.0174615 | -0.061270482 | %p | 0.75841707 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 952.86561 | -11.27668 | price | 1.1696074 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1695.3055 | -8.6647345 | price | 0.50850268 | improved |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.90815085 | -0.010747503 | ratio | 1.1696074 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.7572296 | 0.10822633 | %p | -2.965915 | worsened |
| 9011 | 무/RETAIL | mae | 97.142292 | 99.675889 | 2.5335968 | price | -2.6081296 | worsened |
| 9011 | 무/RETAIL | rmse | 155.16118 | 156.6686 | 1.5074227 | price | -0.9715205 | worsened |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 1.0379914 | 0.02638403 | ratio | -2.6081296 | worsened |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1946444 | -0.022948748 | %p | 0.31795569 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1422.1146 | -6.2964427 | price | 0.44080047 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2289.6792 | -5.5591751 | price | 0.24220469 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.048962 | -0.0046443013 | ratio | 0.44080047 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 5, 'worsened': 5, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

