"""
Recipe views.

Recipe list and detail pages.
Business logic is handled by the service layer.
"""

from __future__ import annotations

from typing import Any

from django.conf import settings
from django.db.models import QuerySet
from django.http import Http404
from django.views.generic import DetailView, ListView

from common.network import get_client_ip
from interactions.services import CommentService, FavoriteService, RatingService
from recipes.constants import DEFAULT_PAGE_SIZE
from recipes.models import Recipe
from recipes.selectors import RecipeSelector
from recipes.services import RecipeService


class RecipeListView(ListView):
    """Published recipe list."""

    model = Recipe
    template_name = "recipes/list.html"
    context_object_name = "recipes"
    paginate_by = DEFAULT_PAGE_SIZE

    def get_queryset(self) -> QuerySet[Recipe]:
        province_slug = self.request.GET.get(
            "province",
            "",
        ).strip()

        category_slug = self.request.GET.get(
            "category",
            "",
        ).strip()

        return RecipeSelector.get_filtered_published_list(
            province_slug=province_slug,
            category_slug=category_slug,
        )

    def get_context_data(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["current_province"] = self.request.GET.get(
            "province",
            "",
        )

        context["current_category"] = self.request.GET.get(
            "category",
            "",
        )

        return context


class RecipeDetailView(DetailView):
    """Recipe detail page."""

    model = Recipe
    template_name = "recipes/detail.html"
    context_object_name = "recipe"

    def get_object(
        self,
        queryset: QuerySet[Recipe] | None = None,
    ) -> Recipe:
        recipe = RecipeSelector.get_recipe_detail(self.kwargs["slug"])

        if recipe is None:
            raise Http404("Recipe not found.")

        # Yalnızca gerçek sayfa isteklerinde (GET) ve ziyaretçi başına bir kez sayılır.
        if self.request.method == "GET":
            RecipeService.record_view(
                recipe,
                viewer_key=self._get_viewer_key(),
            )

        return recipe

    def _get_viewer_key(self) -> str:
        user = self.request.user

        if user.is_authenticated:
            return f"user:{user.pk}"

        client_ip = get_client_ip(
            self.request,
            trusted_proxy_count=settings.NUM_PROXIES,
        )

        return f"ip:{client_ip}"


    def get_context_data(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        recipe = self.object
        user = self.request.user

        context["related_recipes"] = (
            Recipe.objects.related(
                recipe,
            )
        )

        context["is_favorited"] = FavoriteService.is_favorited(
            user=user,
            recipe=recipe,
        )

        context["user_rating"] = RatingService.get_user_rating(
            user=user,
            recipe=recipe,
        )

        context["average_rating"] = recipe.average_rating
        context["rating_count"] = recipe.rating_count
        context["recipe_images"] = recipe.recipe_images.all()
        context["recipe_ingredients"] = recipe.recipe_ingredients.all()
        context["approved_comments"] = CommentService.get_approved_comments(recipe)

        context["meta_title"] = (
            recipe.meta_title
            or f"{recipe.title} Tarifi | {recipe.province.name}"
        )

        context["meta_description"] = (
            recipe.meta_description
            or recipe.summary[:160]
        )

        context["breadcrumbs"] = [
            {
                "title": "Ana Sayfa",
                "url": "/",
            },
            {
                "title": recipe.province.name,
                "url": recipe.province.get_absolute_url(),
            },
            {
                "title": recipe.title,
                "url": "",
            },
        ]

        return context
