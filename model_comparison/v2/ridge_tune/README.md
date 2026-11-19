note: Ridge v2 전용 실행기(`model_comparison/ridge/v2/run.py`)의 튜닝 기준일 전체 실행 30회(시도 1~30)와 시작 전 실패 4회(`FAILED_PREFLIGHT`, 봉인 검사 실패라 학습 안 함 → 시도로 세지 않음)를 옮겼다. `ensemble_mape_w10`은 XGBoost(`v1feat_xgb_robust`) 0.45 + LightGBM(`v1feat_lgbm`) 0.45 + Ridge 0.1 앙상블(기준 XGBoost+LightGBM 4.2847%), 빈칸은 앙상블을 돌리지 않은 시도. `COMPLETED_WITH_MISSING`은 일부 예측이 공통 규칙대로 Naive로 대체된 정상 완료(성공률 약 99%). Ridge는 결정적이라 시드 반복 없음. 실행 전 점검 2회·1개월 시험 실행 1회는 튜닝 기준일 전체가 아니라 제외. 실행별 상세는 `model_comparison/ridge/v2/EXPERIMENT_LOG.md`, 결과는 RESULTS.md §6.

note (2026-11-19, 시도 31~36): 기준 XGBoost를 튜닝판(`v1feat_xgb_tuned`)으로 바꾼 뒤 돌렸다. 이 6행의 `ensemble_mape_w10`은 XGBoost 튜닝판 0.45 + LightGBM 0.45 + Ridge 0.1(기준 XGBoost 튜닝판+LightGBM 4.2777%)이라 1~30행과 기준이 다르다. 같은 기준에서 기존 `no_ow` 4.2658%, MARKET 4.2699%.

검증 확인(한 번, 시도로 세지 않음): `no_ow_w1095`(`ridge-v2-20261119T084634364391Z-fe6c5bac24aa4b5795455f62f2d4c2fa`, 단독 5.0256%)·`no_ow`(`ridge-v2-20261119T084708506807Z-5eb236c29d114fb1a29f58ce1fe8c4ef`, 단독 5.0025%). 앙상블 수치는 RESULTS.md §10.
