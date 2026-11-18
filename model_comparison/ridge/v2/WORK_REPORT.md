# Ridge v2 구현 완료 보고

작업 브랜치: `feat/ridge-v2`, HEAD: `3b03596557574a703db4085be894b8a3c2e70512`.
실제 Tune/Validation/Test 학습, 기존 p1/p2 재실행, commit/push/PR/merge를 하지 않았다.
실제 데이터로 수행한 작업은 **학습 없는 사전 검증 2회(PLANNED)**뿐이다.

## 1. 파일 범위

기존 파일 수정 0개. 신규 작업물은 전부 `model_comparison/ridge/v2/` 안에 있다.

- 모델: `__init__.py`, `model.py`.
- 실행/감사/비교: `run.py`, `audit.py`, `comparison.py`.
- 설정: `configs/`의 JSON 22개 (아래 목록).
- 테스트: `tests/__init__.py`, `tests/test_model.py`, `tests/test_audit_comparison.py`, `tests/test_integration.py`.
- 문서/원본 연결: `README.md`, `EXPERIMENT_LOG.md`, `RESULTS.md`, `historical_baselines.json`, `WORK_REPORT.md`.
- `experiments/README.md`, 실행 lock 및 PLANNED 폴더 2개: 각 명령·환경·소스 사본·데이터 조건·이벤트·봉인 해시.
- `verification/`: 개발 전/중/후 테스트 원문, 실패 기록, 보호 파일 해시 대조, Git 상태와 실제 파일 목록.

정확한 전체 파일 경로는 [verification/new_files.txt](verification/new_files.txt), 실제 Git 출력은
[verification/git_status_after.txt](verification/git_status_after.txt)에 있다. 소스 사본도 신규 폴더 안에만 저장했다.

## 2. 모델 학습 방식

공통 인터페이스를 준수한다. Ridge(alpha=10, solver=lsqr), seed=42, TRAIN StandardScaler,
1,825일 창, 주 첫 기준일 재학습이다. 10계열 표본을 합쳐 horizon 1..7별 모델 7개를 만든다.
공통 `relative()` 그대로 가격 수준 특징을 현재 가격 대비 비율(변동성은 비율, current는 log)로 바꾸고,
목표는 `target/current-1`, 복원은 `current*(1+prediction)`이다. 입력 배열은 복사한다.

## 3. p2와의 차이

p2는 계열마다 원 가격 목표를 학습하는 모델 하나에 여러 horizon을 넣었다. v2는 10계열을 합치고 7개 horizon 모델과
변화율 목표를 사용한다. p2→v2 변화에는 학습 구조·목표 변환 효과가 포함되므로 변수 효과는 v2 CONTROL과 분리해 해석한다.
공통 코드를 바꾸지 않고 Matrices, feature generator, load_class, prediction_rows, evaluate를 재사용했다.
중단 전 파일 보존을 위해 실행 루프는 Ridge 래퍼에 있으며 공통 `run_pooled.run` 출력과 합성 데이터로 일치 검증했다.

## 4. 설정

CONTROL은 기본 15열+SERIES_ID 6열(모델은 horizon 제거 후 20열)이다.
5개 기존 외부변수와 ORIGIN_WEATHER/WEATHER_ANOM/GARAK/CROSS_ITEM을 각각 CONTROL에 하나씩 추가한다.
`no_series_id`는 CONTROL에서 ID만 뺀다. `all`은 공통 XGBoost all.json과 bundles/blocks가 정확히 같다(188열).
`all_weather_anom`은 WEATHER_ANOM을 더한 214열 확장판이다. ALL의 각 묶음 제거 설정 9개를 제공한다.
각 JSON의 comparison에 기준/추가/제외/고정 조건이 있다. v2 성능을 보고 고른 조합은 아직 없다.

설정 파일: `all.json`, `all_no_series_id.json`, `all_weather_anom.json`, `control.json`, `cross_item.json`, `event.json`, `garak.json`, `macro.json`, `market.json`, `national_weather.json`, `no_cross_item.json`, `no_event.json`, `no_garak.json`, `no_macro.json`, `no_market.json`, `no_national_weather.json`, `no_origin_weather.json`, `no_production.json`, `no_series_id.json`, `origin_weather.json`, `production.json`, `weather_anom.json`.

## 5. 결측값·누출 방지

각 horizon TRAIN의 특징별 중앙값과 평균/scale만 사용한다. TRAIN 전체 결측 열은 0으로 고정하고 예측 시에도 유지한다.
현재 가격/목표값은 양수·유한값이 필수이며 대체하지 않는다. 무한대, 차원/순서/필수 특징/horizon 불일치를 거부한다.
fit 시작에 이전 모델을 무효화하고 7개 전체 성공 후 사용 가능하다. 미래 목표가 재학습일을 넘는 표본을 공통 Matrices가 제외한다.
외부 실측값은 d−1까지, 자기 가격은 d까지, 알려진 달력/생산량 공개일 규칙은 공통 특징 코드를 그대로 따른다.

## 6. 저장과 감사

UTC 마이크로초+UUID의 새 실행 ID를 배타 생성한다. 시작/명령/환경은 설정 파싱·Manifest 확인·모델 import 전에 남긴다.
commit/branch/작업 트리, Python/라이브러리/OS, 소스 사본과 해시, v1/v2 Manifest 원문/ID/SHA,
날짜·계열 목록/개수, 특징과 변경, 매 재학습 표본 수를 저장한다.
매 horizon의 결측 수·비율/중앙값/전체 결측/mean/scale/계수·절댓값·부호/절편을 JSONL로 보존하며 SVD는 계산하지 않는다.
predictions는 기준일·계열 7행마다 flush+fsync한다. 공통 metrics와 추가 full-precision 지표를 별도로 보존한다.
벽 시간/CPU 시간/프로세스 peak RSS를 기록하며 마지막에 모든 산출물 SHA-256을 봉인한다.

## 7. 개선·악화와 비교 가능성

오차 절대차=신규−기준, 상대 개선률=(기준−신규)/기준×100이며 양수 개선/음수 악화다.
MAPE 차이는 %p, MAE/RMSE는 가격 단위, rMAE는 비율 차이. 기준 0/없음은 N/A다.
성공률의 %p 차이와 상대 변화율을 구분하고 건수는 건수 차이로 남긴다. v2는 반올림 전 보조 지표로 계산한다.
과거 결과는 원본 metrics의 저장 정밀도를 유지하고 없는 수치를 추정하지 않는다. 알려진 과거 원본 해시가 바뀌면 비교를 거부한다.
양쪽 snapshot ID/SHA, 데이터 기간, Tune/Validation 목록·날짜·계열·horizon, 평가 규칙/소스/유효 집합이
모두 알려지고 같아야 direct다. 다르거나 모르면 reference다. 과거 p1/p2는 보수적으로 reference 처리한다.

## 8. 전체/계열별 표

공통 policy/model_only MAPE·MAE/rMAE·micro MAPE·bootstrap·세부 분해·adoption은 metrics 원문으로 보존한다.
보조 JSON은 macro MAPE/MAE/RMSE/rMAE, 성공/실패 건수와 성공률, 각 계열 전체 지표를 제공한다.
RESULTS 생성기는 전체 요약과 모든 계열×모든 주요 지표의 기준/신규/차이/개선·변화/판정 표를 생성한다.
품목·시장, 예측 성공률 변화, 유효 건수 차이를 포함한다. MAPE 개선/악화/동일/불가 개수를 분모와 함께 집계한다.
원 예측 집합 차집합과 common_eligible_policy/common_success 대응 분석도 별도로 보존한다.
대응 분석으로 과거 공식 지표를 교체하거나 reference를 direct로 승격하지 않는다.

## 9. 실패·중단·재시도

FAILED_PREFLIGHT/FAILED/PARTIAL/INTERRUPTED를 기록하고 오류 시각·단계·traceback·영향 origin/계열을 남긴다.
재시도는 새 폴더에 retry-of/수정/이유를 명시하며 기존 실패 폴더를 재사용하지 않는다.
강제 종료는 다음 호출이 OS lock을 얻은 뒤 미봉인 기록을 ABANDONED로 복구한다(정확한 원인은 미상).
경로/디스크/lock 자체 실패로 기록할 수 없으면 stderr와 비정상 종료로 남기고 학습은 시작하지 않는다.

## 10. 테스트 결과

| 검사 | 결과 | 근거 |
| --- | --- | --- |
| 개발 전 기존 p2 합성 회귀 | 38 passed, 1 deselected | verification/baseline_tests.txt |
| 최초 신규 테스트 | 48 passed, 2 failed | verification/v2_tests.txt |
| UTF-8 수정 후 신규 테스트 | 50 passed | verification/v2_tests2.txt |
| 신규+기존 p2+공통 v2 통합 회귀 | 99 passed, 1 deselected | verification/combined_tests.txt |
| 최종 신규 테스트 (원본 pin/보고 포함) | 53 passed | verification/v2_verified_tests.txt |
| 실제 스냅샷 사전 검증 | PLANNED 2회, fit 없음 | verification/preflight_summary.json |
| 보호 파일 해시 대조 | 574개 동일, 누락/추가 0 | verification/preservation_after.json |

최초 실패 2건은 새 테스트가 Windows CP949로 UTF-8 진단 로그를 읽은 문제였다. 읽기 인코딩을 명시해 수정했다.
알려진 `Official p1 artifact changed: README.md` 8건은 개발 전 현재 상태에서 재현되지 않았다.
README의 실제 SHA와 p1 reference가 일치한다. 관련 테스트/p2 코드/reference/README는 로컬 dev와 동일하다.
dev 브랜치로 전환하거나 dev 전체 테스트를 별도로 실행한 것은 아니다.
제외한 1건은 기존 `test_real_p1_snapshot_single_origin_prediction_parity`로, 실제 p1/p2 fit을 피하기 위한 것이다.
실제 Tune/Validation 모델 학습이나 기존 실험 재실행을 테스트로 수행하지 않았다.

## 11. 기존 자료 불변성

기존 Ridge 소스·설정·실험, 팀 v2/tools/tests, 전체 기존 experiments와 v1/원본·정제 스냅샷 등 574개 파일의 바이트 SHA가 같다.
보호 범위에 새 파일도 없다. Git의 기존 추적되지 않은 파일 목록도 v2 경로를 제외하면 시작과 같다.
tracked diff는 비어 있다. 기존 파일을 삭제/덮어쓰거나 p1 README를 고치지 않았다.

## 12. 남은 점과 주의사항

- v2 실제 성능은 미측정이며 모두 N/A다. 실제 실험 실행은 사용자 검토/별도 승인 이후다.
- CONTROL 비교는 --baseline CONTROL=...을 명시해야 한다. 임의의 유리한 기준을 자동 선택하지 않는다.
- 과거에 저장되지 않은 RMSE/반올림 전 지표는 N/A다. 기존 Validation 최적 선택은 선택 편향을 명시한 참고 자료다.
- MAE/RMSE macro는 가격 단위가 다른 계열의 서술용 집계다. 계열별 결과를 함께 읽어야 한다.
- 계수는 log/상대특징의 조건부 연관성이며 공선성/원핫 중복 때문에 인과 효과로 해석할 수 없다.
- timeout은 공통 도구 방식처럼 작업 반환 후 초과 판정한다. 강제 선점 실행기가 아니다.
- SHA 봉인은 사후 변경 검출이며 파일시스템 WORM 보장은 아니다. 강제 종료의 정확한 원인은 복구 시 알 수 없다.
- git status에서 기존 .pytest_cache 접근 권한 경고가 있었으나 검증/봉인은 성공했다. 기존 캐시 권한을 변경하지 않았다.

## 13. 향후 Tune 명령 (제시만 함)

```powershell
.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --execute --config model_comparison/ridge/v2/configs/control.json --origins tune --purpose "Initial CONTROL" --reason "Pre-registered baseline"

.venv\Scripts\python.exe -B -m model_comparison.ridge.v2.run --execute --config model_comparison/ridge/v2/configs/all.json --origins tune --baseline "CONTROL=model_comparison/ridge/v2/experiments/<control-run-id>" --purpose "Team ALL" --changes "Add the pre-registered ALL bundles" --reason "Compare under matching evaluation conditions"
```

## 14. Git 및 실행 기록

브랜치 유지, commit/push/PR/merge 미실행. 기존 변경 없음, 신규 경로 `model_comparison/ridge/v2/`만 추가했다.
전체 실제 변경 파일 목록/Git 전후 상태는 verification에 있다. 이번 PLANNED ID:

- `ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e` (53 Tune 기준일, 10 학습/평가 계열, 학습 없음)
- `ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1` (53 Tune 기준일, 10 학습/평가 계열, 학습 없음)
