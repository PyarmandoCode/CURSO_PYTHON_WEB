from django.shortcuts import render
from .models import Empleo

def lista_empleos(request):
    empleos= Empleo.objects.all().order_by('-fecha_publicacion')
    return render(request,"lista.html",{"empleos":empleos})
