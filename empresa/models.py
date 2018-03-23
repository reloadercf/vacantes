from django.db import models
from django.urls import reverse

# Create your models here.
class Empresa(models.Model):
    nombre_empresa=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    numero_empleados=models.IntegerField()
    avalible=models.BooleanField(default=True)
    descripcion=models.TextField()



    def __str__(self):
        return self.nombre_empresa

    def get_absolute_url(self):
        return reverse('company:detail',args=[self.id])