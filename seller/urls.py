 
 
from django.contrib import admin
from django.urls import path
from .import views
app_name = 'seller'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('delete_product/<str:id>',views.delete_product, name='delete_product'),
    path('New_Item/',views.New_Item, name='New_Item'),
    path('Edit/<str:id>/',views.Edit, name='Edit'),
     
]
