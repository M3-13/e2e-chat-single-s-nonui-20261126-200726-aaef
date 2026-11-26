import pytest

from textutils.word_count import word_count


def test_mixed_whitespace():
    assert word_count("one  two\tthree\nfour") == 4


def test_empty_and_blank():
    assert word_count("") == 0
    assert word_count("   ") == 0
    assert word_count(" \t\n ") == 0


def test_single_word_and_padding():
    assert word_count("hello") == 1
    assert word_count("  hello world  ") == 2


@pytest.mark.parametrize("value", [None, 42])
def test_type_error(value):
    with pytest.raises(TypeError):
        word_count(value)
