from django import forms 

class Anotarse(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    curso = forms.ChoiceField(choices=[
        ('curso1', 'Curso 1'),
        ('curso2', 'Curso 2'),
        ('curso3', 'Curso 3'),
    ])