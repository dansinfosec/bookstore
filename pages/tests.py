from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomePageViewTests(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_view_displays_homepage_content(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class HomePageTests(SimpleTestCase):
    # its best top be over descriptive with your unit tests.
    # each method must start with test
    # the two tests here check that the http status code of the homepage equals 200
    # we're creating a variable called response and then uses assertEqual to check that the status code matches 200
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # here we will test that the homepage uses the correct template
    def test_simplehome_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    # here we will test if the homepage is using the correct html and also does not have incorrect text
    def test_homepage_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "home page")

    def test_homepage_does_not_contain_incorrect(self):
        response = self.client.get("/")
        self.assertNotContains(response, "hi there! i should not be on this page")
