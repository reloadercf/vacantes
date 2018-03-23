from django.db import models
from django.urls import reverse
from empresa.models import Empresa

# Create your models here.
class Job(models.Model):
    name=models.CharField(max_length=100)
    nombre_empresa=models.ForeignKey(Empresa, related_name="Empresa", on_delete=models.CASCADE)
    salario=models.IntegerField()
    avalible=models.BooleanField(default=True)
    descripcion=models.TextField()

    def __str__(self):
        return 'se solicita {} en la empresa {}'.format(self.name,self.nombre_empresa)

    def get_absolute_url(self):
        return reverse('bolsadechamba:detail', args=[self.id])