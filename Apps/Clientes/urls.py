from django.urls import path
from Apps.Clientes.views import *

app_name = 'Clientes'
urlpatterns = [
    path ('crear/', CrearClientes.as_view(), name = 'crear'),
    path ('editar/<int:pk>/', CrearClientes.as_view(), name = 'editar'),
    path ('clasificacion/crear/', CrearClasificacion.as_view(), name = 'clasificacion_crear'),
    path ('clasificacion/editar/<int:pk>/', EditarClasificacion.as_view(), name = 'clasificacion_editar')
]
