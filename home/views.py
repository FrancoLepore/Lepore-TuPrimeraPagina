from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Anotarse
from .models import Alumno
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy #basicamente un redirect
from django.contrib.auth.mixins import LoginRequiredMixin #para que solo los usuarios logueados puedan ver la lista de alumnos
from django.contrib.auth.decorators import login_required #decorador para que solo los usuarios logueados puedan ver la lista de alumnos

def inicio(request):
    return render(request, "home/inicio.html") 

@login_required #esto es para que solo los usuarios logueados puedan ver la lista de alumnos
def anotarse(request):
    if request.method == "POST":
        formulario = Anotarse(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                curso=info["curso"],
                fecha_anotado=info["fecha_anotado"],
            )
            alumno.save()
            return redirect("lista_de_alumnos")

    else:
        formulario = Anotarse()

    return render(request, "home/anotarse.html", {"formulario": formulario})

def lista_de_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "home/lista_de_alumnos.html", {"alumnos": alumnos})

def detalle_alumno(request, alumno_en_especifico):
    alumno = Alumno.objects.get(id=alumno_en_especifico)
    return render(request, "home/detalle_alumno.html", {"alumno": alumno})

#esta es una clase basada en vista. ES LO MISMO QUE LA DE ARRIBA ASI

class VistaDetalleAlumno(DetailView):
    model = Alumno #AUTOMATICAMENTE genera un "alumno" en minuscula, lo que permite que usando el mismo html funque todo.
    template_name = "home/detalle_alumno.html"

#es una clase de vista. pero es oara MODIFICAR (update)
class VistaModificarAlumno(LoginRequiredMixin,UpdateView):
    model = Alumno
    template_name = "home/modificar_alumno.html"
    fields = ["nombre", "apellido", "email"] #con esto armamos los campos para el formulario
    success_url = reverse_lazy("lista_de_alumnos") # te lleva a donde quieras una vez que se modifico el alumno, le pones el name de la url

class VistaEliminarAlumno(LoginRequiredMixin,DeleteView):
    model = Alumno
    template_name = "home/eliminar_alumno.html"
    success_url = reverse_lazy("lista_de_alumnos") 

