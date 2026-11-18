# Ridge v2 실행 이력

2026-11-16 사전 계획: 구현·단위 테스트만 수행. 실제 Tune/Validation/Test 학습 미실행.

CONTROL → 단일 변수 추가 및 SERIES_ID 제외 → 팀 공통 ALL → WEATHER_ANOM 확장 → 사전 ablation을 검토한다.
최초 CONTROL 이후에도 기본 alpha=10/lsqr/seed=42/1825일/주간 재학습을 유지한다.
선택 지표는 전체 policy MAPE·MAE·RMSE·rMAE·성공률과 모든 10계열 결과이며 유리한 일부만 선택하지 않는다.
추가 결과 기반 선택은 실행 intent에 후보/선택 이유/다음 결정과 이전 실행 ID를 기록한다. 현재 선택한 v2 조합이나 성능은 없다.

모든 CLI 호출은 아래에 누적되며 상세 의도·변경·실패/재시도·다음 결정은 각 실행의 events.jsonl에 연결한다.
합성 단위 테스트의 실행 폴더는 임시 폴더에만 생성하며 실제 실험 이력으로 집계하지 않는다.

- 2026-11-16T12:38:20.733744+00:00 `ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e` **STARTED**; [invocation](experiments/ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e/invocation.json)

- 2026-11-16T12:38:27.083991+00:00 `ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e` **PLANNED**; command/intention/errors/retry/next decision: [ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e](experiments/ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e/events.jsonl)
{"purpose": "Implementation preflight only; no training", "changes": "As specified in experiment config", "reason": "Validate manifests and audit integration without --execute", "previous_run_id": null, "retry": false, "next_decision": "PENDING_REVIEW; no automatic favorable feature selection", "result_status": "PLANNED", "summary_source": null, "errors_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261116T123820139238Z-11474de62eba48d793a894711c9ba21e\\events.jsonl"}

- 2026-11-16T12:45:32.486944+00:00 `ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1` **STARTED**; [invocation](experiments/ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1/invocation.json)

- 2026-11-16T12:45:39.257412+00:00 `ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1` **PLANNED**; command/intention/errors/retry/next decision: [ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1](experiments/ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1/events.jsonl)
{"purpose": "Final implementation preflight only; no training", "changes": "As specified in experiment config", "reason": "Verify pinned historical-source audit integration; no --execute", "previous_run_id": null, "retry": false, "next_decision": "PENDING_REVIEW; no automatic favorable feature selection", "result_status": "PLANNED", "summary_source": null, "errors_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261116T124531908357Z-e9ce498a18eb43568a2948d7936ec2a1\\events.jsonl"}

- 2026-11-17T06:07:14.059384+00:00 `ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7` **STARTED**; [invocation](experiments/ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7/invocation.json)

- 2026-11-17T06:07:34.699198+00:00 `ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7` **COMPLETED**; command/intention/errors/retry/next decision: [ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7](experiments/ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7/events.jsonl)
{"purpose": "CONTROL monthly smoke test", "changes": "Initial CONTROL; 2024-11 only", "reason": "Verify training, predictions, metrics and audit before full Tune", "previous_run_id": null, "retry": false, "next_decision": "PENDING_REVIEW; no automatic favorable feature selection", "result_status": "COMPLETED", "summary_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7\\metrics.json", "errors_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261117T060711075974Z-3587ff8438a54562818a68f177034ea7\\events.jsonl"}

- 2026-11-17T06:09:31.766199+00:00 `ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d` **STARTED**; [invocation](experiments/ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d/invocation.json)

- 2026-11-17T06:10:00.316396+00:00 `ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d` **COMPLETED_WITH_MISSING**; command/intention/errors/retry/next decision: [ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d](experiments/ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d/events.jsonl)
{"purpose": "Full CONTROL Tune benchmark", "changes": "Initial full CONTROL; all 53 Tune origins", "reason": "Establish Ridge v2 baseline before feature experiments", "previous_run_id": null, "retry": false, "next_decision": "PENDING_REVIEW; no automatic favorable feature selection", "result_status": "COMPLETED_WITH_MISSING", "summary_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d\\metrics.json", "errors_source": "C:\\FoodValue_was\\model_comparison\\ridge\\v2\\experiments\\ridge-v2-20261117T060931078600Z-5aedd5a6c62a4e6cb409758eb5c3d60d\\events.jsonl"}
