from django.urls import path
from . import views


urlpatterns = [
    path('',views.crear_persona,name='crear_persona'),
    path('lista_personas/',views.lista_personas,name='lista_personas')
]
