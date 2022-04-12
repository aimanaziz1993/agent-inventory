from rest_framework import serializers

from profiles.models import Profile
from inventory_api.serializers import InventorySerializer

class UserProfileSerializer(serializers.ModelSerializer):

    inventories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'photo', 'nickname', 'firstName', 'lastName', 'description', 'phone', 'email',
            'facebook', 'instagram', 'youtube', 'linkedin', 'tiktok', 'inventories'
        )