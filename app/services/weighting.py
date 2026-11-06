"""외부변수 묶음별 가중치. 과거에 실제로 확인된 예측 오차만으로 학습한다.

가격만 쓴 모델(기준 예측) b와, 가격 + 묶음 k 특징을 쓴 전문가 모델 e_k의 '시작일 대비 변화율' 예측을 결합한다.

    결합 예측 = b + Σ_k w_k (e_k - b),   0 <= w_k <= 1

w_k는 '묶음 k의 전문가가 가격 모델을 고치는 만큼을 얼마나 믿을지'다. 0이면 무시, 1이면 그 수정을 그대로 받는다.
가중치는 다음 Ridge 제약 최소제곱(Granger-Ramanathan 결합의 변형)으로 정한다.

    Σ_i (r_i - Σ_k w_k d_ik)² + κ Σ_k w_k² Σ_i d_ik²     (r = 정답 - b, d_k = e_k - b)

- 7개 시점의 표본을 함께 쓰되 시점마다 r의 RMS로 나눠 정규화한다. 긴 시점의 큰 오차가 가중치를 독점하지 않고,
  시점별로 따로 추정할 때보다 표본이 7배라 가중치가 안정적이다.
- 0~1 상자 제약: 음수(전문가와 반대로 가기)나 1 초과(전문가보다 과장)를 막는다. 같은 정보를 가진 묶음이 둘이면
  최소제곱이 몫을 나눈다(정보가 겹치는 만큼 합이 1에 가까워진다).
- κ(규제 강도)는 묶음마다 자기 신호 크기에 비례해 걸린다(척도 무관). 후보 κ와 '가중치 0(가격만)' 중
  시간순 교차검증으로 고른다. 창을 시간순 4구간으로 나눠 앞 2구간 → 3번째, 앞 3구간 → 4번째를 평가한다.
  평가 구간 시작 전에 정답이 확인된 표본만 학습한다. 학습이 창의 절반 미만인 구간은 실제 사용(창 전체로 학습)과
  너무 달라 평가하지 않는다(합성 자료에서 이 구간이 과적합으로 실패해 공개 가중치가 0으로 꺼지는 일이 있었다).
- 채택 조건: 교차검증의 모든 평가 구간에서 가격만 쓴 경우보다 오차가 작고, 합계로도 MIN_GAIN 이상 줄어야 한다.
  아니면 모두 0이다. 이웃한 날·시점의 오차는 서로 겹쳐 표본 수만큼 독립이 아니므로, 한 구간의 우연한 개선이나
  서로 다르게 학습된 두 모델을 평균해서 생기는 분산 감소만으로 외부변수에 가중치가 붙지 않게 한다
  (합성 자료 실험: 잡음뿐인 묶음에 1% 기준·일관성 조건 없이 0.63이 붙었고, 이 조건에서는 0이 됐다).
- 표본이 MIN_SAMPLES 미만이면 모두 0이다. 쓸모를 입증하지 못한 외부변수는 예측을 바꾸지 않는다.
"""
from collections import defaultdict
from dataclasses import dataclass, field

import numpy as np

KAPPAS = (0.0, 0.1, 0.3, 1.0, 3.0)
MIN_SAMPLES = 150  # 7개 시점 합계. 시점당 약 20개(영업일 기준 한 달 남짓)
MIN_GAIN = .03  # 교차검증 제곱오차 합이 가격만 쓴 경우보다 3% 이상 줄어야 가중치를 준다
WINDOW_DAYS = 365  # 최근 1년의 실현 오차만 쓴다. 시장 관계가 바뀌면 오래된 오차는 빠진다.
BLOCKS = 4  # 교차검증: 창을 시간순 4구간으로 나눠 [1,2]→3, [1,2,3]→4를 평가한다(학습이 창의 절반 이상)
FIRST_TEST_BLOCK = 2
ITERATIONS = 300


@dataclass
class Weights:
    values: dict[str, float] = field(default_factory=dict)
    kappa: float | None = None  # None: 가격만(모든 가중치 0)
    samples: int = 0

    def combine(self, base, experts: dict[str, float]):
        return base + sum(self.values.get(name, 0.0) * (value - base) for name, value in experts.items())

    def as_dict(self):
        return {'weights': {k: round(v, 4) for k, v in self.values.items()}, 'kappa': self.kappa, 'samples': self.samples}


def solve(deltas: np.ndarray, residuals: np.ndarray, kappa: float):
    """0~1 상자 제약 Ridge 최소제곱. 가속 사영 경사법(FISTA). 변수가 묶음 수(최대 5)라 반복 비용이 작다."""
    gram = deltas.T @ deltas
    hessian = gram + kappa * np.diag(np.diag(gram))
    linear = deltas.T @ residuals
    w = np.zeros(deltas.shape[1])
    lipschitz = 2 * float(np.linalg.eigvalsh(hessian).max()) if len(gram) else 0.0
    if lipschitz <= 1e-15:
        return w
    momentum, previous, t = w.copy(), w.copy(), 1.0
    for _ in range(ITERATIONS):
        w = np.clip(momentum - 2 * (hessian @ momentum - linear) / lipschitz, 0.0, 1.0)
        t_next = (1 + (1 + 4 * t * t) ** .5) / 2
        momentum = w + (t - 1) / t_next * (w - previous)
        previous, t = w, t_next
    return w


def _loss(deltas, residuals, w):
    return float(((residuals - deltas @ w) ** 2).sum())


def _zero(names, samples):
    return Weights({name: 0.0 for name in names}, None, samples)


def choose(samples, names):
    """samples: [(시작 index, 정답 index, 시점, 정답 변화율, 기준 변화율, {묶음: 전문가 변화율})]."""
    if not samples or not names:
        return _zero(names, 0)
    newest = max(s[0] for s in samples)
    samples = sorted((s for s in samples if s[0] > newest - WINDOW_DAYS), key=lambda s: (s[0], s[2]))
    if len(samples) < MIN_SAMPLES:
        return _zero(names, len(samples))
    origins = np.array([s[0] for s in samples])
    targets = np.array([s[1] for s in samples])
    residuals = np.array([s[3] - s[4] for s in samples])
    deltas = np.array([[s[5][name] - s[4] for name in names] for s in samples])
    # 시점별 정규화: 시점마다 기준 예측 오차의 RMS로 나눈다.
    by_horizon = defaultdict(list)
    for index, s in enumerate(samples):
        by_horizon[s[2]].append(index)
    for rows in by_horizon.values():
        scale = float(np.sqrt(np.mean(residuals[rows] ** 2))) or 1.0
        residuals[rows] /= scale
        deltas[rows] /= scale
    # 앞쪽 구간으로 가중치를 학습해 다음 구간을 평가한다. 평가 구간 시작일에 아직 정답이 확인되지 않은
    # 학습 표본은 쓰지 않는다(실제 운영과 같은 정보만 사용).
    edges = np.linspace(0, len(samples), BLOCKS + 1).astype(int)
    scores = {kappa: [] for kappa in (None, *KAPPAS)}
    for block in range(FIRST_TEST_BLOCK, BLOCKS):
        test = np.arange(edges[block], edges[block + 1])
        train = np.arange(0, edges[block])
        train = train[targets[train] <= origins[test].min()]
        scores[None].append(_loss(deltas[test], residuals[test], np.zeros(len(names))))
        for kappa in KAPPAS:
            scores[kappa].append(_loss(deltas[test], residuals[test], solve(deltas[train], residuals[train], kappa)))
    base = scores[None]
    passing = [kappa for kappa in KAPPAS if base and sum(scores[kappa]) <= sum(base) * (1 - MIN_GAIN)
               and all(loss < reference for loss, reference in zip(scores[kappa], base))]
    if not passing:
        return _zero(names, len(samples))
    # 동률이면 더 보수적인(규제가 큰) 쪽을 고른다.
    best = min(passing, key=lambda kappa: (sum(scores[kappa]), -kappa))
    w = solve(deltas, residuals, best)
    return Weights({name: float(value) for name, value in zip(names, w)}, best, len(samples))
