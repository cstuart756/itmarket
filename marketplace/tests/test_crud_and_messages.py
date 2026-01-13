from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from marketplace.models import Product


class ProductCRUDMessagesTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")

        self.product = Product.objects.create(
            owner=self.owner,
            title="Camera",
            description="Digital camera",
            price="100.00",
        )

    def test_product_list_page_loads(self):
        res = self.client.get(reverse("product_list"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Product Listings")

    def test_create_requires_login(self):
        res = self.client.get(reverse("product_create"))
        # Redirect to login
        self.assertEqual(res.status_code, 302)
        self.assertIn("/accounts/login/", res.url)

    def test_owner_can_create_product_and_sees_message(self):
        self.client.login(username="owner", password="pass12345")
        res = self.client.post(reverse("product_create"), {
            "title": "Headphones",
            "description": "Noise cancelling",
            "price": "50.00"
        }, follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(Product.objects.filter(title="Headphones").exists())
        messages = list(res.context["messages"])
        self.assertTrue(any("Product created successfully." in str(m) for m in messages))

    def test_owner_can_update_product_and_sees_message(self):
        self.client.login(username="owner", password="pass12345")
        res = self.client.post(reverse("product_update", args=[self.product.id]), {
            "title": "Camera Pro",
            "description": "Updated",
            "price": "150.00"
        }, follow=True)

        self.product.refresh_from_db()
        self.assertEqual(self.product.title, "Camera Pro")

        messages = list(res.context["messages"])
        self.assertTrue(any("Product updated successfully." in str(m) for m in messages))

    def test_non_owner_cannot_update_product(self):
        self.client.login(username="other", password="pass12345")
        res = self.client.get(reverse("product_update", args=[self.product.id]))
        self.assertEqual(res.status_code, 404)

    def test_owner_can_delete_product_and_sees_message(self):
        self.client.login(username="owner", password="pass12345")
        res = self.client.post(reverse("product_delete", args=[self.product.id]), follow=True)

        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

        messages = list(res.context["messages"])
        self.assertTrue(any("Product deleted successfully." in str(m) for m in messages))

    def test_non_owner_cannot_delete_product(self):
        self.client.login(username="other", password="pass12345")
        res = self.client.post(reverse("product_delete", args=[self.product.id]))
        self.assertEqual(res.status_code, 404)
