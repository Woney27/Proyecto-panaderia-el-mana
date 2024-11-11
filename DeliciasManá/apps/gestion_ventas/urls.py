from django.urls import path
from . import views

app_name = 'apps.gestion_ventas'
urlpatterns = [
    path('ventas', views.registrar_ventas, name='ventas'),
    path('mayoristas', views.registrar_cliente_mayorista, name='mayoristas'),
    path('modificar_cliente/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
]