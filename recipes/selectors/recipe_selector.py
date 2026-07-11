from django.db.models import Q

from recipes.models import Recipe
from recipes.models.recipe import Status


class RecipeSelector:
    """Read-only queries for recipes."""

    @staticmethod
    def get_queryset():
        return (
            Recipe.objects.filter(
                status=Status.PUBLISHED,
                is_active=True,
            )
            .select_related(
                "province",
                "category",
                "author",
            )
            .prefetch_related(
                "images",
                "ingredients",
                "tags",
            )
        )

    @staticmethod
    def get_all():
        return (
            RecipeSelector.get_queryset()
            .order_by(
                "-published_at",
                "-created_at",
            )
        )

    @staticmethod
    def get_by_slug(slug: str):
        return (
            RecipeSelector.get_queryset()
            .filter(slug=slug)
            .first()
        )

    @staticmethod
    def get_featured(limit: int = 8):
        return (
            RecipeSelector.get_queryset()
            .filter(
                is_featured=True,
            )
            .order_by(
                "-published_at",
            )[:limit]
        )

    @staticmethod
    def get_latest(limit: int = 12):
        return (
            RecipeSelector.get_queryset()
            .order_by(
                "-published_at",
                "-created_at",
            )[:limit]
        )

    @staticmethod
    def get_by_province(province):
        return (
            RecipeSelector.get_queryset()
            .filter(
                province=province,
            )
            .order_by(
                "title",
            )
        )

    @staticmethod
    def get_by_category(category):
        return (
            RecipeSelector.get_queryset()
            .filter(
                category=category,
            )
            .order_by(
                "title",
            )
        )

    @staticmethod
    def search(query: str):
        return (
            RecipeSelector.get_queryset()
            .filter(
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(province__name__icontains=query)
                | Q(category__name__icontains=query)
            )
            .distinct()
        )

    @staticmethod
    def get_count() -> int:
        return RecipeSelector.get_queryset().count()