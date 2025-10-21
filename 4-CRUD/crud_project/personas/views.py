from django.shortcuts import render,redirect

from .models import Persona
from .forms import PersonaForm

def listar_personas(request):
    personas= Persona.objects.all()
    context = {
        "personas":personas
    }
    return render(request,"lista.html",context)

def crear_personas(request):
    if request.method =="POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_personas")
    else:
        form=PersonaForm()
        context = {'form'
            :form}
    return render(request,"formulario.html",context)        