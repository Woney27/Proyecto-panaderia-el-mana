from django.urls import path
from . import views

app_name = 'gestion_proveedores'

urlpatterns = [
    path('', views.registrar_proveedor, name='proveedores'),  # Página principal para listar y registrar proveedores
    path('modificar/<int:proveedor_id>/', views.modificar_proveedor, name='modificar_proveedor'),  # Modificar proveedor
    path('eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),  # Eliminar proveedor
]
