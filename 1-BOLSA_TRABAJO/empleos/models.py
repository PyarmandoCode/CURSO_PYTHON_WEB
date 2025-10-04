from django.db import models

class Empleo(models.Model):
    titulo=models.CharField(max_length=200)
    empresa=models.CharField(max_length=200)
    descripcion=models.TextField()
    ubicacion=models.CharField(max_length=150)
    salario=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    fecha_publicacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"
