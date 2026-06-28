import json
from django.core.management.base import BaseCommand
from provinces.models import Province

class Command(BaseCommand):
    help = 'Türkiye\'nin 81 ilini veritabanına yükler.'

    def handle(self, *args, **kwargs):
        provinces_data = [
            {"plate_code": 1, "name": "Adana", "region": "Akdeniz", "latitude": 37.0000, "longitude": 35.3213},
            {"plate_code": 2, "name": "Adıyaman", "region": "Güneydoğu Anadolu", "latitude": 37.7648, "longitude": 38.2786},
            {"plate_code": 3, "name": "Afyonkarahisar", "region": "Ege", "latitude": 38.7507, "longitude": 30.5567},
            {"plate_code": 4, "name": "Ağrı", "region": "Doğu Anadolu", "latitude": 39.7191, "longitude": 43.0503},
            {"plate_code": 5, "name": "Amasya", "region": "Karadeniz", "latitude": 40.6499, "longitude": 35.8353},
            {"plate_code": 6, "name": "Ankara", "region": "İç Anadolu", "latitude": 39.9208, "longitude": 32.8541},
            {"plate_code": 7, "name": "Antalya", "region": "Akdeniz", "latitude": 36.8841, "longitude": 30.7056},
            {"plate_code": 8, "name": "Artvin", "region": "Karadeniz", "latitude": 41.1828, "longitude": 41.8183},
            {"plate_code": 9, "name": "Aydın", "region": "Ege", "latitude": 37.8390, "longitude": 27.8456},
            {"plate_code": 10, "name": "Balıkesir", "region": "Marmara", "latitude": 39.6484, "longitude": 27.8826},
            {"plate_code": 11, "name": "Bilecik", "region": "Marmara", "latitude": 40.1451, "longitude": 29.9798},
            {"plate_code": 12, "name": "Bingöl", "region": "Doğu Anadolu", "latitude": 38.8854, "longitude": 40.4980},
            {"plate_code": 13, "name": "Bitlis", "region": "Doğu Anadolu", "latitude": 38.4006, "longitude": 42.1095},
            {"plate_code": 14, "name": "Bolu", "region": "Karadeniz", "latitude": 40.7392, "longitude": 31.6116},
            {"plate_code": 15, "name": "Burdur", "region": "Akdeniz", "latitude": 37.7183, "longitude": 30.2823},
            {"plate_code": 16, "name": "Bursa", "region": "Marmara", "latitude": 40.1826, "longitude": 29.0669},
            {"plate_code": 17, "name": "Çanakkale", "region": "Marmara", "latitude": 40.1553, "longitude": 26.4089},
            {"plate_code": 18, "name": "Çankırı", "region": "İç Anadolu", "latitude": 40.6013, "longitude": 33.6134},
            {"plate_code": 19, "name": "Çorum", "region": "Karadeniz", "latitude": 40.5489, "longitude": 34.9533},
            {"plate_code": 20, "name": "Denizli", "region": "Ege", "latitude": 37.7765, "longitude": 29.0864},
            {"plate_code": 21, "name": "Diyarbakır", "region": "Güneydoğu Anadolu", "latitude": 37.9144, "longitude": 40.2306},
            {"plate_code": 22, "name": "Edirne", "region": "Marmara", "latitude": 41.6818, "longitude": 26.5623},
            {"plate_code": 23, "name": "Elazığ", "region": "Doğu Anadolu", "latitude": 38.6810, "longitude": 39.2264},
            {"plate_code": 24, "name": "Erzincan", "region": "Doğu Anadolu", "latitude": 39.7500, "longitude": 39.5000},
            {"plate_code": 25, "name": "Erzurum", "region": "Doğu Anadolu", "latitude": 39.9000, "longitude": 41.2700},
            {"plate_code": 26, "name": "Eskişehir", "region": "İç Anadolu", "latitude": 39.7767, "longitude": 30.5206},
            {"plate_code": 27, "name": "Gaziantep", "region": "Güneydoğu Anadolu", "latitude": 37.0662, "longitude": 37.3833},
            {"plate_code": 28, "name": "Giresun", "region": "Karadeniz", "latitude": 40.9128, "longitude": 38.3895},
            {"plate_code": 29, "name": "Gümüşhane", "region": "Karadeniz", "latitude": 40.4600, "longitude": 39.4817},
            {"plate_code": 30, "name": "Hakkari", "region": "Doğu Anadolu", "latitude": 37.5833, "longitude": 43.7333},
            {"plate_code": 31, "name": "Hatay", "region": "Akdeniz", "latitude": 36.4018, "longitude": 36.3498},
            {"plate_code": 32, "name": "Isparta", "region": "Akdeniz", "latitude": 37.7648, "longitude": 30.5566},
            {"plate_code": 33, "name": "Mersin", "region": "Akdeniz", "latitude": 36.8000, "longitude": 34.6333},
            {"plate_code": 34, "name": "İstanbul", "region": "Marmara", "latitude": 41.0082, "longitude": 28.9784},
            {"plate_code": 35, "name": "İzmir", "region": "Ege", "latitude": 38.4192, "longitude": 27.1287},
            {"plate_code": 36, "name": "Kars", "region": "Doğu Anadolu", "latitude": 40.6013, "longitude": 43.0975},
            {"plate_code": 37, "name": "Kastamonu", "region": "Karadeniz", "latitude": 41.3887, "longitude": 33.7827},
            {"plate_code": 38, "name": "Kayseri", "region": "İç Anadolu", "latitude": 38.7312, "longitude": 35.4787},
            {"plate_code": 39, "name": "Kırklareli", "region": "Marmara", "latitude": 41.7333, "longitude": 27.2167},
            {"plate_code": 40, "name": "Kırşehir", "region": "İç Anadolu", "latitude": 39.1425, "longitude": 34.1709},
            {"plate_code": 41, "name": "Kocaeli", "region": "Marmara", "latitude": 40.8533, "longitude": 29.8815},
            {"plate_code": 42, "name": "Konya", "region": "İç Anadolu", "latitude": 37.8667, "longitude": 32.4833},
            {"plate_code": 43, "name": "Kütahya", "region": "Ege", "latitude": 39.4167, "longitude": 29.9833},
            {"plate_code": 44, "name": "Malatya", "region": "Doğu Anadolu", "latitude": 38.3552, "longitude": 38.3095},
            {"plate_code": 45, "name": "Manisa", "region": "Ege", "latitude": 38.6191, "longitude": 27.4289},
            {"plate_code": 46, "name": "Kahramanmaraş", "region": "Akdeniz", "latitude": 37.5858, "longitude": 36.9371},
            {"plate_code": 47, "name": "Mardin", "region": "Güneydoğu Anadolu", "latitude": 37.3212, "longitude": 40.7245},
            {"plate_code": 48, "name": "Muğla", "region": "Ege", "latitude": 37.2153, "longitude": 28.3636},
            {"plate_code": 49, "name": "Muş", "region": "Doğu Anadolu", "latitude": 38.7432, "longitude": 41.4910},
            {"plate_code": 50, "name": "Nevşehir", "region": "İç Anadolu", "latitude": 38.6244, "longitude": 34.7144},
            {"plate_code": 51, "name": "Niğde", "region": "İç Anadolu", "latitude": 37.9667, "longitude": 34.6833},
            {"plate_code": 52, "name": "Ordu", "region": "Karadeniz", "latitude": 40.9839, "longitude": 37.8764},
            {"plate_code": 53, "name": "Rize", "region": "Karadeniz", "latitude": 41.0201, "longitude": 40.5234},
            {"plate_code": 54, "name": "Sakarya", "region": "Marmara", "latitude": 40.7569, "longitude": 30.3783},
            {"plate_code": 55, "name": "Samsun", "region": "Karadeniz", "latitude": 41.2867, "longitude": 36.3300},
            {"plate_code": 56, "name": "Siirt", "region": "Güneydoğu Anadolu", "latitude": 37.9333, "longitude": 41.9500},
            {"plate_code": 57, "name": "Sinop", "region": "Karadeniz", "latitude": 42.0231, "longitude": 35.1531},
            {"plate_code": 58, "name": "Sivas", "region": "İç Anadolu", "latitude": 39.7477, "longitude": 37.0179},
            {"plate_code": 59, "name": "Tekirdağ", "region": "Marmara", "latitude": 40.9833, "longitude": 27.5167},
            {"plate_code": 60, "name": "Tokat", "region": "Karadeniz", "latitude": 40.3167, "longitude": 36.5500},
            {"plate_code": 61, "name": "Trabzon", "region": "Karadeniz", "latitude": 41.0015, "longitude": 39.7178},
            {"plate_code": 62, "name": "Tunceli", "region": "Doğu Anadolu", "latitude": 39.1079, "longitude": 39.5401},
            {"plate_code": 63, "name": "Şanlıurfa", "region": "Güneydoğu Anadolu", "latitude": 37.1500, "longitude": 38.8000},
            {"plate_code": 64, "name": "Uşak", "region": "Ege", "latitude": 38.6823, "longitude": 29.4082},
            {"plate_code": 65, "name": "Van", "region": "Doğu Anadolu", "latitude": 38.4891, "longitude": 43.3889},
            {"plate_code": 66, "name": "Yozgat", "region": "İç Anadolu", "latitude": 39.8181, "longitude": 34.8147},
            {"plate_code": 67, "name": "Zonguldak", "region": "Karadeniz", "latitude": 41.4564, "longitude": 31.7762},
            {"plate_code": 68, "name": "Aksaray", "region": "İç Anadolu", "latitude": 38.3687, "longitude": 34.0370},
            {"plate_code": 69, "name": "Bayburt", "region": "Karadeniz", "latitude": 40.2552, "longitude": 40.2249},
            {"plate_code": 70, "name": "Karaman", "region": "İç Anadolu", "latitude": 37.1811, "longitude": 33.2222},
            {"plate_code": 71, "name": "Kırıkkale", "region": "İç Anadolu", "latitude": 39.8468, "longitude": 33.5153},
            {"plate_code": 72, "name": "Batman", "region": "Güneydoğu Anadolu", "latitude": 37.8812, "longitude": 41.1351},
            {"plate_code": 73, "name": "Şırnak", "region": "Güneydoğu Anadolu", "latitude": 37.5228, "longitude": 42.4594},
            {"plate_code": 74, "name": "Bartın", "region": "Karadeniz", "latitude": 41.6344, "longitude": 32.3375},
            {"plate_code": 75, "name": "Ardahan", "region": "Doğu Anadolu", "latitude": 41.1105, "longitude": 42.7022},
            {"plate_code": 76, "name": "Iğdır", "region": "Doğu Anadolu", "latitude": 39.9237, "longitude": 44.0450},
            {"plate_code": 77, "name": "Yalova", "region": "Marmara", "latitude": 40.6500, "longitude": 29.2667},
            {"plate_code": 78, "name": "Karabük", "region": "Karadeniz", "latitude": 41.2061, "longitude": 32.6228},
            {"plate_code": 79, "name": "Kilis", "region": "Güneydoğu Anadolu", "latitude": 36.7184, "longitude": 37.1147},
            {"plate_code": 80, "name": "Osmaniye", "region": "Akdeniz", "latitude": 37.0742, "longitude": 36.2475},
            {"plate_code": 81, "name": "Düzce", "region": "Karadeniz", "latitude": 40.8438, "longitude": 31.1565},
        ]

        created_count = 0
        for data in provinces_data:
            province, created = Province.objects.get_or_create(
                plate_code=data["plate_code"],
                defaults={
                    "name": data["name"],
                    "region": data["region"],
                    "latitude": data["latitude"],
                    "longitude": data["longitude"]
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Başarıyla {created_count} yeni il eklendi. Toplam 81 il mevcut.'))
