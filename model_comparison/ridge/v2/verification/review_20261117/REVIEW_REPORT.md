# Ridge v2 보완 검토 결과 — 2026-11-17

브랜치는 시작과 종료 모두 `feat/ridge-v2`다. 기존 작업 트리를 초기화하거나 기존 미추적 파일을 삭제하지 않았다.
Git commit, push, PR 생성, merge를 수행하지 않았다. 기존 설계를 유지하고 아래 5개 기존 파일과 신규 테스트 1개만 보완했다.

## 변경 파일

| 파일 | 보완 내용 |
| --- | --- |
| [run.py](../../run.py) | 기존 상태/후처리를 유지하고 별도 건강도 분류 및 prediction_health.json 추가. 예상 학습 표본 부족과 실제 fit/predict 예외 구분. 시간 초과·비정상 값 별도 집계. 결측만 있으면 COMPLETED_WITH_MISSING/코드 0. 봉인 실패 후 중복 종료 기록 방지 |
| [comparison.py](../../comparison.py) | direct/reference 유지. reference 수치의 직접 개선 효과 미입증을 JSON과 보고서에 명시. 실제 grid 차이도 reference. model_only 비교를 policy 및 동일 성공 집합 대응 비교와 구분. 미봉인/복구/중단 결과의 비교 원본 사용 거부. 비유한 비교값은 N/A |
| [audit.py](../../audit.py) | outcome 존재·봉인 부재를 INCOMPLETE로 판정. recovery.json에 이전 주장과 유효 ABANDONED 상태를 구분. 원 outcome 보존. 복구 재중단 시 재개 가능. 중복 finish는 기록 변경 전 거부 |
| [model.py](../../model.py) | fit 시작/실패 시 models, fitted_, diagnostics_, names, keep를 초기화. 실패한 재학습에서 이전 진단/계수 노출 차단. 성공 시 계수·결측 감사 기록 유지 |
| [README.md](../../README.md) | 건강도 분류·분모·오류 행/이벤트 차이, 종료 코드, effective_outcome 사용, reference 해석 문서화 |
| [test_review_regressions.py](../../tests/test_review_regressions.py) | 신규 회귀 사례 27개. 합성 입력과 임시 감사 레지스트리 사용 |

이번 검증 자료는 이 새 디렉터리에만 추가했다. 기존 WORK_REPORT.md, RESULTS.md, EXPERIMENT_LOG.md 및 과거 verification 자료는 수정하지 않았다.

## 예측 집계와 종료 코드

기존 예측 상태 및 tools.evaluate의 평가 대상·Naive 대체·성공률 규칙은 유지했다.
학습 표본이 없거나 일부 horizon의 표본이 없으면 기존 FIT_FAILED/NOT_FITTED 행을 유지하되 expected_missing으로 분류한다.
NO_INPUT도 expected_missing이다. 실제 fit/predict 예외, 시간 초과, 비정상 값은 오류로 분리한다.

prediction_health.json의 성공률과 결측률은 **전체 출력 행**을 분모로 하며 값의 범위는 0~1이다.
공통 metrics.json의 success_rate는 **평가 가능한 관측치**가 분모다. 두 분모를 혼동하지 않도록 문서화했다.
error_row_count와 예외/시간 초과 error_event_count를 구분한다. 하나의 재학습 실패는 여러 예측 행에 영향을 줄 수 있다.
기존 failed_predictions/failed_rows는 Naive 대체 대상 또는 비OK 행 수여서 예상 결측도 포함하며, 실제 모델 오류 건수가 아니다.

- 코드 0: PLANNED / COMPLETED / COMPLETED_WITH_MISSING / REPORTED / HELP.
- 코드 1: PARTIAL / FAILED / FAILED_PREFLIGHT 등 오류 종료.
- 코드 2: 잠금·할당·감사 기록/봉인 기반 처리 실패.
- KeyboardInterrupt: INTERRUPTED 기록 후 재발생. 프로세스 종료 코드는 OS/Python 실행기에 따른다.

COMPLETED_WITH_MISSING은 모델 성공이 0건이어도 가능하다. 이는 요청 처리가 예상 결측만으로 종료되었다는 뜻이며 모델 학습 성공이나 성능 입증을 뜻하지 않는다.

## 비교 검증

전체 및 10개 계열별 MAPE·MAE·RMSE·rMAE 계산과 macro 집계를 유지했다.

- 절대 차이는 `신규 - 기준`. MAPE 차이는 %p이며, 음수는 오차 감소다.
- 오차 상대 개선률은 `(기준 - 신규) / 기준 * 100`, 단위 %. 양수 개선, 음수 악화다.
- 기준 0이면 상대 개선률은 null. 기준/신규 결측 또는 비유한 값이면 변화는 N/A다.
- Naive MAE가 0이면 rMAE는 null이다.
- 실제 grid와 평가 유효 관측치 집합 차이는 reference로 분류하며 차집합을 기록한다. 대응 truth/Naive 값 불일치는 오류다.
- policy는 Naive 대체 포함, model_only는 각 실행의 모델 성공점만, paired_analysis.common_success는 양쪽 모두 성공한 동일 관측치만 사용한다.
- reference 개선률 숫자는 유지하되 `effect_attribution=not_established`와 보고서 경고로 직접 개선 효과 미입증을 명시한다. 개선 계열 수로 집계하지 않는다.

과거 공식 지표를 재계산하거나 덮어쓰지 않았다. 실제 신규 성능 개선 여부를 측정한 작업은 아니다.

## 실패·중단·복구 및 Windows 잠금

outcome.json이 COMPLETED를 주장해도 봉인이 없으면 effective_outcome은 INCOMPLETE다.
복구 후에는 원본 outcome.json을 보존하고 recovery.json이 원 주장은 미확정이며 유효 상태는 ABANDONED임을 설명한다.
복구 봉인은 잔여 파일의 무결성만 뜻하며 정상 실험 완료를 뜻하지 않는다. 해당 폴더는 비교 원본으로 거부한다.
정상 봉인 폴더는 recover_incomplete의 대상에서 제외하며, 중복 finish도 쓰기 전에 거부한다.

회귀 테스트에서 다음을 확인했다.

- 고정 시각·UUID를 강제한 실제 ID 충돌 시 기존 폴더의 모든 파일 보존.
- exclusive 생성으로 파일 덮어쓰기 차단.
- Windows msvcrt 잠금의 별도 프로세스 간 충돌 거부 및 강제 종료 후 재획득.
- 봉인 쓰기 실패 시 코드 2, 종료 레코드 중복/변경 방지.
- 종료 레코드만 있는 상태와 복구 도중 재중단된 상태의 재개·유효 상태·봉인 검증.
- 이전 모델 재사용 방지, fit 검증 단계 및 중간 horizon 실패 후 이전 진단/계수 제거.
- 기존 중단/예외 테스트에서 flush된 예측과 감사 문맥 보존.

## 테스트 결과와 기존 오류 구분

| 검사 | 결과 |
| --- | --- |
| 수정 전 기준선 | 141 passed, 23 warnings, 95.58초 |
| Ridge v2 보완 후 | 80 passed, 경고 없음, 37.97초 |
| 최종 호환성 검사 | 167 passed, 1 deselected, 경고 없음, 128.49초 |

신규 회귀 사례는 27개이며 신규 실패는 0건이다. 최종 수는 `기준선 141 - 제외 1 + 신규 27 = 167`이다.
기준선의 경고 23개는 공통 테스트 subprocess 출력의 기존 Windows cp949 디코딩 문제다.
최종 검증은 `-X utf8`로 실행했다. 공통 코드를 수정해 이 문제를 해결했다고 주장하지 않는다.

최종 명령:

```powershell
.venv/Scripts/python.exe -X utf8 -B -m pytest model_comparison/ridge/v2/tests tests/test_ridge_p2.py tests/test_v2.py tests/test_standard_tools.py tests/test_backtest_tools.py tests/test_snapshot_tools.py -k 'not real_p1_snapshot_single_origin_prediction_parity' -q -p no:cacheprovider --basetemp model_comparison/ridge/v2/verification/review_20261117/final_tmp
```

로그: [기준선](baseline_tests.txt), [Ridge v2](regression_tests.txt), [최종 검사](final_tests.txt).

### 실행 범위 이탈 기록

초기 기준선 실행에서 기존 `test_real_p1_snapshot_single_origin_prediction_parity`를 제외하지 못했다.
이 테스트는 실제 스냅샷의 2025-01-06, 계열 1과 9001에 대해 p1/p2를 각각 fit한다(총 4회).
사용자의 실제 학습 금지 요청을 완전히 지키지 못한 부분이다. 사용자에게 작업 중 알렸으며, 이후 검증에서는 제외했다.
공식 Tune/Validation/Test 실험·백테스트나 새로운 공식 실험 폴더는 생성하지 않았고, 기존 산출물도 변경하지 않았다.

## 이전 결과 불변성

수정 전 기존 파일 948개의 SHA-256을 확보했다. Git 추적 파일과 model_comparison, experiments, data/snapshots,
tools, tests, runs 아래 기존 파일을 포함하며 __pycache__ 등 실행 캐시는 제외했다.
최종 검사에서 허용한 기존 소스/문서 5개만 변경되었고 나머지 **943개는 동일**하다.
원래 파일 누락 0개, 허용하지 않은 변경 0개다. 기존 영역에 새로 생긴 소스 파일은 회귀 테스트 1개뿐이다.
Git 추적 파일 전체 diff는 비어 있다(이번 v2 소스는 원래 미추적 상태였다).

보존된 PLANNED 실행:

| 실행 ID | 봉인 파일 수 | 결과 |
| --- | ---: | --- |
| ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e | 58 | PLANNED 유지, 해시 및 봉인 일치 |
| ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1 | 59 | PLANNED 유지, 해시 및 봉인 일치 |

v1/v2 스냅샷의 고정 manifest 해시, 데이터 파일 해시·행 수 및 공통 snapshot 검사를 읽기 전용으로 통과했다.
p1/p2 코드·과거 실험·기존 검증 자료·팀 공통 코드의 내용은 모두 보존되었다.

근거: [수정 전 해시](before_sha256.json), [초기 상태](initial_state.json),
[1차 불변성 검사](preservation_after.json), [최종 불변성·소스 해시·범위 검사](preservation_final.json).

## 남은 위험 요소

- 시간 초과는 기존처럼 함수 반환 후 경과 시간을 판정한다. 실행 중인 학습/예측을 즉시 강제 중단하지 않는다.
- 외부 집계기는 새 COMPLETED_WITH_MISSING 상태와 effective_outcome 규칙을 적용해야 한다. 원본 outcome.json만 읽으면 복구 전 완료 주장을 오독할 수 있다.
- 파일 봉인은 SHA-256 기반 감사이며 WORM 저장이나 전원 차단 시 원자적 디렉터리 커밋을 보장하지 않는다. 잘린 JSON/봉인은 읽기·검증 오류로 중단되며 자동으로 정상 완료로 승격하지 않는다.
- 기존 공통 subprocess의 cp949 문제는 남아 있다. 이번 검증 환경에서는 UTF-8 모드로 회피했다.
- 실제 Ridge v2 학습과 실제 성능은 이번 보완에서 검증하지 않았다. 초기 기준선의 p1/p2 단일 시점 실제 fit 이탈은 위에 별도 기록했다.
