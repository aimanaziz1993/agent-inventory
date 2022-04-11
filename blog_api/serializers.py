from rest_framework import serializers

from blog.models import Post, PhotoGallery, Photo


class PhotoGallerySerializer(serializers.ModelSerializer):
    photos = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = PhotoGallery
        fields = ('id', 'photos')

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('image', 'gallery')

class PostSerializer(serializers.ModelSerializer):
    photos = PhotoGallerySerializer(read_only=True)

    class Meta:
        fields = ('category', 'id', 'title', 'image', 'slug', 'author', 'excerpt', 'content', 'photos', 'video', 'status')
        model = Post


    