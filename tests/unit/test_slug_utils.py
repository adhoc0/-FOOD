"""Slug üretimi regresyon testleri."""

import pytest

from core.utils.slug import generate_slug
from tests.factories import RecipeFactory


class TestGenerateSlug:
    """Türkçe karakterlerin URL uyumlu biçimde dönüştürülmesini doğrular."""

    def test_transliterates_turkish_characters_to_ascii(self):
        assert generate_slug("Çığ ÖŞÜ İ ı") == "cig-osu-i-i"


@pytest.mark.django_db
class TestRecipeSlugGeneration:
    """Tarif slugı oluşturma davranışını doğrular."""

    def test_factory_creates_an_ascii_slug_for_a_turkish_title(self):
        recipe = RecipeFactory(title="Adana Kebabı")

        assert recipe.slug.startswith("test-tarifi-adana-kebabi-")
        assert recipe.slug.isascii()
        assert recipe.get_absolute_url() == f"/tarifler/{recipe.slug}/"

    def test_pre_save_preserves_an_existing_slug_when_title_changes(self):
        recipe = RecipeFactory(slug="kalici-slug")

        recipe.title = "Değişen Tarif Başlığı"
        recipe.save(update_fields=["title"])
        recipe.refresh_from_db()

        assert recipe.slug == "kalici-slug"
