"""Liste ve detay sorgularının gereksiz ilişki yüklememesi/N+1 üretmemesi."""

from __future__ import annotations

import pytest
from django.db import connection
from django.test.utils import CaptureQueriesContext

from recipes.models import Recipe
from recipes.models.recipe_tag import RecipeTag
from recipes.selectors import RecipeSelector
from tests.factories import RecipeFactory, RecipeIngredientFactory, TagFactory

pytestmark = pytest.mark.django_db


def test_list_queryset_does_not_prefetch_detail_relations() -> None:
    lookups = Recipe.objects.published_with_related()._prefetch_related_lookups
    assert "recipe_images" in lookups
    assert "recipe_ingredients" not in lookups
    assert "recipe_tags" not in lookups


def test_detail_loads_ingredients_and_tags_without_extra_queries() -> None:
    recipe = RecipeFactory()
    for _ in range(3):
        RecipeIngredientFactory(recipe=recipe)
    for _ in range(2):
        RecipeTag.objects.create(recipe=recipe, tag=TagFactory())

    loaded = RecipeSelector.get_recipe_detail(recipe.slug)
    assert loaded is not None

    with CaptureQueriesContext(connection) as ctx:
        names = [item.ingredient.name for item in loaded.recipe_ingredients.all()]
        tags = [item.tag.name for item in loaded.recipe_tags.all()]

    assert len(names) == 3
    assert len(tags) == 2
    assert len(ctx.captured_queries) == 0
