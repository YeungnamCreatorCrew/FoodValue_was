"""지표 공통: 일 가격 → 주 평균. 순수 함수."""
import pandas as pd

from app.core import constants as C


def weekly_mean(prices: pd.Series, min_obs: int = C.LEAD_MIN_WEEK_OBS) -> pd.Series:
    """일 가격(DatetimeIndex) → ISO 주(월~일) 평균, 라벨은 그 주의 일요일. 관측이 min_obs 미만인 주와 중간의 빈 주는 NaN."""
    prices = prices.sort_index()
    grouped = prices.resample('W')
    mean = grouped.mean().where(grouped.count() >= min_obs)
    return mean.reindex(pd.date_range(mean.index.min(), mean.index.max(), freq='W'))
