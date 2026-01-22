from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.db.models import Q
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    MAX_DESCRIPTION_LENGTH = 500

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    title = models.CharField(max_length=120)
    description = models.TextField(
        validators=[MaxLengthValidator(MAX_DESCRIPTION_LENGTH)]
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [
            models.CheckConstraint(
                check=Q(price__gte=0),
                name="product_price_gte_0",
            ),
        ]

    @property
    def primary_image(self):
        return self.images.first()

    @property
    def display_image(self):
        return self.primary_image

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="uploaded_images",
    )
    image = CloudinaryField("image")
    alt_text = models.CharField(max_length=125, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-is_primary", "-created_at")

    @property
    def image_secure_url(self) -> str:
        """
        Always return an https URL for the Cloudinary asset.
        Prefer secure_url; fallback to upgrading url.
        Handles http:// and protocol-relative // URLs.
        """
        secure = getattr(self.image, "secure_url", None)
        if isinstance(secure, str) and secure:
            return secure

        url = (getattr(self.image, "url", "") or "").strip()

        if url.startswith("http://"):
            return "https://" + url[len("http://"):]
        if url.startswith("//"):
            return "https:" + url
        return url

    def __str__(self):
        return f"Image for {self.product.title}"
