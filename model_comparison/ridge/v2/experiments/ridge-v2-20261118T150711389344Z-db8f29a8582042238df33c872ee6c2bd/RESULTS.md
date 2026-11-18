
## ridge-v2-20261118T150711389344Z-db8f29a8582042238df33c872ee6c2bd

| 실행 ID | 실험 | MAPE (%) | MAE | RMSE | rMAE | CONTROL 대비 MAPE 개선률 (%) | Naive 대비 개선률 (%) | 개선 계열 수 |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| ridge-v2-20261118T150711389344Z-db8f29a8582042238df33c872ee6c2bd | market_alpha100 | 4.4912665 | 555.59925 | 916.80348 | 0.99189299 | 2.4964496 (direct) | 2.5140126 (direct) | 9 |

Precision: unrounded errors from common final integer predictions. All aggregate MAE/RMSE values are descriptive macro averages across price units.


### Naive: direct

Matched evaluation conditions; numerical improvements alone do not establish causality.
Metric scope: policy includes Naive fallback. model_only uses successful model predictions; paired_analysis.common_success uses the identical successful observation set (comparison.json).
Reasons: identical recorded evaluation conditions

| 전체 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | ---: | ---: | ---: | --- | ---: | --- |
| mape | 4.6070894 | 4.4912665 | -0.11582281 | %p | 2.5140126 | improved |
| mae | 532.31701 | 555.59925 | 23.282248 | price | -4.3737562 | worsened |
| rmse | 943.1701 | 916.80348 | -26.366614 | price | 2.7955312 | improved |
| rmae | 1 | 0.99189299 | -0.0081070077 | ratio | 0.81070077 | improved |
| success_rate_pct | 100 | 99.239392 | -0.76060849 | %p | -0.76060849 | worsened |
| valid_predictions | 2498 | 2479 | -19 | count | -0.76060849 | count_change |
| failed_predictions | 0 | 19 | 19 | count | N/A | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.7684965 | 4.4368173 | -0.33167927 | %p | 6.9556362 | improved |
| 1 | 대파/RETAIL | mae | 138.26877 | 129.01186 | -9.256917 | price | 6.6948716 | improved |
| 1 | 대파/RETAIL | rmse | 210.78605 | 192.05094 | -18.735106 | price | 8.8882095 | improved |
| 1 | 대파/RETAIL | rmae | 1 | 0.93305128 | -0.066948716 | ratio | 6.6948716 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.5020618 | 5.7068277 | 0.20476593 | %p | -3.7216218 | worsened |
| 2 | 대파/WHOLESALE | mae | 115.75099 | 119.02767 | 3.2766798 | price | -2.8308008 | worsened |
| 2 | 대파/WHOLESALE | rmse | 171.13609 | 180.44333 | 9.3072377 | price | -5.4385008 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1 | 1.028308 | 0.028308008 | ratio | -2.8308008 | worsened |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.8934034 | 2.740216 | -0.15318741 | %p | 5.2943674 | improved |
| 7 | 양파/WHOLESALE | mae | 518.09486 | 494.12253 | -23.972332 | price | 4.627016 | improved |
| 7 | 양파/WHOLESALE | rmse | 828.46348 | 792.80326 | -35.660217 | price | 4.30438 | improved |
| 7 | 양파/WHOLESALE | rmae | 1 | 0.95372984 | -0.04627016 | ratio | 4.627016 | improved |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5066419 | 4.4088952 | -0.09774667 | %p | 2.1689469 | improved |
| 8 | 양파/RETAIL | mae | 100.63745 | 98.501992 | -2.1354582 | price | 2.1219319 | improved |
| 8 | 양파/RETAIL | rmse | 158.86309 | 158.25039 | -0.61269807 | price | 0.38567679 | improved |
| 8 | 양파/RETAIL | rmae | 1 | 0.97878068 | -0.021219319 | ratio | 2.1219319 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 0.79734567 | 1.0311302 | 0.23378456 | %p | -29.320353 | worsened |
| 9 | 깐마늘/WHOLESALE | mae | 1331.6964 | 1666.1205 | 334.42411 | price | -25.112638 | worsened |
| 9 | 깐마늘/WHOLESALE | rmse | 2873.1904 | 2804.8795 | -68.31094 | price | 2.3775291 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1 | 1.2511264 | 0.25112638 | ratio | -25.112638 | worsened |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 100 | 91.517857 | -8.4821429 | %p | -8.4821429 | worsened |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 224 | 205 | -19 | count | -8.4821429 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 0 | 19 | 19 | count | N/A | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.449684 | 3.4541526 | 0.0044685658 | %p | -0.12953551 | worsened |
| 10 | 깐마늘/RETAIL | mae | 368.16996 | 369.41502 | 1.2450593 | price | -0.33817514 | worsened |
| 10 | 깐마늘/RETAIL | rmse | 552.35443 | 550.60557 | -1.7488656 | price | 0.31662019 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1 | 1.0033818 | 0.0033817514 | ratio | -0.33817514 | worsened |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 5.3318013 | 4.73088 | -0.60092124 | %p | 11.270511 | improved |
| 9001 | 배추/RETAIL | mae | 249.55159 | 221.61111 | -27.940476 | price | 11.196273 | improved |
| 9001 | 배추/RETAIL | rmse | 410.05649 | 358.84957 | -51.206913 | price | 12.487771 | improved |
| 9001 | 배추/RETAIL | rmae | 1 | 0.88803727 | -0.11196273 | ratio | 11.196273 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.5865937 | 7.9411167 | -0.64547707 | %p | 7.5172657 | improved |
| 9002 | 배추/WHOLESALE | mae | 1049.2372 | 959.05138 | -90.185771 | price | 8.5953657 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1830.8586 | 1714.1025 | -116.75607 | price | 6.3771212 | improved |
| 9002 | 배추/WHOLESALE | rmae | 1 | 0.91404634 | -0.085953657 | ratio | 8.5953657 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6275579 | 3.3518812 | -0.27567677 | %p | 7.5995139 | improved |
| 9011 | 무/RETAIL | mae | 96.027668 | 89.158103 | -6.8695652 | price | 7.1537353 | improved |
| 9011 | 무/RETAIL | rmse | 154.88288 | 140.8945 | -13.988381 | price | 9.0315859 | improved |
| 9011 | 무/RETAIL | rmae | 1 | 0.92846265 | -0.071537353 | ratio | 7.1537353 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 6.6073073 | 7.1107486 | 0.50344128 | %p | -7.6194622 | worsened |
| 9012 | 무/WHOLESALE | mae | 1355.7352 | 1409.9723 | 54.237154 | price | -4.0005714 | worsened |
| 9012 | 무/WHOLESALE | rmse | 2241.1094 | 2275.1552 | 34.045814 | price | -1.51915 | worsened |
| 9012 | 무/WHOLESALE | rmae | 1 | 1.0400057 | 0.040005714 | ratio | -4.0005714 | worsened |
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
| mape | 4.6062595 | 4.4912665 | -0.11499295 | %p | 2.4964496 | improved |
| mae | 565.55167 | 555.59925 | -9.9524181 | price | 1.7597717 | improved |
| rmse | 926.40586 | 916.80348 | -9.6023732 | price | 1.0365191 | improved |
| rmae | 1.0199316 | 0.99189299 | -0.028038576 | ratio | 2.7490644 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.729811 | 4.4368173 | -0.29299374 | %p | 6.1946184 | improved |
| 1 | 대파/RETAIL | mae | 137.83004 | 129.01186 | -8.8181818 | price | 6.3978664 | improved |
| 1 | 대파/RETAIL | rmse | 209.17894 | 192.05094 | -17.127998 | price | 8.1882039 | improved |
| 1 | 대파/RETAIL | rmae | 0.99682694 | 0.93305128 | -0.063775656 | ratio | 6.3978664 | improved |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7321563 | 5.7068277 | -0.025328626 | %p | 0.44186906 | improved |
| 2 | 대파/WHOLESALE | mae | 119.66403 | 119.02767 | -0.63636364 | price | 0.53179191 | improved |
| 2 | 대파/WHOLESALE | rmse | 178.73898 | 180.44333 | 1.7043433 | price | -0.95353752 | worsened |
| 2 | 대파/WHOLESALE | rmae | 1.0338057 | 1.028308 | -0.0054976951 | ratio | 0.53179191 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.6804386 | 2.740216 | 0.059777403 | %p | -2.2301352 | worsened |
| 7 | 양파/WHOLESALE | mae | 490.60474 | 494.12253 | 3.5177866 | price | -0.71703069 | worsened |
| 7 | 양파/WHOLESALE | rmse | 779.08186 | 792.80326 | 13.721406 | price | -1.7612278 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.94693999 | 0.95372984 | 0.0067898503 | ratio | -0.71703069 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.5910002 | 4.4088952 | -0.182105 | %p | 3.9665649 | improved |
| 8 | 양파/RETAIL | mae | 102.95618 | 98.501992 | -4.4541833 | price | 4.3262905 | improved |
| 8 | 양파/RETAIL | rmse | 165.03507 | 158.25039 | -6.7846739 | price | 4.1110499 | improved |
| 8 | 양파/RETAIL | rmae | 1.0230404 | 0.97878068 | -0.044259699 | ratio | 4.3262905 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0666711 | 1.0311302 | -0.035540912 | %p | 3.3319465 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1711.4688 | 1666.1205 | -45.348214 | price | 2.6496665 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2838.9402 | 2804.8795 | -34.060704 | price | 1.1997683 | improved |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2851793 | 1.2511264 | -0.034052967 | ratio | 2.6496665 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.5386936 | 3.4541526 | -0.084540951 | %p | 2.3890442 | improved |
| 10 | 깐마늘/RETAIL | mae | 378.0751 | 369.41502 | -8.6600791 | price | 2.2905711 | improved |
| 10 | 깐마늘/RETAIL | rmse | 565.37403 | 550.60557 | -14.768467 | price | 2.6121588 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0269037 | 1.0033818 | -0.02352196 | ratio | 2.2905711 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7784957 | 4.73088 | -0.047615729 | %p | 0.99645855 | improved |
| 9001 | 배추/RETAIL | mae | 225.22222 | 221.61111 | -3.6111111 | price | 1.6033547 | improved |
| 9001 | 배추/RETAIL | rmse | 373.33966 | 358.84957 | -14.490085 | price | 3.881207 | improved |
| 9001 | 배추/RETAIL | rmae | 0.90250767 | 0.88803727 | -0.014470399 | ratio | 1.6033547 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 8.078732 | 7.9411167 | -0.1376153 | %p | 1.703427 | improved |
| 9002 | 배추/WHOLESALE | mae | 964.14229 | 959.05138 | -5.0909091 | price | 0.52802466 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1703.9703 | 1714.1025 | 10.132277 | price | -0.5946276 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91889835 | 0.91404634 | -0.0048520099 | ratio | 0.52802466 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.6490033 | 3.3518812 | -0.29712211 | %p | 8.1425553 | improved |
| 9011 | 무/RETAIL | mae | 97.142292 | 89.158103 | -7.9841897 | price | 8.2190666 | improved |
| 9011 | 무/RETAIL | rmse | 155.16118 | 140.8945 | -14.266678 | price | 9.1947472 | improved |
| 9011 | 무/RETAIL | rmae | 1.0116073 | 0.92846265 | -0.08314468 | ratio | 8.2190666 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.2175931 | 7.1107486 | -0.10684452 | %p | 1.4803345 | improved |
| 9012 | 무/WHOLESALE | mae | 1428.4111 | 1409.9723 | -18.438735 | price | 1.2908564 | improved |
| 9012 | 무/WHOLESALE | rmse | 2295.2384 | 2275.1552 | -20.083152 | price | 0.87499198 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0536063 | 1.0400057 | -0.013600543 | ratio | 1.2908564 | improved |
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
| mape | 4.5011413 | 4.4912665 | -0.0098747735 | %p | 0.21938377 | improved |
| mae | 557.9753 | 555.59925 | -2.3760498 | price | 0.42583423 | improved |
| rmse | 915.84853 | 916.80348 | 0.95494935 | price | -0.10426935 | worsened |
| rmae | 0.99470404 | 0.99189299 | -0.0028110525 | ratio | 0.2826019 | improved |
| success_rate_pct | 99.239392 | 99.239392 | 0 | %p | 0 | same |
| valid_predictions | 2479 | 2479 | 0 | count | 0 | count_change |
| failed_predictions | 19 | 19 | 0 | count | 0 | count_change |

| 계열 | 품목/시장 | 지표 | 기준 | 신규 | 절대 차이 | 단위 | 상대 개선/변화 (%) | 판정 |
| --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 대파/RETAIL | mape | 4.4264277 | 4.4368173 | 0.010389523 | %p | -0.23471575 | worsened |
| 1 | 대파/RETAIL | mae | 128.74704 | 129.01186 | 0.26482213 | price | -0.20569183 | worsened |
| 1 | 대파/RETAIL | rmse | 191.58023 | 192.05094 | 0.47071521 | price | -0.24570135 | worsened |
| 1 | 대파/RETAIL | rmae | 0.93113601 | 0.93305128 | 0.0019152707 | ratio | -0.20569183 | worsened |
| 1 | 대파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 1 | 대파/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 1 | 대파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 2 | 대파/WHOLESALE | mape | 5.7329145 | 5.7068277 | -0.026086816 | %p | 0.45503584 | improved |
| 2 | 대파/WHOLESALE | mae | 119.51779 | 119.02767 | -0.49011858 | price | 0.41008003 | improved |
| 2 | 대파/WHOLESALE | rmse | 180.87209 | 180.44333 | -0.42875834 | price | 0.23705058 | improved |
| 2 | 대파/WHOLESALE | rmae | 1.0325423 | 1.028308 | -0.0042342496 | ratio | 0.41008003 | improved |
| 2 | 대파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 2 | 대파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 2 | 대파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 7 | 양파/WHOLESALE | mape | 2.7343152 | 2.740216 | 0.0059007785 | %p | -0.21580462 | worsened |
| 7 | 양파/WHOLESALE | mae | 493.7747 | 494.12253 | 0.34782609 | price | -0.070442265 | worsened |
| 7 | 양파/WHOLESALE | rmse | 788.25789 | 792.80326 | 4.5453737 | price | -0.57663536 | worsened |
| 7 | 양파/WHOLESALE | rmae | 0.95305848 | 0.95372984 | 0.00067135599 | ratio | -0.070442265 | worsened |
| 7 | 양파/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 7 | 양파/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 7 | 양파/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 8 | 양파/RETAIL | mape | 4.4251885 | 4.4088952 | -0.016293274 | %p | 0.36819389 | improved |
| 8 | 양파/RETAIL | mae | 98.860558 | 98.501992 | -0.35856574 | price | 0.36269848 | improved |
| 8 | 양파/RETAIL | rmse | 158.71298 | 158.25039 | -0.46258189 | price | 0.29145814 | improved |
| 8 | 양파/RETAIL | rmae | 0.98234363 | 0.97878068 | -0.0035629454 | ratio | 0.36269848 | improved |
| 8 | 양파/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 8 | 양파/RETAIL | valid_predictions | 251 | 251 | 0 | count | 0 | count_change |
| 8 | 양파/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9 | 깐마늘/WHOLESALE | mape | 1.0408994 | 1.0311302 | -0.0097691549 | %p | 0.93853018 | improved |
| 9 | 깐마늘/WHOLESALE | mae | 1681.6964 | 1666.1205 | -15.575893 | price | 0.92620122 | improved |
| 9 | 깐마늘/WHOLESALE | rmse | 2794.4083 | 2804.8795 | 10.471194 | price | -0.37471954 | worsened |
| 9 | 깐마늘/WHOLESALE | rmae | 1.2628227 | 1.2511264 | -0.011696279 | ratio | 0.92620122 | improved |
| 9 | 깐마늘/WHOLESALE | success_rate_pct | 91.517857 | 91.517857 | 0 | %p | 0 | same |
| 9 | 깐마늘/WHOLESALE | valid_predictions | 205 | 205 | 0 | count | 0 | count_change |
| 9 | 깐마늘/WHOLESALE | failed_predictions | 19 | 19 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | mape | 3.4576913 | 3.4541526 | -0.003538743 | %p | 0.1023441 | improved |
| 10 | 깐마늘/RETAIL | mae | 369.85375 | 369.41502 | -0.43873518 | price | 0.11862396 | improved |
| 10 | 깐마늘/RETAIL | rmse | 551.58736 | 550.60557 | -0.98179765 | price | 0.17799495 | improved |
| 10 | 깐마늘/RETAIL | rmae | 1.0045734 | 1.0033818 | -0.0011916648 | ratio | 0.11862396 | improved |
| 10 | 깐마늘/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 10 | 깐마늘/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 10 | 깐마늘/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9001 | 배추/RETAIL | mape | 4.7542722 | 4.73088 | -0.023392186 | %p | 0.49202453 | improved |
| 9001 | 배추/RETAIL | mae | 222.59921 | 221.61111 | -0.98809524 | price | 0.44388983 | improved |
| 9001 | 배추/RETAIL | rmse | 357.26432 | 358.84957 | 1.5852482 | price | -0.44371858 | worsened |
| 9001 | 배추/RETAIL | rmae | 0.89199676 | 0.88803727 | -0.0039594829 | ratio | 0.44388983 | improved |
| 9001 | 배추/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9001 | 배추/RETAIL | valid_predictions | 252 | 252 | 0 | count | 0 | count_change |
| 9001 | 배추/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9002 | 배추/WHOLESALE | mape | 7.9397931 | 7.9411167 | 0.0013236053 | %p | -0.016670526 | worsened |
| 9002 | 배추/WHOLESALE | mae | 959.84585 | 959.05138 | -0.7944664 | price | 0.082770208 | improved |
| 9002 | 배추/WHOLESALE | rmse | 1709.8839 | 1714.1025 | 4.2186351 | price | -0.24672056 | worsened |
| 9002 | 배추/WHOLESALE | rmae | 0.91480353 | 0.91404634 | -0.00075718478 | ratio | 0.082770208 | improved |
| 9002 | 배추/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9002 | 배추/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9002 | 배추/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9011 | 무/RETAIL | mape | 3.3570825 | 3.3518812 | -0.0052013035 | %p | 0.15493523 | improved |
| 9011 | 무/RETAIL | mae | 89.268775 | 89.158103 | -0.11067194 | price | 0.12397609 | improved |
| 9011 | 무/RETAIL | rmse | 141.13088 | 140.8945 | -0.236376 | price | 0.16748709 | improved |
| 9011 | 무/RETAIL | rmae | 0.92961515 | 0.92846265 | -0.0011525005 | ratio | 0.12397609 | improved |
| 9011 | 무/RETAIL | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9011 | 무/RETAIL | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9011 | 무/RETAIL | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |
| 9012 | 무/WHOLESALE | mape | 7.1428288 | 7.1107486 | -0.032080165 | %p | 0.4491241 | improved |
| 9012 | 무/WHOLESALE | mae | 1415.5889 | 1409.9723 | -5.6166008 | price | 0.39676778 | improved |
| 9012 | 무/WHOLESALE | rmse | 2284.7874 | 2275.1552 | -9.6321587 | price | 0.4215779 | improved |
| 9012 | 무/WHOLESALE | rmae | 1.0441486 | 1.0400057 | -0.0041428451 | ratio | 0.39676778 | improved |
| 9012 | 무/WHOLESALE | success_rate_pct | 100 | 100 | 0 | %p | 0 | same |
| 9012 | 무/WHOLESALE | valid_predictions | 253 | 253 | 0 | count | 0 | count_change |
| 9012 | 무/WHOLESALE | failed_predictions | 0 | 0 | 0 | count | N/A | count_change |

Series counts: {'improved': 7, 'worsened': 3, 'same': 0, 'unavailable': 0}/10

Point set differences and paired policy/common-success metrics: see comparison.json.

