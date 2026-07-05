from provinces.models import Region


def get_regions():
    """
    Tüm bölgeleri döndürür.
    """
    return Region.objects.all()


def get_active_regions():
    """
    Aktif bölgeleri döndürür.
    """
    return Region.objects.filter(is_active=True)


def get_region_by_slug(slug: str):
    """
    Slug'a göre bölge döndürür.
    """
    return Region.objects.filter(
        slug=slug,
        is_active=True,
    ).first()