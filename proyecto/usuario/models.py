from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
# Create your models here.

def validate_telefono_length(value):
    if len(str(value)) != 8:
        raise ValidationError('El número de teléfono debe tener exactamente 8 dígitos.')
def validate_dpi_length(value):
    if len(str(value)) != 13:
        raise ValidationError('El número de teléfono debe tener exactamente 13 dígitos.')
def validate_imagen_presence(value):
    if not value:
        raise ValidationError('Se requiere proporcionar una imagen.')

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

    dpi = models.BigIntegerField(validators=[validate_dpi_length,])   
    #ALTER TABLE usuario_usuario ALTER COLUMN dpi TYPE BIGINT;
    fecha_nacimiento=models.CharField(max_length=10)
    telefono = models.IntegerField(validators=[validate_telefono_length,])
    email=models.EmailField(default="example@example.com") 
    imagen = models.ImageField(upload_to="usuarios", null=True, blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def _str_(self):
        return self.nombre
    


