import pytest
from elrahpy.cryptokit.cesar import crypt_cesar, search_cesar, verify_cesar, z_cesar


def test_should_crypt_word():
    word = "Bonjour"
    k = 3
    expected_value = "Erqmrxu"
    assert crypt_cesar(word=word, operation=1, k=k) == expected_value


def test_should_decrypt_word():
    word = "Erqmrxu"
    k = 3
    expected_value = "Bonjour"
    assert crypt_cesar(word=word, operation=-1, k=k) == expected_value


def test_should_verify_cesar():
    word = "Bonjour"
    k = 3
    expected_value = "Erqmrxu"
    assert verify_cesar(word=word, crypted_word=expected_value, k=k)


def test_should_contains_word_searched():
    word = "Bonjour"
    values = search_cesar("Erqmrxu")
    assert word in list(values)


def test_should_contains_text_searched():
    txt = "Bonjour , vous tous"
    values = z_cesar(txt)
    assert txt in list(values.values())
