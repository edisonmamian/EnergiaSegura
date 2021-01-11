from django import forms
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from .models import *
from Apps.TiposCilindros.models import TiposCilindros

class FormCrearCliente (forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'estado',
            'tipo_identifcacion',
            'numero_identificacion',
            'clasificacion',
            'departamento',
            'ciudad',
            'direccion',
            'responsable_tecnico',
            'telefono_tecnico',
            'email_tecnico',
            'responsable_comercial',
            'telefono_comercial',
            'email_comercial',
            'responsable_contabilidad',
            'telefono_contabilidad',
            'email_contabilidad',
            'responsable_administrativo',
            'telefono_administrativo',
            'email_administrativo',
        ]

        widgets = {
            'clasificacion' : ModelSelect2MultipleWidget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
                }
            ),
            'departamento' : ModelSelect2Widget (
                model = Departamentos,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'ciudad' : ModelSelect2Widget (
                model = Ciudades,
                search_fields = ['nombre__icontains'],
                dependent_fields = {
                    'departamento': 'departamento'
                },
                attrs = {
                    'class': 'select2_demo_2 form-control'
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
        self.fields['ciudad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['direccion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_administrativo'].widget.attrs = {
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

class FormEditarCliente (forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'estado',
            'tipo_identifcacion',
            'numero_identificacion',
            'clasificacion',
            'departamento',
            'ciudad',
            'direccion',
            'responsable_tecnico',
            'telefono_tecnico',
            'email_tecnico',
            'responsable_comercial',
            'telefono_comercial',
            'email_comercial',
            'responsable_contabilidad',
            'telefono_contabilidad',
            'email_contabilidad',
            'responsable_administrativo',
            'telefono_administrativo',
            'email_administrativo',
        ]

        widgets = {
            'clasificacion' : ModelSelect2MultipleWidget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormEditarCliente, self).__init__(*args, **kwargs)
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
        self.fields['responsable_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_administrativo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_administrativo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_administrativo'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormEditarCliente, self).clean()

        try:
            fase = Clientes.objects.exclude(
                    numero_identificacion=self.instance.numero_identificacion
                ).get(
                tipo_identifcacion=form_data['tipo_identifcacion'],
                numero_identificacion=form_data['numero_identificacion'],
                )
            self._errors['numero_identificacion'] = ["El cliente ya existe"]
        except Clientes.DoesNotExist:
            pass


class FormCrearClasificacion (forms.ModelForm):
    class Meta:
        model = ClasificacionClientes
        fields = [
            'nombre',
            'tipos_cilindros',
            'estado'
        ]

        widgets = {
            'tipos_cilindros' : ModelSelect2MultipleWidget (
                model = TiposCilindros,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearClasificacion, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearClasificacion, self).clean()

        try:
            clasificacion = ClasificacionClientes.objects.get(nombre = form_data['nombre'])
            self._errors['nombre'] = ['La clasificación de clientes ya existe']
        except ClasificacionClientes.DoesNotExist:
            pass

class FormEditarClasificacion (forms.ModelForm):
    class Meta:
        model = ClasificacionClientes
        fields = [
            'nombre',
            'tipos_cilindros',
            'estado'
        ]

        widgets = {
            'tipos_cilindros' : ModelSelect2MultipleWidget (
                model = TiposCilindros,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        super(FormCrearClasificacion, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCrearClasificacion, self).clean()

        try:
            clasificacion = ClasificacionClientes.objects.exclude(
                nombre = self.instance
            ).get(nombre = form_data['nombre'])
            self._errors['nombre'] = ['La clasificación de clientes ya existe']
        except ClasificacionClientes.DoesNotExist:
            pass
