import cloudinary.uploader
from django.conf import settings
from main.models import Training_Webinars_Table
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
    tmd = get_object_or_404(Training_Webinars_Table, id=tmd_id)
    
    if request.method == 'POST':
        file = request.FILES['file']
        
        tmd.attendance_sheet = file
        tmd.save()
        
        tmdupdatedattendanceurl = tmd.attendance_sheet.url # Assuming attendance_sheet is a FileField or ImageField
        
        return JsonResponse({
            'message': 'File uploaded successfully',
            'tmdupdatedattendanceurl': tmdupdatedattendanceurl # Include the URL in the response
        })
    
    else:
        return JsonResponse({'error': 'Invalid request method'})
