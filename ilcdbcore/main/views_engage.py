# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from main.models import engage
# Create your views here.

def engage(request):
    applications = engage.objects.all()
    return render(request, '3_epmd_page/engage/index.html',{'applications': applications})


def add_data_engage_form(request):
    return render(request, '3_epmd_page/engage/add_data_engage_form.html')

def insert_data_engage(request):
    if request.method == 'POST':
        province = request.POST.get('province')
        category = request.POST.get('category')
        nameofoffice = request.POST.get('nameofoffice')
        contactnumber = request.POST.get('contactnumber')
        
        new_application = engage(
            province=province,
            category=category,
            nameofoffice=nameofoffice,
            contactnumber=contactnumber
        )
        
        new_application.save()
        
        return redirect('engage')  # Redirect to 'epmd_ojt' URL pattern
    else:
        return HttpResponse('Please use a POST request to insert data.')
    
    
def edit_data_engage(request, application_id):
    # Retrieve the application object from the database based on the application_id
    application = get_object_or_404(engage, id=application_id)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        province = request.POST.get('province')
        category = request.POST.get('category')
        nameofoffice = request.POST.get('nameofoffice')
        contactnumber = request.POST.get('contactnumber')
        
        # Update the fields of the retrieved application object
        application.province = province
        application.category = category
        application.nameofoffice = nameofoffice
        application.contactnumber = contactnumber

        
        # Save the updated application object to the database
        application.save()
        
        # Redirect to a success page or any other page
        return redirect('engage')  # You can change 'home' to the appropriate URL name
        
    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, '3_epmd_page/engage/edit_data_engage.html', {'application': application})

def view_data_engage(request, application_id):
    # Retrieve the application object from the database based on the application_id
    application = get_object_or_404(engage, id=application_id)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        province = request.POST.get('province')
        category = request.POST.get('category')
        nameofoffice = request.POST.get('nameofoffice')
        contactnumber = request.POST.get('contactnumber')
        
        # Update the fields of the retrieved application object
        application.province = province
        application.category = category
        application.nameofoffice = nameofoffice
        application.contactnumber = contactnumber

        
        # Save the updated application object to the database
        application.save()
        
        # Redirect to a success page or any other page
        return redirect('engage')  # You can change 'home' to the appropriate URL name
        
    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, '3_epmd_page/engage/view_data_ojt.html', {'application': application})