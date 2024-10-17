from django.shortcuts import render


def registrar_productos(request):
    return render(request, 'gestion_productos/registro_productos.html')
