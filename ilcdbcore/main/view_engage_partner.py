# myapp/views.py
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Engage_Partners_Table

# Create your views here.


# Ojt Trainees
def epmd_engage_partner(request):
    partners = Engage_Partners_Table.objects.all()
    return render(request, "3_epmd_page/partner/index.html", {"partners": partners})


def view_data_engage_partner(request, partner_id):

    partners = get_object_or_404(Engage_Partners_Table, id=partner_id)

    return render(request, "3_epmd_page/partner/view_data_partner.html", {"partner": partners})


def add_data_engage_partner(request):
    if request.method == "POST":
        # Get the form data from POST request
        


        # Create a new intern_table instance with the form data
        new_partner = Engage_Partners_Table(
           
        )

        # Save the new intern_table instance
        new_partner.save()

        # Redirect to a specific page (change "epmd_ojt" to your desired URL name)
        return redirect("epmd_partners")
    else:
        # Render the form page if the request method is not POST
        return render(request, "3_epmd_page/ojt/add_data_ojt.html")







def update_data_engage_partner(request, partner_id):
  
    partner = get_object_or_404(Engage_Partners_Table, id=partner_id)

    if request.method == "POST":
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        
       

        # Update the fields of the retrieved application object
        
        # Save the updated application object to the database
        partner.save()

        # Redirect to a success page or any other page
        return redirect(
            "epmd_partners"
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "3_epmd_page/partner/update_data_partner.html", {"partner": partner})




def delete_data_engage_partner(request, partner_id):
    # Get the intern instance to be deleted or return 404 if not found
    partner = get_object_or_404(Engage_Partners_Table, id=partner_id)

    if request.method == "POST":
        # Delete the intern instance
        partner.delete()

        return redirect("epmd_ojt")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(request, "3_epmd_page/ojt/delete_confirmation.html", {"partner": partner})







