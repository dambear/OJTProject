# # myapp/views.py
# from datetime import datetime
# from django.shortcuts import render, redirect, get_object_or_404
# from main.models import MyModel
# from django.contrib.auth.decorators import login_required

# # Create your views here.





# def add_data_model(request):
#     if request.method == "POST":
#         # Get the form data from POST request
#         aaa_file = request.FILES['aaa']
#         bbb_file = request.FILES['bbb']
#         ccc_file = request.FILES['ccc']

#         # Read the file content as binary data
#         aaa_binary = aaa_file.read()
#         bbb_binary = bbb_file.read()
#         ccc_binary = ccc_file.read()

#         # Save binary data to the database
#         new_model_entry = MyModel(aaa=aaa_binary, bbb=bbb_binary, ccc=ccc_binary)
#         new_model_entry.save()

       
#         # Redirect to a specific page (change "partner_engagement" to your desired URL name)
#         return redirect("/")
#     else:
#         # Render the form page if the request method is not POST
#         return render(request, "3_epmd_page/engage/add_data_model.html")



