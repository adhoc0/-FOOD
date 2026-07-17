"""
Interaction views.

Kullanıcı etkileşimleri: yorum, favori, puanlama.
Business Logic servis katmanında — view yalnızca HTTP işlemlerini yönetir.
"""

from __future__ import annotations

import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from interactions.services import CommentService
from recipes.models import Recipe
from recipes.services import FavoriteService, RatingService

logger = logging.getLogger(__name__)


@login_required
@require_POST
def add_comment(request, recipe_id):
    """Tarife yorum ekleme."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    content = request.POST.get("content", "").strip()
    score = request.POST.get("score")

    # ── Yorum ekleme ──
    if content:
        try:
            CommentService.create(
                user=request.user,
                recipe=recipe,
                content=content,
            )
            messages.success(
                request,
                "Yorumunuz alındı, yönetici onayından sonra yayınlanacaktır.",
            )
        except ValidationError as err:
            for message in err.messages:
                messages.error(request, message)

    # ── Puan ekleme ──
    if score and score.isdigit():
        score_int = int(score)
        if 1 <= score_int <= 5:
            RatingService.rate(
                user=request.user,
                recipe=recipe,
                score=score_int,
            )
            messages.success(request, "Puanınız kaydedildi.")

    return redirect("recipes:recipe_detail", slug=recipe.slug)


@login_required
@require_POST
def toggle_favorite(request, recipe_id):
    """Tarifi favorilere ekleme veya çıkarma."""
    recipe = get_object_or_404(Recipe, id=recipe_id)

    added = FavoriteService.toggle(
        user=request.user,
        recipe=recipe,
    )

    if added:
        messages.success(request, f"{recipe.title} favorilerinize eklendi.")
    else:
        messages.info(request, f"{recipe.title} favorilerinizden çıkarıldı.")

    return redirect("recipes:recipe_detail", slug=recipe.slug)
