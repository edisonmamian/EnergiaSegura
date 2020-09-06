from django.urls import path

from Apps.Usuarios.views import *

urlpatterns = [
    path ('index/', Ejemplo.as_view())
]
