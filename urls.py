from django.urls import path
from . import views
from .views import (
    SociosListView,
    RegistroDeSocios,
    ModificarSocio,
    DetalleSocio
)
from webcode.portfolio.communitymgr.views import SociosListView


urlpatterns = [
    path('login/', views.loginUsuario, name='login-admin'),
    path('registrosocio/', views.RegistroDeSocios, name='crear-socio'),
    path('listasocios/', SociosListView.as_view(), name='lista-socios'),
    path('socio/<int:pk>/update', ModificarSocio.as_view(), name='actualiza-socio'),
    path('socio/<int:pk>/detalles', DetalleSocio.as_view(), name='detalle-socio'),
]