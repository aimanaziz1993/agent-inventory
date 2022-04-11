from rest_framework import serializers
from profiles.models import Profile
from users.models import NewUser


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ('id', 'userId', 'nickname', 'firstName', 'lastName', 'photo', 'description', 
#         'phone', 'email', 'top_seller', 'is_verified')


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        # create one to one profile row to userid
        profile = Profile()
        profile.user = instance
        profile.save()
        return instance