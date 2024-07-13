from django.urls import path
from .views import agregar_al_carrito, ver_carrito, eliminar_del_carrito


app_name = 'carro'

urlpatterns = [
    path('agregar_al_carrito/<int:auto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:auto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),

]
