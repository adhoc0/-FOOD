"""
Test factories — Province & Region.

factory-boy ile Province ve Region test verileri.
"""

import factory

from provinces.models import Province, Region


class RegionFactory(factory.django.DjangoModelFactory):
    """Bölge factory."""

    class Meta:
        model = Region

    name = factory.Sequence(lambda n: f"Bölge {n}")
    slug = factory.LazyAttribute(lambda obj: f"bolge-{obj.name.split()[-1].lower()}")
    is_active = True


class ProvinceFactory(factory.django.DjangoModelFactory):
    """İl factory."""

    class Meta:
        model = Province

    region = factory.SubFactory(RegionFactory)
    plate_code = factory.Sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f"İl {n}")
    slug = factory.LazyAttribute(lambda obj: f"il-{obj.plate_code}")
    description = factory.Faker("paragraph", locale="tr_TR")
    latitude = factory.Faker(
        "pydecimal",
        left_digits=2,
        right_digits=6,
        min_value=36,
        max_value=42,
    )
    longitude = factory.Faker(
        "pydecimal",
        left_digits=2,
        right_digits=6,
        min_value=26,
        max_value=45,
    )
    is_featured = False
    is_active = True
