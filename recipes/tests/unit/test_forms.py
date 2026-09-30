"""RecipeCreateForm testleri."""

import pytest

from recipes.choices import Difficulty
from recipes.forms import RecipeCreateForm
from tests.factories import CategoryFactory, ProvinceFactory


def _data(**overrides):
    data = {
        "province": ProvinceFactory().pk,
        "category": CategoryFactory().pk,
        "title": "Ali Nazik",
        "summary": "Közlenmiş patlıcan üzerinde yoğurt ve kuzu etiyle servis edilir.",
        "instructions": (
            "Patlıcanları közleyin, soyun ve ezin. Yoğurtla karıştırıp "
            "üzerine kavrulmuş kuzu eti ekleyerek sıcak servis edin."
        ),
        "preparation_time": 20,
        "cooking_time": 40,
        "servings": 4,
        "difficulty": Difficulty.MEDIUM,
    }
    data.update(overrides)
    return data


@pytest.mark.django_db
class TestRecipeCreateForm:
    def test_valid_data(self):
        form = RecipeCreateForm(data=_data())

        assert form.is_valid(), form.errors

    def test_title_too_short_is_rejected(self):
        form = RecipeCreateForm(data=_data(title="A"))

        assert not form.is_valid()
        assert "title" in form.errors

    def test_summary_too_short_is_rejected(self):
        form = RecipeCreateForm(data=_data(summary="Kısa"))

        assert "summary" in RecipeCreateForm(data=_data(summary="Kısa")).errors
        assert not form.is_valid()

    def test_servings_zero_is_rejected(self):
        form = RecipeCreateForm(data=_data(servings=0))

        assert not form.is_valid()
        assert "servings" in form.errors

    def test_missing_required_fields(self):
        form = RecipeCreateForm(data={})

        assert not form.is_valid()
        assert {"province", "category", "title"} <= set(form.errors)
