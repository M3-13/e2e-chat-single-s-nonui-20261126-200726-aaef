import pytest

from textutils.slugify import slugify


def test_basic() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_accents_and_whitespace() -> None:
    assert slugify("  Crème   Brûlée  ") == "creme-brulee"


@pytest.mark.parametrize("text", ["", "!!!", "  ", "---"])
def test_empty_or_special_only(text: str) -> None:
    assert slugify(text) == ""


def test_underscores_and_runs() -> None:
    assert slugify("a_b -- c") == "a-b-c"


@pytest.mark.parametrize("bad", [None, 42])
def test_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        slugify(bad)
