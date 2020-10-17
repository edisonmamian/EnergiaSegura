from django import forms
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
            tipoCilindro = Roles.objects.exclude(nombre=form_data['nombre']).get(nombre=form_data['nombre'])
            self.errors['nombre'] = ["El rol ya existe"]
        except Roles.DoesNotExist:
            pass
