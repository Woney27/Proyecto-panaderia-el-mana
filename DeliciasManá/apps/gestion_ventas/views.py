from django.shortcuts import render


def registrar_ventas(request):
    return render(request, 'gestion_ventas/gestion_ventas.html')

