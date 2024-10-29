from django import forms
from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'cuit',
            'nombre',
            'telefono',
            'domicilio',
            'fechaNacimiento',
            'fechaIngreso',
            'estadoLaboral',
            'cargo',
        ]
