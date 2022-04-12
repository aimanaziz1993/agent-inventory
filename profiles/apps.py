from django.apps import AppConfig
from django.db.models.signals import post_save

from users.models import NewUser
from profiles.signals import create_user_profile, save_user_profile

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
