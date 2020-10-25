from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
class CrearFase (CreateView):
    model = Fases
    template_name = "AnalisisLaboratorio/fases.html"
    form_class = FormCrearFases

    def get_success_url(self):
        return reverse("AnalisisLaboratorio:fases_crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la fase"
        )
        return super(CrearFase, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la fase, por favor revise los datos"
        )
        return super(CrearFase, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearFase, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['fases']= Fases.objects.all()
        return context

class EditarFase (UpdateView):
    model = Fases
    template_name = "AnalisisLaboratorio/fases.html"
    form_class = FormEditarFases

    def get_success_url(self):
        return reverse("AnalisisLaboratorio:fases_crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la fase"
        )
        return super(EditarFase, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la fase, por favor revise los datos"
        )
        return super(EditarFase, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarFase, self).get_context_data(**kwargs)
        context['boton']= "Editar"
        context['fases']= Fases.objects.all()
        return context
