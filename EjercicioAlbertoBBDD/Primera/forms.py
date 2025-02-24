from django import forms
from Primera.models import Alumno, Ciclos

class Login(forms.Form):
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control'})
    )
    
    contraseña= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'escribe tu contraseña', 'class': 'form-control'})
    )

class Edit(forms.Form):
    nombre= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    telefono= forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    ciclo= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'})
    )
    dni= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'})
    )
class Añadir(forms.Form):
    nombre= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre','class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce el email','class': 'form-control'})
    )    
    contraseña= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'escribe la contraseña', 'class': 'form-control'})
    )
    telefono= forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Introduce el telefono','class': 'form-control'})
    )
    ciclo= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce su ciclo','class': 'form-control', 'readonly':'readonly'})
    )
    dni= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce su dni','class': 'form-control'})
    )
    
class AñadirProfesor(forms.Form):
    nombre= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre','class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce el email','class': 'form-control'})
    )    
    contraseña= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'escribe la contraseña', 'class': 'form-control'})
    )
    ciclo= forms.ModelChoiceField(
        queryset=Ciclos.objects.all(),
        empty_label="Selecciona un ciclo",  
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )
    dni= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce su dni','class': 'form-control'})
    )
    
    
class AñadirCic(forms.Form):
    ciclo= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre','class': 'form-control'})
    )
    profesorDni= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce su dni','class': 'form-control'})
    )
    aulas=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Introduce las aulas','class': 'form-control'})
    )
    
class Tarea(forms.Form):
    ciclo = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Introduce su ciclo',
            'class': 'form-control',
            'readonly': 'readonly'
        })
    )

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        required=False
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Introduce el nombre',
            'class': 'form-control'
        })
    )
