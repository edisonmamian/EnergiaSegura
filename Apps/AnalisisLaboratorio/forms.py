from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from .models import *

class FormCrearFases (forms.ModelForm):
    class Meta:
        model = Fases
        fields = [
            'nombre',
            'fases_previas',
            'estado'
        ]

        widgets = {
            'fases_previas' : ModelSelect2MultipleWidget (
                model = Fases,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearFases, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
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

        widgets = {
            'fases_previas' : ModelSelect2MultipleWidget (
                model = Fases,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormEditarFases, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
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
