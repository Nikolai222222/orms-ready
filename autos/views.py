from django.shortcuts import render, get_object_or_404
from .models import Auto

def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/lista_autos.html', {'autos': autos})

def detalles_autos(request, id):  # Asegúrate de que este nombre coincida
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/detalles_autos.html', {'auto': auto})

def agregar_al_carrito(request, id):
    # Lógica para agregar al carrito
    pass
