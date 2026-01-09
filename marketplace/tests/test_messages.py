from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from marketplace.models import Product


class MessagesTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="msguser", password="password123")
        self.client.login(username="msguser", password="password123")

        self.product = Product.objects.create(
            owner=self.user,
            title="Camera",
            description="Digital Camera",
            price=450
        )

    def test_create_product_message(self):
        response = self.client.post(reverse("product_create"), {
            "title": "Headphones",
            "description": "Noise-cancelling",
            "price": 200
        }, follow=True)

        messages = list(response.context["messages"])
        self.assertTrue(any("Product created successfully." in str(m) for m in messages))

    def test_update_product_message(self):
        response = self.client.post(reverse("product_update", args=[self.product.id]), {
            "title": "Camera Pro",
            "description": "Updated Camera",
            "price": 500
        }, follow=True)

        messages = list(response.context["messages"])
        self.assertTrue(any("Product updated successfully." in str(m) for m in messages))

    def test_delete_product_message(self):
        response = self.client.post(reverse("product_delete", args=[self.product.id]), follow=True)

        messages = list(response.context["messages"])
        self.assertTrue(any("Product deleted successfully." in str(m) for m in messages))
