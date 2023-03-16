from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='usuarios'),
    path('agregarUsuario/', views.AgregarUsuario, name="agregarUsuario"),
]