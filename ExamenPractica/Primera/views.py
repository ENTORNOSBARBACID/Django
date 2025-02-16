from django.shortcuts import render
from django.db import IntegrityError
from Primera.forms import MiFormulario, Login
from django.views.decorators.csrf import csrf_exempt
from Primera.models import Profesor, Laboratorio, Incidencias, Resueltas

def mostrar(request):
        miFrm=MiFormulario()
        return render(request, "Formulario.html", {"form": miFrm})
    
def salir(request):
    profesor = None  # Inicializa profesor como None
    if request.method == "POST":
        miFrm = Login(request.POST)
        if miFrm.is_valid():
            profesor = buscarProfesor(request)
            if profesor is None:
                mensaje = "Profesor no encontrado"
                return render(request, 'index.html', {'mensaje': mensaje})
        else:
            # Si el formulario no es válido, muestra el formulario con errores
            return render(request, 'Formulario.html', {'form': miFrm, 'mensaje':"No se encuentra el correo"})
    
    # Si profesor no es None, inicializa el formulario con sus datos
    if profesor is not None:
        my_frm = MiFormulario()
        my_frm.fields['nombre'].initial = profesor.nombre
        my_frm.fields['email'].initial = profesor.email
        my_frm.fields['contraseña'].initial = profesor.contraseña
        my_frm.fields['laboratorio'].initial = profesor.laboratorio
        return render(request, 'Login.html', {'form': my_frm, 'operacion': 'update'})
    else:
        # Si no hay profesor, muestra el formulario vacío
        my_frm = MiFormulario()
        return render(request, 'Formulario.html', {'form': my_frm, 'mensaje':"No se encuentra el correo"})
            

def salir2(request):
    profesor = None  # Inicializa profesor como None
    if request.method == "POST":
        miFrm = MiFormulario(request.POST)
        if miFrm.is_valid():
            profesor = anyadirProfesor(miFrm)
            try:
                profesor.save()    
                mensaje = 'Alumno añadido'
            except IntegrityError:  
                mensaje = 'Alumno no añadido'
            return render(request, 'Login.html', {'mensaje': mensaje})
        else:
            # Si el formulario no es válido, usa el formulario con errores
            my_frm = miFrm
    else:
        # Si no es una solicitud POST, muestra el formulario vacío
        my_frm = MiFormulario()
    
    # Devuelve el formulario en todos los casos
    return render(request, 'Añadir.html', {'form': my_frm})
            

def anyadirProfesor(frm:MiFormulario):
    nombre=frm.cleaned_data['nombre']
    email=frm.cleaned_data['email']
    contraseña=frm.cleaned_data['contraseña']
    laboratorio=frm.cleaned_data['laboratorio']
    profesor=Profesor(nombre=nombre, email=email, contraseña=contraseña, laboratorio=laboratorio)
    return profesor


def buscarProfesor(request):
    miFrm = Login(request.POST)
    if miFrm.is_valid():
        email = miFrm.cleaned_data['email']
        contraseña = miFrm.cleaned_data['contraseña']
        try:
            # Busca el profesor por email y contraseña
            profesor = Profesor.objects.get(email=email, contraseña=contraseña)
        except Profesor.DoesNotExist:
            return None
        else:
            return profesor
    else:
        # Si el formulario no es válido, devuelve None
        return None