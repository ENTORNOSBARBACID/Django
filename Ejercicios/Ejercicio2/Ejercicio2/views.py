#from django.http import HTTPResponse
from django.shortcuts import render

def plantilla(request):
    
    return render(request, 'plantilla.html')