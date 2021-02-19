from django.urls import path, include
from . import views
from webcode.portfolio.communitymgr.views import (
    SociosListView,
    SociosPrintView,
    RegistroDeSocios,
    ModificarSocio,
    DetalleSocio,
    upload_file_view
)

urlpatterns = [
    path('', SociosListView.as_view(), name='lista-socios'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('change_password/', views.cambio_password, name='cambio-password'),
    path('registrosocio/', views.RegistroDeSocios, name='crear-socio'),
    path('imprimirsocios/', SociosPrintView.as_view(), name='imprimir-socios'),
    path('socio/<int:pk>/update', ModificarSocio.as_view(), name='actualiza-socio'),
    path('socio/<int:pk>/detalles', DetalleSocio.as_view(), name='detalle-socio'),
    path('upload_file/', views.upload_file_view, name='subir-csv'),    
]