from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from users.models import NewUser

@receiver(post_save, sender=NewUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=NewUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()