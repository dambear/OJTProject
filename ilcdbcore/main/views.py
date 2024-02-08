from django.shortcuts import render

# Create your views here.


# Create your views here.
def dashboard(request):
    return render(request, "1_dash_page/index.html")


# EPMD
def epmd_ojt(request):
    return render(request, "3_epmd_page/ojt/index.html")
