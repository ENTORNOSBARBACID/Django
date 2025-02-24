from django.db import models
from datetime import date, timedelta


def una_semana_despues():
    return date.today() + timedelta(days=7)

class Profesor(models.Model):
    nombre= models.CharField(max_length=80)
    email =models.EmailField(max_length=50)
    contraseña= models.CharField(max_length=20)
    ciclo= models.CharField(max_length=80)
    dni=models.CharField(max_length=80)

class Alumno(models.Model):
    nombre= models.CharField(max_length=80)
    email =models.EmailField(max_length=50)
    contraseña= models.CharField(max_length=20)
    telefono= models.IntegerField()
    ciclo= models.CharField(max_length=80)
    dni=models.CharField(max_length=80)
    
class Ciclos(models.Model):
    ciclo=models.CharField(max_length=80)
    profesorDni=models.CharField(max_length=80)
    aulas=models.CharField(max_length=80)
    
    def __str__(self):
        return self.ciclo 

class Tareas(models.Model):
    ciclo=models.CharField(max_length=80)
    nombre=models.CharField(max_length=80)
    fechaEntrega=models.DateField(default=una_semana_despues)
    completada=models.BooleanField(default=False)
