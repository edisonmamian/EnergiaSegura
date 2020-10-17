from django.urls import path

from Apps.Usuarios.views import *

app_name = 'Usuarios'
urlpatterns = [
    path ('roles/crear/', CrearRol.as_view(), name = 'crear_rol'),
    path ('roles/editar/(?P<pk>\d+)/', ActualizarRol.as_view(), name = 'editar_rol')
]
