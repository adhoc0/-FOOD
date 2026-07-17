"""
Recipe image validations.

Yüklenen görsellerin güvenlik ve kalite kontrolünü sağlar.
Dosya uzantısı, MIME type (magic bytes) ve boyut doğrulaması yapar.
"""

from __future__ import annotations

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    ALLOWED_IMAGE_EXTENSIONS,
    ALLOWED_IMAGE_MIME_TYPES,
    MAX_IMAGE_SIZE_BYTES,
    MIN_IMAGE_SIZE_BYTES,
)

# JPEG, PNG ve WebP için magic byte imzaları
_MAGIC_BYTES: dict[str, tuple[bytes, ...]] = {
    "image/jpeg": (b"\xff\xd8\xff",),
    "image/png": (b"\x89PNG\r\n\x1a\n",),
    "image/webp": (b"RIFF",),
}


class ImageValidator:
    """Recipe image validations."""

    # ─────────────────────────────────────────
    # File size
    # ─────────────────────────────────────────
    @staticmethod
    def validate_size(image: UploadedFile) -> None:
        """Dosya boyutu doğrulaması."""
        if image.size is None:
            raise ValidationError(
                _("Dosya boyutu belirlenemedi."),
            )

        if image.size < MIN_IMAGE_SIZE_BYTES:
            raise ValidationError(
                _("Dosya çok küçük. Minimum boyut 1 KB olmalıdır."),
            )

        max_mb = MAX_IMAGE_SIZE_BYTES // (1024 * 1024)

        if image.size > MAX_IMAGE_SIZE_BYTES:
            raise ValidationError(
                _("Resim boyutu %(max)d MB'dan büyük olamaz."),
                params={"max": max_mb},
            )

    # ─────────────────────────────────────────
    # File extension
    # ─────────────────────────────────────────
    @staticmethod
    def validate_extension(image: UploadedFile) -> None:
        """Dosya uzantısı doğrulaması."""
        name = image.name.lower() if image.name else ""

        if not any(name.endswith(ext) for ext in ALLOWED_IMAGE_EXTENSIONS):
            allowed_str = ", ".join(sorted(ALLOWED_IMAGE_EXTENSIONS))
            raise ValidationError(
                _("Desteklenmeyen dosya formatı. İzin verilen: %(allowed)s"),
                params={"allowed": allowed_str},
            )

    # ─────────────────────────────────────────
    # MIME type (magic bytes)
    # ─────────────────────────────────────────
    @staticmethod
    def validate_mime_type(image: UploadedFile) -> None:
        """
        Magic bytes ile gerçek dosya tipini doğrular.

        Dosya uzantısı değiştirilerek yapılan saldırıları engeller.
        Sadece uzantıya güvenmek güvenlik açığı oluşturur.
        """
        try:
            # Dosyanın başındaki byte'ları oku
            image.seek(0)
            header = image.read(16)
            image.seek(0)
        except (OSError, AttributeError) as err:
            raise ValidationError(
                _("Dosya içeriği okunamadı."),
            ) from err

        if not header:
            raise ValidationError(
                _("Boş dosya yüklenemez."),
            )

        for mime_type, signatures in _MAGIC_BYTES.items():
            if mime_type in ALLOWED_IMAGE_MIME_TYPES:
                for signature in signatures:
                    if header.startswith(signature):
                        return

        allowed_str = ", ".join(sorted(ALLOWED_IMAGE_EXTENSIONS))
        raise ValidationError(
            _("Dosya içeriği izin verilen bir görsel formatı değil. İzin verilen: %(allowed)s"),
            params={"allowed": allowed_str},
        )

    # ─────────────────────────────────────────
    # Compose — Tüm doğrulamaları tek seferde çalıştır
    # ─────────────────────────────────────────
    @classmethod
    def validate_image(cls, image: UploadedFile) -> None:
        """Tüm görsel doğrulamalarını sırayla çalıştırır."""
        cls.validate_size(image)
        cls.validate_extension(image)
        cls.validate_mime_type(image)
