from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def get_full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
