from django.shortcuts import render
from django.db import IntegrityError
from Primera.forms import MiFormulario, Login, Alta, Resolver, Detalles
from django.views.decorators.csrf import csrf_exempt
from Primera.models import Profesor, Laboratorio, Incidencias, Resueltas
from datetime import date

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
                return render(request, 'Formulario.html', {'form': miFrm,'mensaje': mensaje})
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
        if(profesor.laboratorio=='T'):
            incidencias=mostrarInc()
            return render(request, 'Tecnico.html', {'form': my_frm, 'Incidencias':incidencias, 'operacion': 'update'})
        else:
            laboratorios=mostrarLab()
            return render(request, 'Profesor.html', {'form': my_frm, 'laboratorios': laboratorios, 'operacion': 'update'})
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
            

def alta(request):
    alta = None
    if request.method == "POST":
        miFrm = Alta(request.POST)
        if miFrm.is_valid():
            alta = anyadirIncidencia(miFrm)
            try:
                alta.save()    
                mensaje = 'Incidencia añadido'
            except IntegrityError:  
                mensaje = 'Incidencia no añadido'
                
            laboratorio=mostrarLab()
            return render(request, 'Profesor.html', {'laboratorios':laboratorio,  'mensaje': mensaje})
        else:
            # Si el formulario no es válido, usa el formulario con errores
            my_frm = miFrm
    else:
        # Si no es una solicitud POST, muestra el formulario vacío
        my_frm = Alta()
    
    # Devuelve el formulario en todos los casos
    return render(request, 'alta_incidencias.html', {'form': my_frm})

def resolver(request, id):
    incidencias = Incidencias.objects.get(numero=id)
    resolver=None
    if request.method == "POST":
        miFrm = Resolver(request.POST)
        if miFrm.is_valid():
            resuelto = anyadirResuelto(miFrm)
            incidencias.resuelta=True
            try:
                resuelto.save()    
                mensaje = 'Incidencia añadido'
            except IntegrityError:  
                mensaje = 'Incidencia no añadido'
                
            try:
                incidencias.save()    
                mensaje2 = 'Incidencia Editada'
            except IntegrityError:  
                mensaje2 = 'Incidencia no Editada'
            
            incidencias=mostrarInc()
            return render(request, 'Tecnico.html', {'Incidencias':incidencias,  'mensaje': mensaje, 'mensaje2': mensaje2})
        else:
            # Si el formulario no es válido, usa el formulario con errores
            my_frm = miFrm
    else:
        # Si no es una solicitud POST, muestra el formulario vacío
        my_frm = Resolver(initial={
            'numero': incidencias.numero,
            'email': incidencias.emailProfesor,
            'numOrdenador':incidencias.numOrdenador
        })
    # Devuelve el formulario en todos los casos
    return render(request, 'resolver.html', {'form': my_frm, 'numero':incidencias.numero})

def detalles(request, id):
    incidencias=Incidencias.objects.get(numero=id)
    if request.method == "POST":
        miFrm = Resolver(request.POST)
        if miFrm.is_valid():
            incidencias=mostrarInc()
            return render(request, 'Tecnico.html', {'Incidencias':incidencias})
        else:
            # Si el formulario no es válido, usa el formulario con errores
            my_frm = miFrm
    else:
        res=Resueltas.objects.get(numeroIncidencia=id)
        my_frm = Detalles(initial={
            'numero': res.numeroIncidencia,
            'email': res.emailProfesor,
            'numOrdenador':incidencias.numOrdenador,
            'descripcion':res.descripcion
        })
    return render(request, 'Detalles.html', {'form': my_frm, 'numero':incidencias.numero})
#Funciones

def anyadirIncidencia(frm:Alta):
    laboratorio=frm.cleaned_data['laboratorio']
    numOrdenador=frm.cleaned_data['nombre']
    email=frm.cleaned_data['email']
    descripcion=frm.cleaned_data['descripcion']
    alta=Incidencias( laboratorio=laboratorio, numOrdenador=numOrdenador, emailProfesor=email, descripcion=descripcion)
    return alta

def anyadirResuelto(frm:Alta):
    numeroIncidencia=frm.cleaned_data['numero']
    emailProfesor=frm.cleaned_data['email']
    descripcion=frm.cleaned_data['descripcion']
    alta=Resueltas( numeroIncidencia=numeroIncidencia, emailProfesor=emailProfesor, descripcion=descripcion)
    return alta


def anyadirProfesor(frm:MiFormulario):
    nombre=frm.cleaned_data['nombre']
    email=frm.cleaned_data['email']
    contraseña=frm.cleaned_data['contraseña']
    laboratorio=frm.cleaned_data['laboratorio']
    profesor=Profesor(nombre=nombre, email=email, contraseña=contraseña, laboratorio=laboratorio)
    return profesor

def mostrarLab():
    laboratorios=Laboratorio.objects.all()
    return laboratorios

def mostrarInc():
    incidencias=Incidencias.objects.all()
    return incidencias


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