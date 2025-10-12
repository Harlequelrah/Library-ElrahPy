import string
import uuid


def is_vowel(vowel: str):
    vowels = [
        "a",
        "e",
        "i",
        "o",
        "u",
        "y",
        "á",
        "é",
        "í",
        "ó",
        "ú",
        "ý",
        "à",
        "è",
        "ì",
        "ò",
        "ù",
        "â",
        "ê",
        "î",
        "ô",
        "û",
        "ä",
        "ë",
        "ï",
        "ö",
        "ü",
        "ÿ",
        "æ",
        "œ",
    ]
    return vowel.lower() in vowels


def count_vowels(seq):
    w = 0
    for v in seq:
        if is_vowel(v):
            w = w + 1
    return w


def check_char_case(char):
    if char in string.ascii_lowercase:
        return -1
    elif char in string.ascii_uppercase:
        return 1
    else:
        return 0


def generate_uuid_code(
    prefix: str | None = None,
    length: int | None = None,
):
    prefix = f"{prefix}-" if prefix else ""
    length = length - len(prefix) if length else 6
    return f"{prefix}{uuid.uuid4().hex[:length].upper()}"


def ispalindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]
