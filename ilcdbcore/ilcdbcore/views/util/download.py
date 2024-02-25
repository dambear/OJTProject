from django.http import HttpResponse
from main.models import Training_Webinars_Table

def download_file_participants_list(request, tmd_id):
   # Assuming you have a model called Training_Webinars_Table with a field named 'attendance_sheet' that stores the binary data of the PDF file
    
    # Retrieve the file object from the database using the tmd_id
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)

    # Set response content type to PDF
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    
    # Set Content-Disposition to 'attachment' to force download
    response['Content-Disposition'] = f'attachment; filename="{tmd_obj.id}.pdf"'

    return response



def download_file_attendance_sheet(request, tmd_id):
    # Assuming you have a model called Training_Webinars_Table with a field named 'attendance_sheet' that stores the binary data of the PDF file
    
    # Retrieve the file object from the database using the tmd_id
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)

    # Set response content type to PDF
    response = HttpResponse(tmd_obj.attendance_sheet, content_type='application/pdf')

    # Set Content-Disposition to 'attachment' to force download
    response['Content-Disposition'] = f'attachment; filename="{tmd_obj.id}.pdf"'

    return response


def download_file_group_photo(request, tmd_id):
    # Assuming you have a model called Training_Webinars_Table with a field named 'attendance_sheet' that stores the binary data of the PDF file
    
    # Retrieve the file object from the database using the tmd_id
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)

    # Set response content type to PDF
    response = HttpResponse(tmd_obj.group_photo, content_type='application/png')

    # Set Content-Disposition to 'attachment' to force download
    response['Content-Disposition'] = f'attachment; filename="{tmd_obj.id}.png"'

    return response


def download_file_certificates_issued(request, tmd_id):
   # Assuming you have a model called Training_Webinars_Table with a field named 'attendance_sheet' that stores the binary data of the PDF file
    
    # Retrieve the file object from the database using the tmd_id
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)

    # Set response content type to PDF
    response = HttpResponse(tmd_obj.certificates_issued, content_type='application/pdf')
    
    # Set Content-Disposition to 'attachment' to force download
    response['Content-Disposition'] = f'attachment; filename="{tmd_obj.id}.pdf"'

    return response


def download_file_resource_persons_cv(request, tmd_id):
   # Assuming you have a model called Training_Webinars_Table with a field named 'attendance_sheet' that stores the binary data of the PDF file
    
    # Retrieve the file object from the database using the tmd_id
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)

    # Set response content type to PDF
    response = HttpResponse(tmd_obj.resource_persons_cv, content_type='application/pdf')
    
    # Set Content-Disposition to 'attachment' to force download
    response['Content-Disposition'] = f'attachment; filename="{tmd_obj.id}.pdf"'

    return response