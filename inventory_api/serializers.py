from rest_framework import serializers

from inventory.models import Category, Inventory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name')

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('category', 'id', 'propertyType', 'propertyTitle', 'saleType',
        'rentalDeposit', 'tenure',
        'slug', 'title', 'location', 'address', 'city', 'state', 'zipcode',
        'description', 'lat', 'lon',
        'price', 'bedrooms', 'bathrooms', 'floorRange', 'furnishing', 'amenities',
        'carpark', 'otherInfo',
        'featureImage', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
        'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10', 'video',
        'realtor'
        )
        model = Inventory