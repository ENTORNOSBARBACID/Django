from django.shortcuts import render
from Ejercicio5.models.Asignaturas import Asignaturas

# Create your views here.
def mostrar(request):
    a=[]
    a.append(Asignaturas("Rosa Rodriguez", "DAW", "1020"))
    a.append(Asignaturas("Yolanda Diaz", "ASIR", "1000"))
    a.append(Asignaturas("Begoña Lopez", "DAW", "1200"))
    return render(request, "plantilla.html", {"asignaturas": a})