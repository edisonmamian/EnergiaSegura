from django.db import models

# Create your models here.
ESTADOS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))
class Roles (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )
    estado = models.CharField(
        max_length=8,
        null=False,
        choices=ESTADOS,
        verbose_name='Estado'
    )

    class Meta:
        verbose_name = "Roles"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre
