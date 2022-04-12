from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from profiles.models import Profile
from .serializers import UserProfileSerializer
from .permissions import ProfileUserWritePermission

# own user view and create
class ProfileView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user:
            return Profile.objects.filter(user=self.request.user.id)

        return Profile.objects.all()

class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [ProfileUserWritePermission]

    def get_object(self, queryset=None, **kwargs):
        user_name = self.kwargs.get('user_name')
        return get_object_or_404(Profile, user__user_name=user_name)


