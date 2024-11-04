from django.urls import path
from . import views

app_name = 'apps.gestion_ventas'
urlpatterns = [
    path('ventas', views.registrar_ventas, name='ventas'),
    path('mayoristas', views.registrar_cliente_mayorista, name='mayoristas')
]
