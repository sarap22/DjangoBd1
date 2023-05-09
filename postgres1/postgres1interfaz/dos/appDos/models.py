from django.db import models
# Create your models here.
class vehiculo(models.Model):
    tipo=models.TextField(max_length=30)
    marca=models.TextField(max_length=30)
    modelo=models.TextField(max_length=30)
    año=models.TextField(max_length=30)
    color=models.TextField(max_length=30)
    precio=models.TextField(max_length=30)
    seguro=models.TextField(max_length=30)
    numPasajeros=models.TextField(max_length=30)
    metodoPago=models.TextField(max_length=30)
    placa=models.TextField(max_length=30)
