from django.shortcuts import render
from appDos.models import*

def tablaV(request):
    listaV= vehiculo.objects.all()
    return render(request, "index.html",{"vehiculo": listaV})

