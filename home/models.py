from django.db import models

class Alumno(models.Model):
    CURSO_CHOICES = [
        ('1', 'Python'),
        ('2', 'Django'),
        ('3', 'JavaScript'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=2, choices=CURSO_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
