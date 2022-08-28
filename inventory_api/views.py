from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters import rest_framework as filters

from inventory.models import Inventory
from .serializers import InventorySerializer
from .permissions import PostUserWritePermission
from .filters import CustomInventoryFilter



# User read/write permission
class InventoryList(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Django Filter Backend
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CustomInventoryFilter
    # filterset_fields = ['realtor__user__user_name']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Inventory.listobjects.filter(realtor=user).order_by('-inventory_date')
        return Inventory.listobjects.all().order_by('-inventory_date')

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, PostUserWritePermission]
    lookup_field = 'id'

# Public
class InventoryProfileDetail(generics.RetrieveAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return get_object_or_404(Inventory, slug=item)
