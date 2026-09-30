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
    """Tarife yorum ve/veya puan ekleme."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    content = request.POST.get("content", "").strip()
    raw_score = request.POST.get("score", "").strip()

    if not content and not raw_score:
        messages.error(request, "Yorum yazın veya puan verin.")
        return redirect("recipes:recipe_detail", slug=recipe.slug)

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

    # ── Puan ekleme ── (1–5 kuralı RatingService'te doğrulanır)
    if raw_score:
        if not raw_score.isdigit():
            messages.error(request, "Puan geçerli bir sayı olmalıdır.")
        else:
            try:
                RatingService.rate(
                    user=request.user,
                    recipe=recipe,
                    score=int(raw_score),
                )
                messages.success(request, "Puanınız kaydedildi.")
            except ValidationError as err:
                for message in err.messages:
                    messages.error(request, message)

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
