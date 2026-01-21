# accounts/views.py
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


@require_POST
@login_required
def logout_view(request):
    """
    Secure logout: POST-only with CSRF protection.
    Prevents logout via GET (logout-CSRF).
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("product_list")
