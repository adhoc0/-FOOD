from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from provinces.models import Province
from recipes.choices import Difficulty, Status
from recipes.querysets.recipe_queryset import RecipeManager

from .category import Category

if TYPE_CHECKING:
    from .recipe_image import RecipeImage


class Recipe(models.Model):
    """Recipe model."""

    objects: ClassVar[RecipeManager] = RecipeManager()

    title = models.CharField(
        _("Title"),
        max_length=255,
    )

    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        unique=True,
    )

    province = models.ForeignKey(
        Province,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    summary = models.TextField(
        _("Summary"),
    )

    instructions = models.TextField(
        _("Instructions"),
    )

    preparation_time = models.PositiveSmallIntegerField(
        _("Preparation Time"),
    )

    cooking_time = models.PositiveSmallIntegerField(
        _("Cooking Time"),
    )

    servings = models.PositiveSmallIntegerField(
        _("Servings"),
        default=1,
    )

    difficulty = models.CharField(
        _("Difficulty"),
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
    )

    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    is_featured = models.BooleanField(
        _("Featured"),
        default=False,
    )

    is_active = models.BooleanField(
        _("Active"),
        default=True,
    )

    view_count = models.PositiveIntegerField(
        _("View Count"),
        default=0,
    )

    favorite_count = models.PositiveIntegerField(
        _("Favorite Count"),
        default=0,
    )

    rating_count = models.PositiveIntegerField(
        _("Rating Count"),
        default=0,
    )

    average_rating = models.DecimalField(
        _("Average Rating"),
        max_digits=3,
        decimal_places=1,
        default=0,
    )

    comment_count = models.PositiveIntegerField(
        _("Comment Count"),
        default=0,
    )

    meta_title = models.CharField(
        _("Meta Title"),
        max_length=255,
        blank=True,
    )

    meta_description = models.CharField(
        _("Meta Description"),
        max_length=320,
        blank=True,
    )

    youtube_url = models.URLField(
        _("YouTube URL"),
        blank=True,
    )

    source_url = models.URLField(
        _("Source URL"),
        blank=True,
    )

    published_at = models.DateTimeField(
        _("Published At"),
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

        ordering = [
            "-published_at",
            "-created_at",
        ]

        get_latest_by = "published_at"

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["status"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["province"]),
            models.Index(fields=["category"]),
            models.Index(fields=["published_at"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["view_count"]),
            models.Index(fields=["favorite_count"]),
            models.Index(fields=["rating_count"]),
            models.Index(fields=["average_rating"]),
        ]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse(
            "recipes:recipe_detail",
            kwargs={
                "slug": self.slug,
            },
        )

    @property
    def cover_image(self) -> RecipeImage | None:
        """Önceden yüklenmiş görseller arasından kapak görselini döndürür."""

        return next(
            (
                image
                for image in self.recipe_images.all()
                if image.is_cover
            ),
            None,
        )

    @property
    def total_time(self) -> int:
        """Return total preparation time."""

        return self.preparation_time + self.cooking_time

    @property
    def is_published(self) -> bool:
        """Return whether the recipe is published."""

        return self.status == Status.PUBLISHED
