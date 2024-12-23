from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProveedorForm
from django.urls import reverse
from .models import Proveedor


def registrar_proveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            nuevo_proveedor = proveedor_form.save(commit=False)
            nuevo_proveedor.save()
            messages.success(request, 'Se ha registrado correctamente el proveedor.')
            return redirect(reverse('gestion_proveedores:proveedores'))
        else:
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        proveedor_form = ProveedorForm()
    
    proveedores = Proveedor.objects.all()
    return render(request, 'gestion_proveedores/registro_proveedores.html', {'form': proveedor_form, 'proveedores': proveedores})

def modificar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)  # Obtener el proveedor por ID
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST, instance=proveedor)  # Pasar la instancia al formulario
        if proveedor_form.is_valid():
            proveedor_form.save()  # Guardar el proveedor modificado
            messages.success(request, 'Proveedor modificado exitosamente.')
            return redirect('gestion_proveedores:proveedores')  # Redirigir después de guardar, hacia la vista de proveedores
    else:
        proveedor_form = ProveedorForm(instance=proveedor)  # Crear el formulario con la instancia existente
    proveedores = Proveedor.objects.all()
    return render(request, 'gestion_proveedores/registro_proveedores.html', {'form': proveedor_form, 'proveedor': proveedor, 'proveedores': proveedores})

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)  # Obtener el proveedor por ID

    if request.method == 'POST':
        proveedor.delete()  # Eliminar 
        messages.success(request, 'Proveedor eliminado exitosamente.')
        return redirect('gestion_proveedores:proveedores')  # Redirigir después de eliminar, hacia la vista de proveedores

    return render(request, 'gestion_proveedores/registro_proveedores.html', {'proveedor': proveedor})

