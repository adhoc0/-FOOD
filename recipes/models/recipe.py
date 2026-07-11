from __future__ import annotations

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from provinces.models import Province

from recipes.managers.recipe_manager import RecipeManager

from .category import Category


class Difficulty(models.TextChoices):
    EASY = "easy", _("Easy")
    MEDIUM = "medium", _("Medium")
    HARD = "hard", _("Hard")


class Status(models.TextChoices):
    DRAFT = "draft", _("Draft")
    PUBLISHED = "published", _("Published")
    ARCHIVED = "archived", _("Archived")


class Recipe(models.Model):
    """Recipe model."""


    title = models.CharField(
        _("Title"),
        max_length=255,
    )

    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        unique=True,
        db_index=True,
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

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    is_featured = models.BooleanField(
        _("Featured"),
        default=False,
        db_index=True,
    )

    is_active = models.BooleanField(
        _("Active"),
        default=True,
        db_index=True,
    )

    view_count = models.PositiveIntegerField(
        _("View Count"),
        default=0,
    )

    favorite_count = models.PositiveIntegerField(
        _("Favorite Count"),
        default=0,
    )

    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
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

    objects = RecipeManager()

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
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["status"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["province"]),
            models.Index(fields=["category"]),
        ]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse(
            "recipes:detail",
            kwargs={"slug": self.slug},
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.title,
                allow_unicode=True,
            )

        super().save(*args, **kwargs)