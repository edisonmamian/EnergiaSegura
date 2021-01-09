import os

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.db import models, connection

def verificar_permiso (permiso_requerido):
    def _method_wrapper (view_method):
        def _arguments_wrapper (request, *args, **kwargs):
            initial_request = request
            if hasattr(request, "request"):
                request = request.request

            try:
                try:
                    permisos = request.session['permisos']
                except KeyError:
                    try:
                        permisos = request.user.usuario.rol.permisos.all()
                        request.session['permisos']
                    except IndexError:
                        messages.error(request, "Para acceder a la página solicitada requiere inicar sesión")
                        return redirect('Usuarios:login')

                    if not (permiso_requerido in permisos):
                        message.error(request, "No cuenta con los permisos requeridos para esta acción")
                        return redirect('Usuarios:login')
            except AttributeError:
                messages.error(request, "Para acceder a la página solicitada requiere inicar sesión")
                return redirect('Usuarios:login')

            return view_method(initial_request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
