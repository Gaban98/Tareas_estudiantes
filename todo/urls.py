from django.urls import path
from . import views

# ESTO ES TODOS #
urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<int:tarea_id>', views.EliminarTarea, name='eliminar'),
    path('editar/<int:tarea_id>', views.EditarTarea, name='editar'),
]