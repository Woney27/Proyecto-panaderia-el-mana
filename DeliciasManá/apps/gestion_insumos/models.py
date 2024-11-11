from django.db import models

class Insumo(models.Model):
    insumo = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=20, choices= [
        ('kilogramos', 'Kilogramos'),
        ('litros', 'Litros'),
        ('unidad', 'Unidad'),
        ('gramos', 'Gramos')], default='Kilogramos')

    def __str__(self):
        return f'Insumo: {self.insumo} - Cantidad: {self.cantidad}'
    
class Pedido_Proveedor(models.Model):
    pedidoNum = models.IntegerField()
    fecha_solicitud = models.DateField()
    idProveedor = models.IntegerField()
    numComprobante = models.IntegerField()
    tipoPago = models.CharField(max_length=20, choices=[
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('tarjeta', 'Tarjeta')],
        default='efectivo')
    producto = models.CharField(max_length=150)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Pedido: {self.producto} {self.idProveedor}'
    
class InsumoPedido(models.Model):
    pedido = models.ForeignKey(Pedido_Proveedor, related_name='insumos_pedido', on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.cantidad} {self.insumo.unidad} de {self.insumo.insumo} para Pedido N° {self.pedido.pedidoNum}'