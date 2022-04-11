from django.contrib import admin

from .models import Category, Post, Photo, PhotoGallery

@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(PhotoGallery)
