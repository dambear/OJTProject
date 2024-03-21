# myapp/views.py
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from main.models import Intern_Table, UploadCache_Table

# Create your views here.


# Ojt Trainees
@login_required(login_url="/login")
def epmd_ojt(request):

    user = request.user

    if user.province.lower() == "cavite":
        ojts = Intern_Table.objects.filter(province__iexact="Cavite")
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

    elif user.province.lower() == "laguna":
        ojts = Intern_Table.objects.filter(province__iexact="Laguna")
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

    elif user.province.lower() == "batangas":
        ojts = Intern_Table.objects.filter(province__iexact="Batangas")
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

    elif user.province.lower() == "rizal":
        ojts = Intern_Table.objects.filter(province__iexact="Rizal")
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

    elif user.province.lower() == "quezon":
        ojts = Intern_Table.objects.filter(province__iexact="Quezon")
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

    else:
        ojts = Intern_Table.objects.all()
        return render(request, "3_epmd/1_ojt/index.html", {"ojts": ojts})

@login_required(login_url="/login")
def view_data_ojt(request, ojt_id):
    ojts = get_object_or_404(Intern_Table, id=ojt_id)
    return render(request, "3_epmd/1_ojt/view_data_ojt.html", {"ojt": ojts})

@login_required(login_url="/login")
def add_data_ojt(request):
    if request.method == "POST":
        # Get the form data from POST request
        ojt_duration = request.POST.get("ojt_duration")
        province = request.POST.get("province")
        school_name = request.POST.get("school_name")
        school_address = request.POST.get("school_address")
        contact_person = request.POST.get("contact_person")
        contact_number = request.POST.get("contact_number")
        student_name = request.POST.get("student_name")
        gender = request.POST.get("gender")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        mode = request.POST.get("mode")
        remarks = request.POST.get("remarks")
        
        #files
        recommendation_letter = request.FILES['recommendation_letter']
        application_form = request.FILES['application_form']
        cv_resume = request.FILES['cv_resume']
        medical_certificate = request.FILES['medical_certificate']
        workplan_form = request.FILES['workplan_form']
        interview_form = request.FILES['interview_form']
        acceptance_letter = request.FILES['acceptance_letter']
        wfh_arrangement = request.FILES['wfh_arrangement']
        nda = request.FILES['nda']
        work_assignment_form = request.FILES['work_assignment_form']
        war = request.FILES['war']
        timesheet = request.FILES['timesheet']
        coc = request.FILES['coc']
        
        
        
        start_date_obj = datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        # Create a new Intern_Table instance with the form data
        new_intern = Intern_Table(
            ojt_duration=ojt_duration,
            province=province,
            school_name=school_name,
            school_address=school_address,
            contact_person=contact_person,
            contact_number=contact_number,
            student_name=student_name,
            gender=gender,
            start_date=start_date_obj,
            end_date=end_date_obj,
            mode=mode,
            remarks=remarks,
            
            
            recommendation_letter=recommendation_letter,
            application_form=application_form,
            cv_resume=cv_resume,
            medical_certificate=medical_certificate,
            workplan_form=workplan_form,
            interview_form=interview_form,
            acceptance_letter=acceptance_letter,
            wfh_arrangement=wfh_arrangement,
            nda=nda,
            work_assignment_form=work_assignment_form,
            war=war,
            timesheet=timesheet,
            coc=coc,
            
        )

        # Save the new Intern_Table instance
        new_intern.save()

        # Redirect to a specific page (change "epmd_ojt" to your desired URL name)
        return redirect("epmd_ojt")
    else:
        # Render the form page if the request method is not POST
        return render(request, "3_epmd/1_ojt/add_data_ojt.html")

@login_required(login_url="/login")
def update_data_ojt(request, ojt_id):

    ojt = get_object_or_404(Intern_Table, id=ojt_id)
    
    if not UploadCache_Table.objects.filter(id=ojt.id).exists():
        
        new_upload_cache = UploadCache_Table(
            id = ojt.id,

            recommendation_letter = ojt.recommendation_letter,
            application_form = ojt.application_form,
            cv_resume = ojt.cv_resume,
            medical_certificate = ojt.medical_certificate,
            workplan_form = ojt.workplan_form,
            interview_form = ojt.interview_form,
            acceptance_letter = ojt.acceptance_letter,
            wfh_arrangement = ojt.wfh_arrangement,
            nda = ojt.nda,
            work_assignment_form = ojt.work_assignment_form,
            war = ojt.war,
            timesheet = ojt.timesheet,
            coc = ojt.coc,
            
                    
            )
        
        new_upload_cache.save()

    if request.method == "POST":
        # Handle form submission to update data
        # Assuming you receive data from a form POST request
        ojt_duration = request.POST.get("ojt_duration")
        province = request.POST.get("province")
        school_name = request.POST.get("school_name")
        school_address = request.POST.get("school_address")
        contact_person = request.POST.get("contact_person")
        contact_number = request.POST.get("contact_number")
        student_name = request.POST.get("student_name")
        gender = request.POST.get("gender")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        mode = request.POST.get("mode")
        remarks = request.POST.get("remarks")
        
        
        
        
        
        
        start_date_obj = datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        # Update the fields of the retrieved application object
        ojt.ojt_duration = ojt_duration
        ojt.province = province
        ojt.school_name = school_name
        ojt.school_address = school_address
        ojt.contact_person = contact_person
        ojt.contact_number = contact_number
        ojt.student_name = student_name
        ojt.gender = gender
        ojt.start_date = start_date_obj
        ojt.end_date = end_date_obj
        ojt.mode = mode
        ojt.remarks = remarks
        

        # Save the updated application object to the database
        ojt.save()
        
        upload = get_object_or_404(UploadCache_Table, id=ojt_id)
        
        ojt.recommendation_letter = upload.recommendation_letter
        ojt.application_form = upload.application_form  
        ojt.cv_resume = upload.cv_resume
        ojt.medical_certificate = upload.medical_certificate  
        ojt.workplan_form = upload.workplan_form
        ojt.interview_form = upload.interview_form  
        ojt.acceptance_letter = upload.acceptance_letter
        ojt.wfh_arrangement = upload.wfh_arrangement  
        ojt.nda = upload.nda
        ojt.work_assignment_form = upload.work_assignment_form  
        ojt.war = upload.war
        ojt.timesheet = upload.timesheet
        ojt.coc = upload.coc
        
        
        ojt.save()

        # Redirect to a success page or any other page
        return redirect(
            "epmd_ojt"
        )  # You can change 'epmd_ojt' to the appropriate URL name

    # Render the edit_data_ojt.html template with the retrieved application object
    return render(request, "3_epmd/1_ojt/update_data_ojt.html", {"ojt": ojt})

@login_required(login_url="/login")
def delete_data_ojt(request, ojt_id):
    # Get the intern instance to be deleted or return 404 if not found
    ojt = get_object_or_404(Intern_Table, id=ojt_id)

    if request.method == "POST":
        # Delete the intern instance
        ojt.delete()

        return redirect("epmd_ojt")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(
            request, "3_epmd/1_ojt/delete_confirmation.html", {"ojt": ojt}
        )
