
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import ojttrainee

def insert_data(request):
    if request.method == 'POST':
        # Assuming you receive data from a form POST request
        id = request.POST.get('id')
        ojt_duration = request.POST.get('ojt_duration')
        province = request.POST.get('province')
        school = request.POST.get('school')
        school_address = request.POST.get('school_address')
        contact_person = request.POST.get('contact_person')
        contact_number = request.POST.get('contact_number')
        name_student = request.POST.get('contact_number')
        sex = request.POST.get('sex')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        mode=request.POST.get('end_date')
        recommendation_letter=request.POST.get('recommendation_letter')
        application_form = request.POST.get('application_form')
        cv_resume = request.FILES['cv_resume']  # Assuming 'cv_resume' is the name attribute in your HTML form for file input
        medical_certificate = request.POST.get('medical_certificate')
        workplan_form = request.POST.get('workplan_form')
        interview_form_evaluation = request.POST.get('interview_form_evaluation')
        acceptance_letter = request.POST.get('acceptance_letter')
        wfh_arrangement = request.POST.get('wfh_arrangement')
        nda = request.POST.get('nda')
        work_assignment_schedule_form = request.POST.get('work_assignment_schedule_form')
        timesheet = request.POST.get('timesheet')
        coc = request.POST.get('coc')
        remarks = request.POST.get('remarks')

        # Create an instance of InternshipApplication with the provided id
        new_application = ojttrainee(
            id=id,
            ojt_duration=ojt_duration,
            province=province,
            school=school,
            school_address=school_address,
            contact_person=contact_person,
            contact_number=contact_number,
            name_student=name_student,
            sex=sex,
            start_date=start_date,
            end_date=end_date,
            mode=mode,
            recommendation_letter=recommendation_letter,
            application_form=application_form,
            cv_resume=cv_resume,
            medical_certificate=medical_certificate,
            workplan_form=workplan_form,
            interview_form_evaluation=interview_form_evaluation,
            acceptance_letter=acceptance_letter,
            wfh_arrangement=wfh_arrangement,
            nda=nda,
            work_assignment_schedule_form=work_assignment_schedule_form,
            timesheet=timesheet,
            coc=coc,
            remarks=remarks
         


        )
        
        # Save the new application to the database
        new_application.save()
        
        return HttpResponse('Data inserted successfully!')
    else:
        return HttpResponse('Please use a POST request to insert data.')
