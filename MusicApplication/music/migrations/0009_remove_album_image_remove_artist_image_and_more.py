# Generated by Django 4.2.5 on 2023-09-22 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_alter_album_image_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='image',
        ),
        migrations.RemoveField(
            model_name='track',
            name='image',
        ),
    ]