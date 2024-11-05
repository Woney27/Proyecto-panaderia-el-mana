from django import forms
from django.forms import inlineformset_factory
from .models import Venta, Item, ClienteMayorista


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


class MayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = ('razonSocial', 'cuit', 'domicilio', 'telefono', 'email')

    def init(self, *args, **kwargs):
        super(MayoristaForm, self).__init__(*args, **kwargs)
        self.fields['razonSocial'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['cuit'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['domicilio'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['email'].widget.attrs.update({'class': 'form-agregar-cliente'})
