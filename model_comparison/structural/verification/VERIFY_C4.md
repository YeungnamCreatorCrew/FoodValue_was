# VERIFY_C4 — 최종 설정(t18_retail_t01)과 compare.py 독립 검증

검증자: verifier 서브에이전트. 구현 코드·설정 수정 없음, tuning_log.csv 행 추가 없음(19줄 = 헤더+18행, 시작·종료 동일). **struct 모델을 검증 기준일로 돌리지 않았다.** 검증 구간 수치는 기존 모델(experiments/*)의 predictions와 naive만 계산했다. 재계산 코드는 scratchpad `.../scratchpad/verify/`(`c4_t18.py`, `c4_cmp.py`). 사용량을 아끼라는 요청에 따라 무거운 재실행은 하지 않았고, 기존 모델 예측 읽기와 tune 53기준일 채점만 했다.

## 해시(검증 종료 시점)
model.py `e7fb20f6…`(C3와 동일), run.py `9768c57f…`, score.py `39bbaa35…`, test_leakage.py `85c604fb…`(모두 C3와 동일), test_run.py `8d5c2201…`(C3의 `7fedbad4…`에서 바뀜: mtime 22:01:48, 골든 테스트 대상에 t18 추가), config.json `cbd419c9…`, compare.py `9a2c09dd…`. model/run/score가 같으므로 C1·C3의 코드 판정은 그대로 유효하다.

## 항목별 판정

### 1. t18 tune 재채점 — PASS
독립 채점기(`c4_t18.py`)로 `runs/struct/t18_retail_t01/predictions.csv`(3,710행, 기준일 53개 = 튜닝 목록 전부, OK 3,654 / NO_INPUT 56)를 계산:

| 값 | 구현 주장 | 내 계산 |
|---|---|---|
| 전체 macro MAPE | 4.470077 | 4.470077(tuning_log 마지막 행 4.470077, OK) |
| 소매 5계열 macro | 4.062811 | 4.062811 |
| t13 소매 macro | 4.117355 | 4.117355 |
| t18 vs t13 소매 개선 | 1.325% | 1.3247% |
| 부트스트랩 Δ 95% | [0.0403, 0.2563] | [0.040341, 0.256275](구현 metrics.json과 6자리 일치) |

- §14 판정: 소매 항만 다른 변경이므로 소매 macro로 본다. 1.3247% ≥ 1% → (a)에 따라 최종 = t18. 맞음.
- 추가 확인: t18의 도매 5계열 OK 1,799행 예측 = naive와 정확히 같음(불일치 0). t18의 소매 macro는 t01과 정확히 같다(4.062811, 소수 6자리까지 동일). 소매 예측이 도매 설정과 무관하게 독립이라는 뜻이며 일관적이다.
- t18 전체: 전체 macro 4.470077, naive 대비 +2.974%, rMAE 0.9700, 계열 승 5(소매 5, 도매는 naive와 같아 승 0).

### 2. config 고정 — PASS
`config.json` sha256 `cbd419c9ed7105bc7fa97f6da562adbd37daa1099f72f2554e4614fd8d227e16`. 내용이 `configs/t18_retail_t01.json`과 JSON으로 동일. t01 대비 params 차이는 `wholesale_terms: ['season','event'] → []` 한 가지뿐이고 비-params 항목 차이 없음. t13 대비 차이는 소매 항 복원(`retail_terms`에 ratio, `season_years` 1→3, `season_weights` [1.0]→[0.5,0.3,0.2])으로, 이는 §14가 정한 "소매 항을 t01로 되돌림" 한 변경이다.

### 3. compare.py 정확성 — PASS
독립 재계산(기존 모델 예측 + naive, 검증 구간 전체 244 기준일 × 10계열):
- naive 검증 macro(모델 없이 `Snapshot.naive`와 `actual_price`로 직접): 11,275점, **4.912547**(구현·metrics.json 4.912547과 일치).
- lgbm-p1-20261111-01: 4.768783, naive 대비 +2.926%, rMAE 0.9736, 승 5, 11,275점 — 구현 주장·metrics.json과 일치. 소매 4.5152(3/5), 도매 5.0223(2/5). 독립 부트스트랩 CI [0.010233, 0.301019]도 metrics.json과 일치.
- lgbm-p2-20261111-01: 4.692928, +4.471%, rMAE 0.9629, 승 8, 소매 4.3422(5/5), 도매 5.0436(3/5) — metrics.json과 일치.
- xgb-p1-20261110-01 4.855297(+1.165%), ridge-p2-20261112-02 4.940629(−0.572%)도 metrics.json과 일치. 네 실험이 같은 평가 점 집합(11,275점).
- compare.py를 `lgbm-p2-20261111-01`을 대상 모델로 넣어(출력은 scratchpad) 실행: 표의 LightGBM p1 행 4.769, +2.93%, 소매 4.515(3/5), 도매 5.022(2/5), LightGBM p2 4.693, XGBoost p1 4.855, Ridge p2 4.941 등이 위 독립 값과 같고, "metrics.json과 일치" 표시도 일치. 앙상블 v2 행 4.595(+6.47%)는 PRD가 적은 참고 수치와 같음. 비교 대상 9개가 같은 점 집합, 성공률 99.20%.
- 코드 확인(compare.py): policy는 실패 점을 naive로 대체(`policy_fn` :117), 평가 점은 `tools.evaluate.points_for`(목표일 실제가·naive가 있는 점, :166), 모델 점 ∩ 모든 비교 대상 점으로 같은 점 집합에서 다시 채점(:188-193), 소매·도매는 사전 등록 계열 목록(:34-35)으로 나눠 같은 policy로 계산하고 시장 구분이 목록과 다르면 중단(`check_markets` :125-130), smoke·month 제한·시험 구간 폴더는 거부(:70-80), 비교 대상은 검증 전체·10계열 자격 확인(:83-96). 부트스트랩·macro는 공통 도구(tools.evaluate)를 재사용하며, 위 독립 재계산이 같은 값을 냈다.
- 주의(편향): 비교 대표 중 XGBoost p2(`xgb-p2-20261111-06`)와 Ridge p2(`ridge-p2-20261112-02`)는 "검증 policy macro MAPE 최저"로 골랐다. 검증 성능으로 비교 대상을 고르면 비교 대상에 유리한 쪽으로 편향되며, compare.py도 이를 표에 명시한다. 앙상블 v2는 입력(v2 특징)이 달라 "참고"로만 표시된다. 구현의 compare.py가 `experiments_v2`의 앙상블 예측 한 개를 읽지만 입력으로 쓰지 않고 사후 비교에만 쓴다.

### 4. struct 검증 예측 흔적 — PASS
- `runs/struct` 21개 항목: smoke 2(smoke-v0, smoke-v0b, DO_NOT_USE.txt 있음), tune_trial 18(t01~t18), tuning_log.csv. validation_full·val*·final* 폴더 0개. 모든 config.json의 kind는 tune_trial 18 + smoke 2.
- compare.py는 struct 폴더를 인자로 받을 뿐 내부에서 struct 예측을 읽거나 만들지 않는다(`COMPARATORS`는 모두 experiments/·experiments_v2/). 도구 자체 점검 예시는 기존 실험을 모델로 넣는 것이다.
- `final_params_t18_20250602.json`이 생겼다(2025-06-02 재학습 기준일의 계열별 fit 파라미터 덤프). 키는 계수·k_h·λ·평소 배수·`fit_info`뿐이고 예측·MAPE는 없다. `val_loss_naive`는 fit 내부의 학습 표본 마지막 20% 선택 손실이며 검증 구간 성능 보고가 아니다. 다만 그 날짜는 검증 구간 안이라 `dump_params`가 검증 구간 날짜를 허용하는 점은 기록해 둔다(미확인: 이 파일이 어디에 쓰이는지).

### 5. 테스트·tools·tuning_log — PASS
- `pytest model_comparison/structural` → **91 passed**(test_compare.py 9개 포함). 골든 테스트는 t01·t04·t18의 저장된 tune 예측과 재실행 비교(C3에서 변이 시험으로 실효성 확인, 이번에는 t18 추가만 확인).
- `git diff --stat tools/` 출력 없음.
- tuning_log.csv 19줄(헤더+18행), t18 마지막 행.

## 의견·주의(판정과 별개)
1. 최종 설정의 정직한 요약: 소매는 t01(배수·3년 계절 포함), 도매는 naive. tune 기준 전체 macro 4.470(naive 대비 +2.97%), 소매 +6.3%, 도매 0. 계열 승은 최대 5이므로 G3(6 이상)는 설계상 통과할 수 없고, 도매 이득이 0이라 전체 +5%(G1)도 소매가 약 10% 개선하지 않으면 어렵다. 부트스트랩 하한 0.040은 C3 시점의 t13(0.014)보다 낫지만 여전히 작다. §14가 정한 대로 "도매는 설계상 naive"로 그대로 보고하는 것이 맞다.
2. 결국 C2 소급 단순화(t04, t11)는 t18 한 번으로 되돌려져 소매는 t01이 최선이었다. 이는 §14 보정(영향 범위 기준)이 의도한 결과이며, tune 53개 목록 위에서의 차이(t10 4.464 ~ t18 4.470)는 잡음 범위다.
3. 검증 1회 전에 확정된 것: 설정(config.json = t18), 비교 대상 9개와 그 선택 규칙, 소매 전용 지표의 사전 등록. 검증을 본 뒤에는 바꾸지 않아야 한다.

## 종합 판정: **C4 PASS**
t18의 수치·§14 판정, config 고정, compare.py의 독립 재계산 일치, struct 검증 예측 흔적 없음, 테스트 91개·tools 무변경·tuning_log 18행 모두 확인됐다. 구현 측이 고칠 필수 사항은 없다.
