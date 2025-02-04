#from django.http import HTTPResponse
from django.shortcuts import render
from Ejercicio3.models.Lenguaje import Lenguaje

def plantilla(request):
    lenguajes = [
        Lenguaje(nombre="Java", año=2010, descripcion="Back-end"),
        Lenguaje(nombre="Python", año=2014, descripcion="Front-end"),
        Lenguaje(nombre="JavaScript", año=2000, descripcion="Front-end"),
        Lenguaje(nombre="HTML", año=1994, descripcion="Front-end")
    ]
    return render(request, 'plantilla.html', {"Lenguajes": lenguajes})