"""guiadevopsapp URL Configuration"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio/', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('', views.inicio, name='inicio'),
    path('indexdash/', views.iniciodash, name='indexdash'),
    path('actividades/', views.actividades, name='actividades'),
    path('planificaciontareas/', views.planificaciontareas, name='planificaciontareas'),
    path('planificacionherramientas/', views.planificacionherramientas, name='planificacionherramientas'),
    path('planificacionpracticas/', views.planificacionpracticas, name='planificacionpracticas'),
    path('perfilusuario/', views.perfilusuario, name='perfilusuario'),
    path('codificaciontareas/', views.codificaciontareas, name='codificaciontareas'),
    path('codificacionherramientas/', views.codificacionherramientas, name='codificacionherramientas'),
    path('codificacionpracticas/', views.codificacionpracticas, name='codificacionpracticas'),
    path('construcciontareas/', views.construcciontareas, name='construcciontareas'),
    path('construccionherramientas/', views.construccionherramientas, name='construccionherramientas'),
    path('construccionpracticas/', views.construccionpracticas, name='construccionpracticas'),
    path('pruebastareas/', views.pruebastareas, name='pruebastareas'),
    path('pruebasherramientas/', views.pruebasherramientas, name='pruebasherramientas'),
    path('pruebaspracticas/', views.pruebaspracticas, name='pruebaspracticas'),
    path('liberaciontareas/', views.liberaciontareas, name='liberaciontareas'),
    path('liberacionherramientas/', views.liberacionherramientas, name='liberacionherramientas'),
    path('liberacionpracticas/', views.liberacionpracticas, name='liberacionpracticas'),
    path('desplieguetareas/', views.desplieguetareas, name='desplieguetareas'),
    path('despliegueherramientas/', views.despliegueherramientas, name='despliegueherramientas'),
    path('desplieguepracticas/', views.desplieguepracticas, name='desplieguepracticas'),
    path('operacionestareas/', views.operacionestareas, name='operacionestareas'),
    path('operacionesherramientas/', views.operacionesherramientas, name='operacionesherramientas'),
    path('operacionespracticas/', views.operacionespracticas, name='operacionespracticas'),
    path('monitoreotareas/', views.monitoreotareas, name='monitoreotareas'),
    path('monitoreoherramientas/', views.monitoreoherramientas, name='monitoreoherramientas'),
    path('monitoreopracticas/', views.monitoreopracticas, name='monitoreopracticas'),
    path('referencias/', views.referencias, name='referencias'),
]
