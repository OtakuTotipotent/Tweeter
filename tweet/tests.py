from pathlib import Path
from tempfile import TemporaryDirectory

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Tweet

ONE_PIXEL_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\x0dIDAT\x08\xd7c\xf8\xff\xff?\x00\x05\xfe\x02\xfe"
    b"\xa7\xd2\xcd\x00\x00\x00\x00IEND\xaeB\x60\x82"
)


class TweetImageUploadTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )
        self.client.login(username="testuser", password="TestPassword123!")

    def test_create_tweet_accepts_image_upload(self):
        with (
            TemporaryDirectory() as media_root,
            override_settings(MEDIA_ROOT=media_root),
        ):
            image = SimpleUploadedFile(
                "create.png",
                ONE_PIXEL_PNG,
                content_type="image/png",
            )

            response = self.client.post(
                reverse("tweet_create"),
                {"text": "Tweet with image", "photo": image},
            )

            self.assertRedirects(response, reverse("tweet_list"))
            tweet = Tweet.objects.get(text="Tweet with image")
            self.assertTrue(tweet.photo.name.startswith("photos/"))
            self.assertTrue(Path(tweet.photo.path).exists())

    def test_edit_tweet_updates_text_and_image(self):
        tweet = Tweet.objects.create(user=self.user, text="Original")

        with (
            TemporaryDirectory() as media_root,
            override_settings(MEDIA_ROOT=media_root),
        ):
            image = SimpleUploadedFile(
                "edit.png",
                ONE_PIXEL_PNG,
                content_type="image/png",
            )

            response = self.client.post(
                reverse("tweet_edit", args=[tweet.pk]),
                {"text": "Updated", "photo": image},
            )

            self.assertRedirects(response, reverse("tweet_list"))
            tweet.refresh_from_db()
            self.assertEqual(tweet.text, "Updated")
            self.assertTrue(tweet.photo.name.startswith("photos/"))
            self.assertTrue(Path(tweet.photo.path).exists())
