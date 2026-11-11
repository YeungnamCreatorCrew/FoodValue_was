"""FoodValue Ridge v1 — 공통 base_v1 특징을 사용하는 직접 가격 예측 모델."""

class RidgeModel:
    def __init__(self, alpha=1.0, solver="lsqr"):
        if alpha < 0:
            raise ValueError("alpha must be non-negative")
        if solver != "lsqr":
            raise ValueError("Ridge v1 requires solver='lsqr'")

        self.alpha = float(alpha)
        self.solver = solver
        self.model = None

    def fit(self, history, seed: int) -> None:
        import numpy as np
        from sklearn.linear_model import Ridge
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import Pipeline

        X = np.asarray(history.features, dtype=float)
        y = np.asarray(history.targets, dtype=float).reshape(-1)

        self.feature_names = list(history.feature_names)

        if X.ndim != 2 or X.shape != (len(y), len(self.feature_names)):
            raise ValueError("Invalid training data shape")

        if not np.isfinite(X).all() or not np.isfinite(y).all():
            raise ValueError("Training data contains non-finite values")

        self.model = Pipeline([
            ("scaler", StandardScaler()),
            ("ridge", Ridge(alpha=self.alpha, solver=self.solver))
        ])

        self.model.fit(X, y)

    def predict(self, inputs) -> list[float | None]:
        import numpy as np

        if self.model is None:
            raise RuntimeError("Model must be fitted first")

        if list(inputs.feature_names) != self.feature_names:
            raise ValueError("Feature names do not match")

        horizons = sorted(inputs.features)

        if horizons != list(range(1, 8)):
            raise ValueError("Expected horizons 1 through 7")

        X = np.asarray(
            [inputs.features[h] for h in horizons],
            dtype=float
        )

        predictions = self.model.predict(X)

        return [float(value) for value in predictions]
