# Generated by Django 4.0.3 on 2023-11-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_newuser_serialize_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='user_view',
            field=models.IntegerField(default=0),
        ),
    ]
