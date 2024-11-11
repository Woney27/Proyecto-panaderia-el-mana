from django.shortcuts import render
from django.db.models import Sum, Count
from apps.gestion_ventas.models import Venta, Item
from apps.gestion_productos.models import Producto
from apps.gestion_ventas.models import ClienteMayorista
from apps.gestion_empleados.models import Empleado

def reporte(request):
        # Total de ventas y monto total de ventas
        total_ventas = Venta.objects.count()
        monto_total_ventas = Venta.objects.aggregate(monto_total_sum=Sum('montoTotal'))['monto_total_sum'] or 0

        # Empleados y clientes mayoristas
        total_empleados = Empleado.objects.count()
        total_clientes_mayoristas = ClienteMayorista.objects.count()

        # Productos más vendidos
        
        productos_mas_vendidos = (
            Item.objects
            .values('producto__descripcion')
            .annotate(total_vendido=Sum('cantidad'))
            .order_by('-total_vendido')[:5]
        )

        # Productos faltantes (ajustando a 'cantidad_disponible')
        productos_faltantes = Producto.objects.filter(cantidad_disponible__lte=0)

        context = {
            'total_ventas': total_ventas,
            'monto_total_ventas': monto_total_ventas,
            'total_empleados': total_empleados,
            'total_clientes_mayoristas': total_clientes_mayoristas,
            'productos_mas_vendidos': productos_mas_vendidos,
            'productos_faltantes': productos_faltantes,
        }
    
        return render(request,'gestion_reporte/reporte.html', context)