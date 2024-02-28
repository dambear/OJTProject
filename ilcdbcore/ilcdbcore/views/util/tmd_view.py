
from django.http import HttpResponse
from main.models import Training_Webinars_Table


def tmd_pdf_view_participants_list(request, tmd_id):
    # Retrieve the binary data from your database (replace 'pk' with the actual primary key)
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;  filename="{tmd_id}.pdf"'
    return response

def tmd_pdf_view_attendance_sheet(request, tmd_id):
    # Retrieve the binary data from your database (replace 'pk' with the actual primary key)
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;  filename="{tmd_id}.pdf"'
    return 

def tmd_pdf_view_certificates_issued(request, tmd_id):
    # Retrieve the binary data from your database (replace 'pk' with the actual primary key)
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;  filename="{tmd_id}.pdf"'
    return response

def tmd_pdf_view_participants_list(request, tmd_id):
    # Retrieve the binary data from your database (replace 'pk' with the actual primary key)
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;  filename="{tmd_id}.pdf"'
    return response 

def tmd_pdf_view_group_photo(request, tmd_id):
    # Retrieve the binary data from your database (replace 'pk' with the actual primary key)
    tmd_obj = Training_Webinars_Table.objects.get(id=tmd_id)
    response = HttpResponse(tmd_obj.participants_list, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;  filename="{tmd_id}.pdf"'
    return response