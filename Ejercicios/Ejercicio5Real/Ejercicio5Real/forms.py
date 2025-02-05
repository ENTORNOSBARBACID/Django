from django import forms

class ContactForm(forms.Form):
    nombre=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu nombre"}),label="Nombre")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ejemplo@ejemplo.com'}),label="Email")
    LENGUAJES_CHOICES = [
        ('java', 'Java'),
        ('python', 'Python'),
        ('c++', 'C++'),
        ('javascript', 'JavaScript'),
        ('ruby', 'Ruby'),
    ]
    
    lenguajes = forms.MultipleChoiceField(
        choices=LENGUAJES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),  # Estilo para los checkboxes
        required=False,  # Permite no seleccionar nada si lo deseas
        label="Lenguajes de Programación"
    )