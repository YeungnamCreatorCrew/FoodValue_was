from datetime import date, timedelta

from app.services import merged_series_service
from tools import loader


def test_merged_prices_matches_experiment_merge_rule():
    days = [date(2026, 3, 2) + timedelta(days=i) for i in range(10)]
    obs = [(d, '06', 3000 + i, 11) for i, d in enumerate(days)]
    obs += [(d, '01', 2000 + i, 12) for i, d in enumerate(days[3:], 3)]
    got = merged_series_service.merged_prices(obs, days)
    expected = {r.price_date: r.price for r in loader.merge_kinds(obs, days)}
    assert got == expected and len(got) == len(days)


def test_merged_prices_ignores_non_survey_days():
    obs = [(date(2026, 1, 5), '06', 3000, 1), (date(2026, 1, 4), '06', 9999, 1)]
    assert merged_series_service.merged_prices(obs, [date(2026, 1, 5)]) == {date(2026, 1, 5): 3000}
