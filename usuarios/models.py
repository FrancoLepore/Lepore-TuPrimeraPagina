from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)