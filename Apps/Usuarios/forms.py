from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class FormCrearRoles (forms.ModelForm):
    class Meta:
        model = Roles
        fields = [
            'nombre',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormCrearRoles, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearRoles, self).clean()

        try:
            tipoCilindro = Roles.objects.get(nombre=form_data['nombre'])
            self.errors['nombre'] = ["El tipo rol ya existe"]
        except Roles.DoesNotExist:
            pass


class FormEditarRoles (forms.ModelForm):
    class Meta:
        model = Roles
        fields = [
            'nombre',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormEditarRoles, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormEditarRoles, self).clean()
        try:
            tipoCilindro = Roles.objects.exclude(nombre=self.instance.id).get(nombre=form_data['nombre'])
            self.errors['nombre'] = ["El rol ya existe"]
        except Roles.DoesNotExist:
            pass

class FormCrearUsuario (UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(FormCrearUsuario, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'
        self.fields['username'].label = 'Usuario'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True

    class Meta:
        model = Usuario
        fields = (
            'first_name',
            'segundo_nombre',
            'last_name',
            'segundo_apellido',
            'tipo_documento',
            'numero_documento',
            'telefono',
            'username',
            'rol',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(FormCrearUsuario, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['segundo_nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['segundo_apellido'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tipo_documento'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['numero_documento'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['username'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['rol'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearUsuario, self).clean()

        try:
            documento = Usuario.objects.get(
                numero_documento = form_data['numero_documento'],
                tipo_documento = form_data['tipo_documento']
            )
            self._errors['numero_documento'] = ["Ya existe un usuario con el mismo número de documento"]
        except Usuario.DoesNotExist:
            pass

        try:
            usuario = Usuario.objects.get(
                username = form_data['username']
            )
            self._errors['username'] = ["Ya existe el usuario"]
        except Usuario.DoesNotExist:
            pass

        return form_data
