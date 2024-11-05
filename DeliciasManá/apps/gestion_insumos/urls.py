from django.urls import path
from . import views

app_name = 'apps.gestion_insumos'
urlpatterns = [
    path('', views.registrar_insumos),
    path('/pedir_insumos', views.pedir_insumos)
]