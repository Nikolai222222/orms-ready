from django.urls import path
from django.contrib.auth import views as auth_views
from autos import views as autos_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('autos/', autos_views.lista_autos, name='autos'),
    path('', views.registro, name='registrarse'),
    
]