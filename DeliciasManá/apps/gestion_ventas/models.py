from django.db import models


class Venta(models.Model):
    fechaVenta = models.DateField(auto_now_add=True)
    #idVendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
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
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProducto = models.PositiveIntegerField()
    precioItem = models.DecimalField

    # def save(self, *args, **kwargs):
    #    self.precioItem = self.cantidadProducto * self.producto
    #     super(Item, self).save(*args, **kwargs)


class ClienteMayorista (models.Model):
    razonSocial = models.CharField(max_length=50)
    cuit = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    domicilio = models.CharField(max_length=150)

