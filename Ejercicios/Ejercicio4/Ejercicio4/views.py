#from django.http import HTTPResponse
from django.shortcuts import render
from Ejercicio4.models.Asignaturas import Asignaturas

def mostrar(request):
    a=[]
    a.append(Asignaturas("Rosa Rodriguez", "DAW", "1020"))
    a.append(Asignaturas("Yolanda Diaz", "ASIR", "1000"))
    a.append(Asignaturas("Begoña Lopez", "DAW", "1200"))
    return render(request, "plantilla.html", {"asignaturas": a})