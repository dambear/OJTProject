# myapp/views.py
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Training_Webinars_Table
from django.contrib.auth.decorators import login_required

# Create your views here.


# Ojt Trainees
@login_required(login_url="/login")
def training_webinar(request):
  
    tmd = Training_Webinars_Table.objects.all()
    return render(request, "3_epmd_page/ojt/index.html", {"tmd": tmd})


@login_required(login_url="/login")
def view_data_ojt(request, tmd_id):
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)
    return render(request, "3_epmd_page/ojt/view_data_ojt.html", {"tmd": tmd})


@login_required(login_url="/login")
def add_data_tmd(request):
    if request.method == "POST":
        # Get the form data from POST request

        # Create a new Training_Webinars_Table instance with the form data
        new_tmd = Training_Webinars_Table(
           
        )

        # Save the new Training_Webinars_Table instance
        new_tmd.save()

        # Redirect to a specific page (change "epmd_ojt" to your desired URL name)
        return redirect("")
    else:
        # Render the form page if the request method is not POST
        return render(request, "3_epmd_page/ojt/add_data_ojt.html")


@login_required(login_url="/login")
def update_data_ojt(request, tmd_id):

    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)

    if request.method == "POST":
        # Handle form submission to update data
      

        # Update the fields of the retrieved application object
       

        # Save the updated application object to the database
        tmd.save()

        # Redirect to a success page or any other page
        return redirect(
            ""
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "3_epmd_page/ojt/update_data_ojt.html", {"tmd": tmd})


@login_required(login_url="/login")
def delete_data_ojt(request, tmd_id):
    # Get the intern instance to be deleted or return 404 if not found
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)

    if request.method == "POST":
        # Delete the intern instance
        tmd.delete()

        return redirect("")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(request, "3_epmd_page/ojt/delete_confirmation.html", {"tmd": tmd})
