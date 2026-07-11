from recipes.models import Category


class CategorySelector:
    """Read-only queries for categories."""

    @staticmethod
    def get_all():
        return (
            Category.objects.filter(
                is_active=True,
            )
            .order_by(
                "sort_order",
                "name",
            )
        )

    @staticmethod
    def get_by_slug(slug: str):
        return Category.objects.filter(
            slug=slug,
            is_active=True,
        ).first()

    @staticmethod
    def get_count() -> int:
        return Category.objects.filter(
            is_active=True,
        ).count()