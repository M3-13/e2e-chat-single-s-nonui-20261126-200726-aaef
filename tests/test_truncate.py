import pytest

from textutils import truncate


def test_shortened_with_ellipsis():
    assert truncate("Hello World", 8) == "Hello..."


def test_short_text_unchanged():
    assert truncate("Hi", 8) == "Hi"
    assert truncate("Hello", 5) == "Hello"


def test_small_max_len_plain_cut():
    assert truncate("Hello World", 2) == "He"
    assert truncate("Hello World", 0) == ""
    assert len(truncate("Hello World", 3)) == 3


def test_negative_raises():
    with pytest.raises(ValueError):
        truncate("abc", -1)


@pytest.mark.parametrize("bad", [None, 42])
def test_non_str_raises(bad):
    with pytest.raises(TypeError):
        truncate(bad, 5)
