from django.db import models

class libro(models.Model):
    titulo=models.TextField(max_length=30)
    genero=models.TextField(max_length=30)
    autor=models.TextField(max_length=30)
    año=models.TextField(max_length=30)
    trama=models.TextField(max_length=30)
    espacio=models.TextField(max_length=30)
    tiempo=models.TextField(max_length=30)
    clasificacion=models.TextField(max_length=30)
    editorial=models.TextField(max_length=30)
    cantidadPags=models.IntegerField(default=0)
