from django.urls import path
from . import views

app_name = 'apps.gestion_insumos'
urlpatterns = [
    path('pedir_insumos', views.FormularioPedir, name='pedir_insumos'),
    path('registrar_insumos', views.FormularioInsumo, name= 'registrar_insumos'),
    path('modificar_insumo/<int:insumo_id>', views.modificar_insumo, name='modificar_insumo'),
    path('eliminar_insumo/<int:insumo_id>', views.eliminar_insumo, name='eliminar_insumo'),
    path('modificar_pedido/<int:pedido_id>', views.modificar_pedido, name='modificar_pedido'),
    path('eliminar_pedido/<int:pedido_id>', views.eliminar_pedido, name='eliminar_pedido')

]