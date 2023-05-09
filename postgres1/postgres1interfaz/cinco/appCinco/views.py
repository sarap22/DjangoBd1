from django.shortcuts import render
from appCinco.models import *

def tablaL(request):
    listaL=libro.objects.all()
    return render(request, "index.html",{"libro":listaL})

