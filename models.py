from django.db import models
import math
from datetime import date


class socio(models.Model):
    numero_de_socio = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    codigo_postal = models.IntegerField()
    localidad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=40, null = True)
    fecha_de_alta = models.DateField(null=True)
    fecha_de_pago = models.DateField(null=True)
    fecha_defuncion = models.DateField(null=True)
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
    
    def __str__(self):
        return f"Socio {self.numero_de_socio} | {self.nombre} {self.apellidos}"


    #Cálculo de la edad
    @property
    def edad(self):
       return  int((date.today() - self.fecha_de_nacimiento).days / 365)



#Modelo que genera los campos del archivo cargado
class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"