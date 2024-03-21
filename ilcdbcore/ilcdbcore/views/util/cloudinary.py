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
