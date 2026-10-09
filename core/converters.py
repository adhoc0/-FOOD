from __future__ import annotations


class UnicodeSlugConverter:
    """ASCII dışındaki mevcut slug değerlerini de güvenle çözer."""

    regex = r"[-\w]+"

    def to_python(self, value: str) -> str:
        return value

    def to_url(self, value: str) -> str:
        return value
