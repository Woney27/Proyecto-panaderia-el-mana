from django import forms
from django.forms import DateInput
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'nombre', 'cuit', 'domicilio', 'telefono', 'fecha_nacimiento', 'cargo', 'fecha_ingreso', 'estado'
        )
        widgets = {
            'fecha_nacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_ingreso': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):  # Corrección aquí: __init__ en lugar de init
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['cuit'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['domicilio'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['telefono'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['fecha_nacimiento'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['cargo'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['fecha_ingreso'].widget.attrs.update({'class': 'formulario-empleado'})
        self.fields['estado'].widget.attrs.update({'class': 'formulario-empleado'})
