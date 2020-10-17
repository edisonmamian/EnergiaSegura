from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
