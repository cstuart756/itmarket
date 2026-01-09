from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from marketplace.models import Product


class ProductViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass12345")
        self.client.login(username="user1", password="pass12345")

        self.product = Product.objects.create(
            owner=self.user,
            title="Phone",
            description="Smartphone",
            price=500
        )

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Phone")

    def test_product_create_view(self):
        response = self.client.post(reverse("product_create"), {
            "title": "Tablet",
            "description": "Android tablet",
            "price": 300
        })
        self.assertEqual(Product.objects.count(), 2)

    def test_product_update_view(self):
        response = self.client.post(reverse("product_update", args=[self.product.id]), {
            "title": "Updated Phone",
            "description": "Updated",
            "price": 550
        })
        self.product.refresh_from_db()
        self.assertEqual(self.product.title, "Updated Phone")

    def test_product_delete_view(self):
        response = self.client.post(reverse("product_delete", args=[self.product.id]))
        self.assertEqual(Product.objects.count(), 0)
