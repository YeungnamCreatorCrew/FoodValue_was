# AutoARIMA v2 구성원 튜닝 (2026-11-19)

v2 튜닝 규칙(`model_comparison/v2/README.md` "튜닝 규칙")에 따라 XGBoost 튜닝판 + LightGBM과의 같은 비중 앙상블로 판단했다.
결과와 판단은 `model_comparison/v2/RESULTS.md` §9.

| 설정 | 시도 | 바꾼 것 (기준 `config_p2_event.json`) |
| --- | --- | --- |
| `a01_p2.json` | 1 | 없음 (현재 구성원) |
| `a02_p1_noevent.json` | 2 | 명절 외생변수 없음 (= v1 p1 선택 설정) |
| `a03_level.json` | 3 | level 변환 |
| `a04_win730.json` | 4 | 학습 창 730일 |
| `a05_win365.json` | 5 | 학습 창 365일 |
| `a06_season_approx.json` | 6 | 주간 계절성(근사) |

```powershell
uv run --extra prices python -m tools.run_backtest --config model_comparison/autoarima/v2_tune/a01_p2.json --phase focus --origins tune --out runs/arima-v2 --record-trial runs/arima-v2/trials.csv
```

동시에 여러 개를 돌리면 실험 폴더 번호가 겹칠 수 있으니 `--experiment-id`를 따로 주거나 시작 시점을 몇 초씩 띄운다.
