from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmpleadoForm


def formulario(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulario guardado exitosamente.")
            return redirect('base/base.html')
        else:
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        form = EmpleadoForm()
    return render(request, 'gestion_empleados/gestion_empleados.html', {'form': form})
