from django import forms
from django.forms import inlineformset_factory
from .models import Venta, Item


# Formulario para la venta
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['idVendedor', 'nroComprobante', 'tipoCliente', 'formaPago', 'montoTotal']


# Formulario para los ítems
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['producto', 'cantidadProducto']


# Crear un formset para el modelo Item
ItemFormSet = inlineformset_factory(
    Venta,  # El modelo padre
    Item,  # El modelo hijo
    form=ItemForm,  # El formulario para el hijo
    extra=1,  # Número de formularios adicionales
    can_delete=True  # Permitir eliminar ítems
)


