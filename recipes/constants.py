"""
Recipes application constants.

Tüm sınır değerleri ve sabitler burada tanımlanır.
Magic number kullanımını engeller.
"""

from __future__ import annotations

# ─────────────────────────────────────────────
# Title
# ─────────────────────────────────────────────
MIN_TITLE_LENGTH = 3
MAX_TITLE_LENGTH = 255

# ─────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────
MIN_SUMMARY_LENGTH = 30
MAX_SUMMARY_LENGTH = 1000

# ─────────────────────────────────────────────
# Instructions
# ─────────────────────────────────────────────
MIN_INSTRUCTIONS_LENGTH = 50
MAX_INSTRUCTIONS_LENGTH = 10000

# ─────────────────────────────────────────────
# Time (dakika cinsinden)
# ─────────────────────────────────────────────
MIN_TIME_MINUTES = 0
MAX_TIME_MINUTES = 1440  # 24 saat

# ─────────────────────────────────────────────
# Servings
# ─────────────────────────────────────────────
MIN_SERVINGS = 1
MAX_SERVINGS = 100

# ─────────────────────────────────────────────
# Category
# ─────────────────────────────────────────────
MIN_CATEGORY_NAME_LENGTH = 2
MAX_CATEGORY_NAME_LENGTH = 100
MAX_CATEGORY_DESCRIPTION_LENGTH = 1000

# ─────────────────────────────────────────────
# Cuisine
# ─────────────────────────────────────────────
MIN_CUISINE_NAME_LENGTH = 2
MAX_CUISINE_NAME_LENGTH = 100
MAX_CUISINE_DESCRIPTION_LENGTH = 1000

# ─────────────────────────────────────────────
# Tag
# ─────────────────────────────────────────────
MIN_TAG_NAME_LENGTH = 2
MAX_TAG_NAME_LENGTH = 50
MAX_TAG_DESCRIPTION_LENGTH = 500

# ─────────────────────────────────────────────
# Image
# ─────────────────────────────────────────────
MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB
MIN_IMAGE_SIZE_BYTES = 2048  # 2 KB — bundan küçükse muhtemelen bozuk dosya
ALLOWED_IMAGE_EXTENSIONS = frozenset({".jpg", ".jpeg", ".png", ".webp"})
ALLOWED_IMAGE_MIME_TYPES = frozenset({
    "image/jpeg",
    "image/png",
    "image/webp",
})

# ─────────────────────────────────────────────
# Ingredient
# ─────────────────────────────────────────────
MIN_INGREDIENT_NAME_LENGTH = 2
MAX_INGREDIENT_NAME_LENGTH = 100
MAX_INGREDIENT_QUANTITY = 99999
MIN_INGREDIENT_QUANTITY = 0

# ─────────────────────────────────────────────
# Comment
# ─────────────────────────────────────────────
MIN_COMMENT_LENGTH = 10
MAX_COMMENT_LENGTH = 2000
COMMENT_COOLDOWN_SECONDS = 60  # Aynı kullanıcı 60 saniye içinde tekrar yorum yapamaz

# ─────────────────────────────────────────────
# Contact Form
# ─────────────────────────────────────────────
MIN_CONTACT_NAME_LENGTH = 2
MAX_CONTACT_NAME_LENGTH = 100
MIN_CONTACT_SUBJECT_LENGTH = 5
MAX_CONTACT_SUBJECT_LENGTH = 200
MIN_CONTACT_MESSAGE_LENGTH = 20
MAX_CONTACT_MESSAGE_LENGTH = 5000

# ─────────────────────────────────────────────
# Pagination
# ─────────────────────────────────────────────
DEFAULT_PAGE_SIZE = 24
SEARCH_PAGE_SIZE = 24

# ─────────────────────────────────────────────
# Related recipes
# ─────────────────────────────────────────────
RELATED_RECIPES_LIMIT = 6
