from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import VentaForm, ItemForm
from .models import Venta, Item, ClienteMayorista
from django.views.generic.edit import FormView
from django.forms import formset_factory
from django.forms import modelformset_factory

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
