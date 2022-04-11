from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.conf import settings


def get_upload_path(instance, filename):
    if instance:
        return f'posts/gallery/user/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PhotoGallery(models.Model):
    def default(self):
        return self.photos.filter(default=False).first()

    def get_thumbnail(self):
        return self.photos.filter(width__lte=100, length__lte=100)

    # @property
    # def photos(self):
    #     return self.photos_set.all()

class Photo(models.Model):
    # name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path, default='posts/default.jpg')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    gallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.image.url

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=get_upload_path, default='posts/default.jpg')
    featured_image = models.ImageField(_("Featured Image"), upload_to=get_upload_path, default='posts/featured.jpg')
    video = models.URLField(default='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4')
    photos = models.OneToOneField(PhotoGallery, on_delete=models.CASCADE, related_name='model')
    description = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options , default='published')
    objects = models.Manager() # Default Manager
    postobjects = PostObjects() # Custom Manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


