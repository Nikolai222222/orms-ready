from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from carro.models import Carro
from autos.models import Auto


@login_required
def agregar_al_carrito(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    carro.autos.add(auto)
    return redirect('carro:ver_carrito')

@login_required
def ver_carrito(request):
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    context = {'carro': carro}
    return render(request, 'carro/ver_carrito.html', context)

def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/lista_autos.html', {'autos': autos})

@login_required
def eliminar_del_carrito(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    carro = get_object_or_404(Carro, usuario=request.user)
    carro.autos.remove(auto)
    return redirect('carro:ver_carrito')
