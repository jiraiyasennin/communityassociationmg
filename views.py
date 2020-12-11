from django.shortcuts import render
from django.shortcuts import redirect
from . models import socio
from .forms import FormularioRegistroSocio
from django.views.generic import ListView, CreateView
from django.contrib import messages

class sociosListView(ListView):
    model = socio
    template_name = 'communitymgr/socio_list.html'
    context_object_name = 'socios'
    pass
    

def RegistroDeSocios(request):
    if request.method == 'POST':
        form = FormularioRegistroSocio(request.POST)
        if form.is_valid():
            messages.success(request, f'The user has been created!')
            return redirect('registro-socio')
    else:
        form = FormularioRegistroSocio()
    return render(request, 'communitymgr/socio_create.html', {'form': form})
    