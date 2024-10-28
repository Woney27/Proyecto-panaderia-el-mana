from django import forms
from django.forms import inlineformset_factory
from .models import Venta, Item


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['nroComprobante', 'tipoCliente', 'formaPago', 'montoTotal']



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['producto', 'precioItem', 'cantidadProducto'] 


ItemFormSet = inlineformset_factory(
    Venta, 
    Item,  
    form=ItemForm,  
    extra=1,  
    can_delete=True
)