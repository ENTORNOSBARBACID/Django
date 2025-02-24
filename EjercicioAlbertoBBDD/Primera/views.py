from django.shortcuts import render
from Primera.forms import Login, Edit, Añadir,Tarea, AñadirProfesor, AñadirCic
from django.db import IntegrityError
from Primera.models import Profesor, Alumno, Tareas, Ciclos

def Log(request):
    sesion = None
    if request.method == "POST":
        miFrm = Login(request.POST)
        if(miFrm.is_valid()):
            email = miFrm.cleaned_data['email']
            contraseña = miFrm.cleaned_data['contraseña']
            try:
                sesion = Profesor.objects.get(email=email, contraseña=contraseña)
            except Profesor.DoesNotExist:
                sesion=None
                
                
            if sesion != None:
                alumnos=Alumno.objects.filter(ciclo=sesion.ciclo)
                return render(request, 'Profesor.html', {'alumnos':alumnos, 'ciclo':sesion.ciclo})
            
            else:
                
                try:
                    sesion = Alumno.objects.get(email=email, contraseña=contraseña)
                except Alumno.DoesNotExist:
                    sesion=None
                    
                if sesion!=None:
                    tareas=Tareas.objects.filter(ciclo=sesion.ciclo)
                    return render(request, 'Alumno.html', {'tareas':tareas})
                else:
                    return render(request, 'Login.html', {'mensaje':'Credenciales no encontradas', 'form':miFrm})
                
    else:
        my_frm = Login()
    
    return render(request, 'Login.html', {'form': my_frm})

def EditAl(request, id):
    alumno = Alumno.objects.get(dni=id)
    if request.method == "POST":
        miFrm = Edit(request.POST)
        if(miFrm.is_valid()):
            alumno.email=miFrm.cleaned_data['email']
            alumno.telefono=miFrm.cleaned_data['telefono']
            try:
                alumno.save()
                mensaje="Editado correctamente"
            except IntegrityError:
                mensaje="No editado"
            alumnos=Alumno.objects.filter(ciclo=alumno.ciclo)
            return render(request, 'Profesor.html', {'mensaje':mensaje, 'alumnos':alumnos, 'ciclo':alumno.ciclo})
        else:
            my_frm = miFrm
                
    else:
        my_frm = Edit(initial={
            'nombre':alumno.nombre,
            'email':alumno.email,
            'telefono':alumno.telefono,
            'ciclo':alumno.ciclo,
            'dni':alumno.dni
        })
    
    return render(request, 'edit.html', {'form': my_frm, 'dni':id})

def AñadirAl(request, id):
    alumno=Alumno
    if request.method == "POST":
        miFrm = Añadir(request.POST)
        if(miFrm.is_valid()):
            nombre=miFrm.cleaned_data['nombre']
            email=miFrm.cleaned_data['email']
            contraseña=miFrm.cleaned_data['contraseña']
            telefono=miFrm.cleaned_data['telefono']
            ciclo=miFrm.cleaned_data['ciclo']
            dni=miFrm.cleaned_data['dni']
            alumno=Alumno(nombre=nombre, email=email, contraseña=contraseña, telefono=telefono, ciclo=ciclo, dni=dni)
            try:
                alumno.save()
                mensaje="Guardado correctamente"
            except IntegrityError:
                mensaje="No Guardado"
            alumnos=Alumno.objects.filter(ciclo=alumno.ciclo)
            return render(request, 'Profesor.html', {'mensaje':mensaje, 'alumnos':alumnos, 'ciclo':ciclo})
        else:
            my_frm = miFrm
                
    else:
        my_frm = Añadir(initial={
            'ciclo':id,
        })

    return render(request, 'Añadir.html', {'form': my_frm, 'ciclo':id})

def añadirTar(request, id):
    if request.method == "POST":
        miFrm = Tarea(request.POST)
        if(miFrm.is_valid()):
            nombre=miFrm.cleaned_data['nombre']
            fecha=miFrm.cleaned_data['fecha']
            ciclo=miFrm.cleaned_data['ciclo']
            tarea=Tareas(nombre=nombre, fechaEntrega=fecha, ciclo=ciclo, completada=False)
            try:
                tarea.save()
                mensaje="Guardado correctamente"
            except IntegrityError:
                mensaje="No Guardado, duplicado"
            alumnos=Alumno.objects.filter(ciclo=id)
            return render(request, 'Profesor.html', {'mensaje':mensaje, 'alumnos':alumnos, 'ciclo':ciclo})
        else:
            my_frm = miFrm
                
    else:
        my_frm = Tarea(initial={
            'ciclo':id,
        })

    return render(request, 'Tarea.html', {'form': my_frm, 'ciclo':id})

def cambiarEstado(request, id):
        tarea=Tareas.objects.get(nombre=id)
        tarea.completada=True
        try:
            tarea.save()
            mensaje="Entregado"
        except IntegrityError:
            mensaje="No entregado"
            
        tareas=Tareas.objects.filter(ciclo=tarea.ciclo)
        return render(request, 'Alumno.html', {'mensaje':mensaje, 'tareas':tareas, 'ciclo':tarea.ciclo})
def eliminar(request, id):
    alumno=Alumno.objects.get(dni=id)
    try:
        alumno.delete()
        mensaje="Borrado"
    except IntegrityError:
        mensaje="No Borrado"
        
    alumnos=Alumno.objects.filter(ciclo=alumno.ciclo)
    return render(request, 'Profesor.html', {'mensaje':mensaje, 'alumnos':alumnos, 'ciclo':alumno.ciclo})

def verCiclos(request):
    ciclos=Ciclos.objects.all()
    return render(request, "ciclos.html" ,{'ciclos':ciclos})

def verProfesores(request):
    profesores=Profesor.objects.all()
    return render(request, "ListaProfesores.html", {'profesores':profesores})

def AñadirProf(request):
    if request.method == "POST":
        miFrm = AñadirProfesor(request.POST)
        if(miFrm.is_valid()):
            nombre=miFrm.cleaned_data['nombre']
            email=miFrm.cleaned_data['email']
            contraseña=miFrm.cleaned_data['contraseña']
            ciclo=miFrm.cleaned_data['ciclo']
            dni=miFrm.cleaned_data['dni']
            prof=Profesor(nombre=nombre, email=email, contraseña=contraseña,ciclo=ciclo, dni=dni )
            try:
                prof.save()
                mensaje="Guardado correctamente"
            except IntegrityError:
                mensaje="No Guardado"
            profesores=Profesor.objects.all()
            return render(request, "ListaProfesores.html", {'mensaje':mensaje, 'profesores':profesores})
        else:
            my_frm = miFrm
                
    else:
        my_frm = AñadirProfesor()

    return render(request, 'AñadirProfesor.html', {'form': my_frm})


def añadirCiclo(request):
    if request.method == "POST":
        miFrm = AñadirCic(request.POST)
        if(miFrm.is_valid()):
            ciclo=miFrm.cleaned_data['ciclo']
            profesorDni=miFrm.cleaned_data['profesorDni']
            aulas=miFrm.cleaned_data['aulas']
            ciclo=Ciclos(ciclo=ciclo, profesorDni=profesorDni, aulas=aulas)
            try:
                ciclo.save()
                mensaje="Guardado correctamente"
            except IntegrityError:
                mensaje="No Guardado"
            ciclos=Ciclos.objects.all()
            return render(request, 'ciclos.html', {'mensaje':mensaje, 'ciclos':ciclos})
        else:
            my_frm = miFrm
                
    else:
        my_frm = AñadirCic()

    return render(request, 'AñadirCiclos.html', {'form': my_frm})

