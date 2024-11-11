from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import VentaForm, ItemForm, MayoristaForm, ItemFormSet
from django.urls import reverse
from apps.gestion_ventas.models import Venta, Item, ClienteMayorista


def registrar_venta(request):
    venta_nueva = None
    monto_total = 0
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            formset = ItemFormSet(request.POST, instance=venta)

            if formset.is_valid():
                items = formset.save(commit=False)
                for item in items:
                    # Calcular el monto total de la venta y el de cada item individual
                    if item.producto:
                        item.precioItem = item.cantidad * item.producto.precio_unidad
                        monto_total = monto_total + item.precioItem
                venta.montoTotal = monto_total
                venta.save()

                for item in items:
                    item.save()
                    item.producto.cantidad_disponible -= item.cantidad
                    item.producto.save()

                messages.success(request, "La venta se registró exitosamente.")
                return redirect('apps.gestion_ventas:ventas')
            else:
                messages.error(request, "Por favor revisa los datos de los items del formulario.")
        else:
            messages.error(request, "Por favor revisa los datos del formulario de venta.")
    else:
        form = VentaForm()
        formset = ItemFormSet()
        return render(request, 'gestion_ventas/gestion_ventas.html', {'form': form, 'formset': formset})


def lista_ventas(request):
    ventas = Venta.objects.all().order_by('id')  # Obtener todas las ventas
    return render(request, 'gestion_ventas/lista_ventas.html', {'ventas': ventas})


def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)  # Obtener la venta específica
    items = Item.objects.filter(venta=venta)  # Obtener los items relacionados a esta venta
    return render(request, 'gestion_ventas/detalle_venta.html', {'venta': venta, 'items': items})


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


