from django.core.exceptions import ValidationError


class ImageValidator:
    """Recipe image validations."""

    MAX_IMAGE_SIZE = 5 * 1024 * 1024

    @staticmethod
    def validate_size(image):
        if image.size > ImageValidator.MAX_IMAGE_SIZE:
            raise ValidationError(
                "Resim boyutu 5 MB'dan büyük olamaz."
            )

    @staticmethod
    def validate_extension(image):
        allowed = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
        }

        name = image.name.lower()

        if not any(
            name.endswith(ext)
            for ext in allowed
        ):
            raise ValidationError(
                "Desteklenmeyen resim formatı."
            )