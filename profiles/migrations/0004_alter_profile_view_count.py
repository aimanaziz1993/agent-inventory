# Generated by Django 4.0.3 on 2022-10-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
