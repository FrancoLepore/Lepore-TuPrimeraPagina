from django.urls import path
from .views import inicio, anotarse, lista_de_alumnos

urlpatterns = [
    path("", inicio, name="inicio"), 
    path("alumnos/", lista_de_alumnos, name="lista_de_alumnos"),
    path("alumnos/anotarse/",anotarse, name="anotarse"),
]
