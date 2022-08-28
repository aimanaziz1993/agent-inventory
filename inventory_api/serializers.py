from rest_framework import serializers

from inventory.models import Category, Inventory, PropertyType


class PropertyTypeSerializer(serializers.ModelSerializer):
   class Meta:
        model = PropertyType
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

class InventorySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='realtor.user.user_name', required=False)
    phone_number = serializers.CharField(source='realtor.phone', required=False)
    class Meta:
        fields = ('category', 'id', 'propertyType', 'propertyTitle', 'saleType',
        'rentalDeposit', 'tenure',
        'slug', 'title', 'location', 'address', 'city', 'state', 'zipcode',
        'description', 'lat', 'lon',
        'price', 'bedrooms', 'bathrooms', 'floorRange', 'furnishing', 'amenities',
        'size', 'carpark', 'otherInfo',
        'featureImage', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
        'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10', 'video',
        'realtor', 'user_name', 'phone_number', 'inventory_date'
        )
        model = Inventory
