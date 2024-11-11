from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import VentaForm, ItemForm, MayoristaForm
from django.urls import reverse
from apps.gestion_ventas.models import Venta, Item, ClienteMayorista


def registrar_ventas(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta registrada exitosamente.')
            return redirect('gestion_ventas: ventas')
    else:
        form = VentaForm()
    return render(request, 'gestion_ventas/gestion_ventas.html', {'form': form})


def registrar_cliente_mayorista(request):
    nuevo_mayorista = None
    if request.method == 'POST':
        mayorista_form = MayoristaForm(request.POST)
        if mayorista_form.is_valid():
            print("Formulario válido")
            nuevo_mayorista = mayorista_form.save(commit=False)
            nuevo_mayorista.save()
            messages.success(request, 'Se ha registrado correctamente el cliente mayorista.')
            return redirect(reverse('apps.gestion_ventas:mayoristas'))
        else:
            print("Formulario no válido")
            print(mayorista_form.errors)
            messages.error(request, "Error al guardar el formulario. Verifica los campos.")
    else:
        mayorista_form = MayoristaForm()
    mayoristas = ClienteMayorista.objects.all()
    return render(request, 'gestion_ventas/clientes_mayoristas.html',{'form': mayorista_form, 'mayoristas': mayoristas})


def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)  # Obtener el cliente por ID
    if request.method == 'POST':
        cliente_form = MayoristaForm(request.POST, instance=cliente)  # Pasar la instancia al formulario
        if cliente_form.is_valid():
            cliente_form.save()  # Guardar el cliente modificado
            messages.success(request, 'Cliente modificado exitosamente.')
            return redirect('apps.gestion_ventas:mayoristas')  # Redirigir después de guardar, hacia la vista de mayoristas
    else:
        cliente_form = MayoristaForm(instance=cliente)  # Crear el formulario con la instancia existente

    return render(request, 'gestion_ventas/clientes_mayoristas.html', {'form': cliente_form, 'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(ClienteMayorista, id=cliente_id)  # Obtener el cliente por ID

    if request.method == 'POST':
        cliente.delete()  # Eliminar el cliente
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('apps.gestion_ventas:mayoristas')  # Redirigir después de eliminar, hacia la vista de mayoristas

    return render(request, 'gestion_ventas/eliminar_cliente.html', {'cliente': cliente})


