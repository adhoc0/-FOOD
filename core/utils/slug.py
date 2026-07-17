from __future__ import annotations

from django.utils.text import slugify

TURKISH_SLUG_TRANSLATION = str.maketrans(
    {
        "Ç": "C",
        "ç": "c",
        "Ğ": "G",
        "ğ": "g",
        "İ": "I",
        "ı": "i",
        "Ö": "O",
        "ö": "o",
        "Ş": "S",
        "ş": "s",
        "Ü": "U",
        "ü": "u",
    },
)


def generate_slug(value: str) -> str:
    """Türkçe karakterleri ASCII'ye dönüştürerek SEO uyumlu slug üretir."""

    return slugify(
        value.strip().translate(TURKISH_SLUG_TRANSLATION),
        allow_unicode=False,
    )
