from django import forms
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from django.db.models import Max
from .models import *
from Apps.Clientes.models import Clientes
from Apps.Usuarios.models import Usuario
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
            ),


        }

    def __init__(self, user, *args, **kwargs):
        super(FormRecepcion, self).__init__(*args, **kwargs)


        self.fields['consecutivo'].initial = uuid4().int >> 100
        self.fields['fecha'].initial = datetime.now()
        self.fields['colaborador'].initial = user.usuario



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
