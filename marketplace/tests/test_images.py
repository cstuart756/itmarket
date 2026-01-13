from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch

from marketplace.models import Product, ProductImage


class ProductImageTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")

        self.product = Product.objects.create(
            owner=self.owner,
            title="Phone",
            description="New phone",
            price="200.00",
        )

    @patch("cloudinary.uploader.upload")
    def test_owner_can_upload_image_and_sees_message(self, mock_upload):
        mock_upload.return_value = {
            "public_id": "abc",
            "version": "1",
            "signature": "sig",
            "secure_url": "http://example.com/img.jpg",
        }

        self.client.login(username="owner", password="pass12345")

        res = self.client.post(
            reverse("product_add_image", args=[self.product.id]),
            {
                "alt_text": "Phone image",
                "is_primary": True,
                "image": "dummy",
            },
            follow=True
        )

        self.assertEqual(res.status_code, 200)
        self.assertTrue(ProductImage.objects.filter(product=self.product).exists())

        messages = list(res.context["messages"])
        self.assertTrue(any("Image uploaded successfully." in str(m) for m in messages))

    def test_non_owner_cannot_delete_image(self):
        img = ProductImage.objects.create(
            product=self.product,
            uploaded_by=self.owner,
            image="dummy",
            alt_text="x",
            is_primary=True
        )

        self.client.login(username="other", password="pass12345")
        res = self.client.post(reverse("product_delete_image", args=[img.id]))
        self.assertEqual(res.status_code, 404)

    @patch("cloudinary.uploader.upload")
    def test_primary_image_rule_unsets_previous_primary(self, mock_upload):
        mock_upload.return_value = {
            "public_id": "abc",
            "version": "1",
            "signature": "sig",
            "secure_url": "http://example.com/img.jpg",
        }

        self.client.login(username="owner", password="pass12345")

        # Upload first primary image
        self.client.post(
            reverse("product_add_image", args=[self.product.id]),
            {"alt_text": "First", "is_primary": True, "image": "dummy"},
            follow=True
        )

        # Upload second primary image
        self.client.post(
            reverse("product_add_image", args=[self.product.id]),
            {"alt_text": "Second", "is_primary": True, "image": "dummy"},
            follow=True
        )

        primaries = ProductImage.objects.filter(product=self.product, is_primary=True)
        self.assertEqual(primaries.count(), 1)
        self.assertEqual(primaries.first().alt_text, "Second")
