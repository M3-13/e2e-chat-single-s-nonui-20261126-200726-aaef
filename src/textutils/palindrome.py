"""Check whether a text reads the same in both directions."""


def is_palindrome(text: str) -> bool:
    """Return ``True`` if ``text`` is a palindrome, ignoring case and punctuation.

    Only alphanumeric characters are compared. Raises ``TypeError`` for non-str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]
