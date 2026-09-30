"""Region doğrulayıcı testleri."""

import pytest
from django.core.exceptions import ValidationError

from provinces.validators import validate_map_color


@pytest.mark.parametrize("value", ["#2E7D32", "#abcdef", "#ABCDEF", "#000000"])
def test_accepts_six_digit_hex_colors(value):
    validate_map_color(value)


@pytest.mark.parametrize(
    "value",
    [
        "",
        "2E7D32",
        "#2E7D3",
        "#2E7D322",
        "#GGGGGG",
        "red",
        "#2E7D32\n",
    ],
)
def test_rejects_invalid_colors(value):
    with pytest.raises(ValidationError):
        validate_map_color(value)
