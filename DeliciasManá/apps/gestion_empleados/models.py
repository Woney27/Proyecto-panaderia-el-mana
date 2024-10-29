from django.db import models


class Empleado(models.Model):
    cuit = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=150)
    telefono = models.PositiveIntegerField()
    domicilio = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    fechaIngreso = models.DateField()
    estadoLaboral = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50, choices=[
        ('vendedor', 'Vendedor'),
        ('recepcionista', 'Recepcionista'),
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
        ('reponedor', 'Reponedor'),],
        default='vendedor')

    def __str__(self):
        return f'Empleado: {self.nombre} - CUIT {self.cuit}'


