from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label="Usuario", max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        helps_texts = {"username": "El nombre de usuario debe ser único y no puede contener caracteres especiales.",
                    "email": "Introduce una dirección de correo electrónico válida.",
                    "password1": "La contraseña debe tener al menos 8 caracteres, incluyendo letras y números.",
                    "password2": "Repite la contraseña para confirmarla."}
        
class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label="Email", required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar"]
