import cloudinary.uploader

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import cloudinary.uploader


def upload_file_to_cloudinary(file, folder='pdfs/'):
    # Upload the file to Cloudinary
    response = cloudinary.uploader.upload(file, folder=folder)
    
    
    return response['url']


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
def upload_attendance_sheet_file(request):

    
    if request.method == 'POST':
        attendance_sheet_file = request.FILES['attendance_sheet_file']
        
        
      

        
        tmdupdatedattendanceurl = upload_file_to_cloudinary(attendance_sheet_file)
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedattendanceurl': tmdupdatedattendanceurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_certificates_issued_file(request):
    
    if request.method == 'POST':
        certificates_issued_file = request.FILES['certificates_issued_file']
        
        tmdupdatedcertificatesurl = upload_file_to_cloudinary(certificates_issued_file)
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedcertificatesurl': tmdupdatedcertificatesurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_participants_list_file(request):

    if request.method == 'POST':
        participants_list_file = request.FILES['participants_list_file']
        
        tmdupdatedparticipantsurl = upload_file_to_cloudinary(participants_list_file)
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedparticipantsurl': tmdupdatedparticipantsurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def upload_group_photo_file(request):

    if request.method == 'POST':
        group_photo_file = request.FILES['group_photo_file']
        
        tmdupdatedgroupphotourl = upload_file_to_cloudinary(group_photo_file)
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedgroupphotourl': tmdupdatedgroupphotourl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def upload_resource_persons_cv_file(request):
  
    
    if request.method == 'POST':
        resource_persons_cv_file = request.FILES['resource_persons_cv_file']
        
        
        tmdupdatedresourcepersonscvurl = upload_file_to_cloudinary(resource_persons_cv_file)
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedresourcepersonscvurl': tmdupdatedresourcepersonscvurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})
