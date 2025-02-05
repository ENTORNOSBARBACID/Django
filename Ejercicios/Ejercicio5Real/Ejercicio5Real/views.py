from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Ejercicio5Real.forms import ContactForm


def mostrar(request):
    miFormulario=ContactForm()
    return render(request,'formulario.html',{'form':miFormulario})

def salir(request):
    if request.method == "POST":
        miFrm = ContactForm(request.POST)
        if miFrm.is_valid():
            dicc = miFrm.cleaned_data
            lenguajes_seleccionados = dicc['lenguajes']
            if len(lenguajes_seleccionados) == 0:
                mensaje = "Espabila y ponte a estudiar ya"
            elif len(lenguajes_seleccionados) == 1:
                mensaje = "Estás empezando...."
            else:
                mensaje = "Sabes muchos lenguajes: " + ", ".join(lenguajes_seleccionados)
            dicc['mensaje'] = mensaje
            
            return render(request, "mostrarDatos.html", dicc)
    else:
        miFrm = ContactForm()

    return render(request, "index.html", {"form": miFrm})