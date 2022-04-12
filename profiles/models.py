from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import NewUser

def get_upload_path(instance, filename):
    if instance:
        return f'profile_photo/user_{instance.nickname}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE, related_name="user_profile", primary_key=True)
    nickname = models.CharField(max_length=50, null=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to=get_upload_path, default="profile_photo/avatar.png")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)

    facebook = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    youtube = models.URLField(max_length=200, null=True)
    tiktok = models.URLField(max_length=200, null=True)
    linkedin = models.URLField(max_length=200, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_hired = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.email
