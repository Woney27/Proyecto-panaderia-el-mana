from django.shortcuts import render, redirect
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
    return render(request, 'gestion_ventas/clientes_mayoristas.html',
                  {'form': mayorista_form, 'mayoristas': mayoristas})
