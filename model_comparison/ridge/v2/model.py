"""Common pooled interface; no data access or file writes inside the estimator."""
from contextvars import ContextVar
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from model_comparison.v2.models import relative

VERSION = 'ridge-v2.1'
AUDIT_SINK = ContextVar('ridge_v2_audit', default=None)


class PooledRidgeV2:
    def __init__(self, alpha=10, solver='lsqr', strategy='direct_per_horizon'):
        if isinstance(alpha, bool) or not np.isfinite(alpha) or alpha < 0:
            raise ValueError('alpha must be finite and nonnegative')
        if solver != 'lsqr' or strategy != 'direct_per_horizon':
            raise ValueError('Only lsqr/direct_per_horizon are supported')
        self.alpha, self.solver, self.strategy = float(alpha), solver, strategy
        self.models = {}
        self.fitted_ = False
        self.diagnostics_ = []
        self.names, self.keep = [], []

    @staticmethod
    def _emit(event):
        sink = AUDIT_SINK.get()
        if sink is not None:
            sink(event)

    def _inputs(self, features, horizons, names):
        x = np.array(features, dtype=np.float64, copy=True)
        h = np.asarray(horizons)
        if x.ndim != 2 or x.shape[1] != len(names) or not len(x):
            raise ValueError('Invalid feature matrix shape')
        if h.ndim != 1 or len(h) != len(x) or not np.isin(h, range(1, 8)).all():
            raise ValueError('Expected aligned horizons 1 through 7')
        if np.isinf(x).any():
            raise ValueError('Feature infinity is not missingness')
        current = x[:, names.index('current')]
        if not np.isfinite(current).all() or (current <= 0).any():
            raise ValueError('Current prices must be finite and positive')
        if not np.array_equal(x[:, names.index('horizon')], h):
            raise ValueError('Horizon feature and horizons disagree')
        x, current = relative(x, names)
        if np.isinf(x).any():
            raise ValueError('Relative feature overflow')
        return x, current, h.astype(int)

    @staticmethod
    def _clean(x, state):
        clean = np.where(np.isnan(x), state['median'], x)
        clean[:, state['all_missing']] = 0.0
        return clean

    def fit(self, features, targets, horizons, feature_names, seed=42):
        # Invalidate *before* validating: a failed refit cannot expose old models.
        self.models, self.fitted_ = {}, False
        self.diagnostics_ = []
        self.names, self.keep = [], []
        try:
            names = list(feature_names)
            if (not names or any(not isinstance(n, str) or not n for n in names)
                    or len(set(names)) != len(names) or not {'current', 'horizon'} <= set(names)):
                raise ValueError('Unique feature names including current/horizon required')
            if isinstance(seed, bool) or not isinstance(seed, (int, np.integer)) or seed < 0:
                raise ValueError('seed must be a nonnegative integer')
            x, current, h = self._inputs(features, horizons, names)
            if set(h) != set(range(1, 8)):
                raise ValueError('Training must contain all 7 horizons')
            y = np.asarray(targets, dtype=float)
            if y.ndim != 1 or len(y) != len(x) or not np.isfinite(y).all() or (y <= 0).any():
                raise ValueError('Target prices must be aligned, finite and positive')
            with np.errstate(over='ignore', invalid='ignore', divide='ignore'):
                y = y / current - 1
            if not np.isfinite(y).all():
                raise ValueError('Relative target overflow')
            keep = [i for i, n in enumerate(names) if n != 'horizon']
            kept_names = [names[i] for i in keep]
            models, diagnostics = {}, []
            for g in range(1, 8):
                train = x[h == g][:, keep]
                missing = np.isnan(train)
                empty = missing.all(axis=0)
                median = np.array([0. if empty[j] else np.median(train[~missing[:, j], j])
                                   for j in range(train.shape[1])])
                state = {'median': median, 'all_missing': empty}
                clean = self._clean(train, state)
                scaler = StandardScaler()
                z = scaler.fit_transform(clean)
                ridge = Ridge(alpha=self.alpha, solver=self.solver, random_state=int(seed))
                ridge.fit(z, y[h == g])
                if not all(np.isfinite(a).all() for a in (scaler.mean_, scaler.scale_, ridge.coef_)):
                    raise ValueError('Nonfinite fitted parameters')
                if not np.isfinite(ridge.intercept_):
                    raise ValueError('Nonfinite intercept')
                state.update(scaler=scaler, ridge=ridge)
                models[g] = state
                raw_coef = ridge.coef_ / scaler.scale_
                diagnostics.append({'horizon': g, 'samples': len(train), 'features': {
                    name: {'missing_count': int(missing[:, j].sum()),
                           'missing_rate': float(missing[:, j].mean()), 'all_missing': bool(empty[j]),
                           'median': float(median[j]), 'mean': float(scaler.mean_[j]),
                           'scale': float(scaler.scale_[j]), 'variance': float(scaler.var_[j]),
                           'coefficient': float(ridge.coef_[j]), 'absolute_coefficient': float(abs(ridge.coef_[j])),
                           'coefficient_relative_units': float(raw_coef[j]),
                           'direction': 'positive' if ridge.coef_[j] > 0 else 'negative' if ridge.coef_[j] < 0 else 'zero'}
                    for j, name in enumerate(kept_names)}, 'intercept': float(ridge.intercept_),
                    'intercept_relative_units': float(ridge.intercept_ - raw_coef @ scaler.mean_)})
            self._emit({'event': 'FIT', 'version': VERSION, 'samples': len(y),
                        'input_feature_count': len(names), 'model_feature_count': len(keep),
                        'horizons': diagnostics,
                        'interpretation': 'Conditional associations in relative/log features; correlated predictors share coefficients. No SVD computed.'})
            self.names, self.keep, self.models = names, keep, models
            self.fitted_ = True
            self.diagnostics_ = diagnostics
        except BaseException as error:
            self.models, self.fitted_ = {}, False
            self.diagnostics_ = []
            self.names, self.keep = [], []
            self._emit({'event': 'FIT_FAILED', 'error_type': type(error).__name__, 'message': str(error)})
            raise
        return self

    def predict(self, features, horizons):
        if not self.fitted_:
            raise RuntimeError('Model is not fitted')
        try:
            x, current, h = self._inputs(features, horizons, self.names)
            out = np.full(len(h), np.nan)
            for g, state in self.models.items():
                rows = h == g
                if rows.any():
                    clean = self._clean(x[rows][:, self.keep], state)
                    with np.errstate(over='ignore', invalid='ignore'):
                        out[rows] = current[rows] * (1 + state['ridge'].predict(state['scaler'].transform(clean)))
            bad = ~np.isfinite(out) | (out <= 0)
            if bad.any():
                self._emit({'event': 'INVALID_PREDICTION', 'count': int(bad.sum()), 'horizons': h[bad].tolist()})
                out[bad] = np.nan
            return out
        except Exception as error:
            self._emit({'event': 'PREDICT_FAILED', 'error_type': type(error).__name__, 'message': str(error)})
            raise

    def importance(self):
        if not self.fitted_:
            return {}
        # Standardized relative-target coefficient magnitude, not tree gain.
        values = np.mean([np.abs(s['ridge'].coef_) for s in self.models.values()], axis=0)
        return dict(zip((self.names[j] for j in self.keep), map(float, values)))
