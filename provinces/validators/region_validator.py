import re

from django.core.exceptions import ValidationError

HEX_PATTERN = re.compile(r"#[0-9A-Fa-f]{6}")


def validate_map_color(value: str) -> None:
    """
    HEX renk doğrulaması.
    """
    # fullmatch: `$` satırsonundan önceki eşleşmeyi de kabul ettiği için kullanılmaz.
    if not HEX_PATTERN.fullmatch(value):
        raise ValidationError("Geçerli bir HEX renk kodu giriniz.")
