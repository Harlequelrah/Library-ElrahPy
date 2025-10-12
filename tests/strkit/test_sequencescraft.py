import pytest
from elrahpy.strkit.sequencescraft import (
    count_letters,
    get_all_indexes,
    remove_all_occurrences,
    separate_case,
)


def test_should_return_all_indexes():
    seq = "Sequence"
    el = "e"
    expected_value = [1, 4, 7]
    assert get_all_indexes(seq=seq, element=el) == expected_value


def test_should_remove_all_occurrences():
    seq = "Sequence"
    el = "e"
    expected_value = "Squnc"
    assert remove_all_occurrences(seq=seq, element=el) == expected_value


def test_should_count_letters():
    txt = "Sirops"
    expected_value_1 = {"S": 1, "i": 1, "o": 1, "p": 1, "r": 1, "s": 1}
    expected_value_2 = {"i": 1, "o": 1, "p": 1, "r": 1, "s": 2}
    assert count_letters(txt=txt, sensitive=True) == expected_value_1
    assert count_letters(txt=txt, sensitive=False) == expected_value_2


def test_should_separate_case():
    txt = "Hello"
    expected_value = {
        "lowercase": {"e": 1, "l": 2, "o": 1},
        "uppercase": {"H": 1},
    }
    assert separate_case(txt=txt) == expected_value
