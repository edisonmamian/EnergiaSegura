from django.urls import path

from Apps.Usuarios.views import *

app_name = 'Usuarios'
urlpatterns = [
    path ('roles/crear/', CrearRol.as_view(), name = 'crear_rol'),
    path ('roles/editar/<int:pk>/', ActualizarRol.as_view(), name = 'editar_rol'),
    path ('crear/', CrearUsuario.as_view(), name = 'crear'),
    path ('listar/', ListarUsuario.as_view(), name = 'listar'),
    path ('editar/<int:pk>/', ActualizarUsuario.as_view(), name = 'editar'),
]
