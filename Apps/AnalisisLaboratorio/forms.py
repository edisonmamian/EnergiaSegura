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

class FormCrearAnalisis (forms.ModelForm):
    class Meta:
        model = Analisis
        fields = [
            'nombre',
            'estado',
            'unidad_medida',
            'valor_minimo',
            'valor_maximo',
            'fase'
        ]

    def __init__(self, *args, **kwargs):
        super(FormCrearAnalisis, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['unidad_medida'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['valor_minimo'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['valor_maximo'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['fase'].widget.attrs = {
            'class': 'form-control',
        }

    def clean (self):
        form_data = super(FormCrearAnalisis, self).clean()
        try:
            fase = Fases.objects.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["El análisis de laboratorio ya existe"]
        except Fases.DoesNotExist:
            pass

        if form_data['valor_minimo'] > form_data['valor_maximo']:
            self._errors['valor_minimo'] = ["El valor mínimo debe ser menor al valor máximo"]

        if form_data['valor_maximo'] < form_data['valor_minimo']:
            self._errors['valor_maximo'] = ["El valor máximo debe ser superior al valor mínimo"]

class FormEditarAnalisis (forms.ModelForm):
    class Meta:
        model = Analisis
        fields = [
            'nombre',
            'estado',
            'unidad_medida',
            'valor_minimo',
            'valor_maximo',
            'fase'
        ]

    def __init__(self, *args, **kwargs):
        super(FormEditarAnalisis, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['unidad_medida'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['valor_minimo'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['valor_maximo'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['fase'].widget.attrs = {
            'class': 'form-control',
        }

    def clean (self):
        form_data = super(FormEditarAnalisis, self).clean()
        try:
            fase = Fases.objects.exclude(nombre=self.instance)
            fase = fase.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["El análisis de laboratorio ya existe"]
        except Fases.DoesNotExist:
            pass

        if form_data['valor_minimo'] > form_data['valor_maximo']:
            self._errors['valor_minimo'] = ["El valor mínimo debe ser menor al valor máximo"]

        if form_data['valor_maximo'] < form_data['valor_minimo']:
            self._errors['valor_maximo'] = ["El valor máximo debe ser superior al valor mínimo"]
