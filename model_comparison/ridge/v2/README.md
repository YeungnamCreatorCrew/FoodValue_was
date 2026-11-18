# Ridge v2

`PooledRidgeV2`와 Ridge 전용 실행·감사·비교 시스템이다. 기존 p1/p2, 공통 v2, tools, 스냅샷 및 과거 실험을 수정하지 않는다.
이번 개발에서는 **실제 Tune/Validation 전체 학습 및 Test를 실행하지 않았다.** 실험 성능은 아직 없다.

## 모델과 공통 실행기

- 인터페이스: `fit(features, targets, horizons, feature_names, seed)` / `predict(features, horizons)`.
- 10계열 표본 통합, h=1..7별 Ridge 7개. 기본 alpha=10, solver=lsqr, seed=42.
- 공통 `run_pooled.Matrices`가 1,825일 창을 만들고 해당 ISO 주 첫 기준일에 재학습한다.
  `--series`는 평가 범위만 바꾸며 학습 계열은 항상 전체 10개다.
- 목표일 `o+h <= 재학습일`인 실제 관측 표본만 학습한다. 관측 400개/특징 lookback 28일 등 규칙은 공통 Matrices 그대로다.
- 공통 `models.relative()` 재사용: lag1/7/14/28, mean7/28, counter_price는 current로 나눈 뒤 1을 뺀다.
  volatility7은 current로만 나누고 current는 log로 바꾼다. 기타 특징은 그대로다.
- `y=target/current-1`, 복원 `current*(1+predicted_change)`. 모델별 horizon 열은 제거한다.
- 각 horizon의 TRAIN에서만 특징별 중앙값을 계산하고 NaN을 대체한다. TRAIN 전체 결측 열은 예측 시 관측되어도 0으로 고정한다.
  대체 후 TRAIN만으로 `StandardScaler`를 fit한다. 예측 데이터로 중앙값/평균/스케일을 갱신하지 않는다.
- 원본 배열을 복사해 변환한다. 행렬 차원, 특징명 중복·필수 열, horizon 정합, 무한대, 현재 가격/목표 가격의 유한 양수를 검사한다.
  TRAIN은 모든 7시점이 필요하다. 모델은 각 fit 시작에 이전 상태를 무효화하고 모든 시점 학습이 끝난 뒤에만 사용 가능하다.
- 예측한 가격이 비양수/비유한이면 해당 행은 NaN. 공통 실행기는 NaN→None→PREDICT_FAILED로 처리한다.
  구조/입력 오류는 예외, 전용 래퍼는 배치의 PREDICT_FAILED로 남긴다. 가격을 임의로 보정해 성공시키지 않는다.
- 공통 후처리(`prediction_rows`)가 raw 소수 6자리 → 0.5 올림 가격을 만든다. 평가는 `tools.evaluate` 그대로다.

설정의 클래스 경로는 `model_comparison.ridge.v2.model:PooledRidgeV2`다. 공통 실행기로 직접 동적 로딩할 수 있지만,
실험의 공식 진입점은 이 폴더의 `run.py`다. 공통 `run_pooled.run`은 예측을 끝에 일괄 저장하므로 중단 전 보존이 부족하다.
전용 래퍼는 공통 Matrices/로더/클래스 로딩/후처리/평가를 재사용하는 작은 실행 루프를 사용한다.
공통 코드의 파일이나 전역 함수를 바꾸지 않는다. 합성 데이터에서 두 실행기의 예측과 공식 metrics 일치를 테스트한다.

p2는 계열마다 별도 모델 하나에 여러 horizon을 넣고 원 가격을 학습했다. v2는 통합 계열의 7개 모델과 상대가격 목표를 쓴다.
따라서 p2→v2의 변화는 학습 구조·목표 변환 효과도 포함한다. 외부변수의 효과는 v2 CONTROL과 비교해야 한다.

## 데이터와 시간

| 자료 | 식별자 | manifest SHA-256 |
| --- | --- | --- |
| v1 가격·달력·기존 외부변수 | fv-snap-20261031-v1 | 3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0 |
| 추가 정제본 | fv-v2-extra-20261031-r2 | b23ca4844be2ad3167c2001dd69de276b7f9300aa81c5fc51f78c4d37c7b6acc |

Manifest 원문 해시와 모든 파일 해시/CSV 행 수, v1↔v2 연결, 공통 snapshot 검사를 실행 전에 검증한다.
원본 추가 스냅샷과 정제본을 수정/생성하는 기능은 없다. 정제본의 5개 빈 ton은 NaN이며 0톤과 구분한다.
자기 가격은 d까지, 상대시장/다른 품목/실측 날씨/반입량/환율은 d−1까지, 명절은 알려진 목표일 달력,
생산량은 공통 로더 공개일 규칙을 쓴다. 미래 실측 외부변수는 사용하지 않는다.
평가용 실제 목표 가격은 공통 평가기로만 결합하고 fit/preprocessing에는 전달하지 않는다.
전체 스냅샷은 Test 기간 자료도 포함하지만 **학습/평가 기준일은 Tune/Validation만 허용**하며
공통 `origins.guard('p2', days)`도 통과해야 한다. Test 및 gap 기준일은 설정/명령에 있어도 거부한다.

## 사전 실험 계획

모든 설정의 기본 모델/창/재학습/seed는 같다. 각 JSON의 `comparison`에 기준·추가·제외·고정 조건을 기록했다.

| 설정 | 기준 | 변경 |
| --- | --- | --- |
| control | 최초 기준 | 기본 15열 + SERIES_ID 6열. horizon 제거 후 모델 20열 |
| market / national_weather / event / macro / production | CONTROL | 해당 v1 묶음 하나 추가 |
| origin_weather / weather_anom / garak / cross_item | CONTROL | 해당 v2 묶음 하나 추가 |
| no_series_id | CONTROL | SERIES_ID만 제외. 통합 구조 유지 |
| all | CONTROL | 공통 XGBoost ALL과 같은 5 bundles + ORIGIN_WEATHER/GARAK/CROSS_ITEM/SERIES_ID |
| all_weather_anom | ALL | WEATHER_ANOM 26열 추가. 팀 공통 ALL과 구분 |
| no_market / no_national_weather / no_event / no_macro / no_production | ALL | 해당 묶음만 제외 |
| no_origin_weather / no_garak / no_cross_item / all_no_series_id | ALL | 해당 묶음만 제외 |

ALL은 입력 188열/모델 187열, 확장 ALL은 214/213열이다. CROSS_ITEM은 자기 품목 두 열을 NaN으로 두고
다섯 품목 슬롯 10열을 유지하는 공통 구현이다. 품목 원핫 5열+절편은 선형 종속이므로 계수의 개별 인과 해석은 피한다.
CONTROL→단독→ALL→사전 ablation 순으로 검토한다. 결과를 보고 추가 조합을 선택하면 새 설정과
`--changes`, `--reason`, `--next-decision`에 후보 전체·선택 지표·선택 이유를 남긴다. 자동 유리 조합 선택은 없다.
alpha/window/seed는 새 설정에서 검증된 값으로 바꿀 수 있지만 기본 JSON은 고정한다. 튜닝은 별도 승인 이후 진행한다.

## 실행과 안전장치

기본 명령은 검증·계획만 저장한다. `--execute`를 명시해야 학습한다. 이 개발 중에는 아래 실행 명령을 사용하지 않았다.

```powershell
# 읽기 검증 + 계획 기록 (학습 없음)
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --config model_comparison/ridge/v2/configs/control.json --origins tune

# 사용자 검토/승인 이후 Tune 실행 예시 — 지금 실행하지 말 것
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --execute --config model_comparison/ridge/v2/configs/control.json --origins tune --purpose "Initial CONTROL" --reason "Pre-registered baseline"

# 승인 이후 개별 실험; CONTROL 원본을 명시하여 자동 비교
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --execute --config model_comparison/ridge/v2/configs/garak.json --origins tune --baseline "CONTROL=model_comparison/ridge/v2/experiments/<control-id>"

# 재시도는 새 ID; 원인과 수정 내용을 필수로 기록
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --config model_comparison/ridge/v2/configs/control.json --retry-of <previous-id> --changes "Describe fix" --reason "Describe failure and retry reason"

# 기존 결과만 비교: 원본을 수정하지 않고 새 실행 폴더에 보고서 저장
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --compare-only model_comparison/ridge/v2/experiments/<run-id> --baseline "CONTROL=model_comparison/ridge/v2/experiments/<control-id>" --baseline "p1=experiments/ridge-p1-20261111-07" --baseline "p2_CONTROL=experiments/ridge-p2-20261112-01" --baseline "XGBoost=<folder>"
```

baseline은 LABEL=FOLDER를 반복한다. CONTROL/개별/ALL/ablation/다른 팀 결과를 동일 방식으로 읽는다.
**CONTROL 비교를 원하는 실행은 `--baseline CONTROL=...`을 명시해야 한다.** 없으면 N/A이며 임의 기준을 선택하지 않는다.
Naive는 해당 실행의 원본 공통 평가 대상 기준선으로 자동 연결한다. 기존 p1/p2 수치를 다른 데이터로 다시 계산해 덮지 않는다.
과거 최적 p2를 사용하면 후보 집합/선정 기준을 함께 남긴 `historical_baselines.json`을 참고한다. 과거 Validation 최적 선택은 선택 편향이 있다.

## 실행별 영구 기록

모든 호출은 날짜·마이크로초·UUID 실행 ID로 `experiments/<id>/`를 배타 생성한다. 같은 설정 재시도도 새 ID다.
CLI 파싱/설정 읽기/Manifest 검증/모델 import 전에 `invocation.json`, `STARTED`를 먼저 저장한다.
저장 경로/디스크/OS lock 확보 실패처럼 기록 자체가 불가능하면 stderr와 비정상 종료를 남기고 학습은 시작하지 않는다.
다른 실행과 집계 문서가 충돌하지 않도록 OS lock을 사용한다.

| 파일 | 내용 |
| --- | --- |
| invocation.json | 전체 argv, 인용된 실행 명령, cwd, UTC 시각, PID |
| environment.json / environment.txt | Python/실행 파일/OS/CPU/라이브러리 전체 버전/스레드 환경, commit/branch/작업 트리 |
| sources/ / sources_sha256.json | Ridge·공통 v2·tools·실험 설정·의존성 파일 사본 및 SHA (데이터·비밀정보 제외) |
| requested_config.json / provenance.json | 입력 설정, 양쪽 Manifest 원문/ID/해시, 평가 날짜·계열 목록/개수, 데이터 기간, 특징 목록/변경, 변환 규칙 |
| config.json | 공통 동적 로딩 설정 + 고유 실행/config ID + 전체 설정 해시 |
| predictions.csv | 공통 열/가격 후처리/상태. 각 기준일·계열 7행 저장 후 flush+fsync |
| metrics.json | 공통 평가기 원본(policy/model_only, MAPE, MAE/rMAE, baseline, bootstrap, horizon/시장/계절/작형, adoption) |
| metrics_full_precision.json | v2 반올림 전 보조 policy/model_only/Naive 지표, RMSE/전체 MAE/건수/성공률/계열별 지표 |
| prediction_health.json | 전체 출력 행 기준 성공률·예상 결측률·오류 행 수, 예외/시간 초과 이벤트 수; 공통 평가 지표와 별도 |
| events.jsonl / run.log | 시작·의도·변경/이유·재시도·단계·오류/traceback·FIT 진단·예측 상태·자원·종료 |
| importance.json | 마지막 유효 재학습의 horizon 평균 절댓값 표준화 계수 (gain이 아님) |
| comparison.json / RESULTS.md | 원본 해시와 비교 가능성, 전체/계열별 변화, 관측치 차집합과 대응 비교 |
| outcome.json / artifacts_sha256.json | 종료 상태·벽/CPU 시간·프로세스 최대 메모리, 모든 산출물의 SHA-256 |

FIT 진단은 각 horizon의 TRAIN 표본 수와 특징별 결측 개수·비율, 중앙값, 전체 결측 여부, 평균/scale/분산,
표준화 계수·절댓값·부호·상대특징 단위 계수/절편을 JSONL에 남긴다. 주별 큰 SVD/전체 상관행렬은 계산하지 않는다.
계수는 log/상대특징 공간의 조건부 연관성이며 공선성·원핫 중복 때문에 인과 효과나 tree gain처럼 해석할 수 없다.
메모리는 프로세스 누적 peak이며 학습 작업만의 독립 peak가 아니다. 전체 실행 시간과 fit 시간은 각각 구분한다.

종료 상태: PLANNED / COMPLETED / COMPLETED_WITH_MISSING / PARTIAL / FAILED / FAILED_PREFLIGHT / INTERRUPTED / ABANDONED / REPORTED / HELP.
예측 상태(OK/NO_INPUT/FIT_FAILED/PREDICT_FAILED/INVALID_VALUE/TIMEOUT)와 공통 평가는 바꾸지 않는다.
별도 건강도 분류는 success, expected_missing, fit_failure, predict_failure, timeout, abnormal_prediction이다.
학습 표본이 없거나 7개 horizon 중 표본이 없는 경우 기존 FIT_FAILED/NOT_FITTED 행을 유지하면서 expected_missing으로 분류한다.
NO_INPUT도 expected_missing이다. 실제 학습 예외는 fit_failure, 실제 예측 예외는 predict_failure,
재학습/예측 제한 시간 초과는 timeout, 비정상 값(INVALID_VALUE 및 모델의 NaN→PREDICT_FAILED/NONE)은 abnormal_prediction이다.
재학습 시간 초과의 기존 FIT_FAILED 상태도 유지하며 FIT_TIMEOUT 이벤트와 건강도 분류로 구별한다.
결측만 있으면 COMPLETED_WITH_MISSING이며, 모델 성공이 0건이어도 학습 성공을 뜻하지 않는다.
실제 오류가 있고 성공 행도 있으면 PARTIAL, 성공 행이 없으면 FAILED다. 전부 OK이면 COMPLETED다.

prediction_health.json의 prediction_success_rate와 missing_rate는 각각 성공 행 수/전체 출력 행 수,
예상 결측 행 수/전체 출력 행 수(0~1)다. error_row_count는 나머지 오류 행 수다.
error_event_counts/error_event_count는 포착한 학습·예측 예외와 시간 초과 이벤트 수다.
한 번의 재학습 실패가 여러 origin/계열/horizon 행에 영향을 줄 수 있으므로 이벤트 수와 오류 행 수는 다르다.
비정상 값은 오류 행 수로 센다. has_model_errors는 오류 행 또는 오류 이벤트가 하나라도 있는지 나타낸다.
공통 metrics.json의 success_rate는 기존대로 **평가 가능한 관측치**를 분모로 사용하며,
failed_predictions는 Naive 대체 대상 수여서 예상 결측도 포함한다. 실제 모델 오류 건수로 해석하지 않는다.
중단 전 배치별 상태·건강도 분류는 events.jsonl에 남으며, 루프가 끝나면 prediction_health.json을 작성한다.

CLI 종료 코드:

| 코드 | 의미 |
| --- | --- |
| 0 | PLANNED, COMPLETED, COMPLETED_WITH_MISSING, REPORTED, HELP. 실행 오류 없이 요청을 마침; 학습 성공이나 성능 입증을 뜻하지 않음 |
| 1 | PARTIAL, FAILED, FAILED_PREFLIGHT 등 오류 종료. 예상 결측만으로는 1을 반환하지 않음 |
| 2 | 잠금·실행 폴더 할당·감사 기록/봉인 등 기반 처리 실패. outcome/effective_outcome 확인 필요 |

KeyboardInterrupt는 INTERRUPTED를 기록·봉인한 뒤 다시 발생시킨다. 프로세스 종료 코드는 OS/Python 실행기에 따르므로
호출 함수의 반환값 1과 동일하게 보장하지 않는다. 강제 종료에는 즉시 종료 코드/감사 기록을 보장할 수 없다.
예외/OOM/사용자 중단은 원인과 단계, 당시 결과를 보존한다. 자동 재시도는 없다. retry-of·변경·이유가 재시도 이력이다.
SIGKILL/전원 차단은 즉시 원인 기록이 불가능하다. 다음 호출이 OS lock을 얻은 뒤 미봉인 이전 실행을 ABANDONED로 복구하고
당시 남은 파일을 봉인한다(정확한 중단 원인은 미상). 종료 레코드만 남고 봉인 전에 죽은 경우 원본 outcome.json을 보존하고
recovery.json에 recorded_status와 유효 상태 ABANDONED, normal_completion=false를 기록한다.
집계 시 audit.effective_outcome(folder)를 사용한다. 봉인이 없으면 INCOMPLETE, 복구 기록이 있으면 ABANDONED다.
원본 outcome.json의 COMPLETED/PLANNED 주장만으로 완료로 집계하지 않는다. 복구 후 봉인은 잔여 파일의 무결성만 보증한다.
comparison.load_result는 미봉인/복구/중단 실행을 비교 원본으로 거부한다. 현재 실행의 보고서 생성에만 내부 미봉인 읽기를 허용한다.
기존 정상 봉인 폴더는 복구 대상이 아니며 재봉인하지 않는다. 복구 중 다시 중단되어도 기존 recovery.json을 재사용한다.
완료된 실행의 원본 파일은 재사용/덮어쓰기하지 않는다. 문서는 누적 append하고, 원본 해시 검증으로 사후 변경을 감지한다.
이는 파일시스템 WORM 보장이 아니다. 장기 보존은 별도 백업/접근통제가 필요하다.

## 지표, 비교와 반올림

공통 평가 대상은 실제 목표 가격과 Naive가 모두 있는 점이다. 원 predictions 행 수와 다르다.
policy는 실패점을 Naive로 대체, model_only는 성공점만, common_success는 두 결과 모두 성공한 동일 관측치만 쓴다.
성공률(%)은 `OK 평가 대상 / 평가 대상 ×100`; valid_predictions는 성공 건수, failed_predictions는 나머지 평가 건수다.
평가 제외 행까지 포함한 상태 개수는 별도로 보존한다.

- MAPE = mean(abs(y-p)/y)*100. MAE = mean(abs(y-p)).
- RMSE = sqrt(mean((y-p)^2)). 공통에 없어 보조 지표로 추가한다.
- rMAE = 해당 평가 집합 모델 MAE / 같은 집합 Naive MAE. Naive MAE=0이면 null(N/A).
- 전체 MAPE/MAE/RMSE/rMAE는 유효 계열 지표의 단순평균(macro), metric_series_counts로 분모를 남긴다.
  MAE/RMSE는 품목·시장 가격 단위가 달라 전체 수치는 서술용이며 계열별 해석을 우선한다.
- 오차 절대 차이 = 신규−기준. MAPE는 **%p**, MAE/RMSE는 가격 단위, rMAE는 비율 차이다.
- 오차 상대 개선률(%) = (기준−신규)/기준*100. 양수 개선, 음수 악화, 0 동일. 기준 0/없음은 N/A.
- 성공률은 **%p 차이**와 `(신규−기준)/기준*100` 상대 변화율을 구분한다. 건수는 건수 차이다.
- v2 보조 지표는 공통 후처리를 마친 가격으로 계산한 반올림 전 float 값이며 변화 계산도 그 값을 사용한다.
  공통 metrics.json은 수정하지 않는다. 과거 p1/p2는 원본 소수 6자리 지표만 이용하며 없는 RMSE/전체 MAE는 N/A다.
  과거 소실된 반올림 전 수치를 추정하지 않는다. 원본 계열 MAE와 MAPE/rMAE, 원본 baseline을 그대로 읽는다.

직접 비교는 v1/v2 ID와 Manifest 해시, 데이터 기간, Tune/Validation 목록 이름·실제 기준일 목록,
계열·horizon, 평가 규칙·평가기 소스 해시, 평가 유효 관측치 집합 해시가 모두 같고 알려졌을 때만 허용한다.
알 수 없는 조건도 **참고(reference)**로 표시한다. 과거 p1/p2는 v2 추가 데이터/평가 소스 해시 증거가 부족하므로 보수적으로 참고다.
reference의 개선률 숫자와 improved/worsened는 기술적 수치 변화일 뿐 직접 개선 효과가 입증된 것이 아니다.
JSON의 effect_attribution=not_established와 보고서의 명시적 경고로 표시하며 계열 개선 건수로 집계하지 않는다.
policy 비교와 각 실행의 model_only 비교를 구분하고, model_only 성공 집합이 다를 수 있음을 표시한다.
동일 성공 관측치만 비교하려면 paired_analysis.common_success를 사용한다. 실제 예측 grid 또는 평가 유효 집합이 다르면 reference다.
학습 구조 차이는 README/config에 별도 설명하며 직접 비교 가능해도 변수만의 인과 기여를 보장하지 않는다.
예측 성공 집합은 기준일 집합과 구분한다. 원본 예측에서 실제 유효/성공 집합 차집합과 건수 차이를 기록한다.
가능하면 공통 v1 스냅샷으로 **별도 이름의 대응 분석**(common_eligible_policy / common_success)을 제공한다.
대응 분석은 과거 공식 성능을 대체하거나 다시 계산한 것으로 보고하지 않는다. 참고 비교 지위도 그대로 유지한다.

RESULTS는 전체 성능 한 행과 각 비교의 **모든 계열 × 모든 주요 지표** 기준/신규/절대차/상대개선·변화/판정 표를 만든다.
10계열 각각 품목/시장, 성공률 차이, 유효 예측 수 차이를 포함한다. 개선/악화/동일/비교불가 집계는 MAPE 기준이며
참고 비교는 직접 비교 가능한 계열 수로 세지 않는다. JSON에 전체/대응 분석과 원본 파일 해시를 모두 보존한다.

## 검증

```powershell
.venv\Scripts\python.exe -B -m pytest model_comparison/ridge/v2/tests -p no:cacheprovider -q
```

테스트는 작은 합성 행렬, 합성 스냅샷, 임시 디렉터리만 사용한다. 기존 p1/p2 실제 학습을 호출하지 않는다.
기존 p2 회귀 테스트는 실제 스냅샷 fit 테스트 1건을 제외하고 실행했다. 개발 전 결과 및 최종 결과는 WORK_REPORT.md에 기록한다.
