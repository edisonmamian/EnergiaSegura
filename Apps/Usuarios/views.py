from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearRol (CreateView):
    model = Roles
    template_name = "Usuarios/crear_rol.html"
    form_class = FormCrearRoles

    def get_success_url(self):
        return reverse("Usuarios:crear_rol")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el rol"
        )
        return super(CrearRol, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el rol, por favor revise los datos"
        )
        return super(CrearRol, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearRol, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Roles.objects.all()
        return context

class ActualizarRol (UpdateView):
    model = Roles
    template_name = "Usuarios/crear_rol.html"
    form_class = FormEditarRoles

    def get_success_url(self):
        return reverse("Usuarios:crear_rol")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el Rol"
        )
        return super(ActualizarRol, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el Rol, por favor revise los datos"
        )
        return super(ActualizarRol, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ActualizarRol, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= Roles.objects.all()
        return context
