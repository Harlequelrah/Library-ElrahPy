from elrahpy.intkit.math_utils import fibonacci


def test_should_return_fibonacci():
    number = 5
    expected_value = [0, 1, 1, 2, 3]
    assert fibonacci(number) == expected_value

