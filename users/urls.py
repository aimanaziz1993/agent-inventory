from django.urls import path

from .views import CustomUserRegistration, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register', CustomUserRegistration.as_view(), name="create_user"),
    path('logout', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]