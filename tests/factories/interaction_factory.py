"""
Test factories — Interaction models.

factory-boy ile Favorite, Rating, Comment test verileri.
"""

import factory

from interactions.models import Comment, Favorite, Rating

from .recipe_factory import RecipeFactory
from .user_factory import UserFactory


class FavoriteFactory(factory.django.DjangoModelFactory):
    """Favori factory."""

    class Meta:
        model = Favorite

    user = factory.SubFactory(UserFactory)
    recipe = factory.SubFactory(RecipeFactory)


class RatingFactory(factory.django.DjangoModelFactory):
    """Puanlama factory."""

    class Meta:
        model = Rating

    user = factory.SubFactory(UserFactory)
    recipe = factory.SubFactory(RecipeFactory)
    score = 4


class CommentFactory(factory.django.DjangoModelFactory):
    """Yorum factory."""

    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    recipe = factory.SubFactory(RecipeFactory)
    content = factory.Faker("paragraph", locale="tr_TR")
    is_approved = False
