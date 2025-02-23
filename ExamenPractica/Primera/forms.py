from django import forms
from Primera.models import Laboratorio

class Login(forms.Form):
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control'})
    )
    
    contraseña= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'escribe tu contraseña', 'class': 'form-control'})
    )
    

class MiFormulario(forms.Form):
    nombre=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','placeholder':"Tu nombre"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control'})
    )
    
    contraseña= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'escribe tu contraseña', 'class': 'form-control'})
    )
    
    laboratorio=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','placeholder':"Laboratorio"}))
    
class Alta(forms.Form):
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control'})
    )
    
    laboratorio = forms.ModelChoiceField(
        queryset=Laboratorio.objects.all(),  # Obtiene todos los laboratorios
        empty_label="Selecciona un laboratorio",  # Texto por defecto en el dropdown
        widget=forms.Select(attrs={'class': 'form-control'})  # Personaliza el widget
    )
    nombre=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','placeholder':"Nombre del Ordenador"}))
    descripcion=forms.CharField(max_length=100,widget=forms.TextInput({'class':'form-control','placeholder':"Descipcion"}))
    
class Resolver(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control', 'readonly':'readonly'})
    )
    numero=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control' ,'readonly':'readonly'})
    )
    numOrdenador=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','readonly':'readonly'}))
    descripcion=forms.CharField(max_length=100,widget=forms.TextInput({'class':'form-control','placeholder':"Descipcion"}))
    
class Detalles(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control', 'readonly':'readonly'})
    )
    numero=forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control' ,'readonly':'readonly'})
    )
    numOrdenador=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','readonly':'readonly'}))
    descripcion=forms.CharField(max_length=100,widget=forms.TextInput({'class':'form-control','readonly':'readonly'}))
