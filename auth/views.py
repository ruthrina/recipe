from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse
from django.contrib import messages

# Create your views here.


def login_user(request):
    form = AuthenticationForm()

    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect(reverse("home"))

        else:
            messages.error(request, "Invalid username or password")
            return redirect(reverse("home"))

    context = {"form": form}
    return render(request, "login.html", context)


def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login")
    context = {"form": form}
    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")
