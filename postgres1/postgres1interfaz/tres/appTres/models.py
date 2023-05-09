from django.db import models
# Create your models here.
class paciente(models.Model):
    nombre=models.TextField(max_length=30)
    apellido=models.TextField(max_length=30)
    edad=models.TextField(max_length=30)
    sexo=models.TextField(max_length=30)
    celular=models.TextField(max_length=30)
    rh=models.TextField(max_length=30)
    causa=models.TextField(max_length=30)
    diagnostico=models.TextField(max_length=30)
    medicamento=models.TextField(max_length=30)
    costo=models.TextField(max_length=30)
    


