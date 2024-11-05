from django.contrib import admin
from apps.gestion_empleados.models import Empleado
from apps.gestion_ventas.models import Venta, Item, ClienteMayorista
from apps.gestion_productos.models import Producto


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['cuit', 'nombre', 'telefono', 'domicilio', 'estado', 'cargo']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['fechaVenta', 'nroComprobante', 'tipoCliente', 'montoTotal']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidadProducto', 'precioItem']


@admin.register(ClienteMayorista)
class ClienteMayoristaAdmin(admin.ModelAdmin):
    list_display = ['razonSocial', 'cuit', 'telefono', 'domicilio']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'unidad_medida', 'cantidad_disponible', 'precio_unidad']

