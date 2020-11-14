from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Apps.AnalisisLaboratorio.models import Analisis

# Create your models here.
ESTADOS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))
class TiposCilindros (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )
    vidaUtil = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        validators=[MinValueValidator(0.0)],
        verbose_name='Vida útil en años',
        null=False
    )
    estado = models.CharField(
        max_length=8,
        null=False,
        choices=ESTADOS,
        verbose_name='Estado'
    )

    class Meta:
        verbose_name = "Tipos de cilindros"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre

class TiposCilindros_Analisis (models.Model):
    tipoCilindro = models.ForeignKey(
        TiposCilindros,
        limit_choices_to = {'estado': 'Activo'},
        on_delete = models.CASCADE,
        verbose_name = 'Tipo de cilindro'
    )
    analisis = models.ForeignKey(
        Analisis,
        limit_choices_to = {'estado': 'Activo'},
        on_delete = models.CASCADE,
        verbose_name = 'Análisis de laboratorio'
    )
    min_aceptado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor mínimo aceptado',
        null=False
    )
    max_aceptado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor máximo aceptado',
        null=False
    )
    auto_calculado = models.BooleanField(
        verbose_name="¿Es obligatorio?",
        default = False,
    )

    class Meta:
        unique_together = [['tipoCilindro', 'analisis']]
