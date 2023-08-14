from rest_framework import serializers

from profiles.models import Profile
from users.models import NewUser


class UserProfileSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.user_name', required=False)

    class Meta:
        model = Profile
        fields = ('user_name', 'user', 'photo', 'nickname', 'firstName', 'lastName', 'description', 'phone', 'email',
                  'facebook', 'instagram', 'youtube', 'linkedin', 'tiktok', 'is_verified', 'view_count'
                  )
