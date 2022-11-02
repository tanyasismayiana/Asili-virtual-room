from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

# User = get_user_model() 
# Create your models here.





class Avatar(models.Model):
    user = models.OneToOneField(
        get_user_model(), related_name="profile", on_delete=models.CASCADE
    )
    height = models.CharField(
        verbose_name="Height",
        max_length=255,
        default=None,
        blank=True,
        null=True,

    )

    shoulders = models.CharField(
        verbose_name="Shoulders",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )

    burst = models.CharField(
        verbose_name="Burst",
        max_length=255,
        default=None,
        blank=True,
        null=True,

    )

    waist = models.CharField(
        verbose_name="Waist",
        max_length=255,
        default=None,
        blank=True,
        null=True,

    )

    hips = models.CharField(
        verbose_name="Hips",
        max_length=255,
        default=None,
        blank=True,
        null=True,

    )

@receiver(post_save,sender = get_user_model())
def create_user_profile(sender,instance,created,**__):
    """Hook for creating profiles."""
    if created:
        profile.objects.create(user=instance)


@receiver(post_save,sender = get_user_model())
def save_user_profile(sender,instance, **__):
    """Hook for updating profiles."""
    instance.profile.save()

class Dresses(models.Model):
    name = models.TextField(default="")
    image = models.ImageField(upload_to='static/images/')    

def __str__(self):
    return self.name