# Generated by Django 4.2.4 on 2023-09-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_artist_track_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='track',
            name='genre',
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ManyToManyField(to='home.genre'),
        ),
    ]