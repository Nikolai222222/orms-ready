from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from carro.models import Carro
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse



def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/lista_autos.html', {'autos': autos})

def detalles_autos(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/detalles_autos.html', {'auto': auto})

@require_POST
def agregar_al_carrito(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    carrito = request.session.get('carrito', [])
    carrito.append(auto_id)
    request.session['carrito'] = carrito
    response_data = {
        'success': True,
        'cart_count': len(carrito)
    }
    return JsonResponse(response_data)


def ver_carrito(request):
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    context = {'carro': carro}
    return render(request, 'carro/ver_carrito.html', context)

