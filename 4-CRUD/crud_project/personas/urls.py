from django.urls import path
from .views import listar_personas,crear_personas

urlpatterns = [
    path("",listar_personas,name="listar_personas"),
    path("crear/",crear_personas,name="crear_personas")

]
