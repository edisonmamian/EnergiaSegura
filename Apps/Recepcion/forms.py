from django import forms
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory
from .models import *
from .custom_layout_object import *
from Apps.Clientes.models import Clientes
from Apps.Usuarios.models import Usuario
from Apps.TiposCilindros.models import TiposCilindros
from Apps.AnalisisLaboratorio.models import Analisis
from datetime import datetime
from uuid import uuid4
# form django.db import transaction

class FormRecepcion (forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = [
            'consecutivo',
            'fecha',
            'colaborador',
            'cliente'
        ]

        widgets = {
            'cliente' : ModelSelect2Widget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            )
        }

    def __init__(self, user, *args, **kwargs):
        super(FormRecepcion, self).__init__(*args, **kwargs)
        self.fields['consecutivo'].initial = uuid4().int >> 100
        self.fields['fecha'].initial = datetime.now()
        self.fields['colaborador'].initial = user.usuario

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-12 create-label'
        self.helper.field_class = 'col-md-12'
        self.helper.layout = Layout(
            Div (
                Field('fabricante'),
                Field('serial'),
                Field('capacidad'),
                Field('ultima_prueba'),
                Field('accesorios'),
                Field('valvula'),
                Field('tipo_cilindro'),
                Field('analisis'),
                HTML("<br>"),
                Fieldset('Agregar análisis',
                    Formset('cilindro')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Actualizar')),
            )
        )

        self.fields['consecutivo'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }
        self.fields['fecha'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }
        self.fields['colaborador'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }

class FormEditarRecepcion (forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = [
            'consecutivo',
            'fecha',
            'colaborador',
            'cliente'
        ]

        widgets = {
            'cliente' : ModelSelect2Widget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),


        }

    def __init__(self, user, *args, **kwargs):
        super(FormEditarRecepcion, self).__init__(user, *args, **kwargs)

        self.fields['consecutivo'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }
        self.fields['fecha'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }
        self.fields['colaborador'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly'
        }


class FormCilindros (forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = [
            'fabricante',
            'serial',
            'capacidad',
            'ultima_prueba',
            'accesorios',
            'valvula',
            'tipo_cilindro',
            'analisis'
        ]

        widgets = {
            'tipo_cilindro' : ModelSelect2Widget (
                model = TiposCilindros,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'analisis' : ModelSelect2Widget (
                model = Analisis,
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
        super (FormCilindros, self).__init__(*args, **kwargs)

        self.fields['fabricante'].widget.attrs = {
            'class' : 'form-control'
        }
        self.fields['serial'].widget.attrs = {
            'class' : 'form-control'
        }
        self.fields['capacidad'].widget.attrs = {
            'class' : 'form-control'
        }
        self.fields['ultima_prueba'].widget.attrs = {
            'class' : 'form-control'
        }
        self.fields['accesorios'].widget.attrs = {
            'class' : 'form-control'
        }
        self.fields['valvula'].widget.attrs = {
            'class' : 'form-control'
        }

FormSet_Cilindros = inlineformset_factory(
    Recepcion,
    Cilindro,
    form = FormCilindros,
    fields = [
        'fabricante',
        'serial',
        'capacidad',
        'ultima_prueba',
        'accesorios',
        'valvula',
        'tipo_cilindro',
        'analisis'
    ],
    extra = 1,
    can_delete = True
)
