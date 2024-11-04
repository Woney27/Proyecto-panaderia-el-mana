from django.db import models


class Producto(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('kg', 'Kilogramos'),
        ('g', 'Gramos'),
        ('unidad', 'Unidad'),
    ]

    CATEGORIA_CHOICES = [
        ('panificación', 'Panificación'),
        ('pastelería', 'Pastalería')
    ]

    descripcion = models.CharField(max_length=100, unique=True, null=False)
    unidad_medida = models.CharField(max_length=10, choices=UNIDAD_MEDIDA_CHOICES, default='unidad')
    cantidad_disponible = models.PositiveIntegerField(default=0)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    punto_reposicion = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)

    def _str_(self):
        return f"{self.descripcion} - {self.categoria} - {self.unidad_medida}"


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"