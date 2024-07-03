from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from carro.models import Carro
from django.http import HttpResponse


def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/lista_autos.html', {'autos': autos})

def detalles_autos(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/detalles_autos.html', {'auto': auto})

def agregar_al_carrito(request, auto_id):
    if request.method == 'POST':
        auto = get_object_or_404(Auto, id=auto_id)
        carro, created = Carro.objects.get_or_create(usuario=request.user)
        carro.autos.add(auto)
        return redirect('ver_carrito')
    return HttpResponse(status=405)

def ver_carrito(request):
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    context = {'carro': carro}
    return render(request, 'carro/ver_carrito.html', context)

