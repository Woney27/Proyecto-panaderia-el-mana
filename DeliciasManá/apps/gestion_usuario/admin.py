from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.gestion_usuario.models import Usuario
from apps.gestion_usuario.forms import UsuarioForm


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioForm

    # Definición de fieldsets personalizados, sin incluir `usable_password`
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'cuil', 'domicilio')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Definición de add_fieldsets personalizada para la creación de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'cuil', 'domicilio', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'email', 'cuil')
    list_display = ('username', 'email', 'cuil')
