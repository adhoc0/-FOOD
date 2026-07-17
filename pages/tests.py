from django.test import TestCase
from django.urls import reverse


class PagesViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_about_page(self):
        response = self.client.get(reverse("pages:about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")

    def test_contact_page(self):
        response = self.client.get(reverse("pages:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")

    def test_privacy_page(self):
        response = self.client.get(reverse("pages:privacy"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/privacy.html")

    def test_cookie_page(self):
        response = self.client.get(reverse("pages:cookies"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/cookies.html")

    def test_terms_page(self):
        response = self.client.get(reverse("pages:terms"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/terms.html")

    def test_kvkk_page(self):
        response = self.client.get(reverse("pages:kvkk"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/kvkk.html")
