

import pandas as pd
from django.http import HttpResponse
from django.db import connection
from main.models import Intern_Table

import io

def export_intern_table_to_excel(request):
    # Query the data from the Intern_Table model
    queryset = Intern_Table.objects.all()

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
    response['Content-Disposition'] = 'attachment; filename="intern_table.xlsx"'
    
    return response
