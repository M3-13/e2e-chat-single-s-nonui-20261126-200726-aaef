import pytest

from textutils.palindrome import is_palindrome


def test_sentence_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome() -> None:
    assert is_palindrome("Hello") is False


def test_empty_and_no_alnum() -> None:
    assert is_palindrome("") is True
    assert is_palindrome("!?,. ") is True


def test_single_char_and_case() -> None:
    assert is_palindrome("a") is True
    assert is_palindrome("Racecar") is True


@pytest.mark.parametrize("bad", [None, 42])
def test_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        is_palindrome(bad)
