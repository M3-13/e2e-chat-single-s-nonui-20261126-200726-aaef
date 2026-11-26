"""Reverse the order of the words in a text."""


def reverse_words(text: str) -> str:
    """Return ``text`` with its words in reverse order, joined by single spaces.

    Raises TypeError if ``text`` is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return " ".join(reversed(text.split()))
