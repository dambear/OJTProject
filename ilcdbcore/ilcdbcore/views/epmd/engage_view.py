# myapp/views.py
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Engage_Partners_Table
from django.contrib.auth.decorators import login_required

# Create your views here.


# Ojt Trainees
@login_required(login_url="/login")
def epmd_engage(request):
    engage_partner = Engage_Partners_Table.objects.all()
    return render(request, "3_epmd/2_engage/index.html", {"engage_partner": engage_partner})

@login_required(login_url="/login")
def view_data_engage(request, engage_id):
    engage = get_object_or_404(Engage_Partners_Table, id=engage_id)
    return render(request, "3_epmd/2_engage/view_data_engage.html", {"engage": engage})


def add_data_engage(request):
    if request.method == "POST":
        # Get the form data from POST request
        province = request.POST.get("province")
        category = request.POST.get("category")
        name_of_partner_or_office = request.POST.get("name_of_partner_or_office")
        address = request.POST.get("address")
        contact_person = request.POST.get("contact_person")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        date_engaged = request.POST.get("date_engaged")
        engagement_mode = request.POST.get("engagement_mode")
        loi = request.POST.get("loi")
        remarks = request.POST.get("remarks")

        # Create a new PartnerEngagement instance with the form data
        new_engagement = Engage_Partners_Table(
            province=province,
            category=category,
            name_of_partner_or_office=name_of_partner_or_office,
            address=address,
            contact_person=contact_person,
            email=email,
            contact_number=contact_number,
            date_engaged=date_engaged,
            engagement_mode=engagement_mode,
            loi=loi,
            remarks=remarks
        )

        # Save the new PartnerEngagement instance
        new_engagement.save()

        # Redirect to a specific page (change "partner_engagement" to your desired URL name)
        return redirect("epmd_engage")
    else:
        # Render the form page if the request method is not POST
        return render(request, "3_epmd/2_engage/add_data_engage.html")





def update_data_engage(request, engage_id):
  
    engage = get_object_or_404(Engage_Partners_Table, id=engage_id)
    if request.method == "POST":
        # Handle form submission to update data
        province = request.POST.get("province")
        category = request.POST.get("category")
        name_of_partner_or_office = request.POST.get("name_of_partner_or_office")
        address = request.POST.get("address")
        contact_person = request.POST.get("contact_person")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        date_engaged = request.POST.get("date_engaged")
        engagement_mode = request.POST.get("engagement_mode")
        loi = request.POST.get("loi")
        remarks = request.POST.get("remarks")

        # Update the fields of the retrieved engagement object
        engage.province = province
        engage.category = category
        engage.name_of_partner_or_office = name_of_partner_or_office
        engage.address = address
        engage.contact_person = contact_person
        engage.email = email
        engage.contact_number = contact_number
        engage.date_engaged = date_engaged
        engage.engagement_mode = engagement_mode
        engage.loi = loi
        engage.remarks = remarks

        # Save the updated engagement object to the database
        engage.save()

 # Redirect to a success page or any other page
        return redirect(
            "epmd_engage"
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "3_epmd/2_engage/update_data_engage.html", {"engage": engage})



def delete_data_engage(request, engage_id):
    # Get the intern instance to be deleted or return 404 if not found
    engage = get_object_or_404(Engage_Partners_Table, id=engage_id)

    if request.method == "POST":
        # Delete the intern instance
        engage.delete()

        return redirect("epmd_engage")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(request, "3_epmd/2_engage/delete_confirmation.html", {"engage": engage})

