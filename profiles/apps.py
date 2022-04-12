from django.apps import AppConfig
from django.db.models.signals import post_save

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
