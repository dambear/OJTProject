
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Exam_Table


def c3d2(request):
    c3d2s = Exam_Table.objects.all()
    return render(request, "2_c3d2/index.html", {"c3d2s": c3d2s})


def view_data_c3d2(request, c3d2_id):
    c3d2 = get_object_or_404(Exam_Table, id=c3d2_id)
    return render(request, "2_c3d2/view_data_c3d2.html", {"c3d2": c3d2})

def add_data_c3d2(request):

    if request.method == "POST":
        province = request.POST.get("province")
        name_of_examinee = request.POST.get("name_of_examinee")
        venue_or_school = request.POST.get("venue_or_school")
        gender = request.POST.get("gender")
        time = request.POST.get("time")
        status = request.POST.get("status")
        remark_or_grade = request.POST.get("remark_or_grade")
        
        new_exam = Exam_Table(
                province=province,
                name_of_examinee=name_of_examinee,
                venue_or_school=venue_or_school,
                gender=gender,
                time=time,
                status=status,
                remark_or_grade=remark_or_grade,
                
            )

            # Save the new Intern_Table instance
        new_exam.save()

            # Redirect to a specific page (change "epmd_ojt" to your desired URL name)
        return redirect("c3d2")
    else:
        return render(request, "2_c3d2/add_data_c3d2.html")






def update_data_c3d2(request, c3d2_id):

    c3d2 = get_object_or_404(Exam_Table, id=c3d2_id)

    if request.method == "POST":
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        province = request.POST.get("lgu_m")
        name_of_examinee = request.POST.get("name_of_examinee")
        venue_or_school = request.POST.get("venue_or_school")
        gender = request.POST.get("gender")
        time = request.POST.get("time")
        status = request.POST.get("status")
        remark_or_grade = request.POST.get("remark_or_grade")

        # Update the fields of the retrieved application object
        c3d2.province = province
        c3d2.name_of_examinee = name_of_examinee
        c3d2.venue_or_school = venue_or_school
        c3d2.gender = gender
        c3d2.time = time
        c3d2.status = status
        c3d2.remark_or_grade = remark_or_grade
        

        # Save the updated application object to the database
        c3d2.save()

        # Redirect to a success page or any other page
        return redirect(
            "c3d2"
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "2_c3d2/update_data_c3d2.html", {"c3d2": c3d2})


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