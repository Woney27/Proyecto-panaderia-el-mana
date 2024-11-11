from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    cuit = models.CharField(unique=True)
    domicilio = models.CharField(max_length=100)
    telefono =models.CharField()
    fecha_nacimiento = models.DateField()
    cargo = models.CharField(max_length=50, choices=[
        ('vendedor', 'Vendedor'),
        ('recepcionista', 'Recepcionista'),
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
        ('reponedor', 'Reponedor'),],
        default='vendedor')
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('activo','Activo'),
        ('inactivo', 'Inactivo')
    ], default='activo')


    def __str__(self):
        return f'Empleado: {self.nombre} - CUIT {self.cuit}'