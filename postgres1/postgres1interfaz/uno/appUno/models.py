from django.db import models

# Create your models here.
class producto(models.Model):
    nombre=models.TextField(max_length=30)
    numSerie=models.TextField(max_length=30)
    categoria=models.TextField(max_length=30)
    cantidad=models.TextField(max_length=30)
    precio=models.TextField(max_length=30)