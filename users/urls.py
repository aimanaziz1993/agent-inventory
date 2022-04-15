from django.urls import path

from .views import CustomUserRegistration, BlacklistTokenUpdateView, CustomTokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('register', CustomUserRegistration.as_view(), name="create_user"),

    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]