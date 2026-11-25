# VERIFY_C5 — 검증 1회 결과(val-t18)와 C5_REPORT.md 독립 검증

검증자: verifier 서브에이전트. 구현 코드·설정·보고서 수정 없음. struct 모델은 다시 실행하지 않았고(`runs/struct/val-t18/predictions.csv`만 읽음), tuning_log.csv에 행을 추가하지 않았다. 재계산 코드: scratchpad `.../scratchpad/verify/c5.py`, `c5b.py`, `indep_score.py`(구현의 score.py·run.py·compare.py 미사용, tools.loader.Snapshot만 사용). 지시에 따라 `runs/struct/val-t18`은 이번에 처음 열람했다.

## 1. 독립 재계산 — PASS
`predictions.csv` 17,080행(244기준일 × 10계열 × 7시점), 기준일 집합 = `origins_validation` 244개와 정확히 같음, 목표일 최댓값 2025-11-07(시험 구간 2025-11-10 이전), 상태 OK 16,793 / NO_INPUT 287.

| 값 | 구현 주장 | 내 계산 |
|---|---|---|
| 평가 점 | 11,275 | 11,275 |
| 전체 macro MAPE / naive | 4.764773 / 4.912547 | 4.764773 / 4.912547 |
| naive 대비 | +3.01% | +3.0081% |
| rMAE / 계열 승 / 성공률 | 0.9706 / 5 / 99.20% | 0.9706 / 5 / 0.99202 |
| 부트스트랩 Δ 95% | [0.068, 0.245] | [0.068173, 0.244964] (metrics.json과 6자리 일치) |
| 소매 5계열 macro / naive | 4.383 / 4.678(+6.32%), 5/5 승 | 4.382798 / 4.678346(+6.317%), 5/5 승 |
| 소매 부트스트랩 | [0.136, 0.490] | [0.136346, 0.489928] |
| 도매 5계열 | naive와 같음 | macro 5.146747 = naive 5.146747, OK 8,253행이 `Snapshot.naive`와 전부 일치(불일치 0) |

계열별(소매): 1 +8.06%, 8 +3.69%, 10 +2.17%, 9001 +8.58%, 9011 +8.15%. 도매 5계열은 모두 0%. 비OK 287행은 모두 계열 9(깐마늘 도매) 2025-07~08의 NO_INPUT. metrics.json의 `c546e599…`는 파일 해시로 일치 확인(`shasum`). 추가로 보고서 5절의 계절별·시점별 macro(봄 5.587, 여름 5.264, 가을 4.670, 겨울 3.438, h=1 2.118 … h=7 6.918)와 naive 값, mean7 macro 7.055를 독립 계산으로 확인했고 모두 일치.

## 2. 실행 1회·설정 — PASS
- `runs/struct`의 config.json kind 분포: validation_full **1개**(`val-t18`), tune_trial 18, smoke 2. `val-t18/run.log`는 실행 머리글 1개, 계열 10줄, metrics SHA-256 한 번, 총 7.5s — 재실행 흔적 없음.
- `val-t18/config.json`: kind=validation_full, origins=validation, month 없음, series 10개, origin_count 244, `config_id` = `75eb4346`, params가 현재 `model_comparison/structural/config.json`(sha256 `cbd419c9…`, t18)의 params와 같음.

## 3. 기록·도구·코드 불변 — PASS
- `tuning_log.csv` 19줄(헤더+18행) 그대로. `git diff --stat tools/` 출력 없음.
- 해시를 C4 기록과 비교: model.py `e7fb20f6…`, run.py `9768c57f…`, score.py `39bbaa35…`, test_leakage.py `85c604fb…`, test_run.py `8d5c2201…`, compare.py `9a2c09dd…`, config.json `cbd419c9…` — **모두 C4 때와 동일**. compare.py·test_compare.py는 mtime이 08:10대로 바뀌어 있으나(검증 실행 08:16 이전) compare.py 해시는 C4와 같다. 검증 결과를 본 뒤 바뀐 코드·설정은 없다(수정 시각 모두 val-t18 생성 시각 08:16 이전).
- 테스트 91개 통과(재실행 확인). test_leakage.py는 55개.

## 4. 비교표 — PASS
`val-t18/compare.md`의 같은 평가 점 11,275개(점 집합 동일 "예")에서, C4에서 내가 독립 계산한 값과 같음: LightGBM p1 4.769(+2.93%, 소매 4.515 3/5, 도매 5.022 2/5), LightGBM p2 4.693(+4.47%, 8/10), XGBoost p1 4.855, Ridge p2 4.941(−0.57%). 앙상블 v2 4.595도 PRD 기재와 같음. naive 4.912547은 모델 없이 직접 계산한 값과 같음.

## 5. C5_REPORT.md 수치·서술 — PASS (경미한 표현 주의 3건)
- 핵심 수치(채점표 G1~G5, 전체·소매·도매, 계열별, 계절·시점, 비교표)는 모두 위 독립 계산·metrics.json과 일치. G1 미달(+3.01% < 5%), G2 통과, G3 미달(도매 설계상 naive라 최대 5/10), G4 통과, G5 통과 판정이 숫자와 맞다. "검증 관문은 통과하지 못했다"는 결론, "튜닝 +2.97% → 검증 +3.01%", "소매 +6.32%는 사전 등록 보조 지표이며 주 판정을 대체하지 않는다"는 서술은 과장 없이 정직하다. 한계 절(튜닝 목록 겹침, 기준서 단계 밖 실행, G3 구조적 도달 불가, §14는 사후 규칙, LLM 블라인드와 가설 중복, 도매 미모델링)도 사실과 맞고 숨긴 것이 없다. "R1 … 검증을 다시 돌려 비교하지는 않았다"도 정직한 표기다.
- 표현 주의(수치 오류는 아님, 수정을 권고):
  1. 6절 해석에서 "Ridge p1·p2, AutoARIMA p1·p2보다는 낮다"고 썼지만 AutoARIMA p1(4.855)·p2(4.851)와의 차이는 각각 1.9%·1.8%라 같은 문서가 정한 상대 2% 미만 동률 기준으로는 동률 범위다. "낮다"보다 "숫자상 낮지만 동률 범위"가 맞다(Ridge p1 −6%, p2 −3.7%는 구분됨).
  2. "소매에서는 … p2·앙상블(4.26~4.34)보다는 조금 높다"에서 p2 중 Ridge p2(4.499)와 AutoARIMA p2(4.547)는 struct 소매(4.383)보다 높다. LightGBM p2·XGBoost p2·앙상블에만 해당한다고 좁혀야 한다.
  3. "도매에서 … LightGBM p1·p2, XGBoost, 앙상블(4.93~5.09)보다 높다": XGBoost p1은 5.102라 범위가 4.93~5.10. 사소함.
- 비교 편향: XGBoost p2·Ridge p2 대표를 검증 macro 최저로 골랐다는 편향 명시, 앙상블은 입력 조건이 달라 참고용이라는 명시가 보고서에 있다(적절).

## 종합 판정: **C5 PASS**
검증 1회 결과가 독립 재계산과 일치하고, 실행은 정확히 1회(config_id `75eb4346` = t18), 결과를 본 뒤 코드·설정 변경 없음, tools 무변경, tuning_log 18행, 테스트 91개 통과. 보고서는 "naive는 이기지만(+3.01%) 기준서 G1(+5%)·G3(과반 승)은 못 넘었다"고 있는 그대로 적었다. 구현 측이 고칠 필수 사항은 없고, 위 표현 주의 1~2는 보고서 배포 전에 고치길 권한다.

이것으로 C1~C5 검증이 끝났다.
