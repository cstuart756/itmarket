from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from marketplace.models import Product

class PlaceholderImageTests(TestCase):
    def test_product_list_shows_placeholder_when_no_image(self):
        user = User.objects.create_user(username="u1", password="pass12345")
        Product.objects.create(owner=user, title="No Image Product", description="x", price="10.00")

        res = self.client.get(reverse("product_list"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "marketplace/placeholders/product-default")
