from django.urls import path
from .views import inicio, anotarse

urlpatterns = [
    path("", inicio, name="inicio"), 
    path("alumnos/anotarse/",anotarse, name="anotarse"),
]
