# Generated by Django 4.2.5 on 2023-09-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_track_lyrics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='lyrics',
            field=models.ManyToManyField(null=True, to='music.lyric'),
        ),
    ]
