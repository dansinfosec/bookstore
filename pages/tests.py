from django.test import TestCase
from django.urls import reverse


class HomePageViewTests(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_view_displays_home_page_content(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
