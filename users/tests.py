from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTests(TestCase):
    def setUp(self):
        self.password = "TestPassword123!"
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password=self.password,
        )

    def test_login_page_is_available(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login to Tweeter")

    def test_login_works(self):
        response = self.client.post(
            reverse("login"),
            {"username": self.user.username, "password": self.password},
        )
        self.assertRedirects(response, reverse("tweet_list"))
        self.assertTrue(self.client.session.get("_auth_user_id"))

    def test_protected_tweet_creation_redirects_to_login(self):
        response = self.client.get(reverse("tweet_create"))
        expected = f"{reverse('login')}?next={reverse('tweet_create')}"
        self.assertRedirects(response, expected)
