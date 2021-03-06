from django.urls import path
from Apps.AnalisisLaboratorio.views import *

app_name = 'AnalisisLaboratorio'
urlpatterns = [
    path ('fases/crear/', CrearFase.as_view(), name = 'fases_crear'),
    path ('fases/editar/<int:pk>/', EditarFase.as_view(), name = 'fases_editar'),
    path ('crear/', CrearAnalisis.as_view(), name = 'crear'),
    path ('editar/<int:pk>/', EditarAnalisis.as_view(), name = 'editar')
]
