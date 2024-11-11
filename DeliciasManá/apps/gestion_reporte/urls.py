from django.urls import path
from . import views

app_name='apps.gestion_reporte'

urlpatterns = [
    path('', views.reporte, name='reporte'),
]
