from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Usuario
from django.http import HttpResponseForbidden


# Registro de usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

# Login
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

# Logout
def logout_usuario(request):
    logout(request)
    return redirect('login')

# Redirección según rol
@login_required
def dashboard(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    elif request.user.tipo_usuario == 'cliente':
        return redirect('cliente_dashboard')
    elif request.user.tipo_usuario == 'artista':
        return redirect('artista_dashboard')
    else:
        return HttpResponseForbidden("Tipo de usuario desconocido.")
