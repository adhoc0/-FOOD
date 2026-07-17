"""Backend regresyon testleri."""

import pytest
from django.urls import reverse

from accounts.selectors.user_selector import UserSelector
from recipes.models import Cuisine, RecipeImage, RecipeTag, Tag
from recipes.services.recipe_image_service import RecipeImageService
from tests.factories import RecipeFactory, RecipeImageFactory, TagFactory, UserFactory


@pytest.mark.django_db
class TestUserSelector:
    """Kullanıcı selector'ının sorgu sözleşmesini doğrular."""

    def test_get_all_returns_only_active_users(self):
        active_user = UserFactory(is_active=True)
        UserFactory(is_active=False)

        users = list(UserSelector.get_all())

        assert users == [active_user]

    def test_get_staff_returns_only_active_staff_users(self):
        active_staff_user = UserFactory(is_active=True, is_staff=True)
        UserFactory(is_active=False, is_staff=True)
        UserFactory(is_active=True, is_staff=False)

        users = list(UserSelector.get_staff())

        assert users == [active_staff_user]


@pytest.mark.django_db
class TestTagQuerySet:
    """Etiket tarif sayısı sorgusunu doğrular."""

    def test_with_recipe_count_uses_recipe_tag_relation(self):
        tag = TagFactory()
        RecipeTag.objects.create(recipe=RecipeFactory(), tag=tag)
        RecipeTag.objects.create(recipe=RecipeFactory(), tag=tag)

        tag_with_count = Tag.objects.with_recipe_count().get(pk=tag.pk)

        assert tag_with_count.recipe_count == 2


class TestCuisineQuerySet:
    """Mutfak queryset'inin gerçek veri modeline uymasını doğrular."""

    def test_does_not_expose_recipe_count_queries_without_a_recipe_relation(self):
        assert not hasattr(Cuisine.objects, "with_recipe_count")
        assert not hasattr(Cuisine.objects, "has_recipes")
        assert not hasattr(Cuisine.objects, "active_with_recipe_count")
        assert not hasattr(Cuisine.objects, "active_with_recipes")


@pytest.mark.django_db
class TestRecipeImageService:
    """Kapak görseli kısıtının servis katmanında korunmasını doğrular."""

    def test_create_cover_replaces_existing_cover_before_insert(self):
        recipe = RecipeFactory()
        existing_cover = RecipeImageFactory(recipe=recipe, is_cover=True)
        image_file = RecipeImageFactory.build().image

        new_cover = RecipeImageService.create(
            recipe=recipe,
            image=image_file,
            alt_text="Yeni kapak görseli",
            is_cover=True,
        )

        existing_cover.refresh_from_db()

        assert existing_cover.is_cover is False
        assert RecipeImage.objects.get(recipe=recipe, is_cover=True) == new_cover

    def test_update_to_cover_replaces_existing_cover_before_save(self):
        recipe = RecipeFactory()
        existing_cover = RecipeImageFactory(recipe=recipe, is_cover=True)
        candidate_image = RecipeImageFactory(recipe=recipe, is_cover=False)

        new_cover = RecipeImageService.update(candidate_image, is_cover=True)

        existing_cover.refresh_from_db()

        assert existing_cover.is_cover is False
        assert RecipeImage.objects.get(recipe=recipe, is_cover=True) == new_cover


class TestStaticPageSitemap:
    """Statik sitemap öğelerinin çözümlenebilir URL'ler olmasını doğrular."""

    def test_every_item_resolves_to_a_url(self):
        from pages.sitemaps import StaticPageSitemap

        sitemap = StaticPageSitemap()

        locations = [sitemap.location(item) for item in sitemap.items()]

        assert reverse("pages:home") in locations
