from django.urls import reverse 
from django.shortcuts import render, redirect
from django.http import HttpResponse
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
    productos = Producto.objects.all()
    return render(request, 'gestion_productos/registro_productos.html', {'form': producto_form, 'productos': productos})

    return HttpResponse("Error: Solicitud no procesada correctamente.")