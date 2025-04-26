from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import InfoExtra

@receiver(post_save, sender=User)
def crear_infoextra_usuario(sender, instance, created, **kwargs):
    if created:
        InfoExtra.objects.create(user=instance)
