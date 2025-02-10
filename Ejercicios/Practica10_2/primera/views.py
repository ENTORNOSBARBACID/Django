from django.shortcuts import render
from primera.forms import MiFormulario
def mostrar(request):
        miFrm=MiFormulario()
        return render(request, "formulario.html", {"form": miFrm})
def salir(request):
    if(request.method=="POST"):
        miFrm = MiFormulario(request.POST)
        if miFrm.is_valid():
            dicc = miFrm.cleaned_data
            # sexo_choices=dicc["sexo"]
            # temas_choices=dicc["temas_interes"]
            # preferencias_choices=dicc["preferencias"]
            print("Formulario válido. Datos recibidos:", dicc)
            return render(request, "mostrarDatos.html", dicc)
            
    else:
        miFrm=MiFormulario()
        return render(request, "formulario.html", {"form": miFrm})