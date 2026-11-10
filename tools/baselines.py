"""기준 모델(§8.3). 단계 0 점검과 실행기 동작 확인에 쓴다. 모델 담당자 구현의 가장 단순한 예시이기도 하다.

    uv run --extra prices python -m tools.run_backtest --config tools/configs/naive.json --phase smoke --month 2025-01
"""
from tools.runtime import OriginInputs, TrainingData


class Naive:
    """v[d]를 7개 시점에 그대로 쓴다(저장소 LAST_PRICE)."""

    def __init__(self, **params):
        self.params = params

    def fit(self, history: TrainingData, seed: int) -> None:
        self.current = history.feature_names.index('current')

    def predict(self, inputs: OriginInputs) -> list[float | None]:
        return [float(inputs.features[h][self.current]) for h in sorted(inputs.features)]


class Mean7:
    """v[d-6..d] 평균(저장소 MEAN_7)."""

    def __init__(self, **params):
        self.params = params

    def fit(self, history: TrainingData, seed: int) -> None:
        self.mean7 = history.feature_names.index('mean7')

    def predict(self, inputs: OriginInputs) -> list[float | None]:
        return [float(inputs.features[h][self.mean7]) for h in sorted(inputs.features)]
