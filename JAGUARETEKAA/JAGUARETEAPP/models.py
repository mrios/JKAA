
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
#from django.contrib.auth.models import Producto


# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return f"cliente {self.nombre}, email {self.email}, id {self.id}" 

class Categoria(models.Model):
    marca=models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return f"{self.marca}"

class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=140, null=True)
    precio=models.DecimalField(decimal_places=2, max_digits=10 )
    imagen=models.ImageField(upload_to='imagenes/')
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null= True)
    moderador=models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    fecha = models.DateField(null= False)
    
    
    def __str__(self):
        return f"Zapatillas {self.nombre}, color {self.color}, precio {self.precio}, id {self.id}"



  