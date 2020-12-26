from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ESTADOS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))

class Permisos (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )

    def __str__(self):
        return self.nombre

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
    permisos = models.ManyToManyField(
        Permisos,
        verbose_name='Permisos'
    )

    class Meta:
        verbose_name = "Roles"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre


class Usuario (User):
    IDENTIFICACION_CHOICES = (('CC','CC'),('TI','TI'),('CE','CE'))
    tipo_documento = models.CharField(
        max_length=2,
        verbose_name="Tipo de documento",
        choices = IDENTIFICACION_CHOICES
    )
    numero_documento = models.CharField(
        max_length=20,
        verbose_name="Número de documento",
        unique=True
    )
    telefono = models.CharField(
        max_length=20,
        verbose_name="Número telefónico"
    )
    segundo_nombre = models.CharField(
        max_length=100,
        verbose_name="Segundo nombre",
        blank=True
    )
    segundo_apellido = models.CharField(
        max_length=100,
        verbose_name="Segundo apellido",
        blank=True
    )
    rol = models.ForeignKey(
        Roles,
        limit_choices_to={'estado': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name="Rol"
    )

    def __str__(self):
        return '%s %s %s %s' % (self.first_name , self.segundo_nombre , self.last_name , self.segundo_apellido)
