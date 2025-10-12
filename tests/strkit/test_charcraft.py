import pytest
from elrahpy.strkit.charscraft import (
    check_char_case,
    count_vowels,
    generate_uuid_code,
    is_vowel,
    ispalindrome,
)


@pytest.mark.parametrize(
    "vowel,expected_value", [("a", True), ("ò", True), ("c", False), ("d", False)]
)
def test_should_check_vowel(vowel: str, expected_value: bool):
    assert is_vowel(vowel) == expected_value


def test_should_count_vowels():
    sentence = "Hi I am John"
    expected_value = 4
    assert count_vowels(seq=sentence) == expected_value


@pytest.mark.parametrize("char,expected_value", [("a", -1), ("B", 1), ("-", 0)])
def test_should_check_case(char, expected_value):
    assert check_char_case(char) == expected_value


def test_should_generate_uuid_code():
    prefix = "MX"
    length = 5
    uuid = generate_uuid_code(prefix=prefix, length=length)
    assert len(uuid) == length
    assert uuid.startswith(prefix)


@pytest.mark.parametrize(
    "word,expected_value",
    [("level", True), ("radar", True), ("palindrome", False), ("ramer", False)],
)
def test_should_check_ispalindrome(word: str, expected_value: bool):
    assert ispalindrome(word=word) == expected_value
