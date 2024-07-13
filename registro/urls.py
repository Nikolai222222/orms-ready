from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('autos/', views.lista_autos, name='autos'),
]