from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [
    path('', views.lista_autos, name='lista_autos'),
    path('detalles/<int:id>/', views.detalles_autos, name='detalles_autos'),
    path('agregar_al_carrito/<int:id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

]
