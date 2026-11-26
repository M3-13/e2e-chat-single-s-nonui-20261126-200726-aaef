"""Convert text into a URL-friendly slug."""

import re
import unicodedata

_SEPARATOR_RUN = re.compile(r"[\W_]+")


def slugify(text: str) -> str:
    """Return a lowercase, hyphen-separated slug for ``text``.

    Accents are removed via Unicode NFKD, each run of non-alphanumeric
    characters becomes a single hyphen, and edge hyphens are stripped.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    decomposed = unicodedata.normalize("NFKD", text.lower())
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _SEPARATOR_RUN.sub("-", stripped).strip("-")
