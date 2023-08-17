from django.db import models

# Create your models here.

class Alquileres(models.Model):
    tipo= models.CharField(max_length=50)
    ambientes= models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio= models.IntegerField()


class Venta(models.Model):
    tipo= models.CharField(max_length=30)
    ambientes= models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio= models.IntegerField()

    
    
class Asesores(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    telefono= models.IntegerField()
    email= models.EmailField()