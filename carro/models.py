from django.db import models
from django.contrib.auth.models import User
from autos.models import Auto

class Carro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return f'Carro de {self.usuario.username}'
    
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def agregar_al_carrito(request, auto_id):
    # Lógica para agregar el auto al carrito
    carrito = request.session.get('carrito', {})
    carrito[auto_id] = carrito.get(auto_id, 0) + 1
    request.session['carrito'] = carrito

    cart_count = sum(carrito.values())

    return JsonResponse({
        'success': True,
        'cart_count': cart_count
    })