from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Özel kullanıcı modeli.

    Neden AbstractUser?
    ─────────────────────────────────────────────
    1. AbstractUser, username/email/first_name/last_name gibi
       temel alanları hazır getirir. Sıfırdan yazmaya gerek yok.

    2. AbstractBaseUser'dan farklı olarak, Django'nun tüm
       izin sistemi (groups, permissions) dahildir.

    3. Şu an ekstra alan eklenmese bile, ileride (profil fotoğrafı,
       bio, favori sayısı vb.) sorunsuzca genişletilebilir.

    UYARI: Bu model ilk migration'dan ÖNCE tanımlanmalıdır.
    Sonradan AUTH_USER_MODEL değiştirmek migration cehennemine
    yol açar.
    """

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
        ordering = ['-date_joined']

    def __str__(self):
        """
        Admin panelinde ve shell'de kullanıcıyı temsil eder.
        full_name varsa onu, yoksa username gösterir.
        """
        full_name = self.get_full_name()
        return full_name if full_name else self.username
