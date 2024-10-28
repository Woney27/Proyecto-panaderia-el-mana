from django.urls import path
from . import views

app_name = 'apps.gestion_ventas'
urlpatterns = [
    path('', views.registrar_ventas, name= 'ventas')
]
