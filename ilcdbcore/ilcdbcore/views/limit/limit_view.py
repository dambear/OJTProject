# myapp/views.py
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from main.models import Limit_Table
# Create your views here.


# Ojt Trainees
@login_required(login_url="/login")
def limit(request):

    limit = get_object_or_404(Limit_Table, id=1)
    
    if request.method == "POST":
        exam_cavite_limit = request.POST.get("exam_cavite_limit")
        exam_laguna_limit = request.POST.get("exam_laguna_limit")
        exam_batangas_limit = request.POST.get("exam_batangas_limit")
        exam_rizal_limit = request.POST.get("exam_rizal_limit")
        exam_quezon_limit = request.POST.get("exam_quezon_limit")
        
        engage_cavite_limit = request.POST.get("engage_cavite_limit")
        engage_laguna_limit = request.POST.get("engage_laguna_limit")
        engage_batangas_limit = request.POST.get("engage_batangas_limit")
        engage_rizal_limit = request.POST.get("engage_rizal_limit")
        engage_quezon_limit = request.POST.get("engage_quezon_limit")
        
        ojt_cavite_limit = request.POST.get("ojt_cavite_limit")
        ojt_laguna_limit = request.POST.get("ojt_laguna_limit")
        ojt_batangas_limit = request.POST.get("ojt_batangas_limit")
        ojt_rizal_limit = request.POST.get("ojt_rizal_limit")
        ojt_quezon_limit = request.POST.get("ojt_quezon_limit")
    
        tmd_cavite_limit = request.POST.get("tmd_cavite_limit")
        tmd_laguna_limit = request.POST.get("tmd_laguna_limit")
        tmd_batangas_limit = request.POST.get("tmd_batangas_limit")
        tmd_rizal_limit = request.POST.get("tmd_rizal_limit")
        tmd_quezon_limit = request.POST.get("tmd_quezon_limit")

        # Update the fields of the retrieved application object
        limit.exam_cavite_limit = exam_cavite_limit
        limit.exam_laguna_limit = exam_laguna_limit
        limit.exam_batangas_limit = exam_batangas_limit
        limit.exam_rizal_limit = exam_rizal_limit      
        limit.exam_quezon_limit = exam_quezon_limit        
       
        limit.engage_cavite_limit = engage_cavite_limit
        limit.engage_laguna_limit = engage_laguna_limit
        limit.engage_batangas_limit = engage_batangas_limit
        limit.engage_rizal_limit = engage_rizal_limit      
        limit.engage_quezon_limit = engage_quezon_limit

        limit.ojt_cavite_limit = ojt_cavite_limit
        limit.ojt_laguna_limit = ojt_laguna_limit
        limit.ojt_batangas_limit = ojt_batangas_limit
        limit.ojt_rizal_limit = ojt_rizal_limit      
        limit.ojt_quezon_limit = ojt_quezon_limit

        limit.tmd_cavite_limit = tmd_cavite_limit
        limit.tmd_laguna_limit = tmd_laguna_limit
        limit.tmd_batangas_limit = tmd_batangas_limit
        limit.tmd_rizal_limit = tmd_rizal_limit      
        limit.tmd_quezon_limit = tmd_quezon_limit

            
        # Save the updated application object to the database
        limit.save()

          # Redirect to a success page or any other page
        return redirect(
            "/"
        )  # You can change 'epmd_ojt' to the appropriate URL name
        
    return render(request, "6_limit/index.html", {"limit": limit})  
    
