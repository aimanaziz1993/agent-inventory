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

class InventoryList(generics.ListCreateAPIView, PostUserWritePermission):
    queryset = Inventory.listobjects.all()
    serializer_class = InventorySerializer
    permission_classes = [PostUserWritePermission]

class InventoryDetail(generics.RetrieveUpdateAPIView, PostUserWritePermission):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [PostUserWritePermission]
