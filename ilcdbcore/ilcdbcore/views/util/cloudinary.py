import cloudinary.uploader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import UploadCache_Table
from django.shortcuts import get_object_or_404


# def upload_file_to_cloudinary(file, folder='pdfs/'):
#     # Upload the file to Cloudinary
#     response = cloudinary.uploader.upload(file, folder=folder)
    
    
#     return response['url']


def delete_file_from_cloudinary(url):
    # Extract the public ID from the URL
    public_id = url.split('/')[-1].split('.')[0]
    
    # Delete the file from Cloudinary
    response = cloudinary.uploader.destroy(public_id)
    
    if response['result'] == 'ok':
        print(f"File {public_id} deleted successfully.")
    else:
        print(f"Failed to delete file {public_id}.")
        
        

@csrf_exempt
def upload_attendance_sheet_file(request, tmd_id):
    
    upload = get_object_or_404(UploadCache_Table, id=tmd_id)
    
    if request.method == 'POST':
        attendance_sheet_file = request.FILES['attendance_sheet_file']
        
        upload.attendance_sheet = attendance_sheet_file
        upload.save()
        
        tmdupdatedattendanceurl = upload.attendance_sheet.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedattendanceurl': tmdupdatedattendanceurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_certificates_issued_file(request, tmd_id):
    
    upload = get_object_or_404(UploadCache_Table, id=tmd_id)
    
    if request.method == 'POST':
        certificates_issued_file = request.FILES['certificates_issued_file']
        
        upload.certificates_issued = certificates_issued_file
        upload.save()
        
        
        tmdupdatedcertificatesurl = upload.certificates_issued.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedcertificatesurl': tmdupdatedcertificatesurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_participants_list_file(request, tmd_id):

    upload = get_object_or_404(UploadCache_Table, id=tmd_id)
    if request.method == 'POST':
        participants_list_file = request.FILES['participants_list_file']
        
        upload.participants_list = participants_list_file
        upload.save()
        
        tmdupdatedparticipantsurl = upload.participants_list.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedparticipantsurl': tmdupdatedparticipantsurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_group_photo_file(request, tmd_id):
    upload = get_object_or_404(UploadCache_Table, id=tmd_id)
    if request.method == 'POST':
        group_photo_file = request.FILES['group_photo_file']
        
        
        upload.group_photo = group_photo_file
        upload.save()
        
        tmdupdatedgroupphotourl = upload.group_photo.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedgroupphotourl': tmdupdatedgroupphotourl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_resource_persons_cv_file(request, tmd_id):
  
    upload = get_object_or_404(UploadCache_Table, id=tmd_id)
    if request.method == 'POST':
        resource_persons_cv_file = request.FILES['resource_persons_cv_file']
        
        upload.resource_persons_cv = resource_persons_cv_file
        upload.save()
        
        tmdupdatedresourcepersonscvurl = upload.resource_persons_cv.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedresourcepersonscvurl': tmdupdatedresourcepersonscvurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})



# ------------------------ Start of ojt functions ------------------------

@csrf_exempt
def upload_recommendation_letter_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    
    if request.method == 'POST':
        recommendation_letter_file = request.FILES['recommendation_letter_file']
        
        upload.recommendation_letter = recommendation_letter_file
        upload.save()
        
        ojtupdatedrecommendationletterurl = upload.recommendation_letter.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'ojtupdatedrecommendationletterurl': ojtupdatedrecommendationletterurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_application_form_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        application_form_file = request.FILES['application_form_file']
        
        upload.application_form = application_form_file
        upload.save()
        
        ojtupdatedapplicationformurl = upload.application_form.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'ojtupdatedapplicationformurl': ojtupdatedapplicationformurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_cv_resume_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        cv_resume_file = request.FILES['cv_resume']
        
        upload.cv_resume = cv_resume_file
        upload.save()
        
        tmdupdatedcvresumeurl = upload.cv_resume.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedcvresumeurl': tmdupdatedcvresumeurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_medical_certificate_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        medical_certificate_file = request.FILES['medical_certificate']
        
        upload.medical_certificate = medical_certificate_file
        upload.save()
        
        tmdupdatedmedicalcertificateurl = upload.medical_certificate.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedmedicalcertificateurl': tmdupdatedmedicalcertificateurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_workplan_form_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        workplan_form_file = request.FILES['workplan_form']
        
        upload.workplan_form = workplan_form_file
        upload.save()
        
        tmdupdatedworkplanformurl = upload.workplan_form.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedworkplanformurl': tmdupdatedworkplanformurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_interview_form_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        interview_form_file = request.FILES['interview_form']
        
        upload.interview_form = interview_form_file
        upload.save()
        
        tmdupdatedinterviewformurl = upload.interview_form.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedinterviewformurl': tmdupdatedinterviewformurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_acceptance_letter_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        acceptance_letter_file = request.FILES['acceptance_letter']
        
        upload.acceptance_letter = acceptance_letter_file
        upload.save()
        
        tmdupdatedacceptanceletterurl = upload.acceptance_letter.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedacceptanceletterurl': tmdupdatedacceptanceletterurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_wfh_arrangement_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        wfh_arrangement_file = request.FILES['wfh_arrangement']
        
        upload.wfh_arrangement = wfh_arrangement_file
        upload.save()
        
        tmdupdatedwfharrangementurl = upload.wfh_arrangement.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedwfharrangementurl': tmdupdatedwfharrangementurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_nda_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        nda_file = request.FILES['nda']
        
        upload.nda = nda_file
        upload.save()
        
        tmdupdatedndaurl = upload.nda.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedndaurl': tmdupdatedndaurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_work_assignment_form_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        work_assignment_form_file = request.FILES['work_assignment_form']
        
        upload.work_assignment_form = work_assignment_form_file
        upload.save()
        
        tmdupdatedworkassignmentformurl = upload.work_assignment_form.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedworkassignmentformurl': tmdupdatedworkassignmentformurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_war_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        war_file = request.FILES['war']
        
        upload.war = war_file
        upload.save()
        
        tmdupdatedwarurl = upload.war.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedwarurl': tmdupdatedwarurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_timesheet_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        timesheet_file = request.FILES['timesheet']
        
        upload.timesheet = timesheet_file
        upload.save()
        
        tmdupdatedtimesheeturl = upload.timesheet.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedtimesheeturl': tmdupdatedtimesheeturl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_coc_file(request, ojt_id):
  
    upload = get_object_or_404(UploadCache_Table, id=ojt_id)
    if request.method == 'POST':
        coc_file = request.FILES['coc']
        
        upload.coc = coc_file
        upload.save()
        
        tmdupdatedcocurl = upload.coc.url
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedcocurl': tmdupdatedcocurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})
