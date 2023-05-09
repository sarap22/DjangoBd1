from django.shortcuts import render
from appPostgres1.models import *

def tablaUser(request):
    listaU= usuario.objects.all()
    return render(request, "index.html",{"usuario": listaU})


def tablaCli(request):
    listaC= cliente.objects.all()
    return render(request, "index.html",{"cliente": listaC})

def tablaCre(request):
    listaCre= creditos.objects.all()
    return render(request, "index.html",{"credito": listaCre})

def tablaCre_l(request):
    listaCreLi= creditoLineas.objects.all()
    return render(request, "index.html",{"lineal": listaCreLi})