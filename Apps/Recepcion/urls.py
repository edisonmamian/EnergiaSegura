from django.urls import path
from Apps.Recepcion.views import *

app_name = 'Recepcion'
urlpatterns = [
    path('crear/', CrearRecepcion.as_view(), name='crear')
]
