# Ridge v1 1차 비교(p1) 공식 Validation 제출

모델 구현 PR: [#35](https://github.com/YeungnamCreatorCrew/FoodValue_was/pull/35).

공식 실행 ID: `ridge-p1-20261111-07`; config ID: `bfc463b0`.

**Ridge v1은 공식 채택 기준에 미달했다.** Alpha=10은 튜닝 목록에서 사전 선택했고 공식 Validation 결과를 보고 변경하지 않았다. 이번 제출 준비에서는 기존 실험을 재실행하지 않았으며 최종 Test 및 추가 튜닝도 수행하지 않았다.

## 공식 결과

| 항목 | 원본 metrics.json 값 |
|---|---:|
| policy Macro MAPE | 5.060471% |
| Naive Macro MAPE | 4.912547% |
| Naive 대비 상대 개선율 | -3.011147% |
| Macro rMAE | 1.026703 |
| 평가 대상 성공률 | 99.2018% |
| Naive보다 우수한 계열 | 2/10 |
| 평가 대상 점 | 11275 |
| 전체 예측 행 | 17080 |
| 부트스트랩 Δ 95% 구간 | [-0.346481, 0.070119]%p |

검증 범위는 2024-11-01~2025-10-31의 244개 기준일 × 10개 계열 × 7 horizons다. Δ는 Naive−Ridge Macro MAPE로, 양수일 때 Ridge가 우수하다.

| 관문 | 기준 | 판정 |
|---:|---|---|
| 1 | Naive 대비 상대 개선율 ≥ 5% | 미통과 |
| 2 | Macro rMAE < 1 | 미통과 |
| 3 | 10개 중 6개 이상 계열에서 Ridge 우위 | 미통과 |
| 4 | 평가 대상 성공률 ≥ 99% | 통과 |
| 5 | 부트스트랩 Δ 95% 구간 하한 > 0 | 미통과 |

**검증 관문: 1X 2X 3X 4O 5X.** 형식 검사 통과와 모델 채택 기준 통과는 다른 판정이다.

## 결측 및 성공률 경고

- `OK=16793`, `NO_INPUT=287`. NO_INPUT은 깐마늘 도매의 41개 기준일에서 발생했다.
- 스냅샷의 원천 장기 결측(2025-06-25~2025-07-31)으로 최신 관측이 오래되거나 특징 창에 공백이 남았다. 상세 원인은 run.log와 predictions.csv에 보존했다.
- policy는 예측 실패 점을 Naive로 대체하며, 평가 정답이 없는 날은 공통 평가에서 제외한다.
- 전체 예측 행 성공률은 약 98.32%, 평가 대상 성공률은 99.2018%다. 공통 검사기는 전체 행 기준으로 성공률 경고를 출력하지만 관문 4의 공식 판정은 metrics.success_rate와 metrics.adoption을 따른다.
- 공통 도구나 경고 문구를 수정하지 않았다.

## 설정과 튜닝 이력

- Alpha=10, solver=lsqr, StandardScaler, feature_set=base_v1(15개), target_transform=raw_price, seed=42.
- 전략은 direct_pooled: 계열별 회귀에서 7개 horizon 학습 표본을 함께 사용한다. 10개 계열을 합친 단일 모델은 아니다.
- 공통 로더의 최근 최대 1825일 이동 창과 주별 첫 기준일 재학습을 유지했다.
- 튜닝 6/40회, tuning_log.csv 누적 83.5초. config.json의 seconds_used=84는 공통 실행기의 반올림값이다.

| Trial | Alpha | tune policy Macro MAPE % |
|---:|---:|---:|
| 01 | 1.0 | 4.789801 |
| 02 | 0.1 | 4.797184 |
| 03 | 0.01 | 4.798315 |
| 04 | 10 | 4.785119 |
| 05 | 100 | 5.039178 |
| 06 | 1000 | 5.483619 |

## 원본 보존 및 제출 경로

- 로컬 원본: `runs/ridge-p1-20261111-07/`.
- 저장소 제출본: `experiments/ridge-p1-20261111-07/`(현재 폴더).
- 필수 6개 파일과 model_source.py, invocation.json을 바이트 그대로 복사했다. 아래 해시는 원본과 제출본 모두에 적용된다.
- README.md만 이번 제출 준비에서 신규 작성했다. 기존 실행 결과·분석 문서·튜닝 CSV는 변경하지 않았다.

| 파일 | SHA-256 (원본 = 제출본) |
|---|---|
| `config.json` | `6a9b547da766ec0750f801e3a327ec459a792b314d5b52e1465843bd4c06219e` |
| `predictions.csv` | `1e72a16dcea61989a376b32fb8c5d3854b9f6319f2ffe8c0c9ebdea41427199b` |
| `metrics.json` | `9c3e399dc7dc882b1e1e051e7ddf4a608a928234de79ef1e4f1e4f4c24535902` |
| `environment.txt` | `a7c5f88dc049435e23672889b61b798765c8582d1c81549ecf54acf398090b89` |
| `run.log` | `32693ae628e5af9b8c7238bf610cc025aaa1281a30882a88d0db7b09a4e423e0` |
| `tuning_log.csv` | `b7081be0704acca04d2481f589cec4738dee9e349bedc31fa9e0a714593cf5b3` |
| `model_source.py` | `a73fc3692db47834121c716c41d9ca72dc5ddb536089a6af96a07e34770d934f` |
| `invocation.json` | `7f074419d04fab935e0d1709e22dd2eeeb5cb9a858e84d162a40de65647c1034` |

## 소스와 실행 환경의 출처

- 실제 실행 당시 Git SHA는 `9e73e593738267c3779a9199b1256f2a93d860db`다. 이 값을 새 모델 PR 커밋으로 바꾸지 않았다.
- 실험 당시 Ridge 코드는 미추적 상태였다. environment.txt의 git_dirty=False는 추적 파일 기준이므로 실행 모델 소스까지 커밋되어 있었다는 의미는 아니다.
- 실행 소스 사본 model_source.py SHA-256은 위 표에 보존했다.
- 제출 준비 시 모델 브랜치 커밋: `5b17224eeb7f9aaae993b806bc1a2371b0bb7259`. 해당 커밋의 model.py Git blob SHA-256: `405a9e641103b874c0007b506cba654b19da3ef2dd353be46ba8c5f77d36d091`.
- 실행 소스 사본과 모델 커밋의 코드는 CRLF→LF 정규화 후 동일하다. 실행 소스 사본은 원본 바이트를 유지했으므로 해시가 다를 수 있다.
- 스냅샷 ID: `fv-snap-20261031-v1`; manifest SHA-256: `3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0`.
- Python 3.12.16, OS·CPU·패키지 버전·스레드 환경은 environment.txt에 기록되어 있다.
- invocation.json의 `C:\FoodValue_was`는 실험 당시 프로젝트 작업 경로다. 개인 사용자 홈 경로나 자격증명은 포함하지 않으며 원본 증빙을 위해 수정하지 않았다.

## 분석 문서와 로컬 전용 자료

- [v1 설계·실험·Validation 분석](../../model_comparison/ridge/experiments/v1/ridge_v1.md)
- [Alpha 6개 비교](../../model_comparison/ridge/experiments/v1/experiment_summary.md)
- [Alpha=10 설정 사본](../../model_comparison/ridge/experiments/v1/final_config.json)
- [원본 경로와 해시 매니페스트](../../model_comparison/ridge/experiments/v1/version_manifest.md)
- 분석 문서 내 과거의 “Validation 미실행” 문구는 해당 이력 작성 시점의 상태다. 현재 공식 판정은 문서 상단과 이 README를 따른다.
- ridge_v1.md 계열 표의 “Naive 우위” 열은 실제로 “Ridge가 Naive보다 MAPE가 낮은가”를 표시한다. 예는 양파 도매·깐마늘 소매다. 원본 문서와 수치는 변경하지 않았다.
- 매니페스트에 있는 runs/·automation-*/·audit/ 경로는 로컬 보존 자료다. GitHub 제출 파일의 필수 의존성이 아니며 이번 Staging에는 포함하지 않는다.
- v1 분석 문서 4개도 원본 그대로 제출한다. 로컬 자동화 스크립트·전체 작업공간 감사 로그·스냅샷은 제외한다.

## 재현 및 제출 형식 확인

아래 명령은 참고용이며 이번 제출 준비에서 실행하지 않았다. 재현 실행은 별도로 승인된 경우에만 수행하고, 기존 결과를 덮어쓰지 않도록 존재하지 않는 새 실행 ID를 사용한다. YYYYMMDD와 NN은 실제 실행 날짜·미사용 순번으로 바꾼다.

팀에서 배포한 동일 스냅샷과 environment.txt에 대응하는 환경에서 저장소 루트 기준으로 실행한다.

```bash
python -B -m tools.run_backtest --config model_comparison/ridge/config_alpha_10.json --phase p1 --origins validation --snapshot data/snapshots/fv-snap-20261031-v1 --out runs --experiment-id ridge-p1-YYYYMMDD-NN --where local --tuning-log experiments/ridge-p1-20261111-07/tuning_log.csv
```

이번 작업에서는 학습·예측·평가 지표 재생성 없이 아래 형식 검사만 수행한다.

```bash
python -B -m tools.validate_experiment experiments/ridge-p1-20261111-07
```

최종 Test 및 추가 튜닝을 실행하거나 이 제출 결과로 다른 Alpha를 선택하지 않는다.
