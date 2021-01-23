from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from SistemaInformacion.utilities import verificar_permiso
from .models import *
from .forms import *

# Create your views here.
class CrearRecepcion (CreateView):
    model = Recepcion
    form_class = FormRecepcion
    template_name = "Recepcion/crear.html"

    #@verificar_permiso(permiso_requerido = 'crear roles')
    def dispatch(self, request, *args, **kwargs):
        return super(CrearRecepcion, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(CrearRecepcion, self).get_form_kwargs(**kwargs)
        kwargs['user'] = self.request.user.usuario
        return kwargs

    def get_success_url(self):
        return reverse("Recepcion:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha realizado la recepción de cilindros exitosamente"
        )
        return super(CrearRecepcion, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Error al realizar la recepción, por favor revise el dato"
        )
        return super(CrearRecepcion, self).form_invalid(form)

    def get_context_data (self, **kwargs):
        context = super(CrearRecepcion, self).get_context_data(**kwargs)
        context['boton'] = 'Registrar'
        return context
