from django.contrib.auth.forms import UserCreationForm
from apps.gestion_usuario.models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('cuil', 'domicilio')

