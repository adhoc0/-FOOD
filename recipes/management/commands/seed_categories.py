from django.core.management.base import BaseCommand

from recipes.models import Category

CATEGORIES = (
    "Çorba",
    "Ana Yemek",
    "Kebap",
    "Pilav",
    "Tatlı",
    "Hamur İşi",
    "Kahvaltılık",
    "Salata",
    "Meze",
    "İçecek",
)


class Command(BaseCommand):
    help = "Create default recipe categories."

    def handle(self, *args, **options):
        created = 0

        for name in CATEGORIES:
            _, is_created = Category.objects.get_or_create(
                name=name,
                defaults={
                    "is_active": True,
                },
            )

            if is_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"{created} kategori oluşturuldu."))
