from django.shortcuts import render
from django.shortcuts import redirect
from . models import socio
from .forms import FormularioRegistroSocio
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
class ModificarSocio(LoginRequiredMixin, UpdateView):
   model = socio
   form_class = FormularioRegistroSocio
   template_name = 'communitymgr/actualizasocio_form.html'
   success_url = '/apps/aavvmaresme/listasocios/'
    