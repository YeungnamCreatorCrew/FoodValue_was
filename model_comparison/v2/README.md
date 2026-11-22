# v2 — 모든 자료 연동 + 10계열 통합 학습

v1(4개 모델 비교, 기준서 v1)과 **별도**로 진행하는 확장 실험이다. v1 공통 도구(`tools/`)와 v1 스냅샷은 바꾸지 않고
그 위에 얹는다. 그래서 v1 결과·기준 SHA에 영향이 없다. 평가는 v1과 같은 `tools/evaluate`라 숫자를 바로 비교할 수 있다.

## 자료

v1 스냅샷(`fv-snap-20261031-v1`)은 그대로 쓰고, 옆에 추가 자료 폴더를 만든다. **팀 모두 같은 정제본을 쓴다.**

| 폴더 | 용도 | manifest SHA-256 |
| --- | --- | --- |
| `fv-v2-extra-20261031` | 원본 추출본(가락 API·ASOS 값 그대로). 정제본을 만드는 입력. PR #42 첫 결과는 이 판 | `5bc051c3…324055a` |
| `fv-v2-extra-20261031-r2` | **정제본 — 모든 v2 실험의 입력**(`run_pooled` 기본값) | `b23ca484…7b6acc` |

정제본은 원본에서 반입량 오입력 의심값의 `ton`만 빈 값으로 바꾼 것이다(그 외 파일·글자는 동일). 뺀 값은
`garak_excluded.csv`에, 규칙(직전 20개 반입일 중앙값의 8배 초과, 직전 값 10개 이상일 때만)과 원본 manifest
SHA-256은 정제본 `manifest.json`의 `cleaning`·`derived_from`에 남는다. 현재 5건: 무 2021-11-26(14,762톤),
깐마늘 2021-04-23·08-09·08-26·09-15. 2026-11-16 가락 API 재조회로 원본 값임을 확인했다(한 도매법인 값만 튐).
직접 CSV를 읽는 코드도 **빈 `ton` = 결측(NaN)**, 자료 기간 안에서 행이 없는 날(일요일 등) = 0톤으로 읽어야 같은 자료가 된다.

| 파일 | 내용 | 기간 |
| --- | --- | --- |
| `asos_station_daily.csv` | 품목 주산지 ASOS 관측소 일자료(평균·최저·최고기온, 강수, 습도, 일조) | 2016-01 ~ 2026-10-31 |
| `garak_arrivals_daily.csv` | 가락시장 경매 후 반입물량(톤), 5개 품목 | 2021-01 ~ 2026-10-31 |
| `item_station.csv` | 품목 → 주산지 관측소(`stations.py`, **팀 검토 대상**) | |
| `garak_excluded.csv` | (정제본만) 뺀 반입량: 날짜·품목·원래 톤·직전 중앙값·배수 | |

```powershell
# 스냅샷 담당(공유 DB 보유자) — v1 스냅샷이 data/snapshots/ 에 있어야 함
uv run --extra prices python -m model_comparison.v2.snapshot export --garak ..\garak_arrivals.jsonl
uv run python -m model_comparison.v2.snapshot clean          # 원본 → 정제본(-r2)
# 받는 사람: 정제본을 data/snapshots/fv-v2-extra-20261031-r2/ 에 풀고, manifest SHA-256이 위 표와 같은지 확인
uv run python -m model_comparison.v2.snapshot check
```

## 특징 (한 표본 = 계열 × 기준일 d × 시점 h)

| 묶음 | 개수 | 내용 | 이용 시점 |
| --- | --- | --- | --- |
| v1 기본 | 15 | 가격 이력·달력 | d |
| v1 §5.2 묶음 | 최대 17 | 상대 시장, 전국 기상, 명절, 환율, 생산량 | d−1 / 목표일 / 공개일 |
| `WEATHER_ANOM` | 26 | 주산지 날씨의 평년(지난 1~5년 같은 날) 대비 편차, 과거 13개 4주 블록 | d−1 |
| `ORIGIN_WEATHER` | 130 | 주산지 평균 날씨: 과거 52주 각 주의 평균기온·강수합 + 과거 13개 4주 블록의 최저·최고기온 | d−1 |
| `GARAK` | 10 | 반입량 과거 8주 각 주 합, 최근 7·28일 전년 대비 | d−1 |
| `CROSS_ITEM` | 10 | 다른 품목(같은 시장) 가격 7·28일 변화율 | d−1 |
| `SERIES_ID` | 6 | 품목 원핫 + 도매 여부 | — |
| `PRICE_DYN` | 11 | 자기 가격만으로 만든 동역학(변동 없는 날 비율, 마지막 변동 후 일수, 로그 변화 변동성, 56일 범위 위치, 91·365일 평균 대비, 전년 대비, 3일 변화, 1~3년 전 같은 시기 h일 변화) | d |

| `KREI` | 5 | KREI 관측월보(별도 스냅샷): 이번 달 도매가격 전망 ÷ 지난달 실적, 그 변화를 우리 계열 가격에 옮긴 값, 가격 전망 전년 대비 방향, 전체 출하량 전망(전년 대비), 마지막 호 공개 후 경과일 | d−1 (`available_from`) |
| `KIND` | 5 | 배추·무 작형 전환 신호(이어 붙이기 상태 재현): 후보 작형 연속 관측 수, 후보 최근 가격 ÷ 현재 가격(로그), 경과일, 평년 전환 시기까지 일수, 평년 전환 점프. 그 외 계열은 NaN (RESULTS §11) | d |
| `KIND_OBS` | 3 | `KIND` 중 실제 관측 신호 3개만(평년 특징 제외) | d |

- 추가 자료 폴더는 `ORIGIN_WEATHER`·`WEATHER_ANOM`·`GARAK`을 쓸 때만 필요하다. 그 밖의 묶음만 쓰는 설정은 폴더 없이 돈다.
- `KREI` 묶음은 KREI 스냅샷 폴더(`--krei`, 기본 `data/snapshots/FoodValue_KREI_Snapshot_20261118_r2/`)가 필요하다.
  데이터 담당이 수정판(새 `snapshot_id`)을 내면 그 폴더를 `--krei`로 주거나 `krei.py`의 `SNAPSHOT_ID`를 바꾼다.
  읽는 열: `available_from`·`item_name`·`crop_type`·`metric`·`kind`·`target_start`·`target_end`·`basis`·
  `value`(`value_low`/`value_high`)·`direction`, manifest의 `snapshot_id`·`values_rows`. 데이터 마감일 뒤 공개된 호는 읽지 않고,
  전망 대상 달이 지나면 전망 값은 비운다(1·2월 미발행 기간에 12월 전망을 쓰지 않음).
  KREI 월보 형식이 2025-03에 바뀌어 그 뒤에는 작형별 출하·출하면적·전월 대비·대부분의 평년 대비가 원문에 없다.
  학습 기간에만 있는 특징은 넣지 않는다(평가 때 항상 비어 '값 없음'을 신호로 배움). 엽근 1·2월호는 원래 발행되지 않는다.

- "며칠 / 몇 주 / 몇 달 뒤 영향"을 사람이 정하지 않고, 52주 이력을 모두 주어 모델이 찾게 한다.
- 값이 없으면 NaN(반입량은 2021년 이전, 자료 기간 안의 일요일 등 경매 없는 날은 0톤).
- 정제본의 빈 반입량(오입력 의심값)은 NaN. 판정은 직전 값만 써서 시점 규칙을 지킨다.
- 시점 규칙 테스트: d일과 그 뒤 날씨·반입량을 지워도 기준일 d 특징이 같음(`tests/test_v2.py`).

## 통합 학습

`run_pooled.py`가 v1과 같은 기준일·주 1회 재학습으로, 매번 **10개 계열 표본을 한 모델이** 학습한다(표본 약 8만 개).
가격 수준이 계열마다 다르므로 대상은 변화율, 가격 수준 특징은 current 대비 비율로 바꾼다(`models.py`).

```powershell
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/all.json --origins tune
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/all.json   # 검증 전체
```

| 설정 | 내용 |
| --- | --- |
| `v1feat.json` | 통합 학습 + v1에서 효과 있던 묶음(MARKET·전국 기상·명절)만 — 통합 학습 자체의 효과 |
| `all.json` | 모든 자료 |
| `no_ow.json`, `no_garak.json`, `no_cross.json` | 모든 자료에서 하나씩 빼기 — 무엇이 기여했는지 |
| `v1feat_garak.json`, `v1feat_cross.json`, `v1feat_anom.json` | v1 효과 묶음에 하나씩 더하기 |
| `v1feat_xgb_tuned.json` | **현재 XGBoost 구성원.** robust에서 트리 600·깊이 6·min_child_weight 5·Huber 0.03 (§8, 팀 결정 2026-11-20) |
| `v1feat_xgb_robust.json` | v1feat + Huber 손실 + 계열 변동 크기 가중. 이전 XGBoost 구성원(§3~§7 숫자의 기준, 재현·비교용) |
| `v1feat_lgbm.json` | **현재 LightGBM 구성원.** v1feat를 LightGBM(`PooledLGBM`, 제곱 오차)으로 (§7 튜닝 후 기본값 유지) |
| `v1feat_xgb_robust_krei.json`, `v1feat_lgbm_krei.json` | 위 두 구성원 + `KREI` 묶음 |

### 학습 방식 옵션 (`params`에 넣음)

| 키 | 값 | 설명 |
| --- | --- | --- |
| `objective` | `reg:pseudohubererror`(+`huber_slope`) / `reg:absoluteerror` / LightGBM `huber`(+`alpha`) | 대상이 변화율이라 Huber·MAE가 MAPE에 가깝다. 제곱 오차는 변동 큰 계열에 끌려가 가격이 잘 안 바뀌는 계열에서 naive에 진다 |
| `series_weight` | `inv_scale` / `balanced` | `inv_scale` = 계열 변화율 크기로 나눠 계열마다 손실 기여를 맞춘다(평가가 계열 macro 평균). `balanced` = 표본 수만 맞춤 |
| `halflife_days` | 숫자 | 오래된 표본 가중을 반감(최근 흐름 강조) |
| `strategy` | `pooled_horizon` | 시점 7개를 한 모델로(기본은 시점별 7개) |

`run_pooled`는 모델 `fit`이 `groups`·`ages`를 받으면 계열 번호·표본 경과일을 넘긴다(받지 않는 모델은 그대로 동작).

### 앙상블

끝난 실험 폴더의 예측을 평균해 같은 평가기로 채점한다(재학습 없음, 몇 초). 같은 기준일 목록으로 돌린 실험만 합칠 수 있다.
옵션: `--weights 0.3,0.3,0.4`(순서는 폴더 순서), `--how median`.

## 현재 앙상블 구성 (기준, 2026-11-20)

> **사람·AI 공통 작업 기준.** v2에서 앙상블을 만들거나 "현재 앙상블에 넣었을 때"를 판단할 때는 이 표의 구성원과 설정만 쓴다.
> 여기 없는 설정(예: `v1feat_xgb_robust`)으로 만든 앙상블 숫자는 이전 기준이라 지금 결과와 직접 비교하지 않는다.
> 구성원을 바꾸려면 [튜닝 규칙](#튜닝-규칙-v2-앙상블-구성원)대로 튜닝 기준일에서 고르고 검증에서 한 번 확인한 뒤, 이 표를 고치는 PR을 팀 합의로 머지한다.

| 구성원 | 설정 | 실행기 | 상태 |
| --- | --- | --- | --- |
| XGBoost | `model_comparison/v2/configs/v1feat_xgb_tuned.json` | `model_comparison.v2.run_pooled` | 확정 (§8: 21회 튜닝, 검증·시드 42·43·44 확인) |
| LightGBM | `model_comparison/v2/configs/v1feat_lgbm.json` | `model_comparison.v2.run_pooled` | 확정 (§7: 15회 튜닝, 기본값 유지) |
| AutoARIMA | `model_comparison/autoarima/config_p2_event.json` (p2) | v1 실행기 `tools.run_backtest` | 확정 (§9: 6회 튜닝, p2 유지. p1은 성능 같고 26% 빠름 — 단순한 쪽을 고를지는 팀 판단) |
| Ridge | `model_comparison/ridge/v2/` (`no_ow_w1095`) | Ridge v2 실행기 | **넣지 않음** (§10: 3모델에 10% 더하면 4.5614 → 4.5652%로 나빠짐) |

- 섞는 방식: 같은 비중 평균(구성원별 1/3). 비중 조정은 아직 정하지 않음(정할 때도 튜닝 기준일에서 고르고 검증은 한 번)
- **현재 기준 숫자** (모두 Windows PC, 같은 비중)

| 기준일 | 앙상블 | MAPE | naive 대비 |
| --- | --- | --- | --- |
| 튜닝 53개 (naive 4.607%) | XGBoost 튜닝판 + LightGBM | 4.2777% | |
| 튜닝 53개 | **XGBoost 튜닝판 + LightGBM + AutoARIMA p2** | **4.2637%** | |
| 검증 244개 (naive 4.913%) | XGBoost 튜닝판 + LightGBM | 4.5925% | +6.51% |
| 검증 244개 | **XGBoost 튜닝판 + LightGBM + AutoARIMA p2** | **4.5614%** | **+7.15%** (관문 5개 통과) |

### 현재 앙상블 재현 (PowerShell, 저장소 루트)

```powershell
# 1) 구성원 예측 (검증 244개). 튜닝 기준일이면 각 명령에 --origins tune
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/v1feat_xgb_tuned.json
uv run --extra prices python -m model_comparison.v2.run_pooled --config model_comparison/v2/configs/v1feat_lgbm.json
# AutoARIMA 검증 예측은 저장소에 있음: experiments/arima-p2-20261112-01
# AutoARIMA 튜닝 기준일 예측은 직접 실행(약 40분):
uv run --extra prices python -m tools.run_backtest --config model_comparison/autoarima/config_p2_event.json --phase focus --origins tune --out runs/arima-v2

# 2) 같은 비중 앙상블 (폴더 이름의 날짜·번호는 실행 결과에 맞게)
uv run --extra prices python -m model_comparison.v2.ensemble `
    experiments_v2/v1feat_xgb_tuned-validation-<날짜>-01 `
    experiments_v2/v1feat_lgbm-validation-<날짜>-01 `
    experiments/arima-p2-20261112-01 --name ens-current
```

- 실행 시간(Windows PC 기준): XGBoost 튜닝판은 robust보다 2~3배 느림(튜닝 기준일 약 7분), LightGBM 약 2분, AutoARIMA 튜닝 기준일 약 40분
- 결과 폴더(`experiments_v2/`, `runs/`)는 커밋하지 않는다. 숫자는 [RESULTS.md](RESULTS.md)에 남긴다
- 새 자료·새 모델을 시험할 때도 이 3모델 앙상블에 넣었을 때 좋아지는지로 판단한다

## 튜닝 규칙 (v2 앙상블 구성원)

v2 튜닝은 기준서(`MODEL_TRAINING_STANDARD.md` §6)의 "집중 튜닝(3단계)"으로 보고, 예산은 1차와 같게 둔다.
같은 튜닝 기준일에서 시도를 늘릴수록 그 기준일에만 맞는 설정을 고를 위험이 커지므로(§7 LightGBM 사례),
횟수 상한보다 **검증은 한 번만 보고 멈춘다**는 규칙이 더 중요하다.

| 항목 | 규칙 |
| --- | --- |
| 상한 | 모델별 **최대 40회**(기본 설정 1회 포함, 구속력 있는 상한). 누적 3시간은 권장 상한 |
| 시도 1회 | 설정 하나로 튜닝 기준일(`--origins tune`) 전체를 돌린 것. AutoARIMA는 탐색 범위·계절성·외생변수 조합 하나가 1회(내부 차수 탐색은 세지 않고 시간에는 포함) |
| 시드 반복 | XGBoost·LightGBM 상위 후보의 시드 43·44 재실행은 시도로 세지 않는다. Ridge·AutoARIMA는 결정적이라 1회 |
| 판단 기준 | 튜닝 기준일에서 **현재 앙상블에 넣었을 때의 MAPE**(`ensemble.py`). 단독 MAPE가 아님 |
| 검증 확인 | 상위 후보 1~2개를 검증 기준일로 **한 번만** 본다. 본 뒤에는 그 모델 튜닝을 끝낸다(검증을 보고 고르는 것이 되므로) |
| 채택 조건 | 검증에서도 앙상블이 좋아질 때만. 튜닝 기준일에서만 0.01~0.03%p 좋아진 것은 시드·기준일 흔들림 안이라 채택 근거가 아니다 |
| 기록 | 실패를 포함한 모든 시도를 `<모델>_tune/tuning_log.csv`(`trial, config_id, params, macro_mape, seconds, status`)에, 결과는 [RESULTS.md](RESULTS.md)에 남긴다 |
| 시험 기준일 | 튜닝에 쓰지 않는다. 구성원·앙상블 방식을 고정한 뒤 팀 합의로 한 번만 |

모델별 사용 현황 (2026-11-19)

| 모델 | 사용 | 상태 |
| --- | --- | --- |
| LightGBM | 15 / 40 | 검증 확인 후 종료, 기본값(`v1feat_lgbm`) 유지 (§7) |
| XGBoost | 21 / 40 (+ 중단 1회, 결과 없음) | 검증 확인 후 종료, `combo` → `v1feat_xgb_tuned` 후보. 검증에서 앙상블 개선(4.592 → 4.561%)으로 채택 조건 충족, 시드 42·43·44 모두 개선 (§8). v2 구조를 정한 9회(§3)는 세지 않음(팀 결정 2026-11-19) |
| Ridge | 36 / 40 | 검증 확인 후 종료. 검증: XGBoost 튜닝판+LightGBM에 10% 더하면 4.5925 → 4.5833%(`no_ow_w1095`), AutoARIMA p2까지 넣은 3모델(4.5614%)에 더하면 4.5652% (§10). 기록 `ridge_tune/tuning_log.csv`(Ridge v2 실행기, 실패 4회 포함) |
| AutoARIMA | 6 / 40 | 검증 확인 후 종료, p2 유지. 튜닝 목록 최고 p1(명절 없음)이 검증에서 같음(4.5612 vs 4.5614%) (§9). 기록 `model_comparison/autoarima/v2_tune/tuning_log.csv`. v1 p1·p2 시도는 v1 예산으로 따로 셈 |

결과는 [RESULTS.md](RESULTS.md).

결과: `experiments_v2/<설정>-<기준일 목록>-날짜-번호/` (`importance.json`에 특징 중요도). v1 CI 검사 대상이 아니다.
최종 시험 기준일은 쓰지 않는다(팀 합의 후 별도).
