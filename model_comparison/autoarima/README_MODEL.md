# AutoARIMA (담당 C) — 모델 비교 실험 기준서 v1

`model.py`의 `AutoARIMAModel`이 공통 인터페이스(`tools/runtime.py`, 기준서 §9)를 구현한다. 라이브러리는 공통 의존성의 `statsforecast`(2.x)의 `statsforecast.models.AutoARIMA`.

## 실행

```powershell
# 점검(한 달·계열 2개)
uv run --extra prices python -m tools.run_backtest --config model_comparison/autoarima/config.json --phase smoke --month 2025-01 --series 1,9 --out runs

# 튜닝 시도 1회(튜닝 목록 53개 기준일). 후보 설정 파일마다 실행해 같은 기록 파일에 누적
uv run --extra prices python -m tools.run_backtest --config <후보>.json --phase p1 --origins tune --out runs --record-trial runs/arima-p1-tuning.csv

# 1차 제출(검증 전체)
uv run --extra prices python -m tools.run_backtest --config model_comparison/autoarima/config.json --phase p1 --tuning-log runs/arima-p1-tuning.csv

# 2차(EVENT)
uv run --extra prices python -m tools.run_backtest --config model_comparison/autoarima/config_p2_event.json --phase p2
```

## 설계

| 항목 | 내용 |
|---|---|
| 계열 구성 | **(a) 달력일 계열**, 앞채움 최대 7일, 계절 주기 m=7. 앞채움으로 못 채우는 학습 창 안의 긴 공백(깐마늘 도매 2022-07, 2025-06~07 등)은 양 끝 관측 사이 선형 보간(양 끝 모두 기준일 이전 값이라 누수 없음) |
| (b) 조사일 계열 | 쓰지 않음. 스냅샷 데이터에는 주말 관측이 0건이지만, 기준서 §5.1이 요구하는 "manifest에 주말 미관측 확인 기록"이 `fv-snap-20261031-v1` manifest에 없다. `series_mode`는 `calendar_day`만 받는다 |
| 학습 창 | 공통 로더가 주는 최근 최대 1,825일(`window_days`로 더 짧게 할 수 있음) |
| 재학습 | `fit`(주 첫 기준일): 차수 탐색 + 계수 추정. `predict`(매 기준일): 학습된 모델에 d까지 새 관측을 넣어 상태만 갱신(`AutoARIMA.forward` → 내부 `Arima(model=…)`, 계수 `fixed`)하고 7일 예측. 주중 차수 재탐색·계수 재추정 없음(§3.4) |
| 예측 | 달력일 h=1~7 = d+1~d+7. 로그 변환이면 `exp(평균)` |
| 탐색 범위 | `max_p=5, max_q=5, max_P=2, max_Q=2`, d·D는 검정(KPSS, seas)으로 결정(`max_d=2, max_D=1`), `ic=aicc`, `stepwise=true`. `n_jobs=1`(모델 클래스를 직접 쓰므로 병렬 없음) |
| `approximation` | 계절 모형은 정확 우도 탐색이 계열·주당 20~40초라 튜닝 시도 1회가 3시간을 넘는다. 계절 후보는 `approximation=true`(탐색 중 CSS 근사, 최종 모형은 다시 추정)로 비교했다 |
| 실패 | 예외를 그대로 올린다. 모델 안에서 naive로 바꾸지 않는다 |

### 외생변수

- 달력(`calendar_exog`): `weekday`(요일 더미 6개, 월요일 기준), `season`(연중일 `sin/cos(2π·yday/365.25)`), `weekday+season`, `none`. 날짜만으로 정해지는 값이고 loader와 같은 식이다. 미래 7일 값은 `inputs.features`의 `target_weekday`·`target_season_sin`과 같은지 매 기준일 확인한다.
- EVENT(`event_exog`, 2차): `extra_features: ["EVENT"]`일 때 공통 로더가 넣어 주는 EVENT 4개 열(목표일 기준 값)을 날짜별로 모은다(`history.features`의 목표일 = 표본 기준일 + h, `inputs.features[h]`의 목표일 = d + h). 학습 표본의 목표일은 실제 관측일뿐이라 주말·휴장일 값이 비므로 다음 규칙으로 채운다. 스냅샷 파일은 읽지 않는다.
  - `days_to_major_holiday`, `days_from_major_holiday`: 알려진 값에서 명절 시작일(= 날짜 + days_to)·끝일(= 날짜 − days_from)을 되살려 loader와 같은 식으로 다시 계산 → 정답과 일치(아래 점검).
  - `target_in_event_window`: 직전 알려진 날의 값.
  - `target_prev_day_holiday`: 전날이 되살린 명절 기간 안의 평일이면 1, 아니면 0.
  - 점검(대파 소매, 2021-01-01부터 1,700일 중 값이 비어 채운 558일): 열별 불일치 0·0·5·8일. 불일치는 모두 주말·휴장일(가격이 앞채움 값인 날)이다.

## 파일

| 파일 | 내용 |
|---|---|
| `model.py` | `AutoARIMAModel`, 달력일 계열 만들기, 달력·EVENT 외생변수 |
| `config.json` | 1차 선택 설정(제출에 쓴 설정) |
| `config_p2_event.json` | 2차: 1차 설정 + EVENT |
| `p1_trials/*.json` | 1차 튜닝 후보 설정(시도 기록은 제출 폴더의 `tuning_log.csv`) |
