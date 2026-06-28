from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from recipes.models import Recipe
from .models import Comment, Favorite, Rating

@login_required
@require_POST
def add_comment(request, recipe_id):
    """
    Tarife yorum ve/veya puan ekleme.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    content = request.POST.get('content', '').strip()
    score = request.POST.get('score')
    
    # Yorum Ekleme
    if content:
        Comment.objects.create(
            user=request.user,
            recipe=recipe,
            content=content,
            is_approved=False  # Admin onayı gerekiyor
        )
        messages.success(request, 'Yorumunuz alındı, yönetici onayından sonra yayınlanacaktır.')
    
    # Puan Ekleme (Eğer seçildiyse)
    if score and score.isdigit():
        score = int(score)
        if 1 <= score <= 5:
            # Aynı kullanıcının önceki puanını güncelle veya yeni puan ver
            Rating.objects.update_or_create(
                user=request.user,
                recipe=recipe,
                defaults={'score': score}
            )
            messages.success(request, 'Puanınız kaydedildi.')
            
    return redirect('recipes:detail', slug=recipe.slug)


@login_required
@require_POST
def toggle_favorite(request, recipe_id):
    """
    Tarifi favorilere ekleme veya çıkarma.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        # Zaten favorilerdeyse, çıkar
        favorite.delete()
        messages.info(request, f'{recipe.title} favorilerinizden çıkarıldı.')
    else:
        messages.success(request, f'{recipe.title} favorilerinize eklendi.')
        
    return redirect('recipes:detail', slug=recipe.slug)
