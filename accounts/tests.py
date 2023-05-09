from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="daniel", email="daniel@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "daniel")
        self.assertEqual(user.email, "daniel@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="superuser",
            email="superuser@email.com",
            password="testpass123",
        )
        self.assertEqual(superuser.username, "superuser")
        self.assertEqual(superuser.email, "superuser@email.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
