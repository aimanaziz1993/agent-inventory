# Generated by Django 4.0.3 on 2022-04-11 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='profile_photo/avatar.png', upload_to=profiles.models.get_upload_path)),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('top_seller', models.BooleanField(default=False)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('youtube', models.URLField(null=True)),
                ('tiktok', models.URLField(null=True)),
                ('linkedin', models.URLField(null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_hired', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
