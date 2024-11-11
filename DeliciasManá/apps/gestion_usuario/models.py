from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    cuil = models.CharField(max_length=11, unique=True, null=True)
    domicilio = models.CharField(max_length=150)
    password = models.CharField(max_length=128, default='default_password')  # Valor predeterminado temporal
    username = models.CharField(max_length=128, unique=True, default='default_username')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name="custom_user_groups",  # Nombre único para evitar conflicto
        blank=True,
        help_text="Grupos a los que pertenece el usuario.",
        verbose_name="grupos",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custom_user_permissions",  # Nombre único para evitar conflicto
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="permisos de usuario",
    )

    def __str__(self):
        return f'{self.username}'

    def obtener_nombre_completo(self):
        if self.last_name and self.first_name:
            nombre_completo = f'{self.last_name}, {self.first_name}'
            return nombre_completo.strip()
        else:
            return self.username

    obtener_nombre_completo.short_description = 'Nombre Completo'

