from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Anotarse
from .models import Alumno, Curso

def inicio(request):
    return render(request, "home/inicio.html") 

def anotarse(request):
    if request.method == "POST":
        formulario = Anotarse(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"]
            )
            alumno.save()
            return redirect("inicio")

    else:
        formulario = Anotarse()

    return render(request, "home/anotarse.html", {"formulario": formulario})

def lista_de_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "home/lista_de_alumnos.html", {"alumnos": alumnos})