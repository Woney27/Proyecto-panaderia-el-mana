from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from django.http import HttpResponse
from django.urls import reverse
from apps.gestion_empleados.models import Empleado


def formulario(request):
    nuevo_empleado = None
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            nuevo_empleado = empleado_form.save(commit=False)
            nuevo_empleado.save()
            messages.success(request, "Formulario guardado exitosamente.")
            return redirect(reverse('apps.gestion_empleados:formulario'))
        else:
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        empleado_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, 'gestion_empleados/gestion_empleados.html', {'form': empleado_form, 'empleados': empleados})

    return HttpResponse("Error: Solicitud no procesada correctamente.")