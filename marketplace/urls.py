from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("create/", views.product_create, name="product_create"),
    path("update/<int:pk>/", views.product_update, name="product_update"),
    path("delete/<int:pk>/", views.product_delete, name="product_delete"),
    path("product/<int:pk>/images/add/", views.product_add_image, name="product_add_image"),
    path("images/<int:image_id>/delete/", views.product_delete_image, name="product_delete_image"),
]
