from datetime import datetime

import pytest
from elrahpy.utils import datekit


@pytest.mark.parametrize(
    "year,is_bisectile", [(2016, True), (2020, True), (2021, False), (2019, False)]
)
def test_should_return_is_bisectile(year, is_bisectile):
    assert datekit.is_bisectile(year) == is_bisectile


@pytest.mark.parametrize(
    "interval_type,expected_value",
    [("year", 0), ("M", 9), ("DAY", 282), (None, (282, 9, 0))],
)
def test_should_return_interval(interval_type, expected_value):
    interval = datekit.get_interval(
        start_date=datetime(year=2025, month=1, day=1),
        interval_type=interval_type,
        end_date=datetime(year=2025, month=10, day=10),
    )
    assert interval == expected_value
