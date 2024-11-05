from django.urls import path
from . import views

app_name = 'apps.gestion_productos'
urlpatterns = [
    path('registrar', views.registrar_productos, name='registrar_productos'),
    path('modificar/<int:producto_id>', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
]