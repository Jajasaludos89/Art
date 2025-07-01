from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Usuario
from django.contrib.auth import logout

@login_required
def ver_perfil(request):
    return render(request, 'perfil/perfil.html')

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('ver_perfil')
    return render(request, 'perfil/editar_perfil.html', {'usuario': usuario})

@login_required
def eliminar_perfil(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.user == usuario:
        usuario.delete()
        messages.success(request, 'Perfil eliminado correctamente.')
        logout(request)
        return redirect('login')
    else:
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('ver_perfil')
