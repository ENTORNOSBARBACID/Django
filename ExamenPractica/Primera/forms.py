from django import forms

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