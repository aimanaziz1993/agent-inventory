from django.urls import path

from .views import CustomNewPassword, CustomResetPassword, CustomUserRegistration, BlacklistTokenUpdateView, CustomTokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('register', CustomUserRegistration.as_view(), name="create_user"),

    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', BlacklistTokenUpdateView.as_view(), name='blacklist'),

    path('reset/<str:user_name>', CustomResetPassword.as_view(), name="reset_password"),
    path('set-password/<str:temPass>/<str:user_name>', CustomNewPassword.as_view(), name="set_password"),

]
