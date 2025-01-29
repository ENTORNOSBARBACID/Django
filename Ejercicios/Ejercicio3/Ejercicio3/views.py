#from django.http import HTTPResponse
from django.shortcuts import render
from Ejercicio3.models import Lenguaje

def plantilla(request):
    lenguajes=[]
    nuevoLenguaje=Lenguaje(nombre="java", año=2010, descripcion="Back-end")
    lenguajes.append(nuevoLenguaje)
    
    nuevoLenguaje=Lenguaje(nombre="python", año=2014, descripcion="front-end")
    lenguajes.append(nuevoLenguaje)
    
    contexto={
        "Lenguajes":lenguajes,
    }
    return render(request, 'plantilla.html', contexto)