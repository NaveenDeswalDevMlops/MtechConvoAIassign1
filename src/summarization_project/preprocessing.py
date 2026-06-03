"""Cleaning and context-window truncation utilities."""

from __future__ import annotations

import html
import re
import unicodedata

_HTML_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")
_QUOTE_TRANSLATION = str.maketrans(
    {
        "“": '"',
        "”": '"',
        "„": '"',
        "‟": '"',
        "‘": "'",
        "’": "'",
        "‚": "'",
        "‛": "'",
        "—": "-",
        "–": "-",
        "…": "...",
    }
)


def clean_text(text: str) -> str:
    """Remove HTML, normalize unicode/quotes, convert to ASCII, and collapse spaces."""
    if not isinstance(text, str):
        return ""
    text = html.unescape(text)
    text = _HTML_RE.sub(" ", text)
    text = text.translate(_QUOTE_TRANSLATION)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.replace("\x00", " ")
    text = _WHITESPACE_RE.sub(" ", text)
    return text.strip()


def truncate_context_window(text: str, max_tokens: int = 512) -> str:
    """Preserve the beginning and ending tokens when a document is too long.

    Transformers have quadratic self-attention memory in sequence length.  The
    first part of a news article usually contains the lead, while the ending can
    contain concluding facts; keeping both is more informative than a simple
    head-only cut.
    """
    tokens = text.split()
    if len(tokens) <= max_tokens:
        return text
    first_count = max_tokens // 2
    last_count = max_tokens - first_count
    return " ".join(tokens[:first_count] + tokens[-last_count:])


def clean_and_truncate(text: str, max_tokens: int = 512) -> str:
    """Apply assignment-required cleaning followed by context truncation."""
    return truncate_context_window(clean_text(text), max_tokens=max_tokens)
