
from django.contrib import admin
from django.urls import path, include

#from main.views import dashboard, epmd_ojt,insert_data,add_data_ojt_form,edit_data_ojt,view_data_ojt
from main.views import dashboard
from main.view_ojt_trainees import epmd_ojt, view_data_ojt, add_data_ojt, update_data_ojt, delete_data_ojt
from main.views_engage import engage, insert_data_engage,add_data_engage_form,edit_data_engage,view_data_engage






urlpatterns = [
    
    # for auto reload
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('admin/', admin.site.urls),
    
    
    path('', dashboard, name='dashboard'),      
    
    
    # # EMPD
    # path('epmd_ojt', epmd_ojt, name='epmd_ojt'),  
    # path('epmd_ojt/insert_data/', insert_data, name='insert_data'),
    # path('epmd_ojt/add_data_ojt_form/', add_data_ojt_form, name='add_data_ojt_form'),
    # path('epmd_ojt/edit_data_ojt/<int:application_id>/',edit_data_ojt, name='edit_data_ojt'),
    # path('epmd_ojt/view_data_ojt/<int:application_id>/',view_data_ojt, name='view_data_ojt'),
    
    # EMPD
    path('epmd_ojt', epmd_ojt, name='epmd_ojt'),  
    path('epmd_ojt/add_data_ojt/', add_data_ojt, name='add_data_ojt'),
    path('epmd_ojt/update_data_ojt/<int:ojt_id>/',update_data_ojt, name='update_data_ojt'),
    path('epmd_ojt/delete_data_ojt/<int:ojt_id>/',delete_data_ojt, name='delete_data_ojt'),
    path('epmd_ojt/view_data_ojt/<int:ojt_id>/',view_data_ojt, name='view_data_ojt'),
    
    # engage
    path('engage', engage, name='engage'),
    path('engage/insert_data_engage_form/', insert_data_engage, name='insert_data_engage'),
    path('engage/add_data_engage_form/', add_data_engage_form, name='add_data_engage_form'),
    path('engage/edit_data_engage/<int:application_id>/',edit_data_engage, name='edit_data_engage'),
    path('engage/view_data_engage/<int:application_id>/',view_data_engage, name='view_data_engage'),
    
]
