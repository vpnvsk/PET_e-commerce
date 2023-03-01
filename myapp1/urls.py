from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'myapp1'

urlpatterns = [path('', views.ProductView.as_view(), name='index'),
               path('<int:pk>/', views.CertainProductView.as_view()),
               path('signup/', views.sigup, name='signup'),
               path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form= LoginForm), name = 'login')
               ]