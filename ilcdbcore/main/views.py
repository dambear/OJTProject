# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


# Create your views here.
@login_required(login_url="/login")
def dashboard_page(request):
    return render(request, "1_dash_page/index.html")


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return redirect("/login")

    return render(request, "auth/_login.html", {})
