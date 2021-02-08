from django.forms import ModelForm
from webcode.portfolio.communitymgr.models import socio
from django import forms


class FormularioRegistroSocio(ModelForm):
    #Sobre escribimos el atributo fecha_de_nacimiento para agregar
    # el widget que añade el placeholder con el ejemplo de la fecha
    fecha_de_nacimiento = forms.DateField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ejemplo: 14/05/1968", 'type': 'date'}),
    )
    fecha_de_alta = forms.DateField(error_messages={'required': "Dato Requerido",},
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
        
        
        
