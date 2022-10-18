import json
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from users.models import NewUser

from .serializers import CustomUserSerializer, CustomUserTokenObtainPairSerializer, UserSerializer
from profiles.models import Profile
from profiles.serializers import UserProfileSerializer

from django.shortcuts import get_object_or_404

from rest_framework import generics

# from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives

import random


class CustomUserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile()
            profile.user = user
            profile.firstName = user.first_name
            profile.email = user.email
            profile.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomUserTokenObtainPairSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomResetPassword(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # serializer = CustomUserSerializer(data=request.data)

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('user_name')
        user = get_object_or_404(NewUser, user_name=item)
        email = user.email

        rand = random.randint(1000, 2000)

        tempPass = str(rand)

        user.set_password(tempPass)
        user.save()

        print('tempPass', tempPass)

        subject, from_email, to = 'Reset Password', 'admin@admin.com', email,

        text_content = 'This is an important message.'
        html_content = '<p>This is a <strong> temporary link reset password : </strong> <a href=http://127.0.0.1:8000/api/v1/user/set-password/' + \
            tempPass + '/' + item + '> ' + tempPass + ' </a></p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return get_object_or_404(NewUser, user_name=item)


class CustomNewPassword(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, **kwargs):

        item = self.kwargs.get('temPass')
        username = self.kwargs.get('user_name')
        user = get_object_or_404(NewUser, user_name=username)

        if user.check_password(item):
            dataBody = request.data["password"]

            user.set_password(dataBody)
            user.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
