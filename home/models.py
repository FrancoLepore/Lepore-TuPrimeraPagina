from django.db import models

class Alumno(models.Model):
    CURSO_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('JavaScript', 'JavaScript'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=20, choices=CURSO_CHOICES)
    fecha_anotado = models.DateField(null= True) #habilita nulls

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
