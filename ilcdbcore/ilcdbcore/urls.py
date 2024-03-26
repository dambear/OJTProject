from django.contrib import admin
from django.urls import path, include

from .views.epmd.views import index, dash_province


from .views.epmd.ojt_view import epmd_ojt, add_data_ojt, update_data_ojt, delete_data_ojt, view_data_ojt
from .views.epmd.engage_view import epmd_engage, add_data_engage, update_data_engage, delete_data_engage, view_data_engage
from .views.tmd.tmd_view import tmd, add_data_tmd, view_data_tmd, update_data_tmd, delete_data_tmd
from .views.c3d2.c3d2_view import c3d2, add_data_c3d2, update_data_c3d2, delete_data_c3d2, view_data_c3d2



from .views.util.generate import export_intern_table_to_excel, export_exam_table_to_excel, export_engage_partners_table_to_excel, export_trainings_and_webinars_table_to_excel, upload_csv_ojt
#upload_csv_engage, upload_csv_exam, upload_csv_tmd



from .views.util.cloudinary import  upload_attendance_sheet_file, upload_certificates_issued_file, upload_participants_list_file, upload_group_photo_file, upload_resource_persons_cv_file, upload_recommendation_letter_file, upload_application_form_file, upload_acceptance_letter_file, upload_cv_resume_file, upload_coc_file, upload_interview_form_file, upload_medical_certificate_file, upload_nda_file, upload_timesheet_file, upload_war_file, upload_wfh_arrangement_file, upload_work_assignment_form_file, upload_workplan_form_file
from .views.limit.limit_view import limit
from .views.auth.auth import login_page, logout_page, register_page

from django.contrib.auth import views as auth_views

urlpatterns = [
    # for auto reload
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    #
    #
    # auth
    path("login", login_page, name="login_page"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", logout_page, name="logout_page"),
    
    #
    #
    #
    path("register", register_page, name="register"),
    #
    #
    #
    path('export_intern_table_to_excel/', export_intern_table_to_excel, name='export_intern_table_to_excel'),
    path('export_exam_table_to_excel/', export_exam_table_to_excel, name='export_exam_table_to_excel'),
    path('export_engage_partners_table_to_excel/', export_engage_partners_table_to_excel, name='export_engage_partners_table_to_excel'),
    path('export_trainings_and_webinars_table_to_excel/', export_trainings_and_webinars_table_to_excel, name='export_trainings_and_webinars_table_to_excel'),
    #
    #
    #
    path('upload_csv_ojt/', upload_csv_ojt, name='upload_csv_ojt'),
    # path('upload_csv_exam/', upload_csv_exam, name='upload_csv_exam'),
    # path('upload_csv_engage/', upload_csv_engage, name='upload_csv_engage'),
    # path('upload_csv_tmd/', upload_csv_tmd, name='upload_csv_tmd'),
    #
    #
    #
    path("", index, name="index"),
    path("dash_province", dash_province, name="dash_province"),
    #
    #
    #
    path("epmd_ojt/", epmd_ojt, name="epmd_ojt"),
    path("epmd_ojt/add_data_ojt/", add_data_ojt, name="add_data_ojt"),
    path("epmd_ojt/update_data_ojt/<int:ojt_id>/", update_data_ojt, name="update_data_ojt",),
    path("epmd_ojt/delete_data_ojt/<int:ojt_id>/", delete_data_ojt, name="delete_data_ojt",),
    path("epmd_ojt/view_data_ojt/<int:ojt_id>/", view_data_ojt, name="view_data_ojt"),
    
    #
    #
    #
    #
    path('epmd_engage', epmd_engage, name='epmd_engage'),  
    path('epmd_engage/add_data_engage/', add_data_engage, name='add_data_engage'),
    path('epmd_engage/update_data_engage/<int:engage_id>/',update_data_engage, name='update_data_engage'),
    path('epmd_engage/delete_data_engage/<int:engage_id>/',delete_data_engage, name='delete_data_engage'),
    path('epmd_engage/view_data_engage/<int:engage_id>/',view_data_engage, name='view_data_engage'),
    
    #
    #
    path('tmd/', tmd, name='tmd'),
    path('tmd/add_data_tmd/', add_data_tmd, name='add_data_tmd'),
    path('tmd/view_data_tmd/<int:tmd_id>/',view_data_tmd, name='view_data_tmd'),
    path('tmd/delete_data_tmd/<int:tmd_id>/',delete_data_tmd, name='delete_data_tmd'),
    path('tmd/update_data_tmd/<int:tmd_id>/',update_data_tmd, name='update_data_tmd'),


    #

    path('c3d2/', c3d2, name='c3d2'),
    path('c3d2/add_data_c3d2/', add_data_c3d2, name='add_data_c3d2'),
    path('c3d2/update_data_c3d2/<int:c3d2_id>/',update_data_c3d2, name='update_data_c3d2'),
    path('c3d2/delete_data_c3d2/<int:c3d2_id>/',delete_data_c3d2, name='delete_data_c3d2'),
    path('c3d2/view_data_c3d2/<int:c3d2_id>/',view_data_c3d2, name='view_data_c3d2'),
    
    
    path('limit/', limit, name='limit'),
    
    
    
    path('upload_attendance_sheet_file/<int:tmd_id>/', upload_attendance_sheet_file, name='upload_attendance_sheet_file'),
    path('upload_certificates_issued_file/<int:tmd_id>/', upload_certificates_issued_file, name='upload_certificates_issued_file'),
    path('upload_participants_list_file/<int:tmd_id>/', upload_participants_list_file, name='upload_participants_list_file'),
    path('upload_group_photo_file/<int:tmd_id>/', upload_group_photo_file, name='upload_group_photo_file'),
    path('upload_resource_persons_cv_file/<int:tmd_id>/', upload_resource_persons_cv_file, name='upload_resource_persons_cv_file'),
   
   
   
    path('upload_recommendation_letter_file/<int:ojt_id>/', upload_recommendation_letter_file, name='upload_recommendation_letter_file'),
    path('upload_application_form_file/<int:ojt_id>/', upload_application_form_file, name='upload_application_form_file'),
    path('upload_cv_resume_file/<int:ojt_id>/', upload_cv_resume_file, name='upload_cv_resume_file'),
    path('upload_medical_certificate_file/<int:ojt_id>/', upload_medical_certificate_file, name='upload_medical_certificate_file'),
    path('upload_workplan_form_file/<int:ojt_id>/', upload_workplan_form_file, name='upload_workplan_form_file'),
    path('upload_interview_form_file/<int:ojt_id>/', upload_interview_form_file, name='upload_interview_form_file'),
    path('upload_acceptance_letter_file/<int:ojt_id>/', upload_acceptance_letter_file, name='upload_acceptance_letter_file'),
    path('upload_wfh_arrangement_file/<int:ojt_id>/', upload_wfh_arrangement_file, name='upload_wfh_arrangement_file'),
    path('upload_nda_file/<int:ojt_id>/', upload_nda_file, name='upload_nda_file'),
    path('upload_work_assignment_form_file/<int:ojt_id>/', upload_work_assignment_form_file, name='upload_work_assignment_form_file'),
    path('upload_war_file/<int:ojt_id>/', upload_war_file, name='upload_war_file'),
    path('upload_timesheet_file/<int:ojt_id>/', upload_timesheet_file, name='upload_timesheet_file'),
    path('upload_coc_file/<int:ojt_id>/', upload_coc_file, name='upload_coc_file'),

]

