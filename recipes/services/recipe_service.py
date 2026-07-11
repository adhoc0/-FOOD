from django.db import transaction

from recipes.models import Recipe, Status


class RecipeService:
    """Business logic for recipes."""

    @staticmethod
    @transaction.atomic
    def create(*, author, **data) -> Recipe:
        recipe = Recipe.objects.create(
            author=author,
            status=Status.DRAFT,
            **data,
        )

        return recipe

    @staticmethod
    @transaction.atomic
    def publish(recipe: Recipe) -> Recipe:
        recipe.status = Status.PUBLISHED

        if recipe.published_at is None:
            from django.utils import timezone

            recipe.published_at = timezone.now()

        recipe.save(
            update_fields=[
                "status",
                "published_at",
            ],
        )

        return recipe

    @staticmethod
    @transaction.atomic
    def archive(recipe: Recipe) -> Recipe:
        recipe.status = Status.ARCHIVED

        recipe.save(
            update_fields=[
                "status",
            ],
        )

        return recipe

    @staticmethod
    @transaction.atomic
    def increase_view_count(recipe: Recipe):
        recipe.view_count += 1

        recipe.save(
            update_fields=[
                "view_count",
            ],
        )

    @staticmethod
    @transaction.atomic
    def update_favorite_count(recipe: Recipe):
        recipe.favorite_count = recipe.favorites.count()

        recipe.save(
            update_fields=[
                "favorite_count",
            ],
        )