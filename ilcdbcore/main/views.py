# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.db.models import Count
import json

from .models import Intern_Table

# Create your views here.


# Create your views here.
@login_required(login_url="/login")
def dashboard_page(request):

    # Query the database to get the count of interns for each province
    province_counts = Intern_Table.objects.values("province").annotate(
        count=Count("id")
    )

    # Extracting data for chart
    labels = [item["province"] for item in province_counts]
    counts = [item["count"] for item in province_counts]

    # Creating a dictionary to hold the chart data
    chart_data = {
        "labels": labels,
        "counts": counts,
    }

    # Converting chart data to JSON format
    chart_data_json = json.dumps(chart_data)

    return render(request, "1_dash_page/index.html", {"chart_data": chart_data_json})


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
