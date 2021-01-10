from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from SistemaInformacion.utilities import verificar_permiso
from .models import *
from .forms import *
# Create your views here.
class CrearFase (CreateView):
    model = Fases
    template_name = "AnalisisLaboratorio/fases.html"
    form_class = FormCrearFases

    @verificar_permiso(permiso_requerido = 'crear fases')
    def dispatch(self, request, *args, **kwargs):
        return super(CrearFase, self).dispatch(request, *args, **kwargs)

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

    @verificar_permiso(permiso_requerido = 'editar fases')
    def dispatch(self, request, *args, **kwargs):
        return super(EditarFase, self).dispatch(request, *args, **kwargs)

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
            "Error al editar la fase, por favor revise los datos"
        )
        return super(EditarFase, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarFase, self).get_context_data(**kwargs)
        context['boton']= "Editar"
        context['fases']= Fases.objects.all()
        return context

class CrearAnalisis (CreateView):
    model = Analisis
    template_name = "AnalisisLaboratorio/analisis.html"
    form_class = FormCrearAnalisis

    @verificar_permiso(permiso_requerido = 'crear analisis')
    def dispatch(self, request, *args, **kwargs):
        return super(CrearAnalisis, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("AnalisisLaboratorio:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el análisis de laboratorio"
        )
        return super(CrearAnalisis, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al editar el análisis de laboratorio, por favor revise los datos"
        )
        return super(CrearAnalisis, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearAnalisis, self).get_context_data(**kwargs)
        context['boton']= "Crear"
        context['analisis']= Analisis.objects.all()
        return context

class EditarAnalisis (UpdateView):
    model = Analisis
    template_name = "AnalisisLaboratorio/analisis.html"
    form_class = FormEditarAnalisis

    @verificar_permiso(permiso_requerido = 'editar analisis')
    def dispatch(self, request, *args, **kwargs):
        return super(EditarAnalisis, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("AnalisisLaboratorio:crear")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el análisis de laboratorio"
        )
        return super(EditarAnalisis, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al editar el análisis de laboratorio, por favor revise los datos"
        )
        return super(EditarAnalisis, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarAnalisis, self).get_context_data(**kwargs)
        context['boton']= "Editar"
        context['analisis']= Analisis.objects.all()
        return context
