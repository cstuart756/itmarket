from django import forms
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    """
    Enforces UI constraints (min/maxlength) and provides friendly validation errors.
    Model validators still provide the security layer.
    """

    class Meta:
        model = Product
        fields = ["category", "title", "description", "price"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "maxlength": str(Product.MAX_DESCRIPTION_LENGTH),
                    "placeholder": "Describe the product (condition, specs, included items, etc.)",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "step": "0.01",
                    "placeholder": "0.00",
                }
            ),
        }

    def clean_description(self):
        desc = (self.cleaned_data.get("description") or "").strip()
        max_len = Product.MAX_DESCRIPTION_LENGTH
        if len(desc) > max_len:
            raise forms.ValidationError(
                f"Description is too long ({len(desc)} characters). Maximum is {max_len}."
            )
        return desc

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            return price
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text", "is_primary"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "alt_text": forms.TextInput(attrs={"class": "form-control"}),
            "is_primary": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
