from django.db import models
import math
from datetime import date


class socio(models.Model):
    numero_de_socio = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    codigo_postal = models.IntegerField()
    localidad = models.CharField(max_length=20)
    telefono_fijo = models.IntegerField(null = True)
    telefono_movil = models.IntegerField()
    fecha_de_alta = models.DateField(default=date.today, blank=True)
    fecha_de_pago = models.DateField(default=date.today, blank=True)
    fecha_defuncion = models.DateField(default=date.today, blank=True)
    #Constantes del pago actual
    #PAGADO = 'PAGADO'
    #NOPAGADO = 'NO PAGADO'
    #estado_pago_actual = [(PAGADO, 'Pagado'),(NOPAGADO,'No pagado')]
    #pago_año_actual = models.CharField(max_length=10, choices=estado_pago_actual, default=NOPAGADO)

    #Constantes del estatus#
    ALTA = 'AL'
    BAJA = 'BA'
    estados_de_estatus = [(ALTA,'Alta'),(BAJA,'Baja')]
    estatus = models.CharField(max_length=2, choices=estados_de_estatus, default=ALTA)
    años_pagados = models.CharField(max_length=300, null = True)
    
    #Cálculo de la edad
    @property
    def edad(self):
       return  int((date.today() - self.fecha_de_nacimiento).days / 365)
