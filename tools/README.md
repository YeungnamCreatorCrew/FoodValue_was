# tools — 모델 비교 실험 공통 도구

규칙의 정본은 **`model_comparison/MODEL_TRAINING_STANDARD.md`(기준서 v1)** 다. 이 폴더는 그 규칙을 코드로 강제한다.

| 파일 | 상태 | 역할 |
|---|---|---|
| `standard.py` | 완료 | 기준서 고정값(날짜·기준일 구간·학습 창·스레드·시드·튜닝 예산·계열·작형 규칙 값·제출 형식). **숫자를 다른 곳에 직접 쓰지 말고 여기서 가져온다.** 기준서를 바꾸면 같은 PR에서 이 파일도 바꾼다 |
| `origins.py` | 완료 | `calendar_day`로 검증·튜닝·시험 기준일 목록 생성, `guard(phase, origins)`로 단계 밖 기준일 차단(§7.2) |
| `runtime.py` | 완료 | `apply_environment()`(스레드·시드 환경변수 강제), 모델 인터페이스 `Model`·`TrainingData`·`OriginInputs`(§9) |
| `validate_experiment.py` | 완료 | 실험 결과 폴더의 §10 형식·고정값 검사. CI가 PR마다 실행 |
| `snapshot.py` | 완료 | 스냅샷 파일 형식(열), CSV 쓰기(UTF-8·LF라 OS와 무관하게 SHA-256 같음), 계열 품질(§2.1) 계산 |
| `export_snapshot.py` | 완료 | §2.2 CSV·manifest 생성. 스냅샷 담당(공유 DB 보유자)만 실행 |
| `check_snapshot.py` | 완료 | SHA-256·행 수·열·마감일·계열 기간·기준일 목록·이어 붙이기 재계산·연도별 전환 횟수 대조. **받은 사람 모두 실행** |
| `loader.py` | 완료 | `merge_kinds`(§2.3, 이 함수 하나만 씀), `Snapshot`: 기준일 시점 자료(§3.1)·1차 특징 15개(§5.1, 저장소 `features()`와 같은 값), `training_data()`·`origin_inputs()`·`load_as_of()`, 평가용 정답·naive·mean7 |
| `run_backtest.py` | 완료 | 기준일·주 1회 재학습 일정으로 `fit`/`predict` 호출, 실패·NO_INPUT·TIMEOUT 기록, 후처리, `config.json`·`predictions.csv`·`run.log`·`environment.txt`·`tuning_log.csv`, 끝에 평가·형식 검사 |
| `evaluate.py` | 완료 | §8 지표(`policy`·`model_only`·`common_success`, 계열·시장·계절·시점·작형 전환 세부, 월 블록 부트스트랩), 채택 관문 1~5, `metrics.json`. `--compare`로 여러 모델 비교 |
| `baselines.py`, `configs/naive.json` | 완료 | naive·mean7 기준 모델(단계 0 점검, 모델 구현 예시) |

새 도구를 만들 때 지킬 것

- 날짜·숫자는 `tools.standard`에서 가져온다.
- 실행 진입점은 맨 처음 `runtime.apply_environment()`를 부른다.
- 기준일을 받는 모든 실행은 `origins.guard()`를 거친다. test 단계가 아니면 최종 시험 기준일을 거부한다.
- 모델 코드는 스냅샷 파일·DB를 직접 읽지 않고 `TrainingData`·`OriginInputs`만 받는다.

## 스냅샷 만들기·받기

스냅샷 담당(공유 DB 보유자, `.env`에 `DATABASE_URL`·`KOSIS_API_KEY` 필요):

```powershell
uv run --extra prices python -m tools.export_snapshot
# 품질 REVIEW/FAIL 계열을 팀이 빼기로 했으면: --exclude-item 깐마늘
```

`data/snapshots/fv-snap-20261031-v1/`이 생긴다(Git에 올리지 않음). 폴더째 압축해 공유 드라이브에 올리고, 화면 끝의
`manifest SHA-256`을 팀 채팅에 함께 남긴다. DB에 마감일(2026-10-31) 뒤 자료가 있어도 내보낼 때 잘리므로 다시 수집하지 않는다.

받는 사람:

```powershell
# 압축을 풀어 레포의 data/snapshots/fv-snap-20261031-v1/ 에 둔 뒤
uv run python -m tools.check_snapshot data/snapshots/fv-snap-20261031-v1
```

`결과: 통과`이고 마지막 줄 `manifest SHA-256`이 담당자가 남긴 값과 같아야 실험을 시작한다.

## 실험 돌리기 (모델 담당)

1. 모델 클래스를 만든다: `fit(history: TrainingData, seed)`, `predict(inputs: OriginInputs) -> 7개 값`. 예시 `tools/baselines.py`.
   - `history.features`: (표본 수 × 15) numpy 배열, 열 이름 `history.feature_names`(= `standard.BASE_FEATURES`)
   - `history.targets`: 목표일 실제 가격(원), `history.horizons`: 1~7, `history.origins`: 표본 기준일, `history.prices`: 창 안 실제 관측 (날짜, 가격)
   - `inputs.features[h]`: 기준일 d의 시점 h 특징 한 줄, `inputs.prices`: d까지 실제 관측
   - 학습 대상 변환(변화율 등)·전략은 모델 안에서 자유. 출력은 원 단위 가격 7개(실패는 예외나 None)
2. 설정 파일(JSON)을 만든다. 예: `tools/configs/naive.json`

   ```json
   {"model": "LightGBM", "owner": "B", "class": "model_comparison.lightgbm.model:LGBMModel",
    "params": {"num_leaves": 31, "deterministic": true, "force_row_wise": true, "num_threads": 4},
    "feature_set": "base_v1", "extra_features": [], "target_transform": "log_ratio",
    "strategy": "direct_per_horizon", "seed": 42}
   ```

3. 실행한다.

   ```powershell
   # 단계 0 (4명 모두, naive, 2025-01): 마지막 metrics SHA-256이 4명 같아야 함
   uv run --extra prices python -m tools.run_backtest --config tools/configs/naive.json --phase smoke --month 2025-01 --out runs

   # 빠른 점검(일부 계열·한 달)
   uv run --extra prices python -m tools.run_backtest --config my.json --phase smoke --month 2025-01 --series 1,9001 --out runs

   # 튜닝 시도 1회 = 튜닝 목록 전체(약 53개 기준일). 시도마다 기록 파일에 한 줄 추가(최대 40회)
   uv run --extra prices python -m tools.run_backtest --config my.json --phase p1 --origins tune --out runs --record-trial runs/lgbm-p1-tuning.csv

   # 1차 제출: 검증 전체, 튜닝 기록을 함께 넣음 → experiments/<id>/ 를 PR로 올림
   uv run --extra prices python -m tools.run_backtest --config my.json --phase p1 --tuning-log runs/lgbm-p1-tuning.csv
   ```

   - `runs/`는 Git에 올라가지 않는다. 제출할 결과만 `experiments/`에 만든다.
   - 최종 시험 기준일(2025-11-10~)은 `--phase test --where docker`에서만 돈다. 다른 단계에서 쓰면 시작 전에 거부한다.
4. 모델끼리 비교(세 결과·순위·동률·관문):

   ```powershell
   uv run --extra prices python -m tools.evaluate --compare experiments/xgb-p1-... experiments/lgbm-p1-... --out comparison.json
   ```
