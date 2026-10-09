"""RecipeImageService testleri (kapak görseli kuralları)."""

import pytest

from recipes.models import RecipeImage
from recipes.services import RecipeImageService
from tests.factories import RecipeFactory, RecipeImageFactory


@pytest.mark.django_db
class TestRecipeImageService:
    def test_create_cover_clears_previous_cover(self):
        recipe = RecipeFactory()
        old = RecipeImageFactory(recipe=recipe, is_cover=True)

        new = RecipeImageService.create(recipe=recipe, alt_text="Yeni", is_cover=True)

        old.refresh_from_db()
        assert old.is_cover is False
        assert new.is_cover is True

    def test_create_non_cover_keeps_existing_cover(self):
        recipe = RecipeFactory()
        cover = RecipeImageFactory(recipe=recipe, is_cover=True)

        RecipeImageService.create(recipe=recipe, alt_text="Ek", is_cover=False)

        cover.refresh_from_db()
        assert cover.is_cover is True

    def test_set_cover_moves_cover_flag(self):
        recipe = RecipeFactory()
        first = RecipeImageFactory(recipe=recipe, is_cover=True)
        second = RecipeImageFactory(recipe=recipe)

        RecipeImageService.set_cover(second)

        first.refresh_from_db()
        second.refresh_from_db()
        assert (first.is_cover, second.is_cover) == (False, True)

    def test_set_cover_does_not_touch_other_recipes(self):
        other = RecipeImageFactory(is_cover=True)
        target = RecipeImageFactory()

        RecipeImageService.set_cover(target)

        other.refresh_from_db()
        assert other.is_cover is True

    def test_unset_cover(self):
        image = RecipeImageFactory(is_cover=True)

        RecipeImageService.unset_cover(image)

        image.refresh_from_db()
        assert image.is_cover is False

    def test_update_without_data_is_noop(self):
        image = RecipeImageFactory()

        assert RecipeImageService.update(image) is image

    def test_update_to_cover_clears_other_cover(self):
        recipe = RecipeFactory()
        first = RecipeImageFactory(recipe=recipe, is_cover=True)
        second = RecipeImageFactory(recipe=recipe)

        RecipeImageService.update(second, is_cover=True, alt_text="Kapak")

        first.refresh_from_db()
        second.refresh_from_db()
        assert first.is_cover is False
        assert (second.is_cover, second.alt_text) == (True, "Kapak")

    def test_delete(self):
        image = RecipeImageFactory()

        RecipeImageService.delete(image)

        assert not RecipeImage.objects.filter(pk=image.pk).exists()
