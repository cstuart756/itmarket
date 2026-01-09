from django.test import TestCase
from django.contrib.auth.models import User
from marketplace.models import Product


class ProductModelTest(TestCase):

    def test_product_string_representation(self):
        user = User.objects.create_user(username="testuser", password="password123")
        product = Product.objects.create(
            owner=user,
            title="Laptop",
            description="Gaming laptop",
            price=1200
        )
        self.assertEqual(str(product), "Laptop")
