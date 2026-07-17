"""Yorum servisinin moderasyon ve okuma davranışı testleri."""

import pytest

from interactions.services import CommentService
from tests.factories import CommentFactory, RecipeFactory, UserFactory


@pytest.mark.django_db
def test_comment_service_creates_pending_comment() -> None:
    user = UserFactory()
    recipe = RecipeFactory()

    comment = CommentService.create(user, recipe, "Yeterince uzun ve geçerli bir yorum.")

    assert comment.is_approved is False


@pytest.mark.django_db
def test_comment_service_returns_only_approved_comments() -> None:
    user = UserFactory()
    recipe = RecipeFactory()
    CommentFactory(user=user, recipe=recipe, is_approved=False)
    approved = CommentFactory(user=user, recipe=recipe, is_approved=True)

    comments = CommentService.get_approved_comments(recipe)

    assert list(comments) == [approved]
    assert CommentService.get_comment_count(recipe) == 1
