# tools — 모델 비교 실험 공통 도구

규칙의 정본은 **`model_comparison/MODEL_TRAINING_STANDARD.md`(기준서 v1)** 다. 이 폴더는 그 규칙을 코드로 강제한다.

| 파일 | 상태 | 역할 |
|---|---|---|
| `standard.py` | 완료 | 기준서 고정값(날짜·기준일 구간·학습 창·스레드·시드·튜닝 예산·계열·작형 규칙 값·제출 형식). **숫자를 다른 곳에 직접 쓰지 말고 여기서 가져온다.** 기준서를 바꾸면 같은 PR에서 이 파일도 바꾼다 |
| `origins.py` | 완료 | `calendar_day`로 검증·튜닝·시험 기준일 목록 생성, `guard(phase, origins)`로 단계 밖 기준일 차단(§7.2) |
| `runtime.py` | 완료 | `apply_environment()`(스레드·시드 환경변수 강제), 모델 인터페이스 `Model`·`TrainingData`·`OriginInputs`(§9) |
| `validate_experiment.py` | 완료 | 실험 결과 폴더의 §10 형식·고정값 검사. CI가 PR마다 실행 |
| `export_snapshot` | 담당: 스냅샷 담당 | §2.2 CSV·manifest 생성, §2.3 작형 이어 붙이기 결과 |
| `check_snapshot` | 담당: 스냅샷 담당 | SHA-256·행 수·계열 기간·이어 붙이기 재계산 대조 |
| `loader` | 담당: ____ | `load_as_of(series_id, d)`, §5 특징, 이어 붙이기 함수(하나만) |
| `run_backtest` | 담당: ____ | 기준일·주 1회 재학습 일정으로 `fit`/`predict` 호출. **시작할 때 `runtime.apply_environment()`와 `origins.guard(phase, 기준일)`을 반드시 부른다** |
| `evaluate` | 담당: ____ | §8 지표(`policy`·`model_only`·`common_success`, 부트스트랩), `metrics.json` |

새 도구를 만들 때 지킬 것

- 날짜·숫자는 `tools.standard`에서 가져온다.
- 실행 진입점은 맨 처음 `runtime.apply_environment()`를 부른다.
- 기준일을 받는 모든 실행은 `origins.guard()`를 거친다. test 단계가 아니면 최종 시험 기준일을 거부한다.
- 모델 코드는 스냅샷 파일·DB를 직접 읽지 않고 `TrainingData`·`OriginInputs`만 받는다.
