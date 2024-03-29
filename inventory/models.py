from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from profiles.models import Profile

def get_upload_path(instance, filename):
    if instance:
        return f'inventory/user_{instance.realtor.user.user_name}/gallery/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Inventory(models.Model):

    class ListingObjects(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(is_published=True, status=True)

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class TitleType(models.TextChoices):
        STRATA = 'Strata'
        LAND = 'Land'

    class Furnishing(models.TextChoices):
        FULLY_FURNISH = 'Fully furnish'
        PARTIAL_FURNISH = 'Partial'
        NONE = 'None'

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, related_name="category")
    propertyType = models.ForeignKey(PropertyType, on_delete=models.PROTECT, default=1)
    propertyTitle = models.CharField(max_length=50, choices=TitleType.choices, default=TitleType.STRATA)
    saleType = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    rentalDeposit = models.CharField(_("Rental Deposit"), max_length=50, null=True)
    tenure = models.BooleanField(default=False)

    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    location = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    lat = models.DecimalField(_("Latitude"), max_digits=9, decimal_places=6, null=True)
    lon = models.DecimalField(_("Longitude"), max_digits=9, decimal_places=6, null=True)
    
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    floorRange = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    furnishing = models.CharField(max_length=50,choices=Furnishing.choices, default=Furnishing.NONE)
    amenities = models.CharField(max_length=200, null=True)
    carpark = models.IntegerField()
    otherInfo = models.CharField(max_length=255, null=True)

    featureImage = models.ImageField(_("Featured Image"), upload_to=get_upload_path, blank=True, null=True)
    photo_1 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_2 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_3 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_4 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_5 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_6 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_7 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_8 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_9 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    photo_10 = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    video = models.URLField(max_length=200, null=True)

    is_published = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    inventory_date = models.DateTimeField(default=timezone.now)

    realtor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='inventories')

    view_count = models.IntegerField(default=0)

    objects = models.Manager() # Default Manager
    listobjects = ListingObjects() # Custom Manager

    def update_views(self, *args, **kwargs):
        self.view_count = self.view_count + 1
        super(Inventory, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.title)

