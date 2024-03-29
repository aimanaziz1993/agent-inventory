from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import NewUser


def get_upload_path(instance, filename):
    if instance:
        return f'profile_photo/user_{instance.user.user_name}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(
        NewUser, on_delete=models.CASCADE, related_name="user_profile", primary_key=True)
    nickname = models.CharField(max_length=50, null=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, null=True)
    photo = models.ImageField(
        upload_to=get_upload_path, default="profile_photo/avatar.png")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)

    facebook = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    youtube = models.URLField(max_length=200, null=True)
    tiktok = models.URLField(max_length=200, null=True)
    linkedin = models.URLField(max_length=200, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_hired = models.DateTimeField(default=timezone.now, blank=True)
    view_count = models.IntegerField(default=0)

    # Referal
    groupId = models.IntegerField(default=0)
    introducer = models.CharField(max_length=200, null=True)
    groupId = models.IntegerField(default=0)

    def __str__(self):
        return self.email

    # An alternative to use to update the view count

    def update_views(self, *args, **kwargs):
        self.view_count = self.view_count + 1
        super(Profile, self).save(*args, **kwargs)

    def get_introducer_metadata(self, *args, **kwargs):
        try:
            introducerData = NewUser.objects.get(username=self.introducer)
            groupId = introducerData.groupId if introducerData.groupId else None
            return {
                'username': introducerData.username,
                'groupId': groupId
            }
        except NewUser.DoesNotExist:
            return None

    def get_group_id(self, *args, **kwargs):
        introducer_data = self.get_introducer_metadata()
        if introducer_data:
            return introducer_data.get('groupId')
        return None
