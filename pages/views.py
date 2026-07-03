from django.db.models import Avg, Count
from django.views.generic import TemplateView

from provinces.models import Province
from recipes.models import Recipe


class HomePageView(TemplateView):
    """
    Anasayfa görünümü.
    Son eklenen tarifler, popüler bölgeler ve genel istatistikleri gösterir.
    """
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Son eklenen yayınlanmış tarifler
        context['latest_recipes'] = (
            Recipe.objects
            .filter(is_published=True)
            .select_related('province')
            .order_by('-created_at')[:6]
        )

        # En çok tarife sahip bölgeler (Top 7 — her bölge)
        context['top_provinces'] = (
            Province.objects
            .annotate(recipe_count=Count('recipes'))
            .filter(recipe_count__gt=0)
            .order_by('-recipe_count')[:7]
        )

        # Genel istatistikler
        context['total_recipes'] = Recipe.objects.filter(is_published=True).count()
        context['total_provinces'] = Province.objects.filter(recipes__isnull=False).distinct().count()

        return context
