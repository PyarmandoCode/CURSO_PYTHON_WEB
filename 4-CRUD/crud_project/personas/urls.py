from django.urls import path
from .views import listar_personas,crear_personas,eliminar_persona,editar_persona

urlpatterns = [
    path("",listar_personas,name="listar_personas"),
    path("crear/",crear_personas,name="crear_personas"),
    path("eliminar/<int:id>/",eliminar_persona,name="eliminar_persona"),
    path("editar/<int:id>/",editar_persona,name="editar_persona")

]
