from django.urls import reverse 
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.contrib import messages
from .forms import ProductoForm
from apps.gestion_productos.models import Producto




def registrar_productos(request):
    nuevo_producto = None
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            nuevo_producto = producto_form.save(commit=False)
            nuevo_producto.save()
            messages.success(request, 'Se ha agregado correctamente el producto')
            return redirect(reverse('apps.gestion_productos:registrar_productos'))
    else:
        producto_form = ProductoForm()
    productos = Producto.objects.all().order_by('id')
    return render(request, 'gestion_productos/registro_productos.html', {'form': producto_form, 'productos': productos})


def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  # Obtener el producto por ID
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)  # Pasar la instancia al formulario
        if producto_form.is_valid():
            producto_form.save()  # Guardar el producto modificado
            return redirect('apps.gestion_productos:registrar_productos')  # Redirigir después de guardar
    else:
        producto_form = ProductoForm(instance=producto)  # Crear el formulario con la instancia existente
    productos = Producto.objects.all().order_by('id')
    return render(request, 'gestion_productos/registro_productos.html', {'form': producto_form, 'productos': productos})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)  # Obtener el producto por ID

    if request.method == 'POST':
        producto.delete()  # Eliminar el producto
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('apps.gestion_productos:registrar_productos')  # Redirigir después de eliminar

    productos = Producto.objects.all().order_by('id')
    return render(request, 'gestion_productos/registro_productos.html', {'productos': productos})

