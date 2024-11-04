from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'unidad_medida', 'cantidad_disponible',
                  'precio_unidad', 'punto_reposicion', 'categoria')

    def _init_(self, *args, **kwargs):
        super(ProductoForm, self)._init_(*args, **kwargs)
        self.fields['descripcion'].widget.attrs.update({'class': 'form-agregar-producto'})  # Puedes agregar más clases si lo deseas
        self.fields['unidad_medida'].widget.attrs.update({'class': 'form-agregar-producto'})
        self.fields['cantidad_disponible'].widget.attrs.update({'class': 'form-agregar-producto'})
        self.fields['precio_unidad'].widget.attrs.update({'class': 'form-agregar-producto'})
        self.fields['punto_reposicion'].widget.attrs.update({'class': 'form-agregar-producto'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-agregar-producto'})