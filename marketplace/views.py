from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, ProductImage
from .forms import ProductForm, ProductImageForm


def product_list(request):
    products = (
        Product.objects.all()
        .select_related("owner", "category")
        .prefetch_related("images")
    )
    return render(request, "marketplace/product_list.html", {"products": products})


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            messages.success(request, "Product created successfully.")
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "marketplace/product_form.html", {"form": form, "mode": "Create"})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "marketplace/product_form.html", {"form": form, "mode": "Update"})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("product_list")

    return render(request, "marketplace/product_confirm_delete.html", {"product": product})


@login_required
def product_add_image(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.product = product
            img.uploaded_by = request.user

            if img.is_primary:
                ProductImage.objects.filter(product=product, is_primary=True).update(is_primary=False)

            img.save()
            messages.success(request, "Image uploaded successfully.")
            return redirect("product_list")
    else:
        form = ProductImageForm()

    return render(request, "marketplace/product_image_form.html", {"form": form, "product": product})


@login_required
def product_delete_image(request, image_id):
    image = get_object_or_404(ProductImage, pk=image_id)

    if image.product.owner != request.user:
        raise Http404("Not found")

    if request.method == "POST":
        image.delete()
        messages.success(request, "Image deleted successfully.")
        return redirect("product_list")

    return render(request, "marketplace/product_image_confirm_delete.html", {"image": image})
