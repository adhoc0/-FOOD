from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _


class Difficulty(models.TextChoices):
    """Recipe difficulty choices."""

    EASY = "easy", _("Easy")
    MEDIUM = "medium", _("Medium")
    HARD = "hard", _("Hard")


class Status(models.TextChoices):
    """Recipe publication status."""

    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")
    ARCHIVED = "archived", _("Archived")


class Unit(models.TextChoices):
    """Recipe ingredient units."""

    GRAM = "g", _("Gram")
    KILOGRAM = "kg", _("Kilogram")
    MILLILITER = "ml", _("Milliliter")
    LITER = "l", _("Liter")
    TEASPOON = "tsp", _("Tea Spoon")
    TABLESPOON = "tbsp", _("Table Spoon")
    CUP = "cup", _("Cup")
    PIECE = "piece", _("Piece")
    PINCH = "pinch", _("Pinch")
    OPTIONAL = "optional", _("Optional")
