"""
Interaction views.

Kullanıcı etkileşimleri: yorum, favori, puanlama.
Business Logic servis katmanında — view yalnızca HTTP işlemlerini yönetir.
"""

from __future__ import annotations

import logging
from typing import cast

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from accounts.models import CustomUser
from interactions.services import CommentService, FavoriteService, RatingService
from recipes.models import Recipe

logger = logging.getLogger(__name__)

Feedback = list[tuple[str, str]]  # (seviye, mesaj) — seviye: "success" | "info" | "error"


def _wants_json(request: HttpRequest) -> bool:
    """İstek fetch ile JSON yanıt bekliyorsa True (ilerleyici geliştirme)."""

    return "application/json" in request.headers.get("Accept", "")


def _respond(
    request: HttpRequest,
    recipe: Recipe,
    feedback: Feedback,
    **payload: object,
) -> HttpResponse:
    """JSON isteğe JSON, normal form gönderimine flash mesaj + yönlendirme döner."""

    has_error = any(level == "error" for level, _ in feedback)
    has_success = any(level != "error" for level, _ in feedback)

    if _wants_json(request):
        return JsonResponse(
            {
                "ok": not has_error or has_success,
                "messages": [{"level": level, "text": text} for level, text in feedback],
                **payload,
            },
            status=400 if has_error and not has_success else 200,
        )

    for level, text in feedback:
        getattr(messages, level)(request, text)
    return redirect("recipes:recipe_detail", slug=recipe.slug)


@login_required
@require_POST
def add_comment(request: HttpRequest, recipe_id: int) -> HttpResponse:
    """Tarife yorum ve/veya puan ekleme."""
    user = cast(CustomUser, request.user)
    recipe = get_object_or_404(Recipe, id=recipe_id)
    content = request.POST.get("content", "").strip()
    raw_score = request.POST.get("score", "").strip()
    feedback: Feedback = []

    if not content and not raw_score:
        return _respond(request, recipe, [("error", "Yorum yazın veya puan verin.")])

    # ── Yorum ekleme ──
    if content:
        try:
            CommentService.create(
                user=user,
                recipe=recipe,
                content=content,
            )
            feedback.append(
                ("success", "Yorumunuz alındı, yönetici onayından sonra yayınlanacaktır.")
            )
        except ValidationError as err:
            feedback.extend(("error", message) for message in err.messages)

    # ── Puan ekleme ── (1–5 kuralı RatingService'te doğrulanır)
    if raw_score:
        if not raw_score.isdigit():
            feedback.append(("error", "Puan geçerli bir sayı olmalıdır."))
        else:
            try:
                RatingService.rate(
                    user=user,
                    recipe=recipe,
                    score=int(raw_score),
                )
                feedback.append(("success", "Puanınız kaydedildi."))
            except ValidationError as err:
                feedback.extend(("error", message) for message in err.messages)

    recipe.refresh_from_db(fields=["average_rating", "rating_count"])
    return _respond(
        request,
        recipe,
        feedback,
        average_rating=str(recipe.average_rating),
        rating_count=recipe.rating_count,
    )


@login_required
@require_POST
def toggle_favorite(request: HttpRequest, recipe_id: int) -> HttpResponse:
    """Tarifi favorilere ekleme veya çıkarma."""
    user = cast(CustomUser, request.user)
    recipe = get_object_or_404(Recipe, id=recipe_id)

    added = FavoriteService.toggle(
        user=user,
        recipe=recipe,
    )

    feedback: Feedback = (
        [("success", f"{recipe.title} favorilerinize eklendi.")]
        if added
        else [("info", f"{recipe.title} favorilerinizden çıkarıldı.")]
    )
    return _respond(request, recipe, feedback, favorited=added)
