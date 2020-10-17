from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearTipoCilindro (CreateView):
    model = TiposCilindros
    template_name = "TiposCilindros/CrearTiposCilindros.html"
    form_class = FormCrearTiposCilindros

    def get_success_url(self):
        return reverse("TiposCilindros:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el Tipo de cilindro"
        )
        return super(CrearTipoCilindro, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el tipo de cilindro, por favor revise los datos"
        )
        return super(CrearTipoCilindro, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearTipoCilindro, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= TiposCilindros.objects.all()
        return context

class ActualizarTipoCilindro (UpdateView):
    model = TiposCilindros
    template_name = "TiposCilindros/CrearTiposCilindros.html"
    form_class = FormEditarTiposCilindros

    def get_success_url(self):
        return reverse("TiposCilindros:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el Tipo de cilindro"
        )
        return super(ActualizarTipoCilindro, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el tipo de cilindro, por favor revise los datos"
        )
        return super(ActualizarTipoCilindro, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ActualizarTipoCilindro, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= TiposCilindros.objects.all()
        return context
