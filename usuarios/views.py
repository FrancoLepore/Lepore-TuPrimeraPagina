from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil, FormularioLogin
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.views.generic import DetailView

def login(request):
    if request.method == "POST":
        formulario = FormularioLogin(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect("inicio")
    else:
        formulario = FormularioLogin()
        
    return render(request, "usuarios/login.html", {"formulario": formulario})


def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect("login")
    else:
        formulario = FormularioRegistro()

    return render(request, "usuarios/registro.html", context={"formulario": formulario})

@login_required
def editar_perfil(request):
    infoextra = request.user.infoextra

    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance = request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get("avatar"):
                infoextra.avatar = formulario.cleaned_data.get("avatar")
            
            infoextra.save()

            formulario.save()

            return redirect("inicio") #despues modificar para que vaya al perfil !!!
    else:
        formulario = FormularioEdicionPerfil(initial = {"avatar": infoextra.avatar},instance = request.user)

    return render(request, "usuarios/editar_perfil.html", context={"formulario": formulario})

class VistaDetalleUsuario(DetailView):
    model = InfoExtra
    template_name = "usuarios/detalle_usuario.html"

