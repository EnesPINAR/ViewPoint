# Generated by Django 4.1.3 on 2024-01-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_camera_post_camera_settings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]