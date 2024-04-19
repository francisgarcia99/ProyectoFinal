from django import forms
from usuario.models import Usuario

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre','apellido','dpi','fecha_nacimiento','telefono','email','imagen')