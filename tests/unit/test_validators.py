"""
Validator unit tests.

RecipeValidator, ImageValidator, IngredientValidator, CommentValidator testleri.
"""

import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from interactions.validators import CommentValidator
from recipes.constants import (
    MAX_COMMENT_LENGTH,
    MAX_INGREDIENT_NAME_LENGTH,
    MAX_INSTRUCTIONS_LENGTH,
    MAX_SERVINGS,
    MAX_SUMMARY_LENGTH,
    MAX_TIME_MINUTES,
    MAX_TITLE_LENGTH,
    MIN_INSTRUCTIONS_LENGTH,
    MIN_SUMMARY_LENGTH,
    MIN_TITLE_LENGTH,
)
from recipes.validators import ImageValidator, IngredientValidator, RecipeValidator


# ─────────────────────────────────────────────
# RecipeValidator
# ─────────────────────────────────────────────
class TestRecipeValidatorTitle:
    """RecipeValidator.validate_title testleri."""

    def test_valid_title(self):
        RecipeValidator.validate_title("Ali Nazik")

    def test_title_too_short(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_title("AB")

    def test_title_exactly_min_length(self):
        RecipeValidator.validate_title("A" * MIN_TITLE_LENGTH)

    def test_title_too_long(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_title("A" * (MAX_TITLE_LENGTH + 1))

    def test_title_only_whitespace(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_title("   ")


class TestRecipeValidatorSummary:
    """RecipeValidator.validate_summary testleri."""

    def test_valid_summary(self):
        RecipeValidator.validate_summary("A" * MIN_SUMMARY_LENGTH)

    def test_summary_too_short(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_summary("Kısa")

    def test_summary_too_long(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_summary("A" * (MAX_SUMMARY_LENGTH + 1))


class TestRecipeValidatorInstructions:
    """RecipeValidator.validate_instructions testleri."""

    def test_valid_instructions(self):
        RecipeValidator.validate_instructions("A" * MIN_INSTRUCTIONS_LENGTH)

    def test_instructions_too_short(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_instructions("Kısa talimat")

    def test_instructions_too_long(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_instructions("A" * (MAX_INSTRUCTIONS_LENGTH + 1))


class TestRecipeValidatorTime:
    """RecipeValidator.validate_preparation_time / validate_cooking_time testleri."""

    def test_valid_preparation_time(self):
        RecipeValidator.validate_preparation_time(30)

    def test_negative_preparation_time(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_preparation_time(-1)

    def test_preparation_time_over_limit(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_preparation_time(MAX_TIME_MINUTES + 1)

    def test_valid_cooking_time(self):
        RecipeValidator.validate_cooking_time(60)

    def test_negative_cooking_time(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_cooking_time(-5)

    def test_cooking_time_over_limit(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_cooking_time(MAX_TIME_MINUTES + 1)


class TestRecipeValidatorServings:
    """RecipeValidator.validate_servings testleri."""

    def test_valid_servings(self):
        RecipeValidator.validate_servings(4)

    def test_servings_zero(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_servings(0)

    def test_servings_over_limit(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_servings(MAX_SERVINGS + 1)


class TestRecipeValidatorStatusTransition:
    """RecipeValidator.validate_status_transition testleri."""

    def test_draft_to_published(self):
        RecipeValidator.validate_status_transition("draft", "published")

    def test_published_to_draft(self):
        RecipeValidator.validate_status_transition("published", "draft")

    def test_published_to_archived(self):
        RecipeValidator.validate_status_transition("published", "archived")

    def test_archived_to_draft(self):
        RecipeValidator.validate_status_transition("archived", "draft")

    def test_draft_to_archived_not_allowed(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_status_transition("draft", "archived")

    def test_archived_to_published_not_allowed(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_status_transition("archived", "published")

    def test_same_status_no_error(self):
        RecipeValidator.validate_status_transition("draft", "draft")


class TestRecipeValidatorCompose:
    """RecipeValidator.validate_recipe_data testleri."""

    def test_valid_data(self):
        RecipeValidator.validate_recipe_data({
            "title": "Ali Nazik Kebabı",
            "summary": "A" * MIN_SUMMARY_LENGTH,
            "instructions": "A" * MIN_INSTRUCTIONS_LENGTH,
            "preparation_time": 15,
            "cooking_time": 30,
            "servings": 4,
        })

    def test_invalid_title_in_compose(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_recipe_data({"title": "AB"})

    def test_partial_data_validates_only_present_fields(self):
        RecipeValidator.validate_recipe_data({"servings": 4})


# ─────────────────────────────────────────────
# ImageValidator
# ─────────────────────────────────────────────
class TestImageValidatorSize:
    """ImageValidator.validate_size testleri."""

    def test_valid_size(self):
        image = SimpleUploadedFile("test.jpg", b"x" * 10000, content_type="image/jpeg")
        ImageValidator.validate_size(image)

    def test_too_small(self):
        image = SimpleUploadedFile("test.jpg", b"x" * 100, content_type="image/jpeg")
        with pytest.raises(ValidationError):
            ImageValidator.validate_size(image)

    def test_too_large(self):
        image = SimpleUploadedFile(
            "test.jpg", b"x" * (6 * 1024 * 1024), content_type="image/jpeg"
        )
        with pytest.raises(ValidationError):
            ImageValidator.validate_size(image)


class TestImageValidatorExtension:
    """ImageValidator.validate_extension testleri."""

    def test_valid_jpg(self):
        image = SimpleUploadedFile("photo.jpg", b"content", content_type="image/jpeg")
        ImageValidator.validate_extension(image)

    def test_valid_png(self):
        image = SimpleUploadedFile("photo.png", b"content", content_type="image/png")
        ImageValidator.validate_extension(image)

    def test_valid_webp(self):
        image = SimpleUploadedFile("photo.webp", b"content", content_type="image/webp")
        ImageValidator.validate_extension(image)

    def test_invalid_extension(self):
        image = SimpleUploadedFile("photo.bmp", b"content", content_type="image/bmp")
        with pytest.raises(ValidationError):
            ImageValidator.validate_extension(image)

    def test_executable_extension(self):
        image = SimpleUploadedFile("shell.exe", b"content", content_type="application/octet")
        with pytest.raises(ValidationError):
            ImageValidator.validate_extension(image)


class TestImageValidatorMimeType:
    """ImageValidator.validate_mime_type testleri."""

    def test_valid_jpeg_magic_bytes(self):
        content = b"\xff\xd8\xff\xe0" + b"\x00" * 100
        image = SimpleUploadedFile("test.jpg", content, content_type="image/jpeg")
        ImageValidator.validate_mime_type(image)

    def test_valid_png_magic_bytes(self):
        content = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
        image = SimpleUploadedFile("test.png", content, content_type="image/png")
        ImageValidator.validate_mime_type(image)

    def test_invalid_magic_bytes(self):
        content = b"This is not an image file"
        image = SimpleUploadedFile("test.jpg", content, content_type="image/jpeg")
        with pytest.raises(ValidationError):
            ImageValidator.validate_mime_type(image)

    def test_empty_file(self):
        image = SimpleUploadedFile("test.jpg", b"", content_type="image/jpeg")
        with pytest.raises(ValidationError):
            ImageValidator.validate_mime_type(image)


# ─────────────────────────────────────────────
# IngredientValidator
# ─────────────────────────────────────────────
class TestIngredientValidator:
    """IngredientValidator testleri."""

    def test_valid_name(self):
        IngredientValidator.validate_name("Patlıcan")

    def test_name_too_short(self):
        with pytest.raises(ValidationError):
            IngredientValidator.validate_name("A")

    def test_name_too_long(self):
        with pytest.raises(ValidationError):
            IngredientValidator.validate_name("A" * (MAX_INGREDIENT_NAME_LENGTH + 1))

    def test_valid_quantity(self):
        IngredientValidator.validate_quantity(500)

    def test_negative_quantity(self):
        with pytest.raises(ValidationError):
            IngredientValidator.validate_quantity(-1)


# ─────────────────────────────────────────────
# CommentValidator
# ─────────────────────────────────────────────
class TestCommentValidatorContent:
    """CommentValidator.validate_content testleri."""

    def test_valid_content(self):
        CommentValidator.validate_content("Bu tarif çok güzelmiş, teşekkürler!")

    def test_content_too_short(self):
        with pytest.raises(ValidationError):
            CommentValidator.validate_content("Güzel")

    def test_content_too_long(self):
        with pytest.raises(ValidationError):
            CommentValidator.validate_content("A" * (MAX_COMMENT_LENGTH + 1))
