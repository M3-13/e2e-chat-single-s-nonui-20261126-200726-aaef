# textutils

`textutils` ist eine kleine, eigenständige Python-Bibliothek mit fünf einfachen String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Die Funktionen sind voneinander unabhängig, nutzen ausschließlich die Python-Standardbibliothek und haben keine Benutzeroberfläche und keine Datenspeicherung.

## Tech-Stack

- Python 3.10 oder neuer
- Nur Standardbibliothek (keine Laufzeit-Abhängigkeiten)
- Packaging über `pyproject.toml` (setuptools)
- Tests mit pytest, Linting mit ruff

## Installation

```bash
pip install -e .[dev]
```

Ohne die Entwickler-Extras (pytest, ruff) genügt `pip install .`.

## Verwendung

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

Alle Funktionen lösen einen `TypeError` aus, wenn das Text-Argument kein `str` ist (z. B. `None` oder `42`).

### `slugify(text: str) -> str`

Wandelt Text in einen URL-freundlichen Slug um: Kleinbuchstaben, Akzente entfernt, Wörter mit `-` verbunden, Sonderzeichen entfernt.

```python
slugify("Hello, World!")  # 'hello-world'
slugify("  Crème   Brûlée  ")  # 'creme-brulee'
```

### `truncate(text: str, max_len: int) -> str`

Kürzt Text auf höchstens `max_len` Zeichen und hängt bei Kürzung `...` an. Ein negatives `max_len` löst einen `ValueError` aus.

```python
truncate("Hello World", 8)  # 'Hello...'
truncate("Hello World", 2)  # 'He'
```

### `word_count(text: str) -> int`

Zählt die durch Leerraum getrennten Wörter.

```python
word_count("one  two\tthree\nfour")  # 4
```

### `is_palindrome(text: str) -> bool`

Prüft, ob ein Text vorwärts und rückwärts gleich gelesen wird – Groß-/Kleinschreibung und Satzzeichen werden ignoriert.

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("Hello")  # False
```

### `reverse_words(text: str) -> str`

Kehrt die Reihenfolge der Wörter um; überflüssiger Leerraum wird entfernt.

```python
reverse_words("the quick  brown fox")  # 'fox brown quick the'
```

## Tests und Linting

```bash
pytest
ruff check .
```

## Funktionen

- `slugify`, `truncate`, `word_count`, `is_palindrome`, `reverse_words`
- Keine Abhängigkeiten außerhalb der Standardbibliothek
- Jede Funktion ist ein eigenes Modul ohne Import der anderen
- Eigene Unit-Tests pro Funktion
