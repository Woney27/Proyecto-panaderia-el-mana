from django.shortcuts import render

def pedir_insumos(request):
    return render(request, 'gestion_insumos/pedidos_proveedores.html')
