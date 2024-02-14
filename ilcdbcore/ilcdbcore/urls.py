
from django.contrib import admin
from django.urls import path, include


from main.views import dashboard_page, login_page, logout_page
from main.view_ojt_trainees import epmd_ojt, view_data_ojt, add_data_ojt, update_data_ojt, delete_data_ojt
from main.view_engage_partner import  epmd_engage, add_data_engage_partner,view_data_engage,update_data_engage, delete_data_engage
from django.contrib.auth import views as auth_views





urlpatterns = [
    
    # for auto reload
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('admin/', admin.site.urls),
    
    
    
    path('login', login_page, name='login_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout', logout_page, name='logout_page'),
    
    # path('register', register_page, name='register_page'),  
     
    
    
    path('', dashboard_page, name='dashboard_page'),      
    
    
    # # engage
     path('epmd_engage', epmd_engage, name='epmd_engage'),  
     path('epmd_engage/add_data_engage/', add_data_engage_partner, name='add_data_engage'),
     path('epmd_engage/update_data_engage/<int:engage_id>/',update_data_engage, name='update_data_engage'),
     path('epmd_engage/delete_data_engage/<int:engage_id>/',delete_data_engage, name='delete_data_engage'),
     path('epmd_engage/view_data_engage/<int:engage_id>/',view_data_engage, name='view_data_engage'),
    
    # EMPD
    path('epmd_ojt', epmd_ojt, name='epmd_ojt'),  
    path('epmd_ojt/add_data_ojt/', add_data_ojt, name='add_data_ojt'),
    path('epmd_ojt/update_data_ojt/<int:ojt_id>/',update_data_ojt, name='update_data_ojt'),
    path('epmd_ojt/delete_data_ojt/<int:ojt_id>/',delete_data_ojt, name='delete_data_ojt'),
    path('epmd_ojt/view_data_ojt/<int:ojt_id>/',view_data_ojt, name='view_data_ojt'),
    
    
    
]
