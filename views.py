from django.shortcuts import render
from django.shortcuts import redirect
from .models import socio
from .forms import FormularioRegistroSocio
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#Dependencias de subida de archivos
from .forms import CsvModelForm
from .models import Csv
import csv, datetime
#Dependencias cambio de password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



#Clase que genera el listado de socios
class SociosListView(LoginRequiredMixin, ListView):
    model = socio
    template_name = 'communitymgr/socio_list.html'
    context_object_name = 'socios'
    ordering = ['numero_de_socio']

#Clase que genera el listado de socios
class SociosPrintView(LoginRequiredMixin, ListView):
    model = socio
    template_name = 'communitymgr/socio_print.html'
    context_object_name = 'socios'
    ordering = ['numero_de_socio']


#Clase que muestra el detalle de cada socio
class DetalleSocio(LoginRequiredMixin, DetailView):
    model = socio


#Clase que genera el formulario de registro de los socios
@login_required
def RegistroDeSocios(request):
    if request.method == 'POST':
        form = FormularioRegistroSocio(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'El usuario ha sido creado correctamente')
            return redirect('crear-socio')
    else:
        form = FormularioRegistroSocio()
    return render(request, 'communitymgr/socio_create.html', {'form': form})

#Clase que genera el formulario para modificar los datos del socio
class ModificarSocio(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
   model = socio
   form_class = FormularioRegistroSocio
   template_name = 'communitymgr/actualizasocio_form.html'
   success_url = '/apps/aavvmaresme/'
   success_message = 'El socio ha sido modificado correctamente'

#Clase que borra el usuario elegido
class BorrarSocio(LoginRequiredMixin, DeleteView):
    model = socio
    template_name = 'communitymgr/socio_delete.html'
    success_url = '/apps/aavvmaresme/'
    success_message = 'El socio ha sido borrado correctamente'
    
    # Función que muestra el mensaje al borrar el socio
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BorrarSocio, self).delete(request, *args, **kwargs)

#Clase que lee el archivo CSV y guarda los datos en el bd
@login_required
def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    años = ""
                   
                    if row[10] != "":
                         años = row[10]
                    else:
                       pass
                    if row[10] or row[11] != "":
                        años += '  '+row[11]
                    else:
                        pass
                    if row[11] or row[12] != "":
                        años +='  '+row[12]
                    else:
                        pass
                    if row[12] or row[13] != "":
                        años += '  '+row[13]
                    else:
                        pass
                    if row[13] or row[14] != "":
                        años += '  '+row[14]
                    else:
                        pass
                    if row[14] or row[15] != "":
                        años +='  '+row[15]
                    else:
                        pass
                    #Verificar y corregir el campo estatus
                    if row[16].upper() == "ALTA":
                        estatus = "AL"
                    else:
                        estatus = "BA" 
                    
                    socio.objects.create(
                        numero_de_socio = row[0],
                        nombre = row[2].capitalize(),
                        apellidos = row[1].title(),
                        dni = row[3],
                        email = row[9],
                        #Se cambia el formato de la fecha
                        fecha_de_nacimiento = datetime.datetime.strptime(row[4], "%d/%m/%Y").strftime("%Y-%m-%d"),
                        direccion = row[5].title(),
                        codigo_postal = row[6],
                        localidad = row[7],
                        telefono = row[8],
                        estatus = estatus,
                        años_pagados = años,
                    )
                    obj.activated=True
                    obj.save()
    return render(request, 'communitymgr/upload.html', {'form': form})

@login_required
def cambio_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #important!!
            messages.success(request, 'El password ha sido cambiado correctamente')
            return redirect('cambio-password')
        else:
            messages.error(request, 'Por favor corregir el error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form':form})
