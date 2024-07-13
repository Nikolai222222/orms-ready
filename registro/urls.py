from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
 path('login/', login_view, name='login'),   
 path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('autos/', views.lista_autos, name='autos'),
]