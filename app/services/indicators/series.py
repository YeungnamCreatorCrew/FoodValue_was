"""지표 공통: 일 가격 → 주 평균. 순수 함수."""
import pandas as pd

from app.core import constants as C


def weekly_mean(prices: pd.Series, min_obs: int = C.LEAD_MIN_WEEK_OBS) -> pd.Series:
    """일 가격(DatetimeIndex) → ISO 주(월~일) 평균, 라벨은 그 주의 일요일. 관측이 min_obs 미만인 주와 중간의 빈 주는 NaN."""
    prices = prices.sort_index()
    grouped = prices.resample('W')
    mean = grouped.mean().where(grouped.count() >= min_obs)
    return mean.reindex(pd.date_range(mean.index.min(), mean.index.max(), freq='W'))


def week_flags(index: pd.DatetimeIndex, dates) -> pd.Series:
    """주 평균 index(일요일 라벨) 위에, dates 중 하나라도 그 주(월~일)에 있으면 True. 작형 전환일 표시용."""
    flags = pd.Series(False, index=index)
    for day in dates or ():
        label = pd.Timestamp(day).normalize() + pd.Timedelta(days=6 - pd.Timestamp(day).weekday())
        if label in flags.index:
            flags[label] = True
    return flags


def crosses_back(flags: pd.Series, span: int) -> pd.Series:
    """t주와 그 span주 전 사이(양 끝 포함)에 표시가 있으면 True. t-span주 → t주 변화율이 서로 다른 작형을 비교하는 경우."""
    return flags.astype(int).rolling(span + 1, min_periods=1).sum() > 0


def crosses_forward(flags: pd.Series, span: int) -> pd.Series:
    """t주와 그 span주 뒤 사이에 표시가 있으면 True. t주 → t+span주 변화율용."""
    return crosses_back(flags.iloc[::-1], span).iloc[::-1]
