
from django.urls import path
from . import views


app_name = 'productsContent'

urlpatterns = [path('', views.ProductView.as_view(), name='index'),
               
               path('<int:pk>/', views.CertainProductView.as_view(), name = 'certain_product' ),
               ]
