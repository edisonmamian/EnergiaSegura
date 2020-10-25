from django import forms
from .models import *

class FormCrearFases (forms.ModelForm):
    class Meta:
        model = Fases
        fields = [
            'nombre',
            'fases_previas',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormCrearFases, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fases_previas'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearFases, self).clean()

        try:
            fase = Fases.objects.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["La fase ya existe"]
        except Fases.DoesNotExist:
            pass

class FormEditarFases (forms.ModelForm):
    class Meta:
        model = Fases
        fields = [
            'nombre',
            'fases_previas',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormEditarFases, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fases_previas'].widget.attrs = {
            'class': 'select2 form-control',
            'multiple': 'multiple'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control',

        }

    def clean (self):
        form_data = super(FormEditarFases, self).clean()
        try:
            fase = Fases.objects.exclude(nombre=self.instance)
            fase = fase.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["La fase ya existe"]
        except Fases.DoesNotExist:
            pass
