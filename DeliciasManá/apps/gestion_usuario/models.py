from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=150, )
    cuil = models.PositiveIntegerField(unique=True)
    email = models.CharField(max_length=100)

    