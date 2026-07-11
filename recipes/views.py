from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from interactions.models import Favorite
from recipes.forms import RecipeCreateForm
from recipes.models import Recipe
from recipes.models.recipe import Status


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 12

    def get_queryset(self):
        queryset = (
            Recipe.objects.filter(
                status=Status.PUBLISHED,
                is_active=True,
            )
            .select_related(
                "province",
                "category",
            )
            .order_by("-published_at", "-created_at")
        )

        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(province__name__icontains=query)
                | Q(category__name__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"

    def get_queryset(self):
        return (
            Recipe.objects.filter(
                status=Status.PUBLISHED,
                is_active=True,
            )
            .select_related(
                "province",
                "category",
                "author",
            )
            .prefetch_related(
                "images",
                "ingredients",
                "tags",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipe = self.object

        if self.request.user.is_authenticated:
            context["is_favorite"] = Favorite.objects.filter(
                user=self.request.user,
                recipe=recipe,
            ).exists()
        else:
            context["is_favorite"] = False

        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("pages:home")

    def form_valid(self, form):
        recipe = form.save(commit=False)

        recipe.author = self.request.user
        recipe.status = status=Status.PUBLISHED,

        recipe.save()

        messages.success(
            self.request,
            "Tarifiniz başarıyla gönderildi.",
        )

        return super().form_valid(form)