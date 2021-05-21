from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from django.contrib.auth.forms import UserCreationForm
from .models import *

class FormCrearRoles (forms.ModelForm):
    class Meta:
        model = Roles
        fields = [
            'nombre',
            'estado',
            'permisos'
        ]

        widgets = {


            'permisos' : ModelSelect2MultipleWidget (
                model = Permisos,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
                }
            ),
        }

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
            self._errors['nombre'] = ["El tipo rol ya existe"]
        except Roles.DoesNotExist:
            pass


class FormEditarRoles (forms.ModelForm):
    class Meta:
        model = Roles
        fields = [
            'nombre',
            'estado',
            'permisos'
        ]

        widgets = {
            'permisos' : ModelSelect2MultipleWidget (
                model = Permisos,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

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
            tipoCilindro = Roles.objects.exclude(nombre=self.instance)
            tipoCilindro = tipoCilindro.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["El rol ya existe"]
        except Roles.DoesNotExist:
            pass

class FormCrearUsuario (UserCreationForm):
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
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'
        self.fields['username'].label = 'Usuario'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True

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

class FormActualizarUsuario (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormCrearUsuario, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'
        self.fields['username'].label = 'Usuario'
        self.fields['is_active'].label = '¿Activo?'
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
            'is_active',
            'rol'
        )

    def __init__(self, *args, **kwargs):
        super(FormActualizarUsuario, self).__init__(*args, **kwargs)
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
        self.fields['is_active'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['rol'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormActualizarUsuario, self).clean()

        try:
            documento = Usuario.objects.exclude(
                numero_documento = self.instance.numero_documento,
                tipo_documento = self.instance.tipo_documento
                ).get(
                numero_documento = form_data['numero_documento'],
                tipo_documento = form_data['tipo_documento']
            )
            self._errors['numero_documento'] = ["Ya existe un usuario con el mismo número de documento"]
        except Usuario.DoesNotExist:
            pass

        try:
            usuario = Usuario.objects.exclude(username = self.instance.username).get(
                username = form_data['username']
            )
            self._errors['username'] = ["Ya existe el usuario"]
        except Usuario.DoesNotExist:
            pass

        return form_data

class FormActualizarPerfil (forms.ModelForm):
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
        )

    def __init__(self, *args, **kwargs):
        super(FormActualizarPerfil, self).__init__(*args, **kwargs)
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

    def clean (self):
        form_data = super(FormActualizarPerfil, self).clean()

        try:
            documento = Usuario.objects.exclude(
                numero_documento = self.instance.numero_documento,
                tipo_documento = self.instance.tipo_documento
                ).get(
                numero_documento = form_data['numero_documento'],
                tipo_documento = form_data['tipo_documento']
            )
            self._errors['numero_documento'] = ["Ya existe un usuario con el mismo número de documento"]
        except Usuario.DoesNotExist:
            pass

        try:
            usuario = Usuario.objects.exclude(username = self.instance.username).get(
                username = form_data['username']
            )
            self._errors['username'] = ["Ya existe el usuario"]
        except Usuario.DoesNotExist:
            pass

        return form_data

class LoginForm (forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label = 'Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
