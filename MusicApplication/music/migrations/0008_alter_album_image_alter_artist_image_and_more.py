# Generated by Django 4.2.4 on 2023-09-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_alter_album_image_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='media/album/'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to='media/nghe-si/'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(upload_to='media/the-loai/'),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(upload_to='media/bai-hat/'),
        ),
    ]
