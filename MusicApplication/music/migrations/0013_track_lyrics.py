# Generated by Django 4.2.5 on 2023-09-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_lyric'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='lyrics',
            field=models.ManyToManyField(to='music.lyric'),
        ),
    ]
