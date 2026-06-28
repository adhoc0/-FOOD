from django.test import TestCase

from .models import CustomUser


class CustomUserModelTest(TestCase):
    """CustomUser model temel testleri."""

    def test_create_user(self):
        """Normal kullanıcı oluşturma."""
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Superuser oluşturma."""
        admin_user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123',
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_str_with_full_name(self):
        """__str__ metodu full name varsa onu döndürmeli."""
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Ali',
            last_name='Yılmaz',
        )
        self.assertEqual(str(user), 'Ali Yılmaz')

    def test_str_without_full_name(self):
        """__str__ metodu full name yoksa username döndürmeli."""
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
        )
        self.assertEqual(str(user), 'testuser')
