from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import models

from inventory.models import Inventory
from .serializers import InventorySerializer
from .permissions import PostUserWritePermission


# User read/write permission
class InventoryList(generics.ListCreateAPIView, PostUserWritePermission):
    # queryset = Inventory.listobjects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PostUserWritePermission]

    def get_queryset(self):
        return Inventory.listobjects.all()

class InventoryDetail(generics.RetrieveUpdateAPIView, PostUserWritePermission):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [PostUserWritePermission]
    lookup_field = 'id'

# Public
class InventoryProfileDetail(generics.RetrieveAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return get_object_or_404(Inventory, slug=item)
