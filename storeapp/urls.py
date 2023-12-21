 
 
from django.contrib import admin
from django.urls import path
from .import views
app_name = 'storeapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('detail/<str:id>',views.detail, name='detail'),
    path('checkout/',views.checkout, name='checkout'),
    path('updateItem/',views.updateItem, name='updateItem'),
    path('updateQuantity/',views.updateQuantity, name='updateQuantity'),
]
