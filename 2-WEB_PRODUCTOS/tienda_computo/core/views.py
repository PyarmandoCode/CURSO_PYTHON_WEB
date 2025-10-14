from django.shortcuts import render
from .models import Producto


def index(request):
    template_name="index.html"
    productos = Producto.objects.all()
    context = { 'productos' :
               productos }
    return render(request,template_name,context)
