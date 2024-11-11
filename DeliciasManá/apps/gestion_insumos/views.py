from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import InsumoForm, PedidoForm
from apps.gestion_insumos.models import Insumo, Pedido_Proveedor, InsumoPedido
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from datetime import datetime
from django.http import JsonResponse

def FormularioInsumo(request):
    nuevo_insumo = None
    if request.method == 'POST':
        insumo_form = InsumoForm(request.POST)
        if insumo_form.is_valid():
            nuevo_insumo = insumo_form.save(commit=False)
            nuevo_insumo.save()
            messages.success(request, "Formulario guardado exitosamente.")
            return redirect(reverse('apps.gestion_insumos:registrar_insumos'))
        else:
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        insumo_form = InsumoForm()
    insumos = Insumo.objects.all()
    return render(request, 'gestion_insumos/registrar_insumos.html', {'form': insumo_form, 'insumos': insumos})
    
def modificar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)  # Obtener el producto por ID
    if request.method == 'POST':
        insumo_form = InsumoForm(request.POST, instance=insumo)  # Pasar la instancia al formulario
        if insumo_form.is_valid():
            insumo_form.save()  # Guardar el producto modificado
            return redirect('apps.gestion_insumos:registrar_insumos')  # Redirigir después de guardar
    else:
        insumo_form = InsumoForm(instance=insumo)  # Crear el formulario con la instancia existente
    insumos = Insumo.objects.all().order_by('id')
    return render(request, 'gestion_insumos/registrar_insumos.html', {'form': insumo_form, 'Insumos': insumos})


def eliminar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)  # Obtener el producto por ID

    if request.method == 'POST':
        insumo.delete()  # Eliminar el producto
        messages.success(request, 'Insumo eliminado exitosamente.')
        return redirect('apps.gestion_insumos:registrar_insumos')  # Redirigir después de eliminar

    insumos = Insumo.objects.all().order_by('id')
    return render(request, 'gestion_insumos/registar_insumos.html', {'Insumos': insumos})



def FormularioPedir(request):
    nuevo_pedido = None
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        if pedido_form.is_valid():
            nuevo_pedido = pedido_form.save(commit=False)
            nuevo_pedido.save()
            messages.success(request, "Formulario guardado exitosamente.")
            return redirect(reverse('apps.gestion_insumos:pedir_insumos'))
        else:
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        pedido_form = PedidoForm()
    pedidos = Pedido_Proveedor.objects.all()
    return render(request, 'gestion_insumos/pedidos_proveedores.html', {'form': pedido_form, 'Pedidos': pedidos})



def modificar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido_Proveedor, id=pedido_id)  # Obtener el producto por ID
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST, instance=pedido)  # Pasar la instancia al formulario
        if pedido_form.is_valid():
            pedido_form.save()  # Guardar el producto modificado
            return redirect('apps.gestion_insumos:pedir_insumos')  # Redirigir después de guardar
    else:
        pedido_form = PedidoForm(instance=pedido)  # Crear el formulario con la instancia existente
    pedidos = Pedido_Proveedor.objects.all().order_by('id')
    return render(request, 'gestion_insumos/pedidos_proveedores.html', {'form': pedido_form, 'Pedidos': pedidos})


def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido_Proveedor, id=pedido_id)  # Obtener el producto por ID

    if request.method == 'POST':
        pedido.delete()  # Eliminar el producto
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('apps.gestion_insumos:pedir_insumos')  # Redirigir después de eliminar

    pedidos = Pedido_Proveedor.objects.all().order_by('id')
    return render(request, 'gestion_insumos/pedidos_proveedores.html', {'Pedidos': pedidos})
