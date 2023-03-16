from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.
def home(request):
    tarea = Tarea.objects.all()
    # tarea es una variable, pero Tarea es el modelo#
    #esto es para que se muestre en el html y uso del ORM#
    context = {'tarea': tarea}
    # la que esta entre comillas que es la que se usa en el html#
    # la que esta en azul es la que se usa en el views#
    return render(request, 'home.html', context)

def agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
        context = {'form': form}
        return render(request, 'agregar.html',context)

def EliminarTarea (request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def EditarTarea (request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'GET':
        form = TareaForm(instance=tarea)
    else:
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'agregar.html', {'form':form})