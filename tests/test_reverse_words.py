import pytest

from textutils.reverse_words import reverse_words


def test_reverses_and_collapses_whitespace():
    assert reverse_words("the quick  brown fox") == "fox brown quick the"


def test_empty():
    assert reverse_words("") == ""


def test_surrounding_whitespace():
    assert reverse_words("  one  ") == "one"


def test_any_whitespace():
    assert reverse_words("a\tb\nc") == "c b a"


@pytest.mark.parametrize("bad", [None, 42])
def test_type_error(bad):
    with pytest.raises(TypeError):
        reverse_words(bad)
