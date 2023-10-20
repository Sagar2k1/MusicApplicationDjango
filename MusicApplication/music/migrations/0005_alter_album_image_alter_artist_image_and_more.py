# Generated by Django 4.2.4 on 2023-09-22 07:45

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_album_image_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(height_field='url_height', upload_to=music.models.upload_to, width_field='url_width'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(height_field='url_height', upload_to=music.models.upload_to, width_field='url_width'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(height_field='url_height', upload_to=music.models.upload_to, width_field='url_width'),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(height_field='url_height', upload_to=music.models.upload_to, width_field='url_width'),
        ),
    ]