
from django.shortcuts import render
from appCuatro.models import *

def tablaM(request):
    listaM= mascota.objects.all()
    return render(request, "index.html",{"mascota":listaM})