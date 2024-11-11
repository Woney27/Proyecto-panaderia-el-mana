from django.db import models

class Proveedor(models.Model):
    razonSocial = models.CharField(max_length=50)
    cuit = models.CharField(max_length=11, unique=True)
    domicilio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'Proveedor: {self.razonSocial} - CUIT: {self.cuit}'