"""
View integration tests.

HTTP response, template usage, context verisi ve erişim kontrol testleri.
"""

import pytest
from django.test import Client
from django.urls import reverse

from recipes.choices import Status
from tests.factories import (
    CategoryFactory,
    CommentFactory,
    FavoriteFactory,
    ProvinceFactory,
    RecipeFactory,
    RecipeImageFactory,
    UserFactory,
)


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def authenticated_client():
    user = UserFactory()
    # Explicitly set password and save to be absolutely sure
    user.set_password("TestPass123!")
    user.save()
    client = Client()
    logged_in = client.login(username=user.username, password="TestPass123!")
    assert logged_in, f"Failed to log in user {user.username}"
    client.user = user
    return client


# ─────────────────────────────────────────────
# Recipe List View
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestRecipeListView:
    """RecipeListView integration testleri."""

    def test_status_200(self, client):
        response = client.get("/tarifler/")
        assert response.status_code == 200

    def test_uses_correct_template(self, client):
        response = client.get("/tarifler/")
        assert "recipes/list.html" in [t.name for t in response.templates]

    def test_context_contains_recipes(self, client):
        RecipeFactory(status=Status.PUBLISHED, is_active=True)
        response = client.get("/tarifler/")
        assert "recipes" in response.context
        assert len(response.context["recipes"]) == 1

    def test_draft_recipes_not_shown(self, client):
        RecipeFactory(status=Status.DRAFT, is_active=True)
        response = client.get("/tarifler/")
        assert len(response.context["recipes"]) == 0

    def test_filter_by_province(self, client):
        province = ProvinceFactory(slug="gaziantep")
        RecipeFactory(province=province, status=Status.PUBLISHED, is_active=True)
        RecipeFactory(status=Status.PUBLISHED, is_active=True)

        response = client.get("/tarifler/?province=gaziantep")
        assert len(response.context["recipes"]) == 1

    def test_filter_by_category(self, client):
        category = CategoryFactory(slug="corbalar")
        RecipeFactory(category=category, status=Status.PUBLISHED, is_active=True)
        RecipeFactory(status=Status.PUBLISHED, is_active=True)

        response = client.get("/tarifler/?category=corbalar")
        assert len(response.context["recipes"]) == 1

    def test_canonical_url_excludes_filter_parameters(self, client):
        response = client.get("/tarifler/?province=gaziantep")

        assert b'href="http://testserver/tarifler/"' in response.content

    def test_social_meta_tags_are_rendered(self, client):
        response = client.get("/tarifler/")

        assert b'property="og:site_name"' in response.content
        assert b'name="twitter:card"' in response.content


# ─────────────────────────────────────────────
# Recipe Detail View
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestRecipeDetailView:
    """RecipeDetailView integration testleri."""

    def test_status_200(self, client):
        recipe = RecipeFactory(slug="test-tarif", status=Status.PUBLISHED, is_active=True)
        response = client.get(f"/tarifler/{recipe.slug}/")
        assert response.status_code == 200

    def test_404_for_nonexistent(self, client):
        response = client.get("/tarifler/nonexistent-slug/")
        assert response.status_code == 404

    def test_context_has_meta(self, client):
        recipe = RecipeFactory(slug="test-meta", status=Status.PUBLISHED, is_active=True)
        response = client.get(f"/tarifler/{recipe.slug}/")
        assert "meta_title" in response.context
        assert "meta_description" in response.context
        assert "breadcrumbs" in response.context

    def test_context_has_related_recipes(self, client):
        recipe = RecipeFactory(slug="main-recipe", status=Status.PUBLISHED, is_active=True)
        response = client.get(f"/tarifler/{recipe.slug}/")
        assert "related_recipes" in response.context

    def test_social_meta_uses_cover_image(self, client):
        recipe = RecipeFactory(slug="cover-image", status=Status.PUBLISHED, is_active=True)
        cover_image = RecipeImageFactory(recipe=recipe, is_cover=True)

        response = client.get(f"/tarifler/{recipe.slug}/")

        image_url = f"http://testserver{cover_image.image.url}".encode()
        assert image_url in response.content

    def test_increments_view_count(self, client):
        recipe = RecipeFactory(
            slug="view-count-test", status=Status.PUBLISHED, is_active=True, view_count=0
        )
        client.get(f"/tarifler/{recipe.slug}/")
        recipe.refresh_from_db()
        assert recipe.view_count == 1


# ─────────────────────────────────────────────
# Category Views
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestCategoryListView:
    """CategoryListView integration testleri."""

    def test_status_200(self, client):
        response = client.get("/tarifler/kategori/")
        assert response.status_code == 200

    def test_context_contains_categories(self, client):
        CategoryFactory(is_active=True)
        response = client.get("/tarifler/kategori/")
        assert "categories" in response.context


@pytest.mark.django_db
class TestCategoryDetailView:
    """CategoryDetailView integration testleri."""

    def test_status_200(self, client):
        category = CategoryFactory(slug="corbalar", is_active=True)
        RecipeFactory(category=category, status=Status.PUBLISHED, is_active=True)
        response = client.get(f"/tarifler/kategori/{category.slug}/")
        assert response.status_code == 200

    def test_404_for_nonexistent(self, client):
        response = client.get("/tarifler/kategori/nonexistent/")
        assert response.status_code == 404


# ─────────────────────────────────────────────
# Search View
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestSearchView:
    """SearchView integration testleri."""

    def test_status_200(self, client):
        response = client.get("/tarifler/ara/")
        assert response.status_code == 200

    def test_search_with_query(self, client):
        RecipeFactory(title="Adana Kebabı", status=Status.PUBLISHED, is_active=True)
        response = client.get("/tarifler/ara/?q=kebab")
        assert response.status_code == 200
        assert "recipes" in response.context

    def test_context_has_filters(self, client):
        response = client.get("/tarifler/ara/?q=test")
        assert "query" in response.context
        assert "provinces" in response.context
        assert "categories" in response.context
        assert "difficulties" in response.context


# ─────────────────────────────────────────────
# Interaction Views
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestToggleFavoriteView:
    """toggle_favorite view testleri."""

    def test_requires_login(self, client):
        recipe = RecipeFactory()
        response = client.post(f"/etkilesim/favori-degistir/{recipe.id}/")
        assert response.status_code == 302  # Redirect to login

    def test_toggle_favorite_adds(self, authenticated_client):
        recipe = RecipeFactory(favorite_count=0)
        response = authenticated_client.post(f"/etkilesim/favori-degistir/{recipe.id}/")
        assert response.status_code == 302
        recipe.refresh_from_db()
        assert recipe.favorite_count == 1


@pytest.mark.django_db
class TestAddCommentView:
    """add_comment view testleri."""

    def test_requires_login(self, client):
        recipe = RecipeFactory()
        response = client.post(f"/etkilesim/yorum-ekle/{recipe.id}/")
        assert response.status_code == 302  # Redirect to login

    def test_add_comment_with_valid_content(self, authenticated_client):
        recipe = RecipeFactory()
        response = authenticated_client.post(
            f"/etkilesim/yorum-ekle/{recipe.id}/",
            {"content": "Bu tarif gerçekten çok güzelmiş, teşekkür ederim."},
        )
        assert response.status_code == 302

        from interactions.models import Comment

        assert Comment.objects.filter(recipe=recipe).count() == 1


@pytest.mark.django_db
class TestProfileView:
    """Profil sayfası erişim ve bağlam testleri."""

    def test_requires_login(self, client):
        response = client.get(reverse("accounts:profile"))

        assert response.status_code == 302
        assert response.url.startswith(reverse("accounts:login"))

    def test_displays_current_user_interactions(self, authenticated_client):
        recipe = RecipeFactory()
        FavoriteFactory(user=authenticated_client.user, recipe=recipe)
        CommentFactory(user=authenticated_client.user, recipe=recipe)

        response = authenticated_client.get(reverse("accounts:profile"))

        assert response.status_code == 200
        assert response.context["favorites"].count() == 1
        assert response.context["comments"].count() == 1
