from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100,null=True,blank=True)
    edad = models.IntegerField()


    def __str__(self):
        return self.nombre