import textutils
from textutils import is_palindrome, reverse_words, slugify, truncate, word_count


def test_public_names_import_and_are_callable() -> None:
    for func in (slugify, truncate, word_count, is_palindrome, reverse_words):
        assert callable(func)


def test_all_lists_the_five_names() -> None:
    assert set(textutils.__all__) == {
        "slugify",
        "truncate",
        "word_count",
        "is_palindrome",
        "reverse_words",
    }
