from django.urls import path
from . import views

app_name = 'apps.gestion_insumos'
urlpatterns = [
    path('', views.pedir_insumos)
]

