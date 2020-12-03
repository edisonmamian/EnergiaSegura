from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from .models import *

class FormCrearCliente (forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'estado',
            'tipo_identifcacion',
            'numero_identificacion',
            'departamento',
            'ciudad',
            'direccion',
            'telefono_tecnico',
            'email_tecnico',
            'telefono_comercial',
            'email_comercial',
            'telefono_contabilidad',
            'email_contabilidad',
            'telefono_administrativo',
            'email_administrativo',
        ]

        widgets = {
            'fases_previas' : ModelSelect2MultipleWidget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearCliente, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tipo_identifcacion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['numero_identificacion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['departamento'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['ciudad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['direccion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_administrativo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_administrativo'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearFases, self).clean()

        try:
            fase = Clientes.objects.get(
                tipo_identifcacion=form_data['tipo_identifcacion'],
                numero_identificacion=form_data['numero_identificacion'],
                )
            self._errors['numero_identificacion'] = ["El cliente ya existe"]
        except Clientes.DoesNotExist:
            pass
