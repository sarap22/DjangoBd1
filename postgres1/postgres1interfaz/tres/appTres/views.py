from django.shortcuts import render
from appTres.models import *
# Create your views here.
def tablaP(request):
    listaP= paciente.objects.all()
    return render(request, "index.html",{"paciente":listaP})
