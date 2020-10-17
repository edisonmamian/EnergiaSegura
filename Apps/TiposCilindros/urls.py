from django.urls import path
from Apps.TiposCilindros.views import *

app_name = 'TiposCilindros'
urlpatterns = [
    path ('crear/', CrearTipoCilindro.as_view(), name = 'crear'),
    path ('editar/(?P<pk>\d+)/', ActualizarTipoCilindro.as_view(), name = 'editar')
]
