from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),
               path('checkout/', views.get_checkout, name = 'checkout'),
               ]