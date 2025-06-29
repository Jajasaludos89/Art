from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Vista de login usando correo electrónico
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)  # Buscar usuario por email
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/registroArtista/')  # Cambia a tu vista deseada
            else:
                messages.error(request, 'Contraseña incorrecta')
        except User.DoesNotExist:
            messages.error(request, 'No existe una cuenta con ese correo')
    
    return render(request, 'login.html')

# Vista de registro (sin cambios mayores)
def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe una cuenta con ese correo')
        else:
            # Generar un username a partir del email
            username = email.split('@')[0]

            # Asegurar que sea único (por si alguien más usó ese username antes)
            contador = 1
            original_username = username
            while User.objects.filter(username=username).exists():
                username = f"{original_username}{contador}"
                contador += 1

            # Crear usuario con nombre y apellido
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=nombre,
                last_name=apellido
            )
            messages.success(request, 'Usuario creado con éxito. Ahora puedes iniciar sesión.')
            return redirect('/login/')
    
    return render(request, 'registro.html')

# Cierre de sesión
def logout_view(request):
    logout(request)
    return redirect('/login/')
