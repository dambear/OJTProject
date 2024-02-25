from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from main.models import Intern_Table, Engage_Partners_Table

@login_required(login_url="/login")
def index(request):
    
    cavite_count_ojt = Intern_Table.objects.filter(province__iexact="Cavite").count()
    laguna_count_ojt = Intern_Table.objects.filter(province__iexact="Laguna").count()
    batangas_count_ojt = Intern_Table.objects.filter(province__iexact="Batangas").count()
    rizal_count_ojt = Intern_Table.objects.filter(province__iexact="Rizal").count()
    quezon_count_ojt = Intern_Table.objects.filter(province__iexact="Quezon").count()
    
    cavite_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Cavite").count()
    laguna_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Laguna").count()
    batangas_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Batangas").count()
    rizal_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Rizal").count()
    quezon_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Quezon").count()
    
    context = {
        'cavite_count_ojt': cavite_count_ojt,
        'laguna_count_ojt': laguna_count_ojt,
        'batangas_count_ojt': batangas_count_ojt,
        'rizal_count_ojt': rizal_count_ojt,
        'quezon_count_ojt': quezon_count_ojt,
        
        'cavite_count_engage': cavite_count_engage,
        'laguna_count_engage': laguna_count_engage,
        'batangas_count_engage': batangas_count_engage,
        'rizal_count_engage': rizal_count_engage,
        'quezon_count_engage': quezon_count_engage
        
        
    }
    
    
    return render(request, "1_dash/index.html", context)




