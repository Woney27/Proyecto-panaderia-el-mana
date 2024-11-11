from django.urls import path
from . import views

app_name = 'gestion_proveedores'  # Es importante tener esta línea

urlpatterns = [
    path('', views.registrar_proveedor, name='proveedores'),
    path('modificar/<int:proveedor_id>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]