# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registro/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registro/login.html')

@login_required
def home_view(request):
    return render(request, 'registro/home.html')
