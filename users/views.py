from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuariosForm

# Create your views here.

def usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios.html', context)

def AgregarUsuario (request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuariosForm()
        context = {'form': form}
        return render(request, 'agregarusuario.html',context)

