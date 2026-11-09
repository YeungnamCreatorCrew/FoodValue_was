# experiments

모델 비교 실험 결과를 **기준서 v1(`model_comparison/MODEL_TRAINING_STANDARD.md`) §10** 형식으로 둔다.

```
experiments/<experiment_id>/
  config.json  predictions.csv  metrics.json  environment.txt  run.log  tuning_log.csv
```

- `experiment_id` = `<모델>-<단계>-<YYYYMMDD>-<순번>` (예: `xgb-p1-20261116-01`). 모델: `xgb`·`lgbm`·`arima`·`ridge`·`base`, 단계: `smoke`·`p1`·`p2`·`focus`·`test`. 통합 모델은 `xgb-pooled-p1-…`.
- 학습된 모델 파일은 `<experiment_id>/model/`에 두면 Git에 올라가지 않는다(`.gitignore`).
- 결과를 PR로 올리기 전에 직접 검사한다. CI(`.github/workflows/standard.yml`)도 같은 검사를 PR마다 실행하며, 실패하면 머지하지 않는다.

```bash
uv run --extra prices python -m tools.validate_experiment experiments/<experiment_id>
uv run --extra prices python -m tools.validate_experiment --all
```

검사하는 것(요약): 필수 파일, `config.json` 필수 항목과 고정값(기준서 판, 데이터 버전, 단계와 기준일 구간, 주 1회 재학습, 스레드 4, 모델별 결정적 실행 옵션, 튜닝 시도 상한, 최종 시험은 Docker·튜닝 금지), `predictions.csv` 열 순서, 계열×기준일마다 7행, `target_date = origin_date + horizon`, 상태 코드, 반올림 후처리, **최종 시험 기준일을 test 단계 밖에서 쓰지 않았는지**.
