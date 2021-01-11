from django.db import models
from Apps.Usuarios.models import Usuario
from Apps.Clientes.models import Clientes
from Apps.TiposCilindros.models import TiposCilindros, TiposCilindros_Analisis

# Create your models here.
class Recepcion (models.Model):
    fecha = models.DateField(
        null = False,
        blank = False,
        verbose_name = 'Fecha de recepción'
    )
    colaborador = models.ForeignKey(
        Usuario,
        limit_choices_to={'estado': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name = 'Colaborador que recibe'
    )
    cliente = models.ForeignKey(
        Clientes,
        limit_choices_to={'estado': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name = 'Cliente'
    )

class Cilindro (models.Model):
    fabricante = models.CharField(
        max_length=100,
        verbose_name="Fabricante",
    )
    serial = models.CharField(
        max_length=100,
        verbose_name="Serial",
    )
    capacidad = models.CharField(
        max_length=100,
        verbose_name="Capacidad",
    )
    ultima_prueba = models.DateField(
        null = True,
        blank = True,
        verbose_name = 'Fecha de última prueba'
    )
    accesorios = models.CharField(
        max_length=100,
        verbose_name="Accesorios",
    )
    valvula = models.CharField(
        max_length=100,
        verbose_name="Válvula",
    )
    tipo_cilindro = models.ForeignKey(
        TiposCilindros,
        limit_choices_to={'estado': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name = 'Tipo de cilindro'
    )
    analisis = models.ForeignKey (
        TiposCilindros_Analisis,
        limit_choices_to={'estado': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name = 'Análisis a realizar'
    )
