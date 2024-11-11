from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('razonSocial', 'cuit', 'domicilio', 'telefono', 'email')

    def init(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['razonSocial'].widget.attrs.update({'class': 'form-agregar-proveedor'})
        self.fields['cuit'].widget.attrs.update({'class': 'form-agregar-proveedor'})
        self.fields['domicilio'].widget.attrs.update({'class': 'form-agregar-proveedor'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-agregar-poveedor'})
        self.fields['email'].widget.attrs.update({'class': 'form-agregar-proveedor'})
