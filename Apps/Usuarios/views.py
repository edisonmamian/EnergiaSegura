from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
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

class CrearUsuario (CreateView):
    model = Usuario
    template_name = "Usuarios/crear.html"
    form_class = FormCrearUsuario

    def get_success_url(self):
        return reverse("Usuarios:listar")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el usuario"
        )
        return super(CrearUsuario, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el usuario, por favor revise los datos"
        )
        return super(CrearUsuario, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearUsuario, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        return context

class ListarUsuario (ListView):
    model = Usuario
    template_name = "Usuarios/listar.html"


class ActualizarUsuario (UpdateView):
    model = Usuario
    template_name = "Usuarios/crear.html"
    form_class = FormActualizarUsuario

    def get_success_url(self):
        return reverse("Usuarios:listar")

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el usuario"
        )
        return super(ActualizarUsuario, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el usuario, por favor revise los datos"
        )
        return super(ActualizarUsuario, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ActualizarUsuario, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        return context

class ActualizarPerfil (UpdateView):
    model = Usuario
    template_name = "Usuarios/crear.html"
    form_class = FormActualizarPerfil

    def get_success_url(self):
        return reverse("Usuarios:listar")

    def get_object(self):
        usuario = Usuario.objects.get(pk=self.request.user.id)
        return usuario

    def form_valid(self, form):
        message.success(
            self.request,
            "Se ha actualizado exitosamente su perfil"
        )

    def form_invalid(self, form):
        message.error (
            self.request,
            "Error al actualizar su perfil, por favor revise los datos"
        )

    def get_context_data(self, **kwargs):
        context = super(ActualizarPerfil, self).get_context_data(**kwargs)
        context['boton'] = "Actualizar"
        return context

class LoginUsuario(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy ('Usuarios:listar')

    def form_valid(self, form):
        credentials = form.cleaned_data

        user = authenticate(
            username = credentials['username'],
            password = credentials['password']
        )

        if user is not None:
            login (self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.error(
                self.request,
                "No se pudo autenticar en el sistema"
            )
            return HttpResponseRedirect(reverse_lazy('Usuarios:login'))

def LogoutUsuario(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('Usuarios:login'))
