from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu nombre', 'class': 'form-control'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Introduce tu email', 'class': 'form-control'})
    )

    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Introduce tu edad', 'class': 'form-control'}),
        min_value=1
    )

    SEXO_CHOICES = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ]
    sexo = forms.ChoiceField(
        choices=SEXO_CHOICES, 
        widget=forms.RadioSelect
    )

    TEMAS_CHOICES = [
        ('0', 'Programación'),
        ('1', 'Comer'),
        ('2', 'Bailar'),
        ('3', 'Apostar'),
    ]
    temas_interes = forms.ChoiceField(
        choices=TEMAS_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    PREFERENCIAS_CHOICES = [
        ('Lectura', 'Lectura'),
        ('Viajar', 'Viajar'),
        ('Deporte', 'Deporte'),
        ('Cine', 'Cine'),
        ('Música', 'Música'),
    ]
    preferencias = forms.MultipleChoiceField(
        choices=PREFERENCIAS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
