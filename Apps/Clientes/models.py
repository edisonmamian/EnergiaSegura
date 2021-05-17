from django.db import models
from Apps.TiposCilindros.models import TiposCilindros

# Create your models here.
ESTADOS = (('Activo', 'Activo'),('Inactivo', 'Inactivo'))
TIPOS_IDENTIFICACION = (('NIT', 'NIT'), ('CC', 'CC'))

#Modelo para los departamentos de Colombia
class Departamentos (models.Model):
    #Almacena el nombre del departamento
    nombre = models.CharField(
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Departamento'
    )
    #Almacena el código de identificación del departamento
    codigo_dane = models.CharField(
        max_length = 2,
        null = False,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre

#modelo para las ciudades de Colombia
class Ciudades (models.Model):
    #Almacena el nombre de la ciudad
    nombre = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Ciudad'
    )
    #Almacena el departamento en el que está ubicado
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    #Almacena el código de identificación de la ciudad
    codigo_dane = models.CharField (
        max_length = 5,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre

#modelo para la clasificación de los clientes
class ClasificacionClientes (models.Model):
    #almacena el nombre de la clasificación
    nombre = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Nombre'
    )
    #almacena los tipos de cilindros que debería tener el cliente con esta clasificación
    tipos_cilindros = models.ManyToManyField(
        TiposCilindros,
        verbose_name='Tipos de cilindros',
        limit_choices_to={'estado': 'Activo'},
        symmetrical=False,
        blank=True
    )
    estado = models.CharField(
        max_length=8,
        null=False,
        choices=ESTADOS,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre

# modelo para los clientes de Energia Segura
class Clientes (models.Model):
    # almacena el nombre
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
    # el tipo de identifiación del cliente
    tipo_identifcacion = models.CharField(
        max_length = 5,
        null=False,
        choices= TIPOS_IDENTIFICACION,
        verbose_name = 'Tipo de identificación'
    )
    # el número de identificación del cliente
    numero_identificacion = models.CharField(
        max_length = 10,
        null = False,
        verbose_name = 'Número de identificación'
    )
    # la clasificacion del cliente
    clasificacion = models.ManyToManyField(
        ClasificacionClientes,
        verbose_name = 'Clasificación del cliente',
        limit_choices_to = {'estado': 'Activo'}
    )
    # departamento de Colombia dónde está ubicado
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    # ciudad de Colombia dónde está ubicado
    ciudad = models.ForeignKey(
        Ciudades,
        on_delete=models.CASCADE,
        verbose_name='Ciudad'
    )
    # dirección dónde está ublicado
    direccion = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Dirección'
    )
    # el nombre del responsable técnico
    responsable_tecnico = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable técnico',
        null = True,
        blank = True,
    )
    # el teléfono del responsable técnico
    telefono_tecnico = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular del responsable técnico',
        null = True,
        blank = True
    )
    # el email del responsable técnico
    email_tecnico = models.EmailField(
        verbose_name = 'Email del responsable técnico',
        null = True,
        blank = True
    )
    # el nombre del responsable comercial
    responsable_comercial = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable comercial',
        null = True,
        blank = True,
    )
    # el teléfono del responsable comercial
    telefono_comercial = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular comercial',
        null = True,
        blank = True
    )
    # el email del responsable comercial
    email_comercial = models.EmailField(
        verbose_name = 'Email comercial',
        null = True,
        blank = True
    )
    # el nombre del responsable de contabilidad
    responsable_contabilidad = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable de contabilidad',
        null = True,
        blank = True,
    )
    # el telefono del responsable de contabilidad
    telefono_contabilidad = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular de contabilidad',
        null = True,
        blank = True
    )
    # el email del responsable de contabilidad
    email_contabilidad = models.EmailField(
        verbose_name = 'Email de contabilidad',
        null = True,
        blank = True
    )
    # el nombre del responsable administrativo
    responsable_administrativo = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable administrativo',
        null = True,
        blank = True,
    )
    # el telefono del responsable administrativo
    telefono_administrativo = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular administrativo',
        null = True,
        blank = True
    )
    # el email del responsable administrativo
    email_administrativo = models.EmailField(
        verbose_name = 'Email administrativo',
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nombre

# Modelo de sedes de los clientes
class SedeCliente (models.Model):
    # nombre de la sede
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
    # departamento en la que está ubicada la sede
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    # ciudad en la que está ubicada la sede
    ciudad = models.ForeignKey(
        Ciudades,
        on_delete=models.CASCADE,
        verbose_name='Ciudad'
    )
    # dirección de la sede
    direccion = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Dirección'
    )
    # cliente al que pertenece la sede
    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )

    def __str__(self):
        return self.nombre