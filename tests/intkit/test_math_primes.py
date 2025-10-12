import pytest
from elrahpy.intkit.math_primes import (
    count_dividers,
    factor_products,
    is_prime,
    list_dividers,
)


@pytest.mark.parametrize(
    "number,expected_value", [(1, False), (2, True), (6, False), (17, True)]
)
def test_should_check_is_prime(number, expected_value):
    assert is_prime(number) == expected_value


def test_should_return_factor_products():
    number = 18
    expected_value = {2: 1, 3: 2}
    assert factor_products(number) == expected_value


def test_should_return_dividers_count():
    number = 18
    expected_value = 6
    assert count_dividers(number=number) == expected_value


def test_should_list_dividers():
    number = 18
    expected_value = [1, 2, 3, 6, 9, 18]
    assert list_dividers(number) == expected_value
