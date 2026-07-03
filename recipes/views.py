from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from interactions.models import Comment, Favorite
from .forms import RecipeCreateForm
from .models import Ingredient, Recipe, RecipeIngredient


class RecipeListView(ListView):
    """
    Tüm tariflerin listelendiği genel görünüm ve Arama motoru.
    """
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        queryset = Recipe.objects.filter(is_published=True).order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(province__name__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object

        # Sadece onaylanmış yorumları getir
        context['comments'] = recipe.comments.filter(is_approved=True).order_by('-created_at')

        # Malzemeleri getir
        context['ingredients'] = recipe.ingredients.all()

        # Ek resimleri getir
        context['images'] = recipe.images.all()

        # Giriş yapmış kullanıcı için favori durumunu kontrol et
        if self.request.user.is_authenticated:
            context['is_favorite'] = Favorite.objects.filter(user=self.request.user, recipe=recipe).exists()
        else:
            context['is_favorite'] = False

        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    """
    Kullanıcıların tarif önerebilmesi için view.
    """
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('pages:home')  # Veya profile yönlendirilebilir

    def form_valid(self, form):
        # Tarifi kaydet, ama is_published = False olsun
        recipe = form.save(commit=False)
        recipe.is_published = False
        recipe.save()

        # raw_ingredients alanını parçala
        raw_ingredients = form.cleaned_data.get('raw_ingredients', '')
        lines = [line.strip() for line in raw_ingredients.split('\n') if line.strip()]

        for idx, line in enumerate(lines):
            # Normalde çok daha detaylı NLP/Regex gerekir ancak şimdilik:
            parts = line.rsplit(' ', 1)
            if len(parts) == 2:
                qty_unit, ing_name = parts[0], parts[1]
            else:
                qty_unit, ing_name = '', line

            ingredient, created = Ingredient.objects.get_or_create(name=ing_name.lower())

            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                quantity=qty_unit,
                order=idx
            )

        messages.success(self.request, 'Tarifiniz başarıyla gönderildi. Yöneticilerimiz onayladıktan sonra yayına alınacaktır. Teşekkürler!')
        return super().form_valid(form)
