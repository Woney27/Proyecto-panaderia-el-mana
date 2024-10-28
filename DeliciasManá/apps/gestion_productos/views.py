from django.shortcuts import render
from apps.gestion_productos.models import Producto

def registrar_productos(request):
    return render(request, 'gestion_productos/registro_productos.html')


def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion_productos/registro_productos.html', {'productos':productos})
