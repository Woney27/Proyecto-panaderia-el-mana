from django.db import models
from apps.gestion_productos.models import Producto
from apps.gestion_empleados.models import Empleado


class Venta(models.Model):
    fechaVenta = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    nroComprobante = models.IntegerField(unique=True)
    tipoCliente = models.CharField(max_length=50, choices=[
        ('minorista', 'Minorista'),
        ('mayorista', 'Mayorista')],
        default='Minorista')
    formaPago = models.CharField(max_length=20, choices=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia')],
        default='Efectivo')
    montoTotal = models.DecimalField(max_digits=10,decimal_places=2, blank=True, default=0.00)

    def __str__(self):
        return f'Venta {self.nroComprobante} - Fecha de venta {self.fechaVenta}'


class Item(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.PositiveIntegerField()
    precioItem = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class ClienteMayorista (models.Model):
    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=11, unique=True)
    domicilio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'Cliente: {self.razonSocial} - CUIT: {self.cuit}'