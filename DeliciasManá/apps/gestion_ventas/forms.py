from django import forms
from django.forms import inlineformset_factory
from .models import Venta, Item, ClienteMayorista


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['empleado', 'nroComprobante', 'tipoCliente', 'formaPago', 'montoTotal']

    def init(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['empleado'].widget.attrs.update({'class': 'cuadro-datos datos-predefinidos'})
        self.fields['nroComprobante'].widget.attrs.update({'class': 'cuadro-datos datos-predefinidos'})
        self.fields['tipoCliente'].widget.attrs.update({'class': 'cuadro-datos datos-predefinidos'})
        self.fields['montoTotal'].widget.attrs.update({'class': 'cuadro-datos datos-predefinidos'})


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['producto', 'cantidad']

    def init(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['producto'].widget.attrs.update({'class': 'cuadro-datos'})
        self.fields['cantidad'].widget.attrs.update({'class': 'cuadro-datos'})


ItemFormSet = inlineformset_factory(
    Venta,
    Item,
    form=ItemForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True  # Permite eliminar secciones
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
