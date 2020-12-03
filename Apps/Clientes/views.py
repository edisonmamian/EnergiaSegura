from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from .models import *
from .forms import *
import requests
import json

# Create your views here.
class ActualizarDepartamentoCiudades ():

    with open('static/dep_ciudades.json') as file:
        data = json.load(file)

        for municipio in data['Municipios']:
            departamento, created = Departamentos.objects.get_or_create(
                nombre = municipio['Nombre_Departamento'],
                codigo_dane = municipio['Codigo_Deapartamento']
            )

            municipio, created = Ciudades.objects.get_or_create(
                nombre = municipio['Nombre_Municipio'],
                codigo_dane = municipio['Codigo_Deapartamento'] + municipio['Codigo_Municipio'],
                departamento = departamento
            )

class CrearClientes (CreateView):
    model = Clientes
    template_name = "Clientes/crear_cliente.html"
    form_class = FormCrearCliente

    def get_success_url(self):
        return reverse("Clientes:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el cliente"
        )
        return super(CrearClientes, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el cliente, por favor revise los datos"
        )
        return super(CrearClientes, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearClientes, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        return context

class EditarClientes (UpdateView):
    model = Clientes
    template_name = "Clientes/crear_cliente.html"
    form_class = FormCrearCliente

    def get_success_url(self):
        return reverse("Clientes:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha editado exitosamente el cliente"
        )
        return super(EditarClientes, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al editar el cliente, por favor revise los datos"
        )
        return super(EditarClientes, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarClientes, self).get_context_data(**kwargs)
        context['boton']= "Editar"
        return context
