from django.shortcuts import render
from appUno.models import *
# Create your views here.
def tablaPro(request):
    listaP= producto.objects.all()
    return render(request, "index.html",{"producto": listaP})
