from django.db import models

# Create your models here.
class usuario(models.Model):
    documento=models.TextField(max_length=30)
    nombreUser=models.TextField(max_length=30)
    clave=models.TextField(max_length=30)

class cliente(models.Model):
    documento=models.TextField(max_length=30)
    nombre=models.TextField(max_length=30)
    apellido=models.TextField(max_length=30)
    correo=models.TextField(max_length=30)
    celular=models.TextField(max_length=30)
    sexo=models.TextField(max_length=30)

class creditos(models.Model):
    documento=models.TextField(max_length=30)
    codigo=models.TextField(max_length=30)
    monto=models.TextField(max_length=30)
    plazo=models.TextField(max_length=30)
    desembolso=models.TextField(max_length=30)

class creditoLineas(models.Model):
    codigo=models.TextField(max_length=30)
    nombre=models.TextField(max_length=30)
    montoMax=models.TextField(max_length=30)
    plazoMax=models.TextField(max_length=30)
    
    
    
