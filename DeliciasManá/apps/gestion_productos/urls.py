from django.urls import path
from . import views

app_name = 'apps.gestion_productos'
urlpatterns = [
    path('', views.registrar_productos)
]

