from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # Redirige al usuario a la página 'autos' después de iniciar sesión
            return redirect('autos')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registro/login.html', {'form': form})

def lista_autos(request):
    return render(request, 'autos/lista_autos.html')