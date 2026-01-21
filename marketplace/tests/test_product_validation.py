from django.test import TestCase
from django.contrib.auth.models import User
from marketplace.forms import ProductForm
from marketplace.models import Product


class ProductValidationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass12345")

    def test_negative_price_rejected(self):
        form = ProductForm(data={
            "title": "Bad Price",
            "description": "Test",
            "price": "-1.00",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)

    def test_description_too_long_rejected(self):
        too_long = "x" * (Product.MAX_DESCRIPTION_LENGTH + 1)
        form = ProductForm(data={
            "title": "Long Desc",
            "description": too_long,
            "price": "10.00",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)
