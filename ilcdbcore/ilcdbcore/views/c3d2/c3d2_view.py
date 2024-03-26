
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.models import Exam_Table

@login_required(login_url="/login")
def c3d2(request):
    
    user = request.user
    
    if user.province.lower() == "cavite":
        c3d2s = Exam_Table.objects.filter(province__iexact="Cavite")
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})

    elif user.province.lower() == "laguna":
        c3d2s = Exam_Table.objects.filter(province__iexact="Laguna")
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})

    elif user.province.lower() == "batangas":
        c3d2s = Exam_Table.objects.filter(province__iexact="Batangas")
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})

    elif user.province.lower() == "rizal":
        c3d2s = Exam_Table.objects.filter(province__iexact="Rizal")
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})

    elif user.province.lower() == "quezon":
        c3d2s = Exam_Table.objects.filter(province__iexact="Quezon")
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})

    else:
        c3d2s = Exam_Table.objects.all()
        return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})
    
    
    
    

@login_required(login_url="/login")
def view_data_c3d2(request, c3d2_id):
    
    c3d2 = get_object_or_404(Exam_Table, id=c3d2_id)
    return render(request, "2_c3d2/view_data_c3d2.html", {"c3d2": c3d2})

@login_required(login_url="/login")
def add_data_c3d2(request):

    if request.method == "POST":
        province = request.POST.get("province")
        name_of_examinee = request.POST.get("name_of_examinee")
        venue_or_school = request.POST.get("venue_or_school")
        gender = request.POST.get("gender")
        time = request.POST.get("time")
        status = request.POST.get("status")
        remark_or_grade = request.POST.get("remark_or_grade")
        ilcdbcore_component= request.POST.get("ilcdbcore_component")
        date_conducted=request.POST.get("date_conducted")
        type=request.POST.get("type")

        
        date_conducted_obj = datetime.strptime(date_conducted, "%m/%d/%Y").strftime("%Y-%m-%d")
        
        new_exam = Exam_Table(
                province=province,
                name_of_examinee=name_of_examinee,
                venue_or_school=venue_or_school,
                gender=gender,
                time=time,
                status=status,
                remark_or_grade=remark_or_grade,
                ilcdbcore_component=ilcdbcore_component,
                date_conducted=date_conducted_obj,
                type=type,
                
            )

            # Save the new Intern_Table instance
        new_exam.save()

            # Redirect to a specific page (change "epmd_ojt" to your desired URL name)
        return redirect("c3d2")
    else:
        return render(request, "2_c3d2/add_data_c3d2.html")





@login_required(login_url="/login")
def update_data_c3d2(request, c3d2_id):

    c3d2 = get_object_or_404(Exam_Table, id=c3d2_id)

    if request.method == "POST":
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        province = request.POST.get("province")
        name_of_examinee = request.POST.get("name_of_examinee")
        venue_or_school = request.POST.get("venue_or_school")
        gender = request.POST.get("gender")
        time = request.POST.get("time")
        status = request.POST.get("status")
        remark_or_grade = request.POST.get("remark_or_grade")
        ilcdbcore_component= request.POST.get("ilcdbcore_component")
        date_conducted= request.POST.get("date_conducted")
        type= request.POST.get("type")

        date_conducted_obj = datetime.strptime(date_conducted, "%m/%d/%Y").strftime("%Y-%m-%d")

        # Update the fields of the retrieved application object
        c3d2.province = province
        c3d2.name_of_examinee = name_of_examinee
        c3d2.venue_or_school = venue_or_school
        c3d2.gender = gender
        c3d2.time = time
        c3d2.status = status
        c3d2.remark_or_grade = remark_or_grade
        c3d2.ilcdbcore_component = ilcdbcore_component
        c3d2.date_conducted = date_conducted_obj
        c3d2.type = type

        # Save the updated application object to the database
        c3d2.save()

        # Redirect to a success page or any other page
        return redirect(
            "c3d2"
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "2_c3d2/update_data_c3d2.html", {"c3d2": c3d2})

@login_required(login_url="/login")
def delete_data_c3d2(request, c3d2_id):
    # Get the intern instance to be deleted or return 404 if not found
    c3d2 = get_object_or_404(Exam_Table, id=c3d2_id)

    if request.method == "POST":
        # Delete the intern instance
        c3d2.delete()

        return redirect("c3d2")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(request, "2_c3d2/delete_confirmation.html", {"c3d2": c3d2})