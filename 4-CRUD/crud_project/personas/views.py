from django.shortcuts import render,redirect,get_object_or_404

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

def eliminar_persona(request,id):
    persona= get_object_or_404(Persona,id=id)
    if request.method=="POST":
        persona.delete()
        return redirect('listar_personas')
    context = {
        "persona":persona
    }
    return render(request,"confirmar_eliminar.html",context)


def editar_persona(request,id):
    persona=get_object_or_404(Persona,id=id)
    if request.method=="POST":
        form=PersonaForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form=PersonaForm(instance=persona) 
    return render (request,"formulario.html", {'form':form})       