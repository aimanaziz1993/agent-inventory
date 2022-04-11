from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.db import models

from blog.models import PhotoGallery, Photo, Post
from .serializers import PhotoGallerySerializer, PhotoSerializer, PostSerializer
from .permissions import PostUserWritePermission


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.postobjects.all()

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=item)

class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug', '^title']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

# Post Admin

# class CreatePost(generics.CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class CreatePost(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        # print(request.data)
        # print(self.request.FILES.getlist('photos[]'))
        # # print(request.POST.get('photos'))
        # print(self.request.FILES.getlist('photos'))
        # print( len(self.request.FILES.getlist('photos')) )

        photo_gallery_serializer = PhotoGallerySerializer
        length_photos = len(self.request.FILES.getlist('photos'))

        if length_photos > 0:
            photo_gallery = PhotoGallery.objects.all().count()

            if photo_gallery_serializer == 0:
                photo_gallery = PhotoGallery.objects.create(id=1)
            else:
                photo_gallery = PhotoGallery.objects.create(id=photo_gallery+1)

        serializer = PostSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save(photos=photo_gallery)
            for f in self.request.FILES.getlist('photos'):
                photo = Photo.objects.create(
                    image=f,
                    gallery = photo_gallery
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     def get_queryset(self):
#         return Post.objects.all()

# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return response.Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return response.Response(serializer_class.data)

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     pass


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pass


""" 
Concrete View Classes
    #CreateAPIView
        Used for create-only endpoints.
    #ListAPIView
        Used for read-only endpoints to represent a collection of model instances.
    #RetrieveAPIView
        Used for read-only endpoints to represent a single model instance.
    #DestroyAPIView
        Used for delete-only endpoints for a single model instance.
    #UpdateAPIView
        Used for update-only endpoints for a single model instance.
    ##ListCreateAPIView
        Used for read-write endpoints to represent a collection of model instances.
    RetrieveUpdateAPIView
        Used for read or update endpoints to represent a single model instance.
    #RetrieveDestroyAPIView
        Used for read or delete endpoints to represent a single model instance.
    #RetrieveUpdateDestroyAPIView
        Used for read-write-delete endpoints to represent a single model instance.
"""
