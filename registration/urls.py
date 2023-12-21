 
 
from django.contrib import admin
from django.urls import path
from .import views
app_name = 'registration'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_login/',views.user_login, name='user_login'),
     path('signup/',views.signup, name='signup'),
     path('logout/',views.user_logout, name='logout'),
     
]
