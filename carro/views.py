from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from carro.models import Carro
from autos.models import Auto
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.http import JsonResponse



@login_required
def agregar_al_carrito(request, auto_id):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'Necesitas iniciar sesión para agregar autos al carrito.'})
    auto = get_object_or_404(Auto, id=auto_id)
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    carro.autos.add(auto)
    return JsonResponse({'success': True, 'cart_count': carro.autos.count()})

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