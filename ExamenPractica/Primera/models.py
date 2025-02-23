from django.db import models
from datetime import date

# Create your models here.
class Profesor(models.Model):
    nombre= models.CharField(max_length=80)
    email =models.EmailField(max_length=50)
    contraseña= models.CharField(max_length=20)
    laboratorio= models.CharField(max_length=80)
    
class Laboratorio(models.Model):
        nombre= models.CharField(max_length=80)
        numeroOrdenadores= models.IntegerField()
        email= models.EmailField(max_length=50)
        
class Incidencias(models.Model):
                numero=models.AutoField(primary_key=True, serialize=False)
                fecha= models.DateField(default=date.today)
                laboratorio= models.CharField(max_length=80)
                numOrdenador= models.IntegerField()
                emailProfesor= models.EmailField(max_length=50)
                resuelta=models.BooleanField(default=False)
                descripcion= models.CharField(max_length=80)
class Resueltas(models.Model):
                numeroIncidencia= models.IntegerField()
                emailProfesor= models.EmailField(max_length=50)
                fecha= models.DateField(default=date.today)
                descripcion= models.TextField(max_length=100)