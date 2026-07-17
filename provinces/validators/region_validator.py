import re

from django.core.exceptions import ValidationError

HEX_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")


def validate_map_color(value: str):
    """
    HEX renk doğrulaması.
    """
    if not HEX_PATTERN.match(value):
        raise ValidationError("Geçerli bir HEX renk kodu giriniz.")
