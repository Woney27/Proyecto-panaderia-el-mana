from django.urls import path
from . import views

app_name = 'apps.gestion_empleados'
urlpatterns = [
    path('formulario/', views.formulario, name='formulario'),
    path('modificar/<int:empleado_id>', views.modificar_empleado, name='modificar_empleado'),
    path('eliminar/<int:empleado_id>', views.eliminar_empleado, name='eliminar_empleado'),
]
