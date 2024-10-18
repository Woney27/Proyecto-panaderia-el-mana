from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=30)
    CUIT = models.ForeignKey
    