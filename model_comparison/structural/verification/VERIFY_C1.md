# VERIFY_C1 — W1(모델 코드·누수 테스트 + 자체 실행기·채점) 독립 검증

검증자: verifier 서브에이전트(독립 재계산). 구현 코드는 수정하지 않았고, 튜닝 기록(`tuning_log.csv`)에는 행을 추가하지 않았다.
검증 구간(origins_validation) 기준일로 모델을 돌려 성능을 본 적 없음. 재계산 스크립트는 scratchpad `.../scratchpad/verify/`에 있다(`adv_leak.py`, `adv_season.py`, `indep_score.py`, `c1_score.py`, 변이 시험 `mut/`).

## 검토 대상 파일 해시(검토 시작 시점 = 종료 시점, 동일)

```
9318a74ad71f815b3036c7c0796590ff7954087c8ced8b6b52fe1ac7a7ce1d82  model.py        (mtime 20:03:15)
9768c57f4daad75c51499dd0b06d00c956f3df0e439595aae603b9e54d1e1571  run.py          (mtime 19:57:41)
39bbaa35a265001786081f66dba4cc1b0ce8233085cfff93f8a662ea19e0d891  score.py        (mtime 19:57:41)
96e5a8f5ac991efc7abda507294dd147a9b1048e23f14f6d70b2be74e8265404  test_leakage.py (mtime 19:55:51)
60a58389b40fb130e61a618a426ae0c91580936f6946d8eef8c2209d4a4afb70  test_run.py     (mtime 19:58:03)
3c6e285b9c637f2fa5d185c08c77b97941ec462f3ec3da17f16573a6bfc4f871  dump_params.py
d138305181160583a3ddd761a767f16054b12df0fe656a7e85387a29ac7e4359  config.json
```

- 검토 끝에 같은 파일로 해시를 다시 계산했고 시작 시점과 완전히 같다(`diff` 무변경).
- model.py는 20:03:04~20:03:15에 retail_k_grid 패치본으로 바뀌었다가 되돌려졌다고 통보받았다. 내가 model.py 전체를 읽은 것은 19:54:11 판(파일 크기 32,497바이트, 611줄)이었고 그 안에 retail_k_grid는 없었다. 그 읽은 내용을 보관해 둔 사본과 현재 model.py를 `diff`로 비교했을 때 차이가 0이고 크기도 같다(되돌려진 뒤 내용 = 검토 시점 내용). 현재 `grep -c retail_k_grid model.py` = 0건.
- 검토 중 코드 변경이 run.py/score.py에도 있었다는 통보(줄인 실행 정확도 차단)는 19:57:41에 반영되어 있었고, 이후 해시가 바뀌지 않았다. 즉 아래 6(d) 판정은 이 최종본 기준이다.
- 테스트: 71개 통과(`pytest model_comparison/structural`, 시작·종료 시점 모두).

## 항목별 판정

### 1. 누수 없음(L1) — PASS
코드 검토(file:line, 검토본 model.py)
- 계절 항 `season_analog`(model.py:182-217): 시작점 b=o−364k, 끝점 b+h, `end + window <= o`인 위치만 읽음(:203). h≤7, window 3이라 구조적으로 o 이전에만 닿는다(안전 장치가 이중).
- fit의 격자는 `until_ord=as_of_ord`(:475), predict의 격자는 `until_ord=origin_ord`(:573)로 잘림. fit 표본별 계절 항은 위치로 o 이전만 읽음.
- 평소 배수 `_usual_ratio`(:407-417): 넘어온 학습 표본의 마지막 기준일 기준 최근 N일만. 열 크기 `_scale`, λ·k 선택 `_select`(:513-552)는 학습 표본의 기준일 순 마지막 20%(`cut = uniq[int(len*0.8)]`)로 고르고, 선택용 fit 표본은 `origin_ord + horizons < cut`로 정답 날짜까지 거른다(:516).
- 명절 마스크(:383-405, :117-148): fit 표본의 (목표일→target_in_event_window) 대응만 사용. 명절은 사전 확정 달력 값이라 시점 규칙상 허용된다.
- 파일·DB를 여는 코드 없음. model.py import는 math, dataclasses, numpy, scipy.linalg뿐.

적대적 실험(내가 새로 작성, `adv_leak.py`) — 튜닝 기준일만 사용
- Snapshot의 원 관측을 복원해 d 이후(또는 w=재학습 기준일 이후) 가격을 난수(×0.4~2.5)로 바꾸거나 지운 사본으로 `_build_series`를 다시 만들어 같은 fit·predict를 반복. 자기 계열과 상대 시장 둘 다 바꿈.
- 변형 4가지(v0 / season_event_mask=True / season_kind_tol=5 / change28+momentum) × 계열 6(1, 2, 8, 7, 9001, 9002) × 재학습 기준일 4(튜닝 목록 6, 15, 28, 41번째) × d 2개(w, w+2일) × 3가지 시험(재학습일 이후 변조→fit 계수·k_h·λ·평소배수 동일 / d 이후 변조→예측 동일 / d 이후 삭제→예측 동일) = **576회 검사, 불일치 0**.
- 양성 대조(시험이 실제로 변화를 감지하는지): 상대 시장의 d−1 이전 마지막 관측을 ×1.3 → 예측이 바뀜(True), 상대 시장의 d 이후 전부 ×1.3 → 예측 불변(MARKET이 d−1까지만 쓰임을 확인), 자기 계열 d 가격 ×1.3 → 예측 바뀜. 계열 1·9001·10, 기준일 2개에서 모두 기대대로.
- 표본 내부 누수 시험(`adv_season.py`): fit이 내부에서 계산한 표본별 계절 항을 가로채 PRD §10 정의대로 "그 표본 기준일 o 이하 관측만"으로 독립 구현한 값과 비교. 5계열 × 3재학습일 × 300표본 중 비교 가능한 4,439개에서 **불일치 0**. 학습 창 시작 경계(b가 창의 첫 관측일보다 3일 안쪽 앞)의 61개는 모델이 그 해를 버려 값이 다르다. 미래를 쓰는 방향이 아니라 보수적인 쪽이므로 누수 아님(주의사항 참고).
- 구현 측 테스트가 헛테스트인지 변이 시험(변형된 model.py 사본으로 test_leakage.py 실행):
  - 실제 누수 주입(계절 간격 364→5일 + 가드 제거, m5) → 7개 실패(`test_b_fit_season_equals_truncated_computation` 포함)로 잡음. 간격만 5일(m4) → 5개 실패.
  - 선택 구간 정답 거르기 제거(m6) → `test_c_selection_uses_only_last_fraction...` 실패.
  - until_ord 잘라내기 제거(m1, m2), 가드 `end+window<=o` 제거(m3)는 테스트 47개 모두 통과. 이는 364일 간격 때문에 미래 가격에 구조적으로 닿을 수 없는 동등 변이(누수가 아님)라서 테스트 약점이 아니다.
  - 약점 하나: test_leakage.py는 합성 자료만 쓴다. 실제 스냅샷 대상 시험은 위 내 시험이 보완했다.

### 2. 허용 라이브러리 — PASS
model.py의 import는 `math`, `dataclasses`, `numpy`, `scipy.linalg`만. xgboost·lightgbm·sklearn·statsforecast·optuna·pandas·torch 문자열 0건(grep). 구현 쪽 test_e 두 개도 있음. run.py·score.py는 tools(공통)만 읽기 전용 사용.

### 3. 공통 도구 무변경 — PASS
`git diff --stat tools/` 출력 없음. `git status --short`에 tools 관련 항목 없음(untracked는 .ouroboros, experiments_v2, llm_blind, structural, v2/direction.py뿐). 검증 종료 시점에도 동일.

### 4. 채점 정확성 — PASS
- 독립 채점기(`indep_score.py`, tools.loader.Snapshot의 actual_price·naive만 사용): 평가 점 = 목표일 실제가 있고 naive가 있는 점, 실패 점은 naive로 대체, 계열별 MAPE의 단순 평균, 계열 승, macro rMAE.
- smoke-v0(검증 구간 2025-01, 계열 1·2·9001, 이미 있는 결과 파일을 읽음): 나 macro 3.712484, naive 3.304057, 개선 −12.3614%, rMAE 1.1311, 계열 승 0, 점 228, 성공률 1.0 ↔ 구현 3.712484, 3.304058, −12.361356, 1.131131, 0, 228, 1.0. 계열별 MAPE 3개도 소수 6자리 일치. smoke-v0b도 같은 값. (naive 마지막 자리 0.000001 차이는 구현이 6자리 반올림해 저장하기 때문)
- naive를 모델 없이 튜닝 목록에서 직접 계산: 10계열, 2,498점, macro **4.60709**(구현·PRD 값 4.6071와 일치).
- 부트스트랩: score.py는 `tools.evaluate.bootstrap`(공통 도구)을 재사용한다. 코드 확인 결과 기준일 월 블록 재표집, 1,000회, `default_rng(0)`, Δ=naive−model, 2.5·97.5 백분위로 기준서 §8.3과 일치. 독립 재구현(표본 월을 뽑아 점을 실제로 모아 다시 계산)으로 t01 CI = [0.033079, 0.258906], 구현 metrics.json의 [0.033079, 0.258906]과 6자리까지 같음.
- 참고: score.py 자체는 tools.evaluate에 위임하므로, 독립성은 내 재계산이 담당했다.

### 5. 재현성(R1) — PASS
t01 설정으로 튜닝 기준일 53개 × 계열 1·2·9001·9002(1,484행)를 두 번 실행(출력은 scratchpad `out/r1a`, `r1b`). `run` 열(실행 이름)만 빼고 전체 바이트 동일, `predicted_price_raw` 소수 6자리까지 동일. 또 저장된 `runs/struct/t01_v0/predictions.csv`의 같은 1,484행과도 raw·상태 모두 차이 0.

### 6. 예산·엿보기 차단 — PASS (우회 가능 경로는 주의)
시험은 모두 scratchpad `--out`에서 실행(실제 runs/struct/tuning_log.csv는 11줄=헤더+10행 그대로).
- (a) 가짜 로그 40행을 둔 폴더에서 튜닝 시도 → `튜닝 시도가 이미 40회` 거부, 로그·결과 폴더 추가 없음 (run.py:89-93).
- (b) kind=validation_full인 config가 있는 폴더에서 `--origins validation` → `검증 전체 실행은 1회뿐` 거부 (run.py:103-113). 스냅샷 읽기 전에 거부.
- (c) `--origins test`는 argparse가 거부(choices는 tune·validation만). `check_origins`는 2025-10-31 이후(2025-11-05, 11-10 시험)를 RunError로 거부, 2024-10-31도 거부 (run.py:69-78).
- (d) `--series`/`--month`로 줄인 실행(최종본 run.py:320-323, 25-26줄 설명): 위 R1 실행 출력은 `상태 집계 {"OK": 1484} (정확도 지표는 계산하지 않음)`뿐, 결과 폴더에는 config·predictions·run.log·status_summary.json만 있고 metrics.json 없음. `score.py <smoke 폴더>`는 `줄인 실행(smoke)은 채점하지 않음`으로 거부(score.py:79-80). `--origins validation --series 1`(month 없이)과 tune 전체인데 `--record-trial` 없는 경우는 실제 실행으로 거부 확인, smoke에 `--record-trial`을 붙이는 경우는 코드(run.py:121)와 테스트(test_run.py:84)로 확인. 테스트도 있음(test_run.py:169, 180, 195). 현재 테스트 71개 통과.

주의(코드로 막을 수 없는 것)
- `--out`을 다른 폴더로 주면 40회 한도와 검증 1회 기록이 모두 새로 시작된다(기록이 `--out` 안에만 있음). 결과 폴더를 지우면 검증 1회 기록도 사라진다. 절차로 막아야 함.
- 검증 구간에 대해 `--month`로 12번 줄인 실행을 하면 predictions.csv가 남고, 그것은 외부 코드로 채점할 수 있다. run.py는 자기 지표만 막는다.
- runs/struct/smoke-v0, smoke-v0b에는 차단 코드가 들어오기 전에 만든 metrics.json(2025-01 검증 구간 3계열의 정확도)이 남아 있다. PRD §5 3단계가 이 smoke를 허용했고 한 달·3계열 한정이지만 "검증 구간 성능을 본 것"에 해당한다는 점을 기록해 둔다(모델이 그 구간에서 naive보다 나빴다 = 모델 선택에 쓰지 않는 것이 맞음).

### 7. PRD 적합성 — PASS (차이 목록 있음)
일치: 소매 항 = 전달 + 배수 되돌림 + 계절 + 명절 지시변수 2개(momentum 없음), 도매 = 계절 + 명절만, 목표 = log(y/current)·예측 current×exp(k_h·ŷ), 시점 묶음 회귀 1개(절편·시점별 항 없음), k_h 시점별 7개, λ 후보 {0,0.1,1,10,100}, k 후보 {0,.25,.5,.75,1}, 계절 k=1~3 가중 0.5/0.3/0.2·±3일·없는 해 제외 후 재정규화·전부 없으면 0, 평소 배수 = 최근 91일 중앙값(NaN이면 항을 0), 학습 창 1,825일(로더 상한), 예측 NaN·무한이면 None, 무작위 요소 없음, config.json의 모델 필드값(`strategy`, `target_transform`, `feature_set`, `extra_features`) PRD와 같음.
PRD와 다른 점(모두 합리적이지만 보고서에 적어 둘 것):
1. 전달 항이 `counter_change7` 그대로가 아니라 `log1p(counter_change7)`(model.py:334). PRD §10 문구는 counter_change7.
2. 열별 RMS로 나눈 뒤 L2(절편·중심화 없음), λ 동률은 센 수축 우선(:274). PRD는 "특징 표준화 후"라고만 함.
3. 예측 로그 변화율을 [−1, 1]로 자름(`y_clip=1.0`, :586), 선택 표본이 부족하면 λ=1·k=1 대체(:518-522), 학습 표본 100개 미만이면 fit 예외 — PRD에 없는 보조 장치.
4. 자기·상대 NaN 항은 0으로 두고 개수를 기록함(PRD 요구와 일치).
5. predict는 current가 유효하지 않으면 None이 아니라 예외(PREDICT_FAILED로 기록됨).
6. 학습 창 시작 경계에서 계절 비교 연도 하나를 버리는 경우가 있음(보수적, 누수 아님).

## 추가로 확인한 것
- 상태 코드/후처리: 반올림은 0.5 올림·최소 1(run.py:153-174), run_backtest와 같은 규칙이라고 주석에 명시. 재학습은 ISO 주 첫 기준일(run.py:183), 공통 로더(`training_data`, `origin_inputs`)로만 입력. (구현 코드를 읽어 확인, 별도 재구현 없음)
- 재학습은 로더가 `목표일 ≤ as_of` 표본만 주므로(tools/loader.py:270-303) 학습 표본 정답 누수 없음.

## 종합 판정: **C1 PASS**

구현 측이 고쳐야 할 것(필수 없음, 권고)
1. 보고서에 위 "PRD와 다른 점" 1~3을 기록(특히 log1p 전달 항).
2. 우회 가능 경로(`--out` 변경, 폴더 삭제, 검증 구간 smoke 반복)는 코드 대신 절차로 금지한다고 못 박기. 가능하면 예산 기록을 `--out`과 무관한 고정 경로에도 병행 기록.
3. smoke-v0, smoke-v0b의 오래된 metrics.json은 삭제하거나 "참고 금지"로 표시(검증 구간 정확도 포함).
4. 누수 테스트에 실제 스냅샷 기반 시험 1개(상대 시장 d−1, 미래 변조)를 추가하면 더 단단해짐.
