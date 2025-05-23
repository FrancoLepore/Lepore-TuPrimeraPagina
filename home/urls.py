from django.urls import path
from .views import inicio, anotarse, lista_de_alumnos, detalle_alumno, VistaDetalleAlumno, VistaModificarAlumno, VistaEliminarAlumno

urlpatterns = [
    path("", inicio, name="inicio"), 
    path("alumnos/", lista_de_alumnos, name="lista_de_alumnos"),
    path("alumnos/anotarse/",anotarse, name="anotarse"), #seria crear
    #path("alumnos/<int:alumno_en_especifico>/", detalle_alumno, name="detalles"), #estas 3 son clases de vista. 
    path("alumnos/<int:pk>/", VistaDetalleAlumno.as_view(), name="detalles"), #read
    path("alumnos/<int:pk>/modificar",VistaModificarAlumno.as_view(), name="modificar"), #update
    path("alumnos/<int:pk>/eliminar",VistaEliminarAlumno.as_view(), name="eliminar"), #delete
    
]
