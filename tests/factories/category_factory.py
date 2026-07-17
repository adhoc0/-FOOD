"""
Test factories — Category.

factory-boy ile Category test verileri.
"""

import factory

from recipes.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    """Kategori factory."""

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Kategori {n}")
    slug = factory.LazyAttribute(lambda obj: f"kategori-{obj.name.split()[-1].lower()}")
    description = factory.Faker("paragraph", locale="tr_TR")
    is_active = True
