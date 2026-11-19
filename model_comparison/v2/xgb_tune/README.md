# v2 XGBoost 구성원 튜닝 기록 (XGBoost 담당)

- 대상: `configs/v1feat_xgb_robust.json`(Huber + `inv_scale`)의 하이퍼파라미터
- 판단: LightGBM 기본값(`v1feat_lgbm`, seed 42)과의 **같은 비중 앙상블** policy macro MAPE, 튜닝 기준일 53개
- 장비: Windows 11, Intel Core Ultra 5 225H(14코어), 2026-11-18~19
- 시도: **21회**(1단계 후보 20개 + 좋아진 변경 5개를 합친 `combo` 1개), 누적 4,028초. 예산 40회 안.
  2단계(combo 주변 19개)는 첫 후보(깊이 7) 실행 중 중단해 결과 없음. 이 시도는 combo 검증을 본 뒤 시작한 것이라
  팀 튜닝 규칙(검증을 본 뒤에는 그 모델 튜닝 종료)에 맞지 않아 멈췄고, 결과를 만들지도 쓰지도 않았다. 기록에는 ABORTED로 남김
- 선택: 튜닝 기준일 앙상블 최저 = `combo` → `configs/v1feat_xgb_tuned.json`
- 검증 244개는 `combo` 선택 뒤 한 번만 확인. 이후 설정을 바꾸지 않음

| 파일 | 내용 |
| --- | --- |
| `tuning_log.csv` | 팀 규칙 형식(`trial, config_id, params, macro_mape, ensemble_mape_with_lgbm, seconds, status`). 중단된 22번째(ABORTED) 포함 |
| `tune.py` | 실행 스크립트(기준 → 후보 → 합친 설정 → 검증 1회). 결과 폴더는 `experiments_v2/`(커밋하지 않음) |
| `seeds.py` | 기준·최고 설정을 시드 43·44로 다시 돌려 앙상블 비교(시도로 세지 않음) |

결과 요약은 `../RESULTS.md` §8.
