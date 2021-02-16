from django.forms import ModelForm
from webcode.portfolio.communitymgr.models import socio
from django import forms
from .models import Csv
from django.utils.translation import ugettext_lazy as _

#clase que genera el formulario de datos de usuario
#Sobre escribimos los atributos de los campos para agregar
#el widget que añade el placeholder con información
class FormularioRegistroSocio(ModelForm):
    fecha_de_nacimiento = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ejemplo: 14/05/1968", 'type': 'date'}),
    )
    fecha_de_alta = forms.DateField(required=False, error_messages={'required': "Dato Requerido",},
        widget=forms.TextInput(attrs={"placeholder": "Ejemplo: 20/02/2021", 'type': 'date'}),
    )
    fecha_de_pago = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Ejemplo: 20/02/2021", 'type': 'date'}),
    )
    fecha_defuncion = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Ejemplo: 08/10/2015", 'type': 'date'}),
    )
    años_pagados = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Agregar años pagados",}),
    )
    telefono_fijo = forms.IntegerField(required=False)
    class Meta:
        model = socio
        fields = '__all__'
        
        
# Clase que genera el formulario de subida del archivo
# Agrega una etiqueta custom
class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)
        labels = {
            'file_name': _('Seleccione Archivo'),
        }     
