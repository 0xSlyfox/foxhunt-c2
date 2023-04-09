from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/beacons/', views.BeaconList.as_view(), name='beacon_list'),
    path('api/commands/', views.CommandList.as_view(), name='command_list'),
    path('api/logs/', views.LogList.as_view(), name='log_list'),
    path('api/notes/', views.NoteList.as_view(), name='note_list'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views_auth.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('', include('controlpanel.urls')),
]


