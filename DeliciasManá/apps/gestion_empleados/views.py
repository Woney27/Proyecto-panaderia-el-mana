from django.shortcuts import render


def registrarEmpleado(request):
    return render(request,'gestion_empleados/gestion_empleados.html')
