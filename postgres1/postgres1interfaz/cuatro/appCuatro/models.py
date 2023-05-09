from django.db import models
 
class mascota(models.Model):
    tipo=models.TextField(max_length=30)
    raza=models.TextField(max_length=30)
    nombre=models.TextField(max_length=30)
    edad=models.TextField(max_length=30)
    peso=models.TextField(max_length=30)
    color=models.TextField(max_length=30)
    nomDueño=models.TextField(max_length=30)
    guarderia=models.TextField(max_length=30)
    paseador=models.TextField(max_length=30)
    horasPaseo=models.TextField(max_length=30)