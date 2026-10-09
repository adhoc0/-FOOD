"""Recipe ve Tag model testleri."""

import pytest
from django.db import IntegrityError

from recipes.choices import Status
from tests.factories import DraftRecipeFactory, RecipeFactory, TagFactory


@pytest.mark.django_db
class TestRecipeModel:
    def test_str_returns_title(self):
        assert str(RecipeFactory(title="Ali Nazik")) == "Ali Nazik"

    def test_total_time_sums_preparation_and_cooking(self):
        recipe = RecipeFactory(preparation_time=10, cooking_time=25)

        assert recipe.total_time == 35

    def test_is_published_reflects_status(self):
        assert RecipeFactory().is_published is True
        assert DraftRecipeFactory().is_published is False

    def test_status_defaults_to_draft_on_model(self):
        recipe = RecipeFactory(status=Status.DRAFT, published_at=None)

        assert recipe.status == Status.DRAFT

    def test_absolute_url_uses_slug(self):
        recipe = RecipeFactory()

        assert recipe.get_absolute_url() == f"/tarifler/{recipe.slug}/"

    def test_slug_is_unique(self):
        recipe = RecipeFactory()

        with pytest.raises(IntegrityError):
            RecipeFactory(slug=recipe.slug)

    def test_cover_image_is_none_without_images(self):
        assert RecipeFactory().cover_image is None


@pytest.mark.django_db
class TestTagModel:
    def test_str_returns_name(self):
        assert str(TagFactory(name="Vegan")) == "Vegan"

    def test_name_is_unique(self):
        tag = TagFactory()

        with pytest.raises(IntegrityError):
            TagFactory(name=tag.name, slug="baska-slug")
