"""SistemaInformacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('usuarios/', include('Apps.Usuarios.urls')),
    path('tiposcilindros/', include('Apps.TiposCilindros.urls')),
    path('analisislaboratorio/', include('Apps.AnalisisLaboratorio.urls')),
    path('clientes/', include('Apps.Clientes.urls')),
    path('recepcion/', include('Apps.Recepcion.urls')),
    path('select2/', include('django_select2.urls')),
]
