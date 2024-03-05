# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


# Ojt Trainees
@login_required(login_url="/login")
def limit(request):
    return render(request, "6_limit/index.html")
    
    