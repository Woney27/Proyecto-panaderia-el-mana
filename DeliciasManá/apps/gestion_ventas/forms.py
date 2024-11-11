from django import forms
from django.forms import inlineformset_factory
from .models import Venta, Item, ClienteMayorista
from django.core.exceptions import ValidationError


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

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        # Asegurarse de que el teléfono tenga solo números y una longitud válida
        if not telefono.isdigit():
            raise ValidationError("El teléfono debe contener solo números.")
        if len(telefono) < 10:
            raise ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return telefono
    
    def clean_cuit(self):
        cuit = self.cleaned_data.get('cuit')
        # Validación para asegurar que el cuit sea numérico y tenga 11 dígitos (como en Argentina)
        if not cuit.isdigit():
            raise ValidationError("El CUIT debe contener solo números.")
        if len(cuit) != 11:  # Ajusta según el formato que necesites
            raise ValidationError("El CUIT debe tener 11 dígitos.")
        return cuit
    
    def clean(self):
        cleaned_data = super().clean()
        razonSocial = cleaned_data.get("razonSocial")
        domicilio = cleaned_data.get("domicilio")
        email = cleaned_data.get("email")
        
        if not razonSocial or not domicilio or not email:
            raise ValidationError("Todos los campos son obligatorios.")
        return cleaned_data
    
    def init(self, *args, **kwargs):
        super(MayoristaForm, self).__init__(*args, **kwargs)
        self.fields['razonSocial'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['cuit'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['domicilio'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-agregar-cliente'})
        self.fields['email'].widget.attrs.update({'class': 'form-agregar-cliente'})
