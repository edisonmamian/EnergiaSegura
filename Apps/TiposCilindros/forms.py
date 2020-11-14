from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory
from .models import *
from .custom_layout_object import *

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

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-9 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('vidaUtil'),
                Field('estado'),
                HTML("<br>"),
                Fieldset('Agregar análisis',
                    Formset('analisis')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Registrar')),
                )
            )

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
            self._errors['nombre'] = ["El tipo de cilindro ya existe"]
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

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-9 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('vidaUtil'),
                Field('estado'),
                HTML("<br>"),
                Fieldset('Agregar análisis',
                    Formset('analisis')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Actualizar')),
                )
            )

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
            tipoCilindro = TiposCilindros.objects.exclude(nombre=self.instance)
            tipoCilindro = tipoCilindro.get(nombre=form_data['nombre'])
            self._errors['nombre'] = ["El tipo de cilindro ya existe"]
        except TiposCilindros.DoesNotExist:
            pass


#########################################################3
class FormTiposCilindros_Analisis (forms.ModelForm):
    class Meta:
        model = TiposCilindros_Analisis
        fields = [
            'analisis',
            'min_aceptado',
            'max_aceptado',
            'auto_calculado'
        ]

    def __init__ (self, *args, **kwargs):
        super(FormTiposCilindros_Analisis, self).__init__(*args, **kwargs)
        self.fields['analisis'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['min_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['max_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['auto_calculado'].widget.attrs = {
            'class': 'form-control'
        }

        def clean(self):
            form_data = super(FormTiposCilindros_Analisis, self).clean()

            try:
                cilindro_analisis = TiposCilindros_Analisis.objects.get(
                    analisis = form_data['analisis'],
                    tipoCilindro = form_data['tipoCilindro']
                )
                self._errors['analisis'] = ["Este análisis ya fue asignado"]
            except TiposCilindros_Analisis.DoesNotExist:
                pass

            if form_data['min_aceptado'] > form_data['max_aceptado']:
                self._errors['min_aceptado'] = ["Este valor debe ser inferior al Valor máximo aceptado"]
                self._errors['max_aceptado'] = ["Este valor debe ser superior al Valor mínimo aceptado"]

FormSet_TiposCilindros_Analisis = inlineformset_factory(
    TiposCilindros,
    TiposCilindros_Analisis,
    form = FormTiposCilindros_Analisis,
    fields = [
        'analisis',
        'min_aceptado',
        'max_aceptado',
        'auto_calculado'
    ],
    extra = 1,
    can_delete = True
)

class FormEditarTiposCilindros_Analisis (forms.ModelForm):
    class Meta:
        model = TiposCilindros_Analisis
        fields = [
            'analisis',
            'min_aceptado',
            'max_aceptado',
            'auto_calculado'
        ]

    def __init__ (self, *args, **kwargs):
        super(FormEditarTiposCilindros_Analisis, self).__init__(*args, **kwargs)
        self.fields['analisis'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['min_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['max_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['auto_calculado'].widget.attrs = {
            'class': 'form-control'
        }

        def clean(self):
            form_data = super(FormEditarTiposCilindros_Analisis, self).clean()

            try:
                cilindro_analisis = TiposCilindros_Analisis.objects.exclude(
                    id = self.instance.id
                )

                cilindro_analisis = cilindro_analisis.objects.get(
                    analisis = form_data['analisis'],
                    tipoCilindro = form_data['tipoCilindro']
                )

                self._errors['analisis'] = ["Este análisis ya fue asignado"]

            except TiposCilindros_Analisis.DoesNotExist:
                pass

            if form_data['min_aceptado'] > form_data['max_aceptado']:
                self._errors['min_aceptado'] = ["Este valor debe ser inferior al Valor máximo aceptado"]
                self._errors['max_aceptado'] = ["Este valor debe ser superior al Valor mínimo aceptado"]


FormSet_Editar_TiposCilindros_Analisis = inlineformset_factory(
    TiposCilindros,
    TiposCilindros_Analisis,
    form = FormEditarTiposCilindros_Analisis,
    fields = [
        'analisis',
        'min_aceptado',
        'max_aceptado',
        'auto_calculado'
    ],
    extra = 1,
    can_delete = True
)
