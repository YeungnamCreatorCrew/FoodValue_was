"""Ridge p2: training-only median imputation, then the unchanged v1 estimator.

The runner may attach an audit sink; the model never reads data or writes files.
All-missing training columns are frozen at zero until the next weekly fit.
"""
from contextvars import ContextVar

AUDIT_SINK = ContextVar('ridge_p2_audit_sink', default=None)
PREPROCESSING_VERSION = 'ridge-p2-median-v1'


class RidgeP2Model:
    def __init__(self, alpha=10, solver='lsqr'):
        if alpha != 10 or solver != 'lsqr':
            raise ValueError("Ridge p2 fixes alpha=10 and solver='lsqr'")
        self.alpha, self.solver, self.model = float(alpha), solver, None

    @staticmethod
    def _names(names):
        names = list(names)
        if not names or any(not isinstance(n, str) or not n for n in names) or len(set(names)) != len(names):
            raise ValueError('Feature names must be nonempty unique strings')
        return names

    def _matrix(self, values, rows):
        import numpy as np
        X = np.asarray(values, dtype=float)
        if X.ndim != 2 or X.shape != (rows, len(self.feature_names)) or rows == 0:
            raise ValueError('Invalid feature matrix shape')
        # Infinity indicates malformed input, not ordinary source missingness.
        if np.isinf(X).any():
            raise ValueError('Feature infinity is not allowed')
        return X

    def _transform(self, X):
        import numpy as np
        out = np.where(np.isnan(X), self.fill_values_, X)
        out[:, self.all_missing_] = 0.0
        return out

    def fit(self, history, seed: int) -> None:
        import numpy as np
        from sklearn.linear_model import Ridge
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler

        self.model = None  # A failed refit must never leave an earlier model usable.
        if seed != 42:
            raise ValueError('Ridge p2 fixes seed=42')
        self.feature_names = self._names(history.feature_names)
        y = np.asarray(history.targets, dtype=float).reshape(-1)
        X = self._matrix(history.features, len(y))
        if not np.isfinite(y).all() or (y <= 0).any():
            raise ValueError('Target prices must be finite and positive; never imputed')
        missing = np.isnan(X)
        self.all_missing_ = missing.all(axis=0)
        # Explicit per-column calculation avoids nanmedian warnings and sklearn's
        # version-dependent dropping of empty columns. No feature index is fixed.
        self.fill_values_ = np.array([
            0.0 if empty else np.median(X[~missing[:, i], i])
            for i, empty in enumerate(self.all_missing_)
        ])
        self.training_missing_counts_ = missing.sum(axis=0)
        clean = self._transform(X)
        model = Pipeline([('scaler', StandardScaler()),
                          ('ridge', Ridge(alpha=self.alpha, solver=self.solver))])
        model.fit(clean, y)
        self.model = model
        sink = AUDIT_SINK.get()
        if sink is not None:
            scaler, ridge = model.named_steps['scaler'], model.named_steps['ridge']
            z = scaler.transform(clean)
            active = scaler.var_ > 0
            za = z[:, active]
            singular = np.linalg.svd(za, compute_uv=False) if za.shape[1] else np.array([])
            condition = (float(singular[0] / singular[-1])
                         if singular.size and singular[-1] > singular[0] * np.finfo(float).eps else None)
            corr = za.T @ za / len(z) if za.shape[1] else np.empty((0, 0))
            names = [n for n, keep in zip(self.feature_names, active) if keep]
            pairs = [{'left': names[i], 'right': names[j], 'correlation': float(corr[i, j])}
                     for i in range(len(names)) for j in range(i + 1, len(names)) if abs(corr[i, j]) >= .9]
            sink({'event': 'FIT', 'series_id': history.series_id, 'as_of': str(history.as_of),
                  'preprocessing_version': PREPROCESSING_VERSION, 'samples': len(y),
                  'feature_names': self.feature_names, 'feature_count': len(self.feature_names),
                  'features': {n: {'missing_count': int(self.training_missing_counts_[i]),
                                   'missing_rate': float(self.training_missing_counts_[i] / len(y)),
                                   'all_missing': bool(self.all_missing_[i]),
                                   'fill_value': float(self.fill_values_[i]),
                                   'scaler_mean': float(scaler.mean_[i]), 'scaler_scale': float(scaler.scale_[i]),
                                   'coefficient_standardized': float(ridge.coef_[i]),
                                   'coefficient_raw': float(ridge.coef_[i] / scaler.scale_[i])}
                               for i, n in enumerate(self.feature_names)},
                  'intercept_standardized': float(ridge.intercept_),
                  'condition_number_active_standardized': condition,
                  'condition_singular_or_empty': condition is None, 'high_correlation_pairs': pairs})

    def predict(self, inputs) -> list[float | None]:
        import numpy as np
        from tools import standard
        if self.model is None:
            raise RuntimeError('Model must be fitted first')
        if self._names(inputs.feature_names) != self.feature_names:
            raise ValueError('Feature names and order do not match training')
        if sorted(inputs.features) != list(standard.HORIZONS):
            raise ValueError('Expected horizons 1 through 7')
        X = self._matrix([inputs.features[h] for h in standard.HORIZONS], len(standard.HORIZONS))
        values = self.model.predict(self._transform(X))
        sink = AUDIT_SINK.get()
        if sink is not None:
            sink({'event': 'PREDICT', 'series_id': inputs.series_id, 'origin': str(inputs.origin),
                  'missing_counts': {n: int(np.isnan(X[:, i]).sum()) for i, n in enumerate(self.feature_names)},
                  'all_missing_training_columns_frozen_counts': {
                      n: int(np.isfinite(X[:, i]).sum()) for i, n in enumerate(self.feature_names)
                      if self.all_missing_[i]}})
        return [float(v) for v in values]
