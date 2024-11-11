from django.contrib import messages
from django.shortcuts import render, redirect ,get_object_or_404
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
            # Mostrar los errores del formulario
            for field, errors in empleado_form.errors.items():
                for error in errors:
                    print(f"Error en el campo {field}: {error}")
    else:
        empleado_form = EmpleadoForm()
        
    empleados = Empleado.objects.all()
    return render(request, 'gestion_empleados/gestion_empleados.html', {'form': empleado_form, 'empleados': empleados})


def modificar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)  # Obtener el empleado por ID
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST, instance=empleado)  # Pasar la instancia al formulario
        if empleado_form.is_valid():
            empleado_form.save()  # Guardar el empleado modificado
            return redirect('apps.gestion_empleados:formulario')  # Redirigir después de guardar
    else:
        empleado_form = EmpleadoForm(instance=empleado)  # Crear el formulario con la instancia existente
    empleados = Empleado.objects.all().order_by('id')
    return render(request, 'gestion_empleados/gestion_empleados.html', {'form': empleado_form, 'empleados': empleados})


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)  # Obtener el empleado por ID

    if request.method == 'POST':
        empleado.delete()  # Eliminar el empleado
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('apps.gestion_empleados:formulario')  # Redirigir después de eliminar

    empleados = Empleado.objects.all().order_by('id')
    return render(request, 'gestion_empleados/gestion_empleados.html', {'empleados': empleados})