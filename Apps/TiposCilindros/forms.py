from django import forms
from .models import *

class FormCrearTiposCilindros (forms.ModelForm):
    class Meta:
        model = TiposCilindros
        fields = [
            'nombre',
            'vidaUtil',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormCrearTiposCilindros, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['vidaUtil'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
            'value':'10.00'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearTiposCilindros, self).clean()

        try:
            tipoCilindro = TiposCilindros.objects.get(nombre=form_data['nombre'])
            self.errors['nombre'] = ["El tipo de cilindro ya existe"]
        except TiposCilindros.DoesNotExist:
            pass


class FormEditarTiposCilindros (forms.ModelForm):
    class Meta:
        model = TiposCilindros
        fields = [
            'nombre',
            'vidaUtil',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        super(FormEditarTiposCilindros, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['vidaUtil'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
            'value':'10.00'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormEditarTiposCilindros, self).clean()
        try:
            tipoCilindro = TiposCilindros.objects.exclude(nombre=self.instance.id).get(nombre=form_data['nombre'])
            self.errors['nombre'] = ["El tipo de cilindro ya existe"]
        except TiposCilindros.DoesNotExist:
            pass
