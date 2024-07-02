from django.db import models

class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, default="Unknown")
    modelo = models.CharField(max_length=100, default="Default Model")
    año = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/')
    
    def __str__(self):
        return self.nombre