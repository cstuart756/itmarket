from django.contrib import admin
from .models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "category", "price", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description", "owner__username")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "uploaded_by", "is_primary", "created_at")
    list_filter = ("is_primary", "created_at")
    search_fields = ("product__title", "uploaded_by__username", "alt_text")
