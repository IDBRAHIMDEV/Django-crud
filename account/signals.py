from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):

    if created:

        Profile.objects.create(
            user=instance,
            username=instance.username,
            name=instance.first_name,
            email=instance.email
        )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
