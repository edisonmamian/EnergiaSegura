from django.urls import path
from Apps.TiposCilindros.views import *

app_name = 'TiposCilindros'
urlpatterns = [
    path ('crear/', CrearTipoCilindro.as_view(), name = 'crear'),
    path ('editar/<int:tipos_cilidnros_id>/', ActualizarTipoCilindro.as_view(), name = 'editar')
]
