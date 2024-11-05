from django.shortcuts import render


def registrar_insumos(request):
    return render(request, 'gestion_insumos/pedidos_proveedores.html')


def pedir_insumos(request):
    return render(request, 'gestion_insumos/pedir_insumos.html')
