from django import forms
from django.forms import DateInput
from .models import Insumo, Pedido_Proveedor

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = (
            'insumo',
            'cantidad',
            'unidad'
        )

        def init(self, *args, **kwargs):
            super(InsumoForm, self)._init_(*args, **kwargs)

            self.fields['insumo'].widget.attrs.update({'class':'formulario-insumo'})

            self.fields['cantidad'].widget.attrs.update({'class':'formulario-insumo'})

            self.fields['unidad'].widget.attrs.update({'class':'formulario-insumo'})


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_Proveedor
        fields = (
            'pedidoNum',
            'fecha_solicitud',
            'idProveedor',
            'numComprobante',
            'tipoPago',
            'producto',
            'cantidad'
        ) 
        widgets = {
            'fecha_solicitud': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def init(self, *args, **kwargs):
            super(PedidoForm, self)._init_(*args, **kwargs)

            self.fields['pedidoNum'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['fecha_solicitud'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['idProveedor'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['numComprobante'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['tipoPago'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['producto'].widget.attrs.update({'class':'formulario-pedido'})

            self.fields['cantidad'].widget.attrs.update({'class':'formulario-pedido'})