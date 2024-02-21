from django.contrib import admin
from django.urls import path, include

from .views.epmd.views import index


from .views.epmd.ojt_view import epmd_ojt, add_data_ojt, update_data_ojt, delete_data_ojt, view_data_ojt
from .views.epmd.engage_view import epmd_engage, add_data_engage, update_data_engage, delete_data_engage, view_data_engage
from .views.tmd.tmd_view import tmd, add_data_tmd
from .views.c3d2.c3d2_view import c3d2, add_data_c3d2, update_data_c3d2, delete_data_c3d2, view_data_c3d2

from .views.auth.auth import login_page, logout_page

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
    path("", index, name="index"),
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
      #
    #

    path('c3d2/', c3d2, name='c3d2'),
    path('c3d2/add_data_c3d2/', add_data_c3d2, name='add_data_c3d2'),
    path('c3d2/update_data_c3d2/<int:c3d2_id>/',update_data_c3d2, name='update_data_c3d2'),
    path('c3d2/delete_data_c3d2/<int:c3d2_id>/',delete_data_c3d2, name='delete_data_c3d2'),
    path('c3d2/view_data_c3d2/<int:c3d2_id>/',view_data_c3d2, name='view_data_c3d2'),

    
    
]

