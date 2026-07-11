from recipes.models import Tag


class TagSelector:
    """Read-only queries for tags."""

    @staticmethod
    def get_all():
        return (
            Tag.objects.filter(
                is_active=True,
            )
            .order_by(
                "name",
            )
        )

    @staticmethod
    def get_by_slug(slug: str):
        return Tag.objects.filter(
            slug=slug,
            is_active=True,
        ).first()

    @staticmethod
    def get_count() -> int:
        return Tag.objects.filter(
            is_active=True,
        ).count()