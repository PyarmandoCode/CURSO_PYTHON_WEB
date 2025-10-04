from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_empleos,name="lista_empleos")
]
