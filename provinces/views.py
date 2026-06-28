from django.views.generic import DetailView
from .models import Province
from recipes.models import Recipe

class ProvinceDetailView(DetailView):
    model = Province
    template_name = 'provinces/province_detail.html'
    context_object_name = 'province'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # İlgili ile ait tarifleri al
        recipes = Recipe.objects.filter(province=self.object, is_published=True)
        
        # A'dan Z'ye sıralanmış tarifler
        context['recipes_az'] = recipes.order_by('title')
        
        # En iyi tarifler (Şu an rastgele veya son eklenenler, ileride rating'e göre sıralanacak)
        context['top_recipes'] = recipes.order_by('-created_at')[:5]
        
        return context
