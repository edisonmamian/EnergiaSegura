from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from django.forms import formset_factory
from SistemaInformacion.utilities import verificar_permiso
from .models import *
from .forms import *

# Create your views here.
class CrearTipoCilindro (CreateView):
    model = TiposCilindros
    template_name = "TiposCilindros/CrearTiposCilindros.html"
    form_class = FormCrearTiposCilindros

    @verificar_permiso(permiso_requerido = 'crear tipos de cilindros')
    def dispatch(self, request, *args, **kwargs):
        return super(CrearTipoCilindro, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("TiposCilindros:crear")

    def form_valid (self, form):
        context = self.get_context_data()
        analisis = context ['analisis']

        if analisis.is_valid():
            self.object = form.save()
            analisis.instance = self.object
            analisis.save()
        else:
            messages.error (
                self.request,
                "Error al registrar el tipo de cilindro, por favor revise los datos"
            )
            return super(CrearTipoCilindro, self).form_invalid(form)

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

        if self.request.POST:
            context['analisis'] = FormSet_TiposCilindros_Analisis (
                self.request.POST
            )
        else:
            context['analisis'] = FormSet_TiposCilindros_Analisis ()

        return context

class ActualizarTipoCilindro (UpdateView):
    model = TiposCilindros
    template_name = "TiposCilindros/CrearTiposCilindros.html"
    form_class = FormEditarTiposCilindros

    @verificar_permiso(permiso_requerido = 'editar tipos de cilindros')
    def dispatch(self, request, *args, **kwargs):
        return super(ActualizarTipoCilindro, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("TiposCilindros:crear")

    def form_valid (self, form):
        context = self.get_context_data()
        analisis = context ['analisis']

        if analisis.is_valid():
            self.object = form.save()
            analisis.instance = self.object
            analisis.save()
        else:
            messages.error (
                self.request,
                "Error al actualizar el tipo de cilindro, por favor revise los datos"
            )
            return render(self.request, self.template_name, context)

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

        if self.request.POST:
            context['analisis'] = FormSet_Editar_TiposCilindros_Analisis (
                self.request.POST,
                instance=self.object
            )
        else:
            context['analisis'] = FormSet_Editar_TiposCilindros_Analisis (
                instance=self.object
            )

        return context
