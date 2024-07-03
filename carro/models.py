from django.db import models
from django.contrib.auth.models import User
from autos.models import Auto

class Carro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return f'Carro de {self.usuario.username}'
    
