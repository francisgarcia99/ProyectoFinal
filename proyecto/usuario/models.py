from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dpi=models.IntegerField()
    fecha_nacimiento=models.CharField(max_length=10)
    telefono=models.IntegerField()
    email=models.EmailField(default="example@example.com") 
    imagen=models.ImageField(upload_to="alumnos", null=True, blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"

    def _str_(self):
        return self.nombre