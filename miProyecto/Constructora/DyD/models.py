from django.db import models

# Create your models here.

class Empleado(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=60)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    sueldo           = models.CharField(max_length=7)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.rut)+" "+str(self.nombre)

class Producto(models.Model):
    id_prod              = models.AutoField(primary_key=True)
    nombre_prod          = models.CharField(max_length=60)
    cantidad_prod        = models.CharField(max_length=30)
    almacenaje           = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_prod)+" "+str(self.nombre_prod)