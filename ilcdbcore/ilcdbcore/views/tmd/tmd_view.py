from django.shortcuts import render, redirect
from main.models import Training_Webinars_Table
from datetime import datetime

def tmd(request):
    return render(request, "4_tmd/index.html")

def add_data_tmd(request):
    if request.method == "POST":
        # Get the form data from POST request
        province = request.POST.get("province")
        course_name = request.POST.get("course_name")
        training_track = request.POST.get("training_track")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        time = request.POST.get("time")
        total_num_hours = request.POST.get("total_num_hours")
        nga_m = request.POST.get("nga_m")
        nga_f = request.POST.get("nga_f")
        suc_m = request.POST.get("suc_m")
        suc_f = request.POST.get("suc_f")
        lgu_m = request.POST.get("lgu_m")
        lgu_f = request.POST.get("lgu_f")
        others_m = request.POST.get("others_m")
        others_f = request.POST.get("others_f")
        total_m = request.POST.get("total_m")
        total_f = request.POST.get("total_f")
        total_participants = request.POST.get("total_participants")
       
        
        implementation_mode = request.POST.get("implementation_mode")
        
        resource_persons = request.POST.get("resource_persons")
        
        course_officers = request.POST.get("course_officers")
        course_officers_email = request.POST.get("course_officers_email")
        remarks = request.POST.get("remarks")
        
        
        participants_list = request.FILES['participants_list']
        attendance_sheet = request.FILES['attendance_sheet']
        group_photo = request.FILES['group_photo']
        certificates_issued = request.FILES['certificates_issued']
        resource_persons_cv = request.FILES['resource_persons_cv']
        
        
        # Convert files to binary data
        participants_list_binary = participants_list.read()
        attendance_sheet_binary = attendance_sheet.read()
        group_photo_binary = group_photo.read()
        certificates_issued_binary = certificates_issued.read()
        resource_persons_cv_binary = resource_persons_cv.read()
        
        
        start_date_obj = datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        # Create a new instance with the form data
        new_training_webinars =  Training_Webinars_Table(
            province=province,
            course_name=course_name,
            training_track=training_track,
            start_date=start_date_obj,
            end_date=end_date_obj,
            time=time,
            total_num_hours=total_num_hours,
            nga_m=nga_m,
            nga_f=nga_f,
            suc_m=suc_m,
            suc_f=suc_f,
            lgu_m=lgu_m,
            lgu_f=lgu_f,
            others_m=others_m,
            others_f=others_f,
            total_m=total_m,
            total_f=total_f,
            total_participants=total_participants,
    
            implementation_mode=implementation_mode,
      
            resource_persons=resource_persons,
         
            course_officers=course_officers,
            course_officers_email=course_officers_email,
            remarks=remarks,
            
            participants_list = participants_list_binary,
            attendance_sheet = attendance_sheet_binary,
            group_photo = group_photo_binary,
            certificates_issued = certificates_issued_binary,
            resource_persons_cv = resource_persons_cv_binary,
            
            
            
        )

        # Save the new instance
        new_training_webinars.save()

        # Redirect to a specific page
        return redirect("tmd")
    else:
        # Render the form page if the request method is not POST
          return render(request, "4_tmd/add_data_tmd.html")

