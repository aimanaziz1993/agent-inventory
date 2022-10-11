from rest_framework import serializers
from profiles.models import Profile
from users.models import NewUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ('id', 'userId', 'nickname', 'firstName', 'lastName', 'photo', 'description',
#         'phone', 'email', 'top_seller', 'is_verified')

class CustomUserTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomUserTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user_name': self.user.user_name})
        data.update({'email': self.user.email})
        data.update({'id': self.user.id})
        return data


class CustomUserSerializer(serializers.ModelSerializer):

    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:

        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        model = NewUser

    def validate(self, attrs):

        email = attrs.get('email', '')
        user_name = attrs.get('user_name', '')

        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': "Email is already in use."})

        if NewUser.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError(
                {'user_name': "Username is already in use."})

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('id', 'is_superuser', 'user_name', 'password', 'first_name',
                  'email', 'is_staff', 'is_active', 'about')
