from django.shortcuts import render, redirect, get_object_or_404
from main.models import Training_Webinars_Table
from datetime import datetime
from django.contrib.auth.decorators import login_required

import cloudinary.uploader

@login_required(login_url="/login")
def tmd(request):

    user = request.user
    
    if user.province.lower() == "cavite":
        tmd = Training_Webinars_Table.objects.filter(province__iexact="Cavite")
        return render(request, "4_tmd/index.html", {"tmd": tmd})

    elif user.province.lower() == "laguna":
        tmd = Training_Webinars_Table.objects.filter(province__iexact="Laguna")
        return render(request, "4_tmd/index.html", {"tmd": tmd})

    elif user.province.lower() == "batangas":
        tmd = Training_Webinars_Table.objects.filter(province__iexact="Batangas")
        return render(request, "4_tmd/index.html", {"tmd": tmd})

    elif user.province.lower() == "rizal":
        tmd = Training_Webinars_Table.objects.filter(province__iexact="Rizal")
        return render(request, "4_tmd/index.html", {"tmd": tmd})

    elif user.province.lower() == "quezon":
        tmd = Training_Webinars_Table.objects.filter(province__iexact="Quezon")
        return render(request, "4_tmd/index.html", {"tmd": tmd})

    else:
        tmd = Training_Webinars_Table.objects.all()
        return render(request, "4_tmd/index.html", {"tmd": tmd})

 

@login_required(login_url="/login")
def view_data_tmd(request, tmd_id):
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)
    
    return render(request, "4_tmd/view_data_tmd.html", {"tmd": tmd})


@login_required(login_url="/login")
def update_data_tmd(request, tmd_id):
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)

    if request.method == "POST":
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
        
        participants_list = request.POST.get('participants_list')
        attendance_sheet = request.POST.get('attendance_sheet')
        group_photo = request.POST.get('group_photo')
        certificates_issued = request.POST.get('certificates_issued')
        resource_persons_cv = request.POST.get('resource_persons_cv')
        
        start_date_obj = datetime.strptime(start_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        
        
       

        tmd.province = province
        tmd.course_name = course_name 
        tmd.training_track = training_track
        tmd.start_date = start_date_obj   
        tmd.end_date = end_date_obj  
        tmd.time = time
        tmd.total_num_hours = total_num_hours 
        tmd.nga_m = nga_m
        tmd.nga_f = nga_f   
        tmd.suc_m = suc_m   
        tmd.suc_f = suc_f   
        tmd.lgu_m = lgu_m
        tmd.lgu_f = lgu_f   
        tmd.others_m = others_m   
        tmd.others_f = others_f   
        tmd.total_m = total_m
        tmd.total_f = total_f   
        tmd.total_participants = total_participants   
        tmd.implementation_mode = implementation_mode   
        tmd.resource_persons = resource_persons
        tmd.course_officers = course_officers   
        tmd.course_officers_email = course_officers_email   
        tmd.remarks = remarks   
        tmd.participants_list = participants_list
        tmd.attendance_sheet = attendance_sheet  
         
        tmd.group_photo = group_photo
        tmd.certificates_issued = certificates_issued  
        tmd.resource_persons_cv = resource_persons_cv
        
        # Save the updated application object to the database
        tmd.save()

        # Redirect to a success page or any other page
        return redirect(
            "tmd"
        )  # You can change 'epmd_ojt' to the appropriate URL name


    return render(request, "4_tmd/update_data_tmd.html", {"tmd": tmd})


@login_required(login_url="/login")
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
        
        
        participants_list = request.FILES('participants_list')
        attendance_sheet = request.FILES('attendance_sheet')
        group_photo = request.FILES('group_photo')
        certificates_issued = request.FILES('certificates_issued')
        resource_persons_cv = request.FILES('resource_persons_cv')
        
        
        
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
            
            participants_list = participants_list,
            attendance_sheet = attendance_sheet,
            group_photo = group_photo,
            certificates_issued = certificates_issued,
            resource_persons_cv = resource_persons_cv,
            
            
        )

        # Save the new instance
        new_training_webinars.save()

        # Redirect to a specific page
        return redirect("tmd")
    else:
        # Render the form page if the request method is not POST
          return render(request, "4_tmd/add_data_tmd.html")


@login_required(login_url="/login")
def delete_data_tmd(request, tmd_id):
    # Get the intern instance to be deleted or return 404 if not found
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)

    if request.method == "POST":
        # Delete the intern instance
        tmd.delete()

        return redirect("tmd")  # Redirect to 'epmd_ojt' URL pattern
    else:
        # Render a confirmation page with the option to delete
        return render(
            request, "4_tmd/delete_confirmation.html", {"tmd": tmd}
        )
