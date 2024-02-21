# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout





def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return redirect("/login")

    return render(request, "auth/_login.html", {})


def logout_page(request):
    logout(request)
    return redirect("/login")
