"""
Test factories — Recipe and related models.

factory-boy ile Recipe, RecipeImage, RecipeIngredient, Ingredient, Tag test verileri.
"""

import factory
from django.utils import timezone

from core.utils.slug import generate_slug
from recipes.choices import Difficulty, Status
from recipes.models import (
    Ingredient,
    Recipe,
    RecipeImage,
    RecipeIngredient,
    Tag,
)

from .category_factory import CategoryFactory
from .province_factory import ProvinceFactory
from .user_factory import UserFactory


class IngredientFactory(factory.django.DjangoModelFactory):
    """Malzeme factory."""

    class Meta:
        model = Ingredient

    name = factory.Sequence(lambda n: f"Malzeme {n}")
    slug = factory.LazyAttribute(lambda obj: f"malzeme-{obj.name.split()[-1].lower()}")
    is_active = True


class TagFactory(factory.django.DjangoModelFactory):
    """Etiket factory."""

    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f"Etiket {n}")
    slug = factory.LazyAttribute(lambda obj: f"etiket-{obj.name.split()[-1].lower()}")
    is_active = True


class RecipeFactory(factory.django.DjangoModelFactory):
    """Tarif factory — tüm zorunlu ilişkilerle."""

    class Meta:
        model = Recipe

    title = factory.Sequence(lambda n: f"Test Tarifi {n}")
    slug = factory.LazyAttributeSequence(
        lambda obj, sequence: generate_slug(
            f"test-tarifi-{obj.title}-{sequence}",
        ),
    )
    province = factory.SubFactory(ProvinceFactory)
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    summary = factory.Faker("text", max_nb_chars=200, locale="tr_TR")
    instructions = factory.Faker("text", max_nb_chars=500, locale="tr_TR")
    preparation_time = 15
    cooking_time = 30
    servings = 4
    difficulty = Difficulty.MEDIUM
    status = Status.PUBLISHED
    is_featured = False
    is_active = True
    published_at = factory.LazyFunction(timezone.now)


class DraftRecipeFactory(RecipeFactory):
    """Taslak tarif factory."""

    status = Status.DRAFT
    published_at = None


class RecipeImageFactory(factory.django.DjangoModelFactory):
    """Tarif görseli factory."""

    class Meta:
        model = RecipeImage

    recipe = factory.SubFactory(RecipeFactory)
    image = factory.django.ImageField(width=512, height=512, color="blue")
    alt_text = factory.LazyAttribute(lambda obj: f"{obj.recipe.title} görseli")
    is_cover = False
    sort_order = factory.Sequence(lambda n: n)


class RecipeIngredientFactory(factory.django.DjangoModelFactory):
    """Tarif malzemesi factory."""

    class Meta:
        model = RecipeIngredient

    recipe = factory.SubFactory(RecipeFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    quantity = 100
    unit = "g"
    sort_order = factory.Sequence(lambda n: n)
