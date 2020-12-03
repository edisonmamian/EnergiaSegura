from django.db import models

# Create your models here.
ESTADOS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))
TIPOS_IDENTIFICACION = (('NIT', 'NIT'), ('CC', 'CC'))


class Departamentos (models.Model):
    nombre = models.CharField(
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Departamento'
    )
    codigo_dane = models.CharField(
        max_length = 2,
        null = False,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre


class Ciudades (models.Model):
    nombre = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Ciudad'
    )
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    codigo_dane = models.CharField (
        max_length = 5,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre


class Clientes (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Nombre o razón social'
    )
    estado = models.CharField(
        max_length=8,
        null=False,
        choices=ESTADOS,
        verbose_name='Estado'
    )
    tipo_identifcacion = models.CharField(
        max_length = 5,
        null=False,
        choices= TIPOS_IDENTIFICACION,
        verbose_name = 'Tipo de identificación'
    )
    numero_identificacion = models.CharField(
        max_length = 10,
        null = False,
        verbose_name = 'Número de identificación'
    )
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    ciudad = models.ForeignKey(
        Ciudades,
        on_delete=models.CASCADE,
        verbose_name='Ciudad'
    )
    direccion = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Dirección'
    )
    telefono_tecnico = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular del responsable técnico',
        null = True,
        blank = True
    )
    email_tecnico = models.EmailField(
        verbose_name = 'Email del responsable técnico',
        null = True,
        blank = True
    )
    telefono_comercial = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular comercial',
        null = True,
        blank = True
    )
    email_comercial = models.EmailField(
        verbose_name = 'Email comercial',
        null = True,
        blank = True
    )
    telefono_contabilidad = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular de contabilidad',
        null = True,
        blank = True
    )
    email_contabilidad = models.EmailField(
        verbose_name = 'Email de contabilidad',
        null = True,
        blank = True
    )
    telefono_administrativo = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular administrativo',
        null = True,
        blank = True
    )
    email_administrativo = models.EmailField(
        verbose_name = 'Email administrativo',
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nombre
