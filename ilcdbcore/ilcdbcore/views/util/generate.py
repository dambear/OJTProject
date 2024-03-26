
from django.shortcuts import redirect
import pandas as pd
from django.http import HttpResponse
from django.db import connection
from main.models import Intern_Table, Exam_Table, Engage_Partners_Table, Training_Webinars_Table
from ilcdbcore.views.util.upload_excel import upload_csv_data_to_intern_table, upload_csv_data_to_engage_partners_table, upload_csv_data_to_exam_table, upload_csv_data_to_training_webinars_table
import tempfile


import io

def export_intern_table_to_excel(request):
    
    user = request.user
   
    if user.province.lower() == "cavite":
        queryset = Intern_Table.objects.filter(province__iexact="Cavite")
        filename = "intern_table_cavite.xlsx"
    elif user.province.lower() == "laguna":
        queryset = Intern_Table.objects.filter(province__iexact="Laguna")
        filename = "intern_table_laguna.xlsx"
    elif user.province.lower() == "batangas":
        queryset = Intern_Table.objects.filter(province__iexact="Batangas")
        filename = "intern_table_batangas.xlsx"
    elif user.province.lower() == "rizal":
        queryset = Intern_Table.objects.filter(province__iexact="Rizal")
        filename = "intern_table_rizal.xlsx"
    elif user.province.lower() == "quezon":
        queryset = Intern_Table.objects.filter(province__iexact="Quezon")
        filename = "intern_table_quezon.xlsx"
    else:
        queryset = Intern_Table.objects.all()
        filename = "intern_table.xlsx"

    # Get queryset data
    data = list(queryset.values())

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

        
   

def export_exam_table_to_excel(request):
    user = request.user

    if user.province.lower() == "cavite":
        queryset = Exam_Table.objects.filter(province__iexact="Cavite")
        filename = "exam_table_cavite.xlsx"
    elif user.province.lower() == "laguna":
        queryset = Exam_Table.objects.filter(province__iexact="Laguna")
        filename = "exam_table_laguna.xlsx"
    elif user.province.lower() == "batangas":
        queryset = Exam_Table.objects.filter(province__iexact="Batangas")
        filename = "exam_table_batangas.xlsx"
    elif user.province.lower() == "rizal":
        queryset = Exam_Table.objects.filter(province__iexact="Rizal")
        filename = "exam_table_rizal.xlsx"
    elif user.province.lower() == "quezon":
        queryset = Exam_Table.objects.filter(province__iexact="Quezon")
        filename = "exam_table_quezon.xlsx"
    else:
        queryset = Exam_Table.objects.all()
        filename = "exam_table.xlsx"

    # Get queryset data
    data = list(queryset.values())

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response


    
    
    

def export_engage_partners_table_to_excel(request):
    user = request.user

    if user.province.lower() == "cavite":
        queryset = Engage_Partners_Table.objects.filter(province__iexact="Cavite")
        filename = "engage_partners_table_cavite.xlsx"
    elif user.province.lower() == "laguna":
        queryset = Engage_Partners_Table.objects.filter(province__iexact="Laguna")
        filename = "engage_partners_table_laguna.xlsx"
    elif user.province.lower() == "batangas":
        queryset = Engage_Partners_Table.objects.filter(province__iexact="Batangas")
        filename = "engage_partners_table_batangas.xlsx"
    elif user.province.lower() == "rizal":
        queryset = Engage_Partners_Table.objects.filter(province__iexact="Rizal")
        filename = "engage_partners_table_rizal.xlsx"
    elif user.province.lower() == "quezon":
        queryset = Engage_Partners_Table.objects.filter(province__iexact="Quezon")
        filename = "engage_partners_table_quezon.xlsx"
    else:
        queryset = Engage_Partners_Table.objects.all()
        filename = "engage_partners_table.xlsx"

    # Get queryset data
    data = list(queryset.values())

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def export_trainings_and_webinars_table_to_excel(request):
    user = request.user

    if user.province.lower() == "cavite":
        queryset = Training_Webinars_Table.objects.filter(province__iexact="Cavite")
        filename = "trainings_and_webinars_table_cavite.xlsx"
    elif user.province.lower() == "laguna":
        queryset = Training_Webinars_Table.objects.filter(province__iexact="Laguna")
        filename = "trainings_and_webinars_table_laguna.xlsx"
    elif user.province.lower() == "batangas":
        queryset = Training_Webinars_Table.objects.filter(province__iexact="Batangas")
        filename = "trainings_and_webinars_table_batangas.xlsx"
    elif user.province.lower() == "rizal":
        queryset = Training_Webinars_Table.objects.filter(province__iexact="Rizal")
        filename = "trainings_and_webinars_table_rizal.xlsx"
    elif user.province.lower() == "quezon":
        queryset = Training_Webinars_Table.objects.filter(province__iexact="Quezon")
        filename = "trainings_and_webinars_table_quezon.xlsx"
    else:
        queryset = Training_Webinars_Table.objects.all()
        filename = "trainings_and_webinars_table.xlsx"

    # Get queryset data
    data = list(queryset.values())

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file
    response = HttpResponse(excel_file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response


# ------------------------------ Uploads -------------------------- --------------------

def convert_xlsx_to_csv(xlsx_file):
    # Create a temporary file to store the converted .csv
    temp_csv_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_csv_file.close()
    
    # Load the .xlsx file into a pandas DataFrame
    xlsx_data = pd.read_excel(xlsx_file)
    
    # Convert the DataFrame to .csv and save it to the temporary file
    xlsx_data.to_csv(temp_csv_file.name, index=False)
    
    return temp_csv_file.name




def upload_csv_ojt(request):
    if request.method == 'POST':
        xlsx_file = request.FILES.get('dropzone-file')
        if xlsx_file and xlsx_file.name.endswith('.xlsx'):
            # Convert .xlsx to .csv
            csv_file_path = convert_xlsx_to_csv(xlsx_file)
            # Process the .csv file
            upload_csv_data_to_intern_table(csv_file_path)
            
            return redirect("epmd_ojt") 
        
        elif request.FILES.get('csv_file') and request.FILES['csv_file'].name.endswith('.csv'):
            # Process the .csv file directly
            upload_csv_data_to_intern_table(request.FILES['csv_file'])
            return redirect("epmd_ojt") 
        else:
            return redirect("epmd_ojt")  # make this to go to an error page or functions
    return redirect("epmd_ojt") 




def upload_csv_engage(request):
    if request.method == 'POST':
        xlsx_file = request.FILES.get('dropzone-file')
        if xlsx_file and xlsx_file.name.endswith('.xlsx'):
            # Convert .xlsx to .csv
            csv_file_path = convert_xlsx_to_csv(xlsx_file)
            # Process the .csv file
            upload_csv_data_to_engage_partners_table(csv_file_path)
            
            return redirect("epmd_engage") 
        
        elif request.FILES.get('csv_file') and request.FILES['csv_file'].name.endswith('.csv'):
            # Process the .csv file directly
            upload_csv_data_to_engage_partners_table(request.FILES['csv_file'])
            return redirect("epmd_engage") 
        else:
            return redirect("epmd_engage")   # make this to go to an error page or functions
    return redirect("epmd_engage") 



def upload_csv_exam(request):
    if request.method == 'POST':
        xlsx_file = request.FILES.get('dropzone-file')
        if xlsx_file and xlsx_file.name.endswith('.xlsx'):
            # Convert .xlsx to .csv
            csv_file_path = convert_xlsx_to_csv(xlsx_file)
            # Process the .csv file
            upload_csv_data_to_exam_table(csv_file_path)
            
            return redirect("c3d2") 
        
        elif request.FILES.get('csv_file') and request.FILES['csv_file'].name.endswith('.csv'):
            # Process the .csv file directly
            upload_csv_data_to_exam_table(request.FILES['csv_file'])
            return redirect("c3d2") 
        else:
            return redirect("c3d2")  # make this to go to an error page or functions
    return redirect("c3d2") 




def upload_csv_tmd(request):
    if request.method == 'POST':
        xlsx_file = request.FILES.get('dropzone-file')
        if xlsx_file and xlsx_file.name.endswith('.xlsx'):
            # Convert .xlsx to .csv
            csv_file_path = convert_xlsx_to_csv(xlsx_file)
            # Process the .csv file
            upload_csv_data_to_training_webinars_table(csv_file_path)
            
            return redirect("tmd") 
        
        elif request.FILES.get('csv_file') and request.FILES['csv_file'].name.endswith('.csv'):
            # Process the .csv file directly
            upload_csv_data_to_training_webinars_table(request.FILES['csv_file'])
            return redirect("tmd") 
        else:
            return redirect("tmd")  # make this to go to an error page or functions
    return redirect("tmd") 




