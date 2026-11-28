# 구조적 가격 전달 모델 (struct) — 읽는 순서와 실행 방법

멘토 제안 두 가지를 실험한 결과다.
1. LLM에게 직접 예측을 시켜 보기 → `model_comparison/llm_blind/RESULTS.md`
2. 기성 ML 모델(XGBoost·LightGBM)을 튜닝하지 말고, 모델 구조를 새로 설계해 다듬기 → 이 폴더

## 결론 (검증 244 기준일, 평가 점 11,275개)

| 모델 | macro MAPE | naive 대비 | 소매 5계열 | 도매 5계열 |
|---|---|---|---|---|
| naive (직전 가격 유지) | 4.913% | — | 4.678 | 5.147 |
| **struct (이 모델)** | **4.765%** | **+3.01%** | **4.383 (+6.32%, 5/5 승)** | 5.147 (설계상 naive) |
| LightGBM p1 | 4.769% | +2.93% | 4.515 | 5.022 |
| LightGBM p2 | 4.693% | +4.47% | 4.342 | 5.044 |
| XGBoost p2 | 4.694% | +4.44% | 4.304 | 5.085 |
| 앙상블 v2 (참고, 입력 조건 다름) | 4.595% | +6.47% | 4.260 | 4.929 |

- naive는 이겼다. 월 블록 부트스트랩 95% 구간은 [+0.068, +0.245]로, 하한이 0보다 크다.
- 기준서 §8.4 채택 관문 중 +5% 개선(G1)과 과반 계열 승(G3)은 미달했다. G3는 도매를 naive로 두었기 때문에 최대 5/10이다.
- LightGBM·XGBoost와는 통계적으로 구분되지 않는다. LightGBM p2 대비 차이의 95% 구간은 [−0.17, +0.04]다.
- 소매는 트리 모델과 비슷한 수준이다. 격차의 대부분은 도매에서 나온다.
- 장점은 설명력이다. 계수 몇 개로 성능이 나오고, 각 항을 그대로 읽을 수 있다: "도매 1주 변화의 일부가 소매로 전달된다", "소매/도매 배수가 평소로 돌아온다", "작년 같은 시기의 흐름을 따른다".

## 모델 한 줄 요약

```
소매 log(가격(d+h)/현재가) = k_h · [ a·log1p(도매 7일 변화) + b·(log 소매/도매 배수 − 최근 91일 중앙값)
                                   + c·(1~3년 전 같은 시기 h일 변화, 가중 0.5/0.3/0.2) + d·명절 지시변수 ]
도매 = 직전 가격 유지(naive)
```

- 계열별 최소제곱에 L2 정규화를 더해 푼다. λ와 시점별 축소 계수 k_h는 학습 표본의 마지막 20%(시간순)로 고른다.
- numpy와 scipy만 쓴다. 트리나 sklearn 모델은 쓰지 않는다.

## 읽는 순서
1. `C5_REPORT.md`: 최종 검증 결과, 관문, 세부 지표, 비교, 한계
2. `README_MODEL.md`: PRD와 다르게 구현한 점, 튜닝 18회 경로, 최종 파라미터
3. `PRD.md`: 기획서(§1~§14). 실험 도중의 결정과 보정까지 시간순으로 적었다.
4. `verification/VERIFY_C1~C5.md`: 구현과 따로 돌린 검증 에이전트의 판정(누수, 재채점, 재현성). 모두 PASS다.

## 진행 방식 (공정성 장치)
- 기준서 v1과는 별개 트랙이다(사용자 결정). 공통 도구(`tools/`)는 고치지 않았다. 입력은 공통 로더 `tools.loader`만 읽기 전용으로 쓴다.
- 튜닝은 튜닝 목록(53 기준일)에서만 했다. 예산 40회 중 18회를 썼다.
- 검증 전체(244 기준일)는 마지막에 1회만 돌렸다. 최종 시험 구간(2025-11-10~)은 쓰지 않았다.
- 역할을 셋으로 나눴다: 계획(PRD·결정), 구현(코드·튜닝), 검증(독립 재계산). 각 확인 지점에서 검증이 PASS해야 다음 단계로 넘어갔다.

## 직접 돌려 보기

**준비**
- 팀 공유 드라이브의 스냅샷 `fv-snap-20261031-v1`을 `data/snapshots/fv-snap-20261031-v1/`에 둔다. 이 폴더는 Git에 없다.
- 무결성을 확인한다.

```bash
uv sync --extra prices
uv run python -m tools.check_snapshot data/snapshots/fv-snap-20261031-v1   # "결과: 통과" 확인
```

**1) 저장된 결과를 다시 채점**

모델은 실행하지 않는다. 이 폴더의 `results/val-t18/predictions.csv`가 검증 1회 결과다.

```bash
uv run --extra prices python -m model_comparison.structural.compare model_comparison/structural/results/val-t18 --out-dir /tmp/struct-check
```

- `/tmp/struct-check/compare.md`가 `results/val-t18/compare.md`와 같으면 된다.
- 비교 대상 중 앙상블 v2 행은 `experiments_v2/`(Git에 없음)가 있어야 나온다. 없으면 그 행만 빠진다.

**2) 모델을 처음부터 다시 실행 (10초 안팎)**

```bash
# 최종 설정(t18)으로 검증 기준일 전체를 실행. 결과는 --out 폴더에 생긴다
uv run --extra prices python -m model_comparison.structural.run \
  --config model_comparison/structural/config.json --name val-t18 --origins validation --out /tmp/struct-runs
uv run --extra prices python -m model_comparison.structural.compare /tmp/struct-runs/val-t18 --out-dir /tmp/struct-runs/val-t18
```

- 예측은 결정적이다. `results/val-t18/predictions.csv`와 행 단위로 같아야 한다.
- 실행기는 같은 `--out` 폴더에서 검증 실행 2회째와 튜닝 시도 41회째를 거부한다.

**3) 테스트**

```bash
uv run --group dev --extra prices pytest model_comparison/structural -q   # 91 passed
```

- `test_leakage.py`: 기준일 이후 가격을 바꿔도 예측이 같은지 등 누수 검사
- `test_run.py`: 튜닝 결과 골든값 재현
- `test_compare.py`: 채점이 기존 실험의 metrics.json과 같은지

**4) 다른 구조를 직접 시험해 보고 싶다면**
- `configs/`의 설정 하나를 복사해서 파라미터를 바꾼다. 쓸 수 있는 키는 `model.py`의 `StructuralModel` 기본값을 보면 된다.
- 튜닝 목록으로 돌린다: `--origins tune --record-trial --out <폴더>`.
- 검증 구간은 이미 한 번 봤다. 그래서 검증 구간으로 다시 비교하면 검증 데이터를 보고 고친 셈이 된다는 점에 주의한다.

## 파일
- `model.py`: StructuralModel. `run.py`: 자체 백테스트 실행기. `score.py`: 채점. `compare.py`: 기존 모델과 같은 점 집합에서 비교
- `config.json`: 최종 설정(t18_retail_t01, sha256 `cbd419c9…`). `configs/`: 튜닝 시도 18개의 설정
- `results/tuning_log.csv`: 튜닝 18회 기록. `results/val-t18/`: 검증 1회 결과(예측, 지표, 비교표, 로그)
- `final_params_t18_20250602.json`: 2025-06-02 재학습 시점의 계열별 계수
- `runs/struct/smoke-v0*`(Git에 없음): 초기 점검용. 검증 구간 일부의 정확도가 들어 있어 사용 금지

## 서비스에서 쓰기 (앙상블과 같은 응답 형식)
- 배치(`FOODVALUE_PRICE_MODEL=v2`)는 v2 대상 계열마다 앙상블 실행 뒤에 struct 실행을 따로 저장한다(`price_model_run.model_track='STRUCT'`). `FOODVALUE_STRUCT_MODEL=0`이면 struct를 끈다.
- API는 `?model=STRUCT`로 고른다(기본 ENSEMBLE). 코드: `app/services/struct_service.py`
- 공개 규칙은 앙상블과 같다: `service/calibration.json`(검증 1회 결과 `results/val-t18`로 만듦, `python -m app.struct_calibrate`)에서 naive보다 나은 계열만 VALIDATED. 소매 5계열 VALIDATED, 도매 5계열 BASELINE(직전 가격 유지)
- 서비스는 기준일마다 재학습한다. 실험은 주 첫 기준일에만 재학습했으므로, 주 첫 기준일(예: 2025-06-02)에서만 실험 예측과 같다(`tests/test_struct_service.py`가 확인)
- 요인(`/factors?model=STRUCT`)은 7일 뒤 예측의 항별 원 단위 분해다. (예측가 − 현재가)를 항별 로그 기여 비율로 나눈다
