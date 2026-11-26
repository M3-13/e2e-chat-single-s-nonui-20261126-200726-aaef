"""Shorten text to a maximum length."""

_ELLIPSIS = "..."


def truncate(text: str, max_len: int) -> str:
    """Return ``text`` shortened to at most ``max_len`` characters.

    Longer text is cut so the result, including a trailing ``...``, is exactly
    ``max_len`` characters; for ``max_len < 3`` it is a plain cut.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if max_len < 0:
        raise ValueError("max_len must not be negative")
    if len(text) <= max_len:
        return text
    if max_len < len(_ELLIPSIS):
        return text[:max_len]
    return text[: max_len - len(_ELLIPSIS)] + _ELLIPSIS
