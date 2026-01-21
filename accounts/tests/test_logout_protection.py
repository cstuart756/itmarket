from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LogoutProtectionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass12345")

    def test_logout_requires_post(self):
        self.client.login(username="u1", password="pass12345")
        res = self.client.get(reverse("logout"))
        self.assertEqual(res.status_code, 405)

    def test_logout_post_logs_user_out(self):
        self.client.login(username="u1", password="pass12345")
        res = self.client.post(reverse("logout"), follow=True)
        self.assertEqual(res.status_code, 200)

        # Confirm user is logged out
        res2 = self.client.get(reverse("product_list"))
        self.assertFalse(res2.wsgi_request.user.is_authenticated)
