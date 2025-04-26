from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(
        label="Usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu usuario'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu email'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu contraseña'})
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetí tu contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormularioEdicionPerfil(UserChangeForm):
    password = None

    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu email'})
    )
    first_name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu nombre'})
    )
    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu apellido'})
    )
    avatar = forms.ImageField(
        label="Cambiar Avatar (opcional)",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar"]

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresá tu usuario'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresá tu contraseña'
        })
    )