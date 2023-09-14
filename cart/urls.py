from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [path('add-to-cart/<int:pk>/', views.AddToCartView.as_view(), name='add-to-cart'),
               path('checkout/', views.get_checkout, name = 'checkout'),
               path('remove-from-cart/<int:pk>/', views.remove_from_cart, name= 'remove-from-cart'),
               ]