from django.urls import path
from . import views

app_name = 'apps.gestion_empleados'
urlpatterns = [
    path('', views.registrarEmpleado)
]