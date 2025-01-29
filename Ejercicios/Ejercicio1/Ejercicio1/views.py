#from django.http import HTTPResponse
from django.shortcuts import render

def edad(request, e, año):
    edadFutura=(año-2024)+e
    contexto={
        "edad":e,
        "año":año,
        "futuro":edadFutura
        }
    return render(request, 'index.html', contexto)