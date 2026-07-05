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

        from django.contrib.auth import get_user_model
        from interactions.models import Rating

        User = get_user_model()

        # Son eklenen yayınlanmış tarifler
        context['latest_recipes'] = (
            Recipe.objects
            .filter(is_published=True)
            .select_related('province')
            .order_by('-created_at')[:6]
        )

        # En çok tarife sahip bölgeler
        context['top_provinces'] = (
            Province.objects
            .annotate(recipe_count=Count('recipes'))
            .filter(recipe_count__gt=0)
            .order_by('-recipe_count')[:7]
        )

        # En çok beğenilen 10 yemek
        context['top_10_recipes'] = (
            Recipe.objects
            .filter(is_published=True)
            .annotate(
                avg_score=Avg('ratings__score'),
                like_count=Count('favorited_by', distinct=True)
            )
            .order_by('-avg_score', '-like_count')[:10]
        )

        # Dinamik istatistikler
        avg_rating_dict = Rating.objects.aggregate(Avg('score'))
        avg_rating = avg_rating_dict['score__avg'] or 0

        context['stats'] = {
            'provinces': Province.objects.count(),
            'recipes': Recipe.objects.filter(is_published=True).count(),
            'users': User.objects.count(),
            'avg_rating': round(avg_rating, 1)
        }

        return context
