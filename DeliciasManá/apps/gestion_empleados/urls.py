from django.urls import path
from . import views

app_name = 'apps.gestion_empleados'
urlpatterns = [
    path('formulario/', views.formulario, name='formulario')
]