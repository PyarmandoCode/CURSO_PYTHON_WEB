from django.shortcuts import render,redirect
from .forms import PersonaForm
from .models import Persona

def crear_persona(request):
    if request.method=='POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            form.save() #Guardar en el modelo = Tabla
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request,'crear_persona.html',{'form':form})         

def lista_personas(request):
    personas=Persona.objects.all()
    context = {"personas":personas}
    return render(request,'lista_personas.html',context)

